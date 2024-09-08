from discord import Intents
from asyncio import run

from .constants import Bot
from bot.bot import Pudimversify


async def main() -> None:
    bot = Pudimversify(
        command_prefix=Bot.prefix,
        intents=Intents.all(),
        case_insensitive=True,
    )

    async with bot:
        await bot.start(Bot.token)


if __name__ == "__main__":
    run(main())