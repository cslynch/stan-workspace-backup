#!/bin/bash
# SupaBrain search bridge script

QUERY="$1"
ENDPOINT="https://olmaksvjanknqzndalzv.supabase.co/functions/v1/brain-api"
TOKEN="${BRAIN_API_SECRET}"

if [ -z "$QUERY" ]; then
    echo "Usage: supabrain-search.sh \"<query>\""
    exit 1
fi

if [ -z "$TOKEN" ]; then
    echo "ERROR: BRAIN_API_SECRET not set"
    exit 1
fi

# Call the SupaBrain API
curl -s -X POST "$ENDPOINT" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"action\": \"search\", \"query\": \"$QUERY\"}"

echo ""
