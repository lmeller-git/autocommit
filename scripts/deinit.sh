#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path-to-git-repo>"
    exit 1
fi

TARGET_REPO="$1"
HOOK_DIR="$TARGET_REPO/.git/hooks"

if [ ! -d "$TARGET_REPO/.git" ]; then
    echo "Error: '$TARGET_REPO' is not a valid Git repository."
    exit 1
fi

echo "Removing commit-msg hook from $HOOK_DIR in $TARGET_REPO"
rm "$HOOK_DIR/commit-msg" || { echo "Error: Failed to remove commit-msg hook."; exit 1; }

echo "Succesfully removed commit-msg hook. Autocommit deactivated for $TARGET_REPO"


