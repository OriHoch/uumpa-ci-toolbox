import os
import json
import datetime
import subprocess
from textwrap import dedent


def _render_markdown_from_click_cli_command(python_venv, cli_command, command, sub_commands):
    cli_bin = os.path.join(python_venv, 'bin', cli_command) if python_venv else cli_command
    if command:
        help_text = subprocess.check_output([cli_bin, *command, '--help']).decode()
        help_markdown = '\n#### {}\n\n```\n{}```\n'.format(' '.join([cli_command, *command]), help_text)
    else:
        help_text = subprocess.check_output([cli_bin, '--help']).decode()
        help_markdown = '\n### {}\n\n```\n{}```\n'.format(cli_command, help_text)
    for sub_command in sub_commands:
        sub_command_command = [*command, sub_command['name']]
        help_markdown += _render_markdown_from_click_cli_command(python_venv, cli_command, sub_command_command, sub_command['sub_commands'])
    return help_markdown


def render_markdown_from_click_cli(python_venv, cli_command, cli_module, main_command, output_file, start_line_contains, end_line_contains):
    python_bin = os.path.join(python_venv, 'bin', 'python') if python_venv else 'python'
    main_subcommands = json.loads(subprocess.check_output([python_bin, '-c', dedent("""
        import json
        import {cli_module}
        
        def get_sub_commands(command):
            sub_commands = []
            if hasattr(command, 'commands'):
                for sub_command_name, sub_command in command.commands.items():
                    sub_commands.append(dict(
                        name=sub_command_name,
                        sub_commands=get_sub_commands(sub_command)
                    ))
            return sub_commands
        
        print(json.dumps(get_sub_commands({cli_module}.{main_command})))
    """.format(cli_module=cli_module, main_command=main_command))]).decode())
    help_markdown = _render_markdown_from_click_cli_command(python_venv, cli_command, [], main_subcommands)
    help_markdown += '\n\n<!-- Generated at: {} -->\n\n'.format(datetime.datetime.now())
    lines = []
    wait_for_end_line = False
    with open(output_file) as f:
        for line in f:
            if wait_for_end_line:
                if end_line_contains in line:
                    wait_for_end_line = False
                    lines.append(line)
            elif start_line_contains in line:
                lines += [line, help_markdown]
                wait_for_end_line = True
            else:
                lines.append(line)
    with open(output_file, 'w') as f:
        f.writelines(lines)
