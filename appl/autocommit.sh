#!/bin/bash

BASE_DIR=$(dirname "$(dirname "${BASH_SOURCE[0]}")")
INSTALL_SCRIPT="$BASE_DIR/scripts/init.sh"
PYTHON_SCRIPT="$BASE_DIR/message_gen/src/main.py"

# echo "$BASE_DIR"

if [[ $# -eq 1 && -d "$1" ]]; then
    "$INSTALL_SCRIPT" "$1"
    exit 0
fi


VENV_DIR="$BASE_DIR/venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Error: Virtual environment not found in autocommit directory. Please run install.sh again." >&2
    exit 1
fi


if [[ "$1" == "--diff" && -n "$2" && "$3" == "--old" && -n "$4" ]]; then
    # echo gen: 2: "$2", 4: "$4", end
    echo $("$VENV_DIR/bin/python" "$ "$PYTHON_SCRIPT" "$2" "$4")
    exit 0
fi

echo "Usage:"
echo "  autocommit <repo_dir>  # Install hooks in the specified repo"
echo "  autocommit --diff <diff_file> --old <old_message>  # Generate a commit message"
exit 1
