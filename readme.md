# Log Generator

This script automates the creation of log files based on templates and user input. It pulls configuration settings from a YAML file and allows flexible log generation through Windows batch and Linux shell scripts.

The default settings are for a [Dendron](https://www.dendron.so/) file system, but are pretty general to any log or note taking system in markdown.

## File Structure

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

Create a `config.yaml` file in the `log` directory with the following contents:

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

Additionally, you can add the directory containing this repository to you user or global environment variable, then enter the command without changing directories.

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
- Generates a unique ID and timestamp for each log entry for the frontmatter contents.
- Formats and writes the log based on the specified template.
- Opens the generated log in the user-specified text editor.

## Notes

- Ensure `config.yaml` and template files are correctly set up.
- Adjust the `text_editor_path` and `log_dir` paths in `config.yaml` for your environment.

---

Enjoy automated logging!
