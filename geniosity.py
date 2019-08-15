from discord.utils import *


async def print_geniosity(bot, message):
	await bot.send_message(message.channel, '<:geniosity:554459617271480321>')


async def react_geniosity(bot, message):
	emoji = get(bot.get_all_emojis(), name='geniosity')
	await bot.add_reaction(message, emoji)


async def react_wtmoo(bot, message):
	emoji = get(bot.get_all_emojis(), name='wtmoo')
	await bot.add_reaction(message, emoji)


async def react_headpat(bot, message):
	emoji = get(bot.get_all_emojis(), name='blobpat')
	await bot.add_reaction(message, emoji)

async def react_ayaya(bot, message):
	emoji = get(bot.get_all_emojis(), name='ayaya')
	await bot.add_reaction(message, emoji)

async def react_egg(bot, message):
	await bot.add_reaction(message, "🥚")

async def react_ship(bot, message):
	await bot.add_reaction(message, "❤")
	await bot.add_reaction(message, "🚢")

async def react_orz(bot, message):
	emoji = get(bot.get_all_emojis(), name='orz')
	await bot.add_reaction(message, emoji)


async def react_juicy(bot, message):
	emoji = get(bot.get_all_emojis(), name='juicy')
	await bot.add_reaction(message, emoji)


async def react_tmw(bot, message):
	await bot.add_reaction(message, '🇹')
	await bot.add_reaction(message, '🇲')
	await bot.add_reaction(message, '🇼')
	await bot.add_reaction(message, '❤')
