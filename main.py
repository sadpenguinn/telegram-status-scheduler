import asyncio
import logging
import zoneinfo
import os

import uvloop
import aiocron
import yaml
import dotenv
from pyrogram import Client, types


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def load_dotenv():
    dotenv.load_dotenv()


def parse_config():
    with open('config.yaml', 'r') as config_file:
        return yaml.safe_load(config_file)


def setup_cron():
    logging.info('Setup cron schedule')

    tz = zoneinfo.ZoneInfo("Europe/Moscow")
    cfg = parse_config()

    for emoji, schedule in cfg['schedule'].items():
        emoji_id = cfg['emoji'][emoji]
        for schedule_time in schedule:
            aiocron.crontab(schedule_time, func=set_emoji_status, args=(emoji_id,), start=True, tz=tz)


async def set_emoji_status(emoji: int):
    logging.info('Set emoji status {}'.format(emoji))

    api_id = os.environ['TELEGRAM_API_ID']
    api_hash = os.environ['TELEGRAM_API_HASH']

    async with Client(':memory:', api_id, api_hash) as telegram:
        result = await telegram.set_emoji_status(
            types.EmojiStatus(custom_emoji_id=emoji))
        if result is not True:
            logging.error('Cannot set emoji status')


async def main():
    logging.info('Start scheduler')
    load_dotenv()
    setup_cron()
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    # uvloop.install() speeds up pyrogram performance
    uvloop.install()
    asyncio.run(main())
