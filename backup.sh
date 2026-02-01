#!/bin/bash
# Daily backup script for Stan's workspace

cd /home/clawdbot/.openclaw/workspace

# Add all changes
git add .

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
  echo "No changes to backup"
  exit 0
fi

# Commit with timestamp
git commit -m "Auto-backup: $(date '+%Y-%m-%d %H:%M:%S')"

# Push to GitHub
git push origin master

echo "Backup complete: $(date)"
