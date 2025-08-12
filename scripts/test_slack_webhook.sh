
#!/usr/bin/env bash
set -euo pipefail
if [ -z "${ALERT_SLACK_WEBHOOK:-}" ]; then
  echo "Set ALERT_SLACK_WEBHOOK env variable first"; exit 1;
fi
curl -X POST -H 'Content-type: application/json'   --data '{"text":"Test alert from Smart Retail Intelligence :rocket:"}'   "$ALERT_SLACK_WEBHOOK"
echo "OK"
