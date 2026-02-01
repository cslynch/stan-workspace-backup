#!/bin/bash
cd ~/.openclaw/workspace
git add -A
git commit -m "$1"
git push origin master
