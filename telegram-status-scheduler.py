import asyncio
import logging
import zoneinfo
import os
from enum import Enum

from pyrogram import Client, types
import uvloop
import aiocron


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class EmojiStatus(Enum):
    """Enum values must be equal to telegram emoji ids"""
    WORK = 5249273776079640466
    REST = 5246842176050046092
    SLEEP = 5247100325059370738
    EAT = 5244508282231465075


def setup_cron():
    """Declare scheduler cron-like rules here"""
    logging.info('Setup cron schedule')
    tz = zoneinfo.ZoneInfo("Europe/Moscow")
    
    # Work - Weekdays from 11:15
    aiocron.crontab('15 11 * * 1-5', func=set_emoji_status, args=(EmojiStatus.WORK,), start=True, tz=tz)
    # Rest - Weekdays from 20:00
    aiocron.crontab('0 20 * * 1-5', func=set_emoji_status, args=(EmojiStatus.REST,), start=True, tz=tz)
    # Rest - Weekend from 12:00
    aiocron.crontab('0 12 * * 6-7', func=set_emoji_status, args=(EmojiStatus.REST,), start=True, tz=tz)
    # Sleep - Every day from 23:00
    aiocron.crontab('0 23 * * *', func=set_emoji_status, args=(EmojiStatus.SLEEP,), start=True, tz=tz)


async def set_emoji_status(emoji: EmojiStatus):
    logging.info('Set emoji status {}'.format(emoji.name))

    client_name = 'telegram'
    api_id = os.environ['TELEGRAM_API_ID']
    api_hash = os.environ['TELEGRAM_API_HASH']

    async with Client(client_name, api_id, api_hash) as telegram:
        result = await telegram.set_emoji_status(
            types.EmojiStatus(custom_emoji_id=emoji.value))
        if result is not True:
            logging.error('Cannot set emoji status')


async def main():
    logging.info('Start scheduler')
    setup_cron()
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    # uvloop.install() speeds up pyrogram performance
    uvloop.install()
    asyncio.run(main())
