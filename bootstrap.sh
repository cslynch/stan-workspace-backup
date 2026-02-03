#!/bin/bash

# bootstrap.sh — Automated Stan Recovery Script
# Purpose: Rebuild Stan environment from scratch in ~30 min
# Status: Current as of Feb 3, 2026
# Usage: bash bootstrap.sh
# Requirements: Fresh Ubuntu 24.04 + internet access

set -e  # Exit on error

echo "🚀 STAN DISASTER RECOVERY BOOTSTRAP"
echo "=================================="
echo ""
echo "This script will reinstall Stan's environment."
echo "Estimated time: 30 minutes (excluding credential entry)"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 1
fi

echo ""
echo "=================================="
echo "PHASE 1: SYSTEM PACKAGES"
echo "=================================="

# Check if running as sudo for some commands
if [[ $EUID -ne 0 ]]; then
    echo "⚠️  Some commands need sudo. You may be prompted for password."
fi

echo "📦 Installing system dependencies..."
sudo apt update
sudo apt install -y \
    git \
    curl \
    python3-pip \
    pipx \
    chromium-browser \
    openssh-server \
    xrdp

echo "✅ System packages installed"

echo ""
echo "=================================="
echo "PHASE 2: NODE.JS & NPM"
echo "=================================="

# Check if NVM exists
if [ ! -d "$HOME/.nvm" ]; then
    echo "📥 Installing NVM (Node Version Manager)..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
else
    echo "✅ NVM already installed"
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
fi

echo "📥 Installing Node.js v22.22.0..."
nvm install 22.22.0
nvm use 22.22.0
nvm alias default 22.22.0

echo "✅ Node.js installed"

echo ""
echo "📥 Installing global NPM packages..."
npm install -g clawhub openclaw playwright pnpm

echo "✅ Global NPM packages installed"

# Verify
echo ""
echo "🔍 Verifying installations..."
echo "  Node: $(node --version)"
echo "  NPM: $(npm --version)"
echo "  OpenClaw: $(openclaw --version)"

echo ""
echo "=================================="
echo "PHASE 3: PYTHON PACKAGES"
echo "=================================="

echo "📥 Installing Python packages..."
pip3 install --upgrade pip
pip3 install \
    argcomplete \
    Pygments \
    requests \
    rich

echo "✅ Python packages installed"

echo ""
echo "=================================="
echo "PHASE 4: SKILLS REINSTALLATION"
echo "=================================="

# Determine workspace location
WORKSPACE="${1:-.openclaw/workspace}"
if [[ ! "$WORKSPACE" = /* ]]; then
    WORKSPACE="$HOME/$WORKSPACE"
fi

echo "📦 Target workspace: $WORKSPACE"

if [ -d "$WORKSPACE/skills" ]; then
    echo "✅ Workspace already exists with skills directory"
else
    echo "⚠️  Skills directory not found. Ensure git clone was successful."
    echo "    Expected: $WORKSPACE/skills"
fi

echo ""
echo "📥 Installing ClawHub skills..."

# Skills to install via clawhub
SKILLS=(
    "ai-pdf-builder"
    "airtable"
    "apollo"
    "bird"
    "ga4"
    "gsc"
    "google-workspace"
    "marketing-skills"
    "md-slides"
    "nano-pdf"
    "otter"
    "pdf"
    "pdf-form-filler"
    "pdf-merge-split"
    "pdf-to-docx"
    "quality-documentation-manager"
    "report-generator"
    "slidespeak"
    "tweet-writer"
    "weather"
)

count=0
for skill in "${SKILLS[@]}"; do
    count=$((count + 1))
    echo "  [$count/20] Installing $skill..."
    cd "$WORKSPACE" && clawhub install "$skill" --no-input 2>/dev/null || echo "    ⚠️  $skill install returned status code $?"
done

echo "✅ ClawHub skills installed"

echo ""
echo "=================================="
echo "PHASE 5: CRON JOBS"
echo "=================================="

echo "⏰ Setting up cron job for daily backups..."
# Add cron job if not present
if ! crontab -l 2>/dev/null | grep -q "backup.sh"; then
    (crontab -l 2>/dev/null || echo ""; echo "# Daily git backup at 2 AM"; echo "0 2 * * * $WORKSPACE/backup.sh >> /tmp/backup.log 2>&1") | crontab -
    echo "✅ Cron job added"
else
    echo "✅ Cron job already exists"
fi

echo ""
echo "=================================="
echo "PHASE 6: VERIFICATION"
echo "=================================="

echo "🔍 Verifying complete installation..."

# Check key files exist
if [ -f "$WORKSPACE/MEMORY.md" ]; then
    echo "  ✅ MEMORY.md found"
else
    echo "  ❌ MEMORY.md NOT found (repo may not be cloned)"
fi

if [ -f "$WORKSPACE/.env" ]; then
    echo "  ✅ .env found"
else
    echo "  ⚠️  .env NOT found (expected - credentials needed)"
fi

if [ -d "$WORKSPACE/skills" ]; then
    SKILL_COUNT=$(ls -1 "$WORKSPACE/skills" | wc -l)
    echo "  ✅ Skills directory found ($SKILL_COUNT skills)"
fi

# Check command availability
if command -v openclaw &> /dev/null; then
    echo "  ✅ openclaw command available"
else
    echo "  ❌ openclaw command NOT found"
fi

if command -v clawhub &> /dev/null; then
    echo "  ✅ clawhub command available"
else
    echo "  ❌ clawhub command NOT found"
fi

echo ""
echo "=================================="
echo "PHASE 7: NEXT STEPS (MANUAL)"
echo "=================================="

echo ""
echo "✅ Automated setup complete!"
echo ""
echo "📝 YOU STILL NEED TO DO:"
echo ""
echo "1️⃣  RESTORE CREDENTIALS (15 min)"
echo "   - Create/update $WORKSPACE/.env with:"
echo "     • ANTHROPIC_API_KEY"
echo "     • X_STANLEYBODEWELL_* (5 keys)"
echo "     • X_ITSOLZ_* (5 keys)"
echo "     • APOLLO_API_KEY"
echo "     • AIRTABLE_API_KEY"
echo ""
echo "2️⃣  UPDATE OPENCLAW CONFIG"
echo "   - Add Telegram bot token to openclaw.json"
echo "   - Add gateway auth token to openclaw.json"
echo ""
echo "3️⃣  VERIFY INSTALLATION"
echo "   $ openclaw status          # Should show agent ready"
echo "   $ clawhub list             # Should show 27+ skills"
echo "   $ source .env && echo \$ANTHROPIC_API_KEY  # Should print key"
echo ""
echo "4️⃣  GIT SSH KEY (if pushing new commits)"
echo "   $ ssh-keygen -t ed25519 -C 'clawdbot@stan'"
echo "   $ ssh -T git@github.com    # Verify connection"
echo ""
echo "❓ Need help? Check REBUILD-INVENTORY.md"
echo ""
echo "=================================="
echo "🎉 BOOTSTRAP COMPLETE!"
echo "=================================="

exit 0
