#!/bin/sh

# CELERY WORKER & BEAT
until cd /app/server; do
  echo "Waiting for server volume..."
done

# run a worker and beat
celery -A fabrique worker --beat --scheduler django --loglevel=info
