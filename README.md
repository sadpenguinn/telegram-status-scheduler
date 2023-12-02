# telegram-status-scheduler

## Description

Change telegram emoji statuses by schedule.

## Dependencies

### Telegram API

Provide credentials with `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `TELEGRAM_PHONE_NUMBER` and `TELEGRAM_PASSWORD`.

## Build & Run

```
docker build -t telegram-status-scheduler -f Dockerfile . && \
docker run -e TELEGRAM_API_ID={your-id} -e TELEGRAM_API_HASH={your-hash} telegram-status-scheduler
```
