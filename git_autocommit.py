#!/usr/bin/env python
import argparse
from os import path
import subprocess
import time

COMMIT_MESSAGE = """{title}

{summary}
"""

parser = argparse.ArgumentParser(
    description="""
    Automatically commit whenever a file is saved.
    """,
)
parser.add_argument(
    'directory',
    nargs="?",
    default=".",
    help="Directory to watch. This directory should be a git repository.",
)
parser.add_argument(
    '-s','--seconds',
    help="How often to commit, in seconds. (Default is every 10s.)",
    type=int,
    default=10
)

def read_status_line(line):
    status, file = line.split(' ', 1)
    return (status.strip(), file.strip())

def format_title(changes):
    #  @TODO filter out additions, deletions and modifications
    # Call out deletions and additions in particular
    # deletions = [file for status, file in changes if status == 'D']
    # additions = [file for status, file in changes if status == 'A']
    # modifications = [file for status, file in changes if status == 'M']
    files = [file for status, file in changes]
    msg = ""
    if len(files) > 2:
        first = ", ".join(files[0:2])
        rest_count = len(files[2:])
        msg = "{}, +{} more".format(first, rest_count)
    elif len(files) > 1:
        msg = ", ".join(files)
    else:
        msg = files[0]
    return "[Auto] {}".format(msg)

def format_summary(changes):
    return "\n".join("{}: {}".format(status, file) for status, file in changes)

def format_message(changes):
    title = format_title(changes)
    summary = format_summary(changes)
    return COMMIT_MESSAGE.format(title=title, summary=summary)

def read_changes(status):
    return [read_status_line(line) for line in status.strip().split('\n')]

def tick(directory):
    subprocess.check_call(['git', 'add', '-A', '.'], cwd=directory)
    status = subprocess.check_output(
        ['git', 'status', '--porcelain'], cwd=directory
    )
    if status:
        changes = read_changes(status)
        commit_message = format_message(changes)
        subprocess.check_call(
            ['git', 'commit', '-m', commit_message], cwd=directory
        )

def main():
    args = parser.parse_args()
    directory = args.directory
    timeout = args.seconds
    if not path.exists(path.join(directory, '.git')):
        raise Exception(
            "Directory \"{}\" is not a git repository".format(directory)
        )

    print('Watching for changes every {}s'.format(timeout))

    try:
        while True:
            tick(directory)
            time.sleep(timeout)
    except KeyboardInterrupt:
        print('Stopped watching')

if __name__ == '__main__':
    main()
