# Log Generator

This script automates the creation of log files based on templates and user input. It pulls configuration settings from a YAML file and allows flexible log generation through Windows batch and Linux shell scripts. 

## Project Structure

- `log/config.yaml`: Configuration file with log parameters, template paths, and user settings.
- `log/templates/`: Template files for markdown logs.
- `log.py`: Main Python script to generate logs.
- `log.bat`: Windows batch script to call `log.py`.
- `log.sh`: Linux shell script to call `log.py`.

## Requirements

- **Python 3**: Make sure Python is installed and accessible from your command line.
- **yaml**: Install `PyYAML` for handling YAML configuration:
  ```bash
  pip install pyyaml
  ```

## Configuration (config.yaml)

Create a `config.yaml` file in the same directory with the following structure:

```yaml
user:
  name: "Your Name"
  text_editor_path: "path_to_your_text_editor" # e.g., "code" for VSCode
  log_dir: "./logs"
  frontmatter_template: "path_to_frontmatter_template.md"
  dir_delimiter: "-"
  log_proj: "Your Project Name"

log_types:
  daily:
    title: "{project} {type} Log {date}"
    desc: "Daily log for project tracking."
    file_name: "{project}{delim}{type}{delim}{date}.md"
    template: "path_to_daily_template.md"

  sim:
    title: "{project} {type} Simulation {date}"
    desc: "Simulation log for capturing results and analysis."
    file_name: "{project}{delim}{type}{delim}{date}.md"
    template: "path_to_simulation_template.md"
```

## Usage

### 1. Windows

1. Use the batch script `log.bat` to create a log by specifying the log type (e.g., `daily`, `sim`):
   ```cmd
   log.bat sim
   ```
2. Follow the prompts to enter additional details such as date and other variables in the template.

### 2. Linux

1. Make the shell script executable:
   ```bash
   chmod +x log.sh
   ```
2. Run the shell script `log.sh` with the log type:
   ```bash
   ./log.sh sim
   ```

### Main Python Script (log.py)

The `log.py` script:
- Loads configurations from `config.yaml`.
- Prompts the user for input to dynamically fill in template variables.
- Generates a unique ID and timestamp for each log entry.
- Formats and writes the log based on the specified template.
- Opens the generated log in the user-specified text editor.

## Functions Overview

- **load_config**: Loads configuration parameters from `config.yaml`.
- **get_log_params**: Retrieves log parameters for the specified type.
- **prompt_for_date**: Asks for a date or uses today's date.
- **prompt_for_vars**: Prompts for variables in the filename template.
- **format_frontmatter**: Fills frontmatter fields for the log file.
- **format_log_template**: Generates the log file's content.
- **main**: Main function, orchestrates log generation and file creation.

## Example Usage

For a configuration in `config.yaml`:

```yaml
log_types:
  sim:
    title: "{project} {type} Simulation {date}"
    file_name: "{project}-{type}-{date}.md"
```

Running:
```bash
./log.sh sim
```

will prompt for `project`, `type`, and `date`, generate the log file, and open it in the specified editor.

## Error Handling

- If the specified log type is not found in `config.yaml`, the script prints an error message.
- If a log file already exists with the generated name, it will not overwrite and will display a warning.

## Notes

- Ensure `config.yaml` and template files are correctly set up.
- Adjust the `text_editor_path` and `log_dir` paths in `config.yaml` for your environment.

---

Enjoy automated logging!
