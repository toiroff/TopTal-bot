from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Restart bot"),
            types.BotCommand("lang", "Choose a Language "),
            types.BotCommand("help", "Commands"),
        ]
    )
