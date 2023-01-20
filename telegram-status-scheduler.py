import asyncio
import datetime
import logging
import time
import os
from enum import Enum

from pyrogram import Client, enums, types
import aioschedule as schedule


loop = asyncio.get_event_loop()


class EmojiStatus(Enum):
    WORK = 5249273776079640466
    REST = 5246842176050046092
    SLEEP = 5247100325059370738
    EAT = 5244508282231465075


async def set_emoji_status(emoji: EmojiStatus):
    client_name = 'telegram'
    api_id = os.environ['TELEGRAM_API_ID']
    api_hash = os.environ['TELEGRAM_API_HASH']

    async with Client(client_name, api_id, api_hash) as telegram:
        await telegram.set_emoji_status(
            types.EmojiStatus(custom_emoji_id=emoji.value))


def main():
    schedule.every().monday.at("11:15").do(set_emoji_status, emoji=EmojiStatus.WORK)
    schedule.every().tuesday.at("11:15").do(set_emoji_status, emoji=EmojiStatus.WORK)
    schedule.every().wednesday.at("11:15").do(set_emoji_status, emoji=EmojiStatus.WORK)
    schedule.every().thursday.at("11:15").do(set_emoji_status, emoji=EmojiStatus.WORK)
    schedule.every().friday.at("11:15").do(set_emoji_status, emoji=EmojiStatus.WORK)

    schedule.every().monday.at("20:00").do(set_emoji_status, emoji=EmojiStatus.REST)
    schedule.every().tuesday.at("20:00").do(set_emoji_status, emoji=EmojiStatus.REST)
    schedule.every().wednesday.at("20:00").do(set_emoji_status, emoji=EmojiStatus.REST)
    schedule.every().thursday.at("20:00").do(set_emoji_status, emoji=EmojiStatus.REST)
    schedule.every().friday.at("20:00").do(set_emoji_status, emoji=EmojiStatus.REST)
    schedule.every().saturday.at("12:00").do(set_emoji_status, emoji=EmojiStatus.REST)
    schedule.every().sunday.at("12:00").do(set_emoji_status, emoji=EmojiStatus.REST)

    schedule.every().monday.at("23:00").do(set_emoji_status, emoji=EmojiStatus.SLEEP)
    schedule.every().tuesday.at("23:00").do(set_emoji_status, emoji=EmojiStatus.SLEEP)
    schedule.every().wednesday.at("23:00").do(set_emoji_status, emoji=EmojiStatus.SLEEP)
    schedule.every().thursday.at("23:00").do(set_emoji_status, emoji=EmojiStatus.SLEEP)
    schedule.every().friday.at("23:00").do(set_emoji_status, emoji=EmojiStatus.SLEEP)
    schedule.every().saturday.at("23:00").do(set_emoji_status, emoji=EmojiStatus.SLEEP)
    schedule.every().sunday.at("23:00").do(set_emoji_status, emoji=EmojiStatus.SLEEP)

    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(1)


if __name__ == "__main__":
    main()
