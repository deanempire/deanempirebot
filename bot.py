import discord
from discord.ext import commands
from discord.ext.commands import Bot

prefix= "+"

Bot = commands.Bot ( command_prefix = prefix )

@Bot.event 

async def on_ready():
    print ( 'BOT connected' )

@Bot.event
async def on_command_error (ctx, error):
	pass

Bot.remove_command('help')

#ahelp
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )
async def ahelp(ctx):
	await ctx.channel.purge (limit = 1)
	await ctx.author.send (f' ```Информация о командах \n \n +mute [Пользователь] [Причина] - Выдать мут участнику \n +ban [Пользователь] [Причина] - Выдать бан участнику \n +uninvite [Пользователь] - Снять роль **♥ Dean Empire ♥**``` ')
	await ctx.author.send (f' ```\n +unban [Пользователь] - Разбанить участника \n +clear [Количество строк] - Удалить сообщения \n +say [Текст] - Сделать объявление \n +kick [Пользователь] [Причина] - Кикнуть участника \n +invite [Пользователь] - Выдать роль **♥ Dean Empire ♥** ``` ')
	await ctx.author.send (f' ```\n +vmute [Пользователь] [Причина] - Выдать мут гостю \n +unvmute [Пользователь] - Снять мут с гостя``` ')

@ahelp.error
async def ahelp_error( ctx, error ):
	author = ctx.message.author

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

#help

@Bot.command(pass_context = True)
async def help (ctx):
	await ctx.send (f' ```Информация о командах \n \n +help - Показать список всех команд \n +пинок [Пользователь] - Дать пинка \n +sms [Пользователь] [Текст] - Отправить личное сообщение пользователю от имени бота``` ')

#MSG
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True ) 

async def say( ctx, *,  arg):
    await ctx.channel.purge (limit = 1) 
    
    await ctx.send( arg)

@say.error
async def say_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+say [Текст]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

# Unban
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def unban(ctx, *, member):
    await ctx.channel.purge (limit = 1)

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban( user )
        await ctx.send (f'Пользователь {user.mention} разбанен.')

        return

@unban.error
async def unban_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+unban [Пользователь]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

#Mute
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def mute(ctx, member: discord.Member, reason = None ):
    await ctx.channel.purge (limit = 1)
    author = ctx.message.author

    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Mute Dean' )

    await member.add_roles (mute_role)

    dean_role = discord.utils.get(ctx.message.guild.roles, name = '♥ Dean Empire ♥')
	
    await member.remove_roles (dean_role)

    await ctx.send( f'Пользователь {member.mention} получил ограничение чата от пользователя {author.mention}. Причина: **{reason}**' )

@mute.error
async def mute_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+mute [Пользователь] [Причина]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

#unmute
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def unmute(ctx, member:discord.Member):
	await ctx.channel.purge (limit = 1)
	author = ctx.message.author

	dean_role = discord.utils.get(ctx.message.guild.roles, name = '♥ Dean Empire ♥')
	
	await member.add_roles (dean_role)

	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Mute Dean')

	await member.remove_roles ( mute_role )

	await ctx.send( f' Пользователь {author.mention} снял ограничения чата с пользователя {member.mention} ' )

@unmute.error
async def unmute_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+unmute [Пользователь]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )
async def vmute(ctx, member: discord.Member, reason = None ):
    await ctx.channel.purge (limit = 1)
    author = ctx.message.author

    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Muted' )

    await member.add_roles (mute_role)

    visitor_role = discord.utils.get(ctx.message.guild.roles, name = 'Гость')
	
    await member.remove_roles (visitor_role)

    await ctx.send( f'Пользователь {member.mention} получил ограничение чата от пользователя {author.mention}. Причина: **{reason}**' )

#unvmute
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def unvmute(ctx, member:discord.Member):
	await ctx.channel.purge (limit = 1)
	author = ctx.message.author

	visitor_role = discord.utils.get(ctx.message.guild.roles, name = 'Гость')
	
	await member.add_roles (visitor_role)

	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')

	await member.remove_roles ( mute_role )

	await ctx.send( f'Пользователь {author.mention} снял ограничения чата с пользователя {member.mention} ' )

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

# Clear message
@Bot.command (pass_context = True)
@commands.has_permissions( administrator = True )

async def clear(ctx, amount = 10 ):
    await ctx.channel.purge( limit = amount)

@clear.error
async def clear_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+clear [Количество строк]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

# Kick
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1 )
    author = ctx.message.author

    await member.send (f'Вы были исключены с сервера пользователем **{ctx.author.name}** по причине "{reason}" ')

    await member.kick(reason = reason)

    await ctx.send (f'Пользователь {author.mention} кикнул {member.mention} с сервера. Причина: "{reason}"')

@kick.error
async def kick_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+kick [Пользователь] [Причина]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

# Ban
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def ban (ctx, member: discord.Member, *, reason = None):
    author = ctx.message.author

    await member.send (f'Вы были забанены пользователем **{ctx.author.name}** по причине "{reason}" ')

    await member.ban(reason = reason)

    await ctx.send (f'Пользователь {author.mention} забанил {member.mention}. Причина: "{reason}"')

@ban.error
async def ban_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+ban [Пользователь] [Причина]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

#Пинок
@Bot.command(pass_context = True)

async def пинок(ctx, member:discord.Member):
	await ctx.channel.purge(limit = 1 )
	author = ctx.message.author

	await ctx.send( f'{author.mention} дал пинка пользователю {member.mention} ' )

	return

@пинок.error
async def пинок_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+пинок [Пользователь]``` ')

#Role Mendez
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def invite(ctx, member:discord.Member):
    await ctx.channel.purge (limit = 1)
    author = ctx.message.author

    dean_role = discord.utils.get(ctx.message.guild.roles, name = '♥ Dean Empire ♥')

    visitor_role = discord.utils.get(ctx.message.guild.roles, name = 'Гость')

    await member.remove_roles (visitor_role)

    await member.add_roles (dean_role)

    await ctx.send( f' Пользователь {author.mention} выдал роль **♥ Dean Empire ♥** пользователю {member.mention} ' )

@invite.error
async def invite_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+invite [Пользователь]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

#uninvite
@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )

async def uninvite(ctx, member:discord.Member):
	await ctx.channel.purge (limit = 1)
	author = ctx.message.author

	dean_role = discord.utils.get(ctx.message.guild.roles, name = '♥ Dean Empire ♥')
	
	await member.remove_roles (dean_role)

	visitor_role = discord.utils.get(ctx.message.guild.roles, name = 'Гость')

	await member.add_roles (visitor_role)

	await ctx.send( f' Пользователь {author.mention} снял роль **♥ Dean Empire ♥** с пользователя {member.mention} ' )

@uninvite.error
async def uninvite_error( ctx, error ):
	author = ctx.message.author
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+uninvite [Пользователь]``` ')

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send (f'{author.mention}, **у вас недостаточно прав для использования данной команды!** ')

#sms
@Bot.command(pass_context = True)

async def sms(ctx, member:discord.Member, *,  arg):
	author = ctx.message.author
	await ctx.channel.purge (limit = 1) 
	await ctx.author.send (f'Ваше сообщение было отправлено {member}. Текст: **{arg}**')
	await member.send(f'Вам сообщение: **{arg}**' )

@sms.error
async def sms_error( ctx, error ):
	
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f' ```+sms [Пользователь] [Текст]``` ')


Bot.run ('Njk3NDEyMjI2MjQzNDkzOTY5.Xo3_pQ.WAsTYLWNxUPEKL5L-f8ULwtIdl4')