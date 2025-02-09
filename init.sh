#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path-to-git-repo>"
    exit 1
fi

TARGET_REPO="$1"
HOOKS_DIR="$TARGET_REPO/.git/hooks"
HOOK_FILE="$HOOKS_DIR/commit-msg"
AUTOCOMMIT_DIR="$HOME/autocommit"
AUTOCOMMIT_DIR="$(dirname "$0")"
VENV_DIR="$AUTOCOMMIT_DIR/venv"

if [ ! -d "$TARGET_REPO/.git" ]; then
    echo "Error: '$TARGET_REPO' is not a valid Git repository."
    exit 1
fi

echo "Installing commit-msg hook in $TARGET_REPO..."

# mkdir -p "$HOOKS_DIR"
cp "$AUTOCOMMIT_DIR/hooks/commit-msg" "$HOOK_FILE"
chmod +x "$HOOK_FILE"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in autocommit repo..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
fi

echo "Installing dependencies in virtual environment..."
"$VENV_DIR/bin/pip" install -r "$AUTOCOMMIT_DIR/requirements.txt"

echo "Installation complete. The commit-msg hook is now active for $TARGET_REPO."
