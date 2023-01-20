import asyncio
import os
from enum import Enum

from pyrogram import Client, types
import uvloop
import aiocron


class EmojiStatus(Enum):
    """Enum values must be equal to telegram emoji ids"""
    WORK = 5249273776079640466
    REST = 5246842176050046092
    SLEEP = 5247100325059370738
    EAT = 5244508282231465075


def setup_cron():
    """Declare scheduler cron-like rules here"""
    # Work - Weekdays from 11:15
    aiocron.crontab('15 11 * * 1-5', func=set_emoji_status, args=(EmojiStatus.WORK,), start=True)
    # Rest - Weekdays from 20:00
    aiocron.crontab('0 20 * * 1-5', func=set_emoji_status, args=(EmojiStatus.REST,), start=True)
    # Rest - Weekend from 12:00
    aiocron.crontab('0 12 * * 6-7', func=set_emoji_status, args=(EmojiStatus.REST,), start=True)
    # Sleep - Every day from 23:00
    aiocron.crontab('0 23 * * *', func=set_emoji_status, args=(EmojiStatus.SLEEP,), start=True)


async def set_emoji_status(emoji: EmojiStatus):
    client_name = 'telegram'
    api_id = os.environ['TELEGRAM_API_ID']
    api_hash = os.environ['TELEGRAM_API_HASH']

    async with Client(client_name, api_id, api_hash) as telegram:
        await telegram.set_emoji_status(
            types.EmojiStatus(custom_emoji_id=emoji.value))


async def main():
    setup_cron()
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    # uvloop.install() speeds up pyrogram performance
    uvloop.install()
    asyncio.run(main())
