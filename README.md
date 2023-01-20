# telegram-status-scheduler

Change telegram emoji statuses by schedule.

### How to use

- Specify telegram emoji ids in `EmojiStatus` enum
- Declare scheduler cron-like rules in `setup_cron()` function
- Run `telegram-status-scheduler.py` from terminal. It will generate `telegram.session` file needed by `docker build`
- Pass `TELEGRAM_API_ID` and `TELEGRAM_API_HASH` to `docker run` command
