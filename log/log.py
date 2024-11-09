import yaml
from datetime import datetime
import time
import random
import os
import sys
import subprocess
import re

F_CONFIG = "./config.yaml"
ID_CHARS = '0123456789abcdefghijklmnopqrstuvwxyaABCDEFGHIJKLMNOPQRSTUVWXYZ'

def load_config(yaml_path:str) -> dict:
    """Read a yaml file that holds basic configuration parameters.

    Input: 
    - yaml_path: relative path to the config file

    Output:
    - config: a dictionary of the parameters read from the config file
    """

    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_log_params(log_type: str, f_config: str = F_CONFIG) -> dict:
    """Get the log parameters from the config file.
    
    Inputs:
    - log_type: the type of log to generate with a type listed in the config file
    - f_config: the config file
    
    Output:
    - params: a dictionary of the log parameters
    """

    config = load_config(f_config)
    user = config['user']
    
    try:
        params = config['log_types'][log_type]
    except Exception:
        print(f"ERROR: Invalid log type entered: {log_type}. Expected types are: {list(config['log_types'].keys())}")
        exit(-1)
    
    return user, params

def prompt_for_date() -> str:
    """Prompt the user for a date.
    
    Output:
    - date_str: a strong containing the formatted date
    """

    # Prompt user for the date or use today's date if left blank
    date_str = input("Enter the date (YYYY-MM-DD) or press Enter to use today's date: ")
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    
    return date_str

def prompt_for_vars(f_string_template: str, delimiter: str = '') -> str:
    """Prompt the user for the values for all keys in an f-string.
    
    Input:
    - f_string_template: the f-string containing keys
    
    Output:
    - formatted_string: the f-string with values assigned to keys
    """
    # Extract variable names within braces (e.g., {project}, {type}, etc.)
    variable_names = re.findall(r'{(\w+)}', f_string_template)

    # Prompt the user for each variable
    values = {}
    values_delim = {}
    for var in variable_names:
        user_input = input(f"Enter value for '{var}': ")
        values[var] =  user_input
        values_delim[var] = user_input.replace(' ','-')
        if user_input:
            values_delim[var] += delimiter

    # Use the values dictionary to format the f-string template
    return f_string_template.format(**values_delim), values

def format_frontmatter(user: dict, log_info: dict, params: dict) -> str:
    """Populate the frontmatter values from an f-string template with keys.
    
    Input:
    - user: the dict containing user parameters
    - log_info: the dict containing the log information parameters
    - params: input parameters from the user for populating info in the title

    Output:
    - the formatted frontmatter string
    """
    # create UNIX timestamp
    timestamp = int(time.time()*1000)

    # create unique ID
    unique_id = ''.join(random.choice(ID_CHARS) for i in range(23))

    # read the frontmatter template file
    with open(user['frontmatter_template'], 'r') as file:
        f_template_str = file.read()

    # return a string with the formatted frontmatter
    return f_template_str.format(
        timestamp = timestamp,
        unique_id = unique_id,
        title = log_info['title'].format(**params),
        author = user['name'],
        description = log_info['desc']
    )

def format_log_template(user: dict, log_info: dict, params: dict) -> str:
    """Populate contents of a log file from a template with keywords.
    
    Input:
    - user: the dict containing user parameters
    - log_info: the dict containing the log information parameters
    - params: input parameters from the user for populating info in the title

    Output:
    - the formatted log file contents
    """
    frontmatter = format_frontmatter(user, log_info, params)

    with open(log_info['template'], 'r') as file:
        log_contents = file.read()
    
    return log_contents.format(frontmatter = frontmatter)

def main():
    # log type is from command line input
    log_type = sys.argv[1]

    # get user and log info from config file
    user, log_info = get_log_params(log_type)
    delim = user['dir_delimiter']
    
    # get date and other parameters from user input
    date_str = prompt_for_date()
    f_name_template = log_info['file_name'].format(
        date = date_str,
        delim = delim
    )
    
    # format the file name
    filename, params = prompt_for_vars(f_name_template, delim)
    log_dir = user['log_dir']
    filepath = '/'.join([log_dir, filename])
    params['date'] = date_str

    # format the file template
    log_template = format_log_template(user, log_info, params)

    # write the template to the log file
    if not os.path.exists(filepath):    
        with open(filepath, 'w') as file:
            file.write(log_template)
        print(f"Markdown file '{filepath}' created successfully!")
    else:
        print(f"File already exists: {filepath}")

    # Open the file in text editor
    print("Opening in text editor...")
    try:
        subprocess.run([user['text_editor_path'], user['log_proj'], filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to open file in text editor: {e}")

# Usage
if __name__ == "__main__":
    main()
