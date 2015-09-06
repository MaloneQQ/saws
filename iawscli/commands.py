# -*- coding: utf-8
from __future__ import unicode_literals
import os
import re
from enum import Enum


# AWS built-in commands, listed for syntax highlighting
# TODO: Generate a full list of these commands and store them
# in data/SOURCES.TXT
RESOURCE_OPTIONS = [
    '--instance-ids',
    '--bucket',
    '--load-balancer-name',
]

# AWS CLI entry point, listed for syntax highlighting
AWS_COMMAND = [
    'aws',
]

# AWS CLI configure command, listed for syntax highlighting
AWS_CONFIGURE = [
    'configure'
]

# iawscli docs
AWS_DOCS = [
    'docs',
]

# iawscli custom keywords for syntax highlighting purposes
CUSTOM_KEYWORDS = [
    'ls',
    '--tags',
]

COMMANDS_HEADER = '[commands]: '
SUB_COMMANDS_HEADER = '[sub_commands]: '
GLOBAL_OPTIONS_HEADER = '[global_options]: '
SOURCES_DIR = os.path.dirname(os.path.realpath(__file__))
SOURCES_PATH = os.path.join(SOURCES_DIR, 'data/SOURCES.txt')


class CommandType(Enum):

    COMMANDS, SUB_COMMANDS, GLOBAL_OPTIONS = range(3)


def generate_all_commands():
    commands = []
    sub_commands = []
    global_options = []
    command_type = CommandType.COMMANDS
    with open(SOURCES_PATH) as f:
        for line in f:
            line = re.sub('\n', '', line)
            if COMMANDS_HEADER in line:
                command_type = CommandType.COMMANDS
                continue
            elif SUB_COMMANDS_HEADER in line:
                command_type = CommandType.SUB_COMMANDS
                continue
            elif GLOBAL_OPTIONS_HEADER in line:
                command_type = CommandType.GLOBAL_OPTIONS
                continue
            if command_type == CommandType.COMMANDS:
                commands.append(line)
            elif command_type == CommandType.SUB_COMMANDS:
                sub_commands.append(line)
            elif command_type == CommandType.GLOBAL_OPTIONS:
                global_options.append(line)
    return sorted(commands), sorted(sub_commands), sorted(global_options)
