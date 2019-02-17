import discord, datetime, time
from discord.ext import commands
import inspect
from discord.utils import get
import random
import json
import asyncio
import traceback
import aiohttp
import os

start_time = time.time()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("d!"))
bot.remove_command('help')
now = datetime.datetime.now()
                 
@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)

cont = ["**|*** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found a common item: **3,500 Crystals**",
        "**|** You found a common item: **125 Double Armor**",
        "**|** You found a common item: **125 Double Damage**",
        "**|** You found a common item: **125 Speed Boost**",
        "**|** You found a common item: **125 Mines**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: **5 Gold Boxes**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: **5 Gold Boxes**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: **5 Gold Boxes**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: **5 Gold Boxes**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommmon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: **5 Gold Boxes**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: **5 Gold Boxes**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: **5 Gold Boxes**",
        "**|** You found an uncommon item: **10,000 Crystals**",
        "**|** You found an uncommon item: **125 Repair Kits**",
        "**|** You found an uncommon item: **100 0f all Supplies**",
        "**|** You found an uncommon item: **3 days of Premium Account**",
        "**|** You found an uncommon item: *5 Gold Boxes**",
        "**|** You found a rare item: **25,000 Crystals**",
        "**|** You found a rare item: **250 of all Supplies**",
        "**|** You found a rare item: **10 days of Premium Account**",
        "**|** You found a rare item: **10 Gold Boxes**",
        "**|** You found a rare item: **A paint from the garage**",
        "**|** You found a rare item: **25,000 Crystals**",
        "**|** You found a rare item: **250 of all Supplies**",
        "**|** You found a rare item: **10 days of Premium Account**",
        "**|** You found a rare item: **10 Gold Boxes**",
        "**|** You found a rare item: **25,000 Crystals**",
        "**|** You found a rare item: **250 of all Supplies**",
        "**|** You found a rare item: **10 days of Premium Account**",
        "**|** You found a rare item: **10 Gold Boxes**",
        "**|** You found a rare item: **25,000 Crystals**",
        "**|** You found a rare item: **250 of all Supplies**",
        "**|** You found a rare item: **10 days of Premium Account**",
        "**|** You found a rare item: **10 Gold Boxes**",
        "**|** You found an epic item: **Frost paint**",
        "**|** You found an epic item: **Golden Star**",
        "**|** You found an epic item: **Frost paint**",
        "**|** You found an epic item: **Golden Star**",
        "**|** You found a legendary item: **Moonwalker paint**",
        "**|** You found a legendary item: **Eternity paint**",
        "**|** You found a legendary item: **Red Suit paint**",
        "**|** You found a legendary item: **Flow**",
        "**|** You found a legendary item: **Nightmare**",
        "**|** You found a legendary item: **Spectre**",
        "**|** You found a legendary item: **Holiday Lights**",
        "**|** You found a legendary item: **Vertigo**",
        "**|** You found a legendary item: **Matrix**",
        "**|** You found a legendary item: **Mosaic**"]

@bot.event
async def on_message(message):
	if message.content.startswith("d!c open"):
		channel = message.channel
		await bot.send_typing(message.channel)
		embed = discord.Embed(title="Tanki Online", url="https://discordbots.org/bot/409253229491126285", descrption="Tanki Online", color=0x42d9f4)
		embed.set_thumbnail(url="https://imgur.com/yf0oeDe.png")
		embed.add_field(name="container", value=random.choice(cont))
		await bot.send_message(channel, embed=embed)
	await bot.process_commands(message)
	
@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is " + str(squared_value))
	
@bot.command(pass_context=True, no_pm=True)
async def infos(ctx):
	"""Show server info."""
	members = set(ctx.message.server.members)
	offline = filter(lambda m: m.status is discord.Status.offline, members)
	offline = set(offline)
	bots = filter(lambda m: m.bot, members)
	bots = set(bots)
	users = members - bots
	servericon = ctx.message.server.icon_url
	channel_passed = (ctx.message.timestamp - ctx.message.channel.created_at).days 
	server_passed = (ctx.message.timestamp - ctx.message.server.created_at).days
	channel_created_at = ("Created on {} ({} days ago!)".format(ctx.message.channel.created_at.strftime("%d %b %Y %H:%M"), channel_passed))
	server_created_at = ("Created on {} ({} days ago!)".format(ctx.message.server.created_at.strftime("%d %b %Y %H:%M"), server_passed))
	try:
		em = discord.Embed(description="{}, here you go:".format(ctx.message.author.mention), color=0X008CFF, title="Server Info")
		em.set_thumbnail(url=servericon)
		em.add_field(name="Server Name", value=str(ctx.message.server.name))
		em.add_field(name="Server ID", value=str(ctx.message.server.id))
		em.add_field(name="Server Region", value=str(ctx.message.server.region))
		em.add_field(name="Server Verification", value=str(ctx.message.server.verification_level))
		em.add_field(name="Server Created At", value=str(server_created_at))
		em.add_field(name="Server Roles", value=str(len(ctx.message.server.roles) - 1))
		em.add_field(name="Server Owner", value=str(ctx.message.server.owner.name))
		em.add_field(name="Owner ID", value=str(ctx.message.server.owner.id))
		em.add_field(name="Owner Nick", value=str(ctx.message.server.owner.nick))
		em.add_field(name="Owner Status", value=str(ctx.message.server.owner.status))
		em.add_field(name="Total Bots", value=str(len(bots)))
		em.add_field(name="Bots Online", value=str(len(bots - offline)))
		em.add_field(name="Bots Offline", value=str(len(bots & offline)))
		em.add_field(name="Total Users", value=str(len(users)))
		em.add_field(name="Online Users", value=str(len(users - offline)))
		em.add_field(name="Offline Users", value=str(len(users & offline)))
		em2 = discord.Embed(color=0X008CFF)
		em2.add_field(name="Channel Name", value=str(ctx.message.channel.name))
		em2.add_field(name="Channel ID", value=str(ctx.message.channel.id))
		em2.add_field(name="Channel Default", value=str(ctx.message.channel.is_default))
		em2.add_field(name="Channel Position", value=str(ctx.message.channel.position + 1))
		em2.add_field(name="Channel Created At", value=str(channel_created_at))
		await bot.say(embed=em)
		await bot.say(embed=em2)
	except discord.HTTPException:
		await bot.say("An unknown error occured while sending the embedded message.")
			
@bot.command(pass_context=True)
async def autobaselink(ctx):
	try:
		x = int(ctx.message.content[15:])
		await bot.say("**Your bot's invite link is:** <https://discordapp.com/oauth2/authorize?&client_id=" + str(x) + "&scope=bot&permissions=8>")
	except:
		text = await bot.say("**Invalid client id, recheck the id and make sure that you didn't accidentally use your bot token or client secret <@" + str(ctx.message.author.id) + ">**")
		await bot.delete_message(ctx.message)
		await asyncio.sleep(5)
		await bot.delete_message(text)

@bot.command(pass_context=True)
async def reverse(self, ctx, *, msg: str):
	"""ffuts esreveR"""
	await bot.say(msg[::-1])
	
@bot.command(pass_context=True)
async def renamechannel(ctx, channel: discord.Channel, *, new_name):
    await channel.edit(name=new_name)
	
@bot.command(pass_context=True)
async def staffrequest(ctx, *, msg):
	owner = ctx.message.server.owner
	author = ctx.message.author
	await bot.send_message(owner, msg)
	await bot.send_message(owner, " Requested by " + author.name)
	await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
async def botinfo(ctx):
	embed=discord.Embed(title="Bot name", description="Tanki Online", color=0xFFFF00)
	embed.add_field(name="Creator", value="noobperson#2436")
	embed.add_field(name="Invite link", value="[Click Here!](https://discordapp.com/api/oauth2/authorize?client_id=409253229491126285&permissions=2146958839&scope=bot)")
	embed.add_field(name="Prefix", value="d!")
	await bot.say(embed=embed)
	
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "Ban list", description = x, color = 0xFFFFF)
    return await bot.say(embed = embed)
	
@bot.command()
async def stats():
	servers = list(bot.servers)
	current_time = time.time()
	difference = int(round(current_time - start_time))
	text = str(datetime.timedelta(seconds=difference))
	embed = discord.Embed(title="Servers:", description=f"{str(len(servers))}", color=0xFFFF)
	embed.add_field(name="Users:", value=f"{str(len(set(bot.get_all_members())))}")
	embed.add_field(name="Uptime:", value=f"{text}")
	await bot.say(embed=embed)
	
@bot.command()
async def invite():
	embed = discord.Embed(description=" ", color=0xFFFF)
	embed.add_field(name="Bot invite", value=f"[Bot invite](https://discordapp.com/api/oauth2/authorize?client_id=409253229491126285&permissions=469854214&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D409253229491126285%26permissions%3D2146958839%26scope%3Dbot&scope=bot)")
	embed.add_field(name="Support server", value=f"[https://discord.gg/bweznkF](https://discord.gg/bweznkF)")
	await bot.say(embed=embed)
			
@bot.command(pass_context=True)
async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color=0x00D5FF)
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = 'Owner', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = 'ID', value = str(server.id))
    join.add_field(name = 'Member Count', value = str(server.member_count));
    join.add_field(name = 'Text/Voice Channels', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await bot.say(embed = join);
				
@bot.command(pass_context=True)
async def ratings(ctx, user: str):
	url = "http://ratings.tankionline.com/get_stat/profile/?user={}&lang=en".format(user)
	async with aiohttp.get(url) as r:
		if r.status == 200:
			try:
				response = (await r.json ())["response"]
				await bot.send_typing(ctx.message.channel)
				kills = response["kills"]
				deaths = response["deaths"]
				crystals = response["earnedCrystals"]
				gold = response["caughtGolds"]
				experience = response["score"]
				premium = response["hasPremium"]
				ranks = response["rank"]
				gearscore = response["gearScore"]
				scores = response["scoreLeft"]
				embed = discord.Embed(title="Statistics for {}".format(user), url="http://ratings.tankionline.com/en/user/{}/".format(user), \
						      description="**Profile:**", color=0x42d9f4)
				embed.add_field(name="Nickname", value="{}".format(user), inline=False)
				embed.add_field(name="Rank", value="{}".format(ranks), inline=False)
				embed.add_field(name="Premium Account", value="{}".format(premium), inline=False)
				embed.add_field(name="Experience", value="{:,}".format(experience), inline=False)
				embed.add_field(name="Experience left", value="{:,}".format(scores), inline=False)
				embed.add_field(name="Crystals Obtained", value="{:,}".format(crystals), inline=False)
				embed.add_field(name="Gold Boxes Caught", value="{:,}".format(gold), inline=False)
				embed.add_field(name="Gear Score", value="{}".format(gearscore), inline=False)
				embed.add_field(name="Kills", value="{:,}".format(kills), inline=False)
				embed.add_field(name="Deaths", value="{:,}".format(deaths), inline=False)
				embed.add_field(name="K/D", value="{0:.2f}".format(kills/deaths), inline=False)
				await bot.say(embed=embed)
				channel = bot.get_channel('525109045221261312')
				embed = discord.Embed(title=f"User: {ctx.message.author.name} have used ratings command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
				await bot.send_message(channel, embed=embed)
			except:
				await bot.say("Account does not exist.")
    			
@bot.command(pass_context=True)
async def noobs(ctx, *, reportmsg: str):
    channel = bot.get_channel('503634621699850250')
    embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Report: {reportmsg}", color=0xff9393)        
    await bot.send_message(channel, embed=embed)
    embed = discord.Embed(title="Your report has been submitted and we will get back to you as soon as possible", description=f"Case details: {reportmsg} ", color=0xff9393)       
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def noobs2(ctx, *, reportmsg: str):
    channel = bot.get_channel('503634621699850250')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Suggestion: {reportmsg}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
    embed = discord.Embed(title="Your suggestion has been submitted and we will get back to you as soon as possible", description=f"Suggestion details: {reportmsg} ", color=0xff9393)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    """Pings the bot and gets a response time."""
    pingtime = time.time()
    pingms = await bot.say("Pinging...")
    ping = (time.time() - pingtime) * 1000
    await bot.edit_message(pingms, "Pong! :ping_pong: ping time is `%dms`" % ping)
	
@bot.command(name="setnick", pass_context=True)
@commands.has_permissions(manage_nicknames=True)     
async def _setnick(ctx, user: discord.Member, *, nickname):
    await bot.change_nickname(user, nickname)
    await bot.delete_message(ctx.message)
    
@_setnick.error
async def setnick_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, you do not have a manage nickname permission.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
		
@bot.command(name="rep", pass_context=True)
@commands.cooldown(1, 86400, commands.BucketType.user)
async def _rep(ctx, user: discord.Member = None):
	author = ctx.message.author
	await bot.say(f"*** :up: | {author.name} has given {user.mention} a reputation point!***".format(author.mention))
	
@_rep.error
async def rep_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
    	msg = ':exclamation: This command is on cooldown, please try again in {:.2f}s :exclamation:'.format(error.retry_after)
    await bot.send_message(ctx.message.channel, msg)
    
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    mod_perms = discord.Permissions(manage_messages=True, kick_members=True, manage_nicknames =True, mute_members=True)
    admin_perms = discord.Permissions(ADMINISTRATOR=True)
    
    await bot.create_role(author.server, name="Owner", permissions=admin_perms)
    await bot.create_role(author.server, name="Admin", permissions=admin_perms)
    await bot.create_role(author.server, name="Senior Moderator", permissions=mod_perms)
    await bot.create_role(author.server, name="G.O.H")
    await bot.create_role(author.server, name="Moderator", permissions=mod_perms)
    await bot.create_role(author.server, name="Muted")
    
    await bot.create_role(author.server, name="Friend of Owner")
    await bot.create_role(author.server, name="Verified")
    everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
    user_perms = discord.PermissionOverwrite(read_messages=True)
    user = discord.ChannelPermissions(target=server.default_role, overwrite=user_perms)
    private_perms = discord.PermissionOverwrite(read_messages=False)
    private = discord.ChannelPermissions(target=server.default_role, overwrite=private_perms)    
    await bot.create_channel(server, '🎉welcome🎉',everyone)
    await bot.create_channel(server, '🎯rules🎯',everyone)
    await bot.create_channel(server, '🎥featured-content🎥',everyone)
    await bot.create_channel(server, '📢announcements📢',everyone)
    await bot.create_channel(server, '📢vote_polls📢',everyone)
    await bot.create_channel(server, 'private_chat',private)
    await bot.create_channel(server, '🎮general_chat🎮',user)
    await bot.create_channel(server, '🎮general_media🎮',user)
    await bot.create_channel(server, '👍bots_zone👍',user)
    await bot.create_channel(server, '🎥youtube_links🎥',user)
    await bot.create_channel(server, '🎥giveaway_links🎥',user)
    await bot.create_channel(server, '🎥other_links🎥',user)
    await bot.create_channel(server, '🔥Music Zone🔥', type=discord.ChannelType.voice)
    await bot.create_channel(server, '🔥music_command🔥s',user)
    await bot.create_channel(server, '🔥Chill Zone🔥', type=discord.ChannelType.voice)
    print(f"{ctx.message.author.name} from {ctx.message.server} used d!setup command")
    
def user_is_me(ctx):
	return ctx.message.author.id == "277983178914922497"
    
@bot.command(name="multicolor", pass_context=True)
@commands.check(user_is_me)
async def _multicolor(ctx, role: discord.Role, speed: int):
	embed = discord.Embed(description=f":rainbow: \n Speed - **{speed}** \n Role - **{role}**")
	await bot.say(embed=embed)
	while True:
		rainrolecolor = random.randint(0, 0xffffff)
		await bot.edit_role(ctx.message.server, role, color=discord.Colour(rainrolecolor))
		await asyncio.sleep(speed)
		
@_multicolor.error
async def multicolor_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, this command is in development so you can't use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
		
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def leave(ctx, *args):
	server = bot.get_server(*args)
	await bot.leave_server(server)
		
@bot.command(pass_context=True)
async def coinflip(ctx):
    user = ctx.message.author
    side = random.randint(0, 1)
    server = ctx.message.server
    join = discord.Embed(title="Tanki Online ", description=" ", color=0x008790)
    if side == 0:
        join.add_field(name="the coin landed on:", value="Heads!", inline=False)
        join.set_footer(text='Requested by: ' + user.name)
        await bot.send_message(ctx.message.channel, embed=join)
    if side == 1:
        join.add_field(name="the coin landed on:", value="Tails!", inline=False)
        join.set_footer(text='Requested by: ' + user.name)
        await bot.send_message(ctx.message.channel, embed=join)
        channel = bot.get_channel('525109045221261312')
        embed = discord.Embed(title=f"User: {ctx.message.author.name} have used coinflip command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
        await bot.send_message(channel, embed=embed)
		
@bot.command(name='eval', pass_context=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await bot.say(await res)
    else:
    	await bot.delete_message(ctx.message)
    	await bot.say(res)
        
@_eval.error
async def eval_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You can't use this command only the bot owner can do this.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command()
@commands.check(user_is_me)
async def servers():
  servers = list(bot.servers)
  await bot.say("Connected on " + str(len(bot.servers)) + " servers:")
  await bot.say('\n'.join(server.name for server in servers))
  await bot.say('\n'.join(server.id for server in servers))

@bot.command(pass_context=True)
@commands.check(user_is_me)
async def addrank(ctx, *, name = None):
	author = ctx.message.author
	server = ctx.message.server
	role = discord.utils.get(ctx.message.server.roles, name=name)
	await bot.create_role(server, name=name)
	text = await bot.say("{} created a role {}".format(author.mention, role.name))
	
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def delrank(ctx, *, role_name):
  role = discord.utils.get(ctx.message.server.roles, name=role_name)
  if role:
    try:
      await bot.delete_role(ctx.message.server, role)
      await bot.say("The role {} has been deleted!".format(role.name))
    except discord.Forbidden:
      await bot.say("Missing Permissions to delete this role!")
  else:
    await bot.say("The role doesn't exist!")
	
@bot.command(pass_context=True)
async def bug(ctx, *, reportmsg: str):
    channel = bot.get_channel('503634621699850250')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name} {ctx.message.author.id}", description=f"Bug reports: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    text = embed = discord.Embed(title="Your bug reports has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    channel = bot.get_channel('525109045221261312')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used bug command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
    
@bot.command(pass_context=True)
async def idea(ctx, *, reportmsg: str):
    channel = bot.get_channel('503634621699850250')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name} {ctx.message.author.id}", description=f"Idea: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    embed = discord.Embed(title="Your idea has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    channel = bot.get_channel('525109045221261312')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used idea command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
		
@bot.command(pass_context=True, no_pm=True)
async def userinfo(ctx, user: discord.Member = None):
	if user is None:
		user = ctx.message.author
	embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
	embed.add_field(name="Name:", value=user.name, inline=True)
	embed.add_field(name="ID:", value=user.id, inline=True)
	embed.add_field(name="Status:", value=user.status, inline=True)
	embed.add_field(name='Playing Status:', value=user.game, inline=True)
	embed.add_field(name="Highest Role:", value=user.top_role.mention, inline=True)
	embed.add_field(name="Account Created:", value=user.created_at.strftime("%A, %B %d %Y %H:%M:%S %p"))
	embed.add_field(name="Joined At:", value=user.joined_at.strftime("%A, %B %d %Y %H:%M:%S %p"))
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
	embed.set_footer(text=" | {}".format(user.name), icon_url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
	await bot.say(embed=embed)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used userinfo command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def userinfos(ctx, user: discord.Member = None):
	if user is None:
		user = ctx.message.author
	roles = [role for role in user.roles]
	embed = discord.Embed(colour=user.colour, timestamp=ctx.message.timestamp)
	embed.set_author(name=user)
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
	embed.add_field(name="ID:", value=user.id)
	embed.add_field(name="Guild name:", value=user.display_name)
	embed.add_field(name="Created at:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
	embed.add_field(name="Joined at:", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
	embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
	embed.add_field(name="Top role:", value=user.top_role.mention)
	await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def info(ctx):
	author = ctx.message.author
	servers = list(bot.servers)
	embed = discord.Embed(title="Tanki Online", color=0xFFFF)
	embed.add_field(name="Servers:", value=f"{str(len(servers))}")
	embed.add_field(name="Users:", value=f"{str(len(set(bot.get_all_members())))}")
	embed.add_field(name="Invite", value=f"[Link](https://discordapp.com/api/oauth2/authorize?client_id=409253229491126285&permissions=2146958839&scope=bot)")
	embed.add_field(name="Support server", value=f"[Link](https://discord.gg/bweznkF)")
	embed.add_field(name="Donate", value=f"[Link](https://www.paypal.me/noobpersonTO2)")
	embed.add_field(name="Upvote me", value=f"[Link](https://discordbots.org/bot/409253229491126285/vote)")
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/409253229491126285/b6a655353cf088ea82f91c281cb97e86.png?size=1024")
	embed.set_footer(text=" | {}".format(bot.user.name), icon_url="https://cdn.discordapp.com/avatars/409253229491126285/b6a655353cf088ea82f91c281cb97e86.png?size=1024")
	await bot.say(embed=embed)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used info command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
		
@bot.command(name="mute", pass_context=True)
@commands.has_permissions(kick_members=True, administrator=True)
async def _mute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Muted")
	await bot.add_roles(user, role)
	embed = discord.Embed(title="Mute", description=" ", color=0xFFA500)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_mute.error
async def mute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(name="unmute", pass_context=True)
@commands.has_permissions(kick_members=True, administrator=True)
async def _unmute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Muted")
	await bot.remove_roles(user, role)
	embed = discord.Embed(title="Unmute", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_unmute.error
async def unmute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

@bot.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def _kick(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	await bot.kick(user)
	embed = discord.Embed(title="Kick", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_kick.error
async def kick_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
  
@bot.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members=True)
async def _ban(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.ban_members:
		return False
	reason = arg
	author = ctx.message.author
	await bot.ban(user)
	embed = discord.Embed(title="Ban", description=" ", color=0xFF0000)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_ban.error
async def ban_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `ban_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(name="warn", pass_context=True)
@commands.has_permissions(kick_members=True)
async def _warn(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("please provide a member")
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	server = ctx.message.server
	embed = discord.Embed(title="Warn", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	await bot.send_message(user, "You have been warned for: {}".format(reason))
	await bot.send_message(user, "from: {} server".format(server))
	
@_warn.error
async def warn_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True, ban_members=True, administrator=True)
async def unban(con,user:int):
    try:
        who=await bot.get_user_info(user)
        await bot.unban(con.message.server,who)
        await bot.say("User has been unbanned")
    except:
        await bot.say("Something went wrong")
    
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def msg(ctx, user: discord.Member, *, msg):
	await bot.send_message(user, msg)
	await bot.delete_message(ctx.message)
	print(f"{ctx.message.author.name} from {ctx.message.server} used d!msg command")
    
@bot.command(name="promote", pass_context=True)
@commands.has_permissions(administrator=True)
async def _promote(ctx, user: discord.Member = None, *, name = None):
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name=name)
	await bot.add_roles(user, role)
	await bot.delete_message(ctx.message)
	text = await bot.say(f"User {user.mention} has been promoted to {role.name} role".format(role.mention))
	await asyncio.sleep(5)
	await bot.delete_message(text)
	print(f"{ctx.message.author.name} from {ctx.message.server} used d!promote command")
	
@_promote.error
async def promote_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have a administrator permission.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

@bot.command(pass_context=True)
async def help(ctx):
	server = ctx.message.server
	author = ctx.message.author
	embed = discord.Embed(title="Help is here!", description="Here are the commands: Example d!ratings noobperson", color=0xFFFF)
	embed.add_field(name="ratings", value="d!ratings <user>")
	embed.add_field(name="bot info", value="d!botinfo")
	embed.add_field(name="stats", value="d!stats - to get how many servers the bot is in and how many users and uptime")
	embed.add_field(name="ping", value="d!ping - get bot's ping time")
	embed.add_field(name="clean", value="d!clean [messages] - clean the chat")
	embed.add_field(name="say", value="d!say [Text] - Make the bot say something - don't abuse this.")
	embed.add_field(name="d!info", value="get info about support server, and more.")
	embed.add_field(name="d!serverinfo", value="get info about the server")
	embed.add_field(name="d!membercount", value="to see how many members are in the server")
	embed.add_field(name="addrole", value="d!addrole @user <role name>")
	embed.add_field(name="removerole", value="d!removerole @user <role name>")
	embed.add_field(name="d!c open", value="opening containers (still adding more items)")
	embed.add_field(name="d!coinflip", value="50 50 chance of getting tails and heads")
	embed.add_field(name="moderations", value="d!moderations - to get list of moderations")
	embed.add_field(name="math", value="d!maths - to get list of math")
	embed.add_field(name="userinfo", value="d!userinfo @user")
	embed.add_field(name="bug", value="d!bug <your message here>")
	embed.add_field(name="idea", value="d!idea <your message here>")
	embed.set_thumbnail(url=server.icon_url)
	embed.set_footer(text="Requested by: " + author.name)
	await bot.say(embed=embed)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used help command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def moderations(ctx):
	embed = discord.Embed(title="ban", description="d!ban @user [your reason here]", color=0xFFFF)
	embed.add_field(name="kick", value="d!kick @user [your reason here]")
	embed.add_field(name="warn", value="d!warn @user [your reason here]")
	embed.add_field(name="mute", value="d!mute @user [your reason here]")
	embed.add_field(name="unmute", value="d!unmute @user [your reason here]")
	embed.add_field(name="unban", value="d!unban user.id | for example d!unban 277983178914922497")
	await bot.say(embed=embed)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used moderations command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)

@bot.command(aliases=['ud'])
async def urban(*msg):
	word = ' '.join(msg)
	api = "http://api.urbandictionary.com/v0/define"
	response = requests.get(api, params=[("term", word)]).json()
	embed = discord.Embed(description="No results found!", colour=0xFF0000)
	if len(response["list"]) == 0:
		return await bot.say(embed=embed)
	embed = discord.Embed(title="Word", description=word, colour=embed.colour)
	embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
	embed.add_field(name="Examples:", value=response['list'][0]["example"])
	await bot.say(embed=embed)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used urban command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def maths(ctx):
	embed = discord.Embed(title="math", description="d!math add (number) (number)", color=0xFFFF)
	embed.add_field(name="math", value="d!math subtract (number) (number)")
	embed.add_field(name="math", value="d!math multiply (number) (number)")
	embed.add_field(name="math", value="d!math divide (number) (number)")
	await bot.say(embed=embed)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used maths command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def rules(ctx):
	embed = discord.Embed(title="1. Please be respectful to everyone in here", description="Do not use any insult/profanity", color=0xFFFF)
	embed.add_field(name="2. Do not spam in any channel", value="you can spam in #bot_spam_1 and #bot_spam_2 only")
	await bot.delete_message(ctx.message)
	await bot.say(embed=embed)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used rules command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True, no_pm=True)
async def membercount(ctx):
	members = set(ctx.message.server.members)
	bots = filter(lambda m: m.bot, members)
	bots = set(bots)
	users = members - bots
	await bot.send_message(ctx.message.channel, embed=discord.Embed(title="Membercount", description="{} there is {} users and {} bots with a total of {} members in this server.".format(ctx.message.author.mention, len(users), len(bots), len(ctx.message.server.members)), colour=0X008CFF))
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used membercount command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
	
@bot.command(name="setgame", pass_context=True, aliases=['game', 'presence'])
@commands.check(user_is_me)
async def _setgame(ctx, *args):
	setgame = ' '.join(args)
	await bot.change_presence(game=discord.Game(name=setgame))
	await bot.delete_message(ctx.message)
	await bot.say(":ballot_box_with_check: Game set to: `" + setgame + "`")
	print("Game set to: `" + setgame + "`")
	
@_setgame.error
async def setgame_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, only the bot owner can use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
        
@bot.command(name="status", pass_context=True)
@commands.check(user_is_me)
async def _status(ctx, *args):
	status = ' '.join(args)
	await bot.change_presence(status=discord.Status(status))
	await bot.delete_message(ctx.message)
	await bot.say(":ballot_box_with_check: Status set to: `" + status + "`")
	print("Status set to: `" + status + "`")
	
@_status.error
async def status_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, only the bot owner can use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

@bot.command(name="say", pass_context=True)
@commands.has_permissions(administrator=True)
async def _say(ctx, *, msg = None):
    await bot.delete_message(ctx.message)

    if not msg: await bot.say("Please specify a message to send")
    else: await bot.say(msg)
    return
    channel = bot.get_channel('525109045221261312')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used say command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
    
@_say.error
async def say_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, you do not have a administrator permission to use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
    
@bot.command(name="clean", pass_context=True, no_pm=True)
@commands.has_permissions(administrator=True)
async def _clean(ctx, amount=100):
    channel = ctx.message.channel
    messages = [ ]
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    msg = await bot.say(f"{amount} message has been deleted.")
    await asyncio.sleep(5)
    await bot.delete_message(msg)
    channel = bot.get_channel('525109045221261312')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used clean command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
    
@_clean.error
async def clean_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have a administrator permission to use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
		
@bot.command(name="purge", pass_context=True, no_pm=True)
@commands.has_permissions(administrator=True)
async def _purge(ctx, amount=100):
    channel = ctx.message.channel
    messages = [ ]
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    channel = bot.get_channel('525109045221261312')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used purge command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
    
@_purge.error
async def purge_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have a administrator permission to use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
    
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def broadcast(ctx, *, msg):
    for server in bot.servers:
        for channel in server.channels:
            try:
                await bot.send_message(channel, msg)
            except Exception:
                continue
            else:
                break

@bot.command(name="addrole", pass_context=True)
@commands.has_permissions(administrator=True, manage_roles=True)
async def _addrole(ctx, user: discord.Member = None, *, name = None):
    author = ctx.message.author
    role = discord.utils.get(ctx.message.server.roles, name=name)
    await bot.add_roles(user, role)
    text = await bot.say(f'{author.mention} I have added the {role.name} role to a user {user.name}'.format(role.name))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(1)
    await bot.delete_message(text)
    channel = bot.get_channel('525109045221261312')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used addrole command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
    
@_addrole.error
async def addrole_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have a manage roles permission to use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

@bot.command(name="removerole", pass_context=True)
@commands.has_permissions(administrator=True, manage_roles=True)
async def _removerole(ctx, user: discord.Member = None, *, name = None):
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name=name)
	await bot.remove_roles(user, role)
	text = await bot.say(f'{author.mention} I have removed the {role.name} role from a user {user.name}'.format(role.name))
	await bot.delete_message(ctx.message)
	await asyncio.sleep(1)
	await bot.delete_message(text)
	channel = bot.get_channel('525109045221261312')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used removerole command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)
	
@_removerole.error
async def removerole_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have a manage roles permission to use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.group()
async def math():
    pass
    
@math.command(pass_context=True, no_pm=True)
async def add(ctx, a: int, b:int):
	await bot.say("{} + {} = {}".format(a, b, a+b))
	
@math.command(pass_context=True, no_pm=True)
async def subtract(ctx, a: int, b:int):
	await bot.say("{} - {} = {}".format(a, b, a-b))
	
@math.command(pass_context=True, no_pm=True)
async def multiply(ctx, a: int, b:int):
	await bot.say("{} x {} = {}".format(a, b, a*b))
	
@math.command(pass_context=True, no_pm=True)
async def divide(ctx, a: int, b:int):
	await bot.say("{} ÷ {} = {}".format(a, b, a/b))
	
bot.run(os.environ['BOT_TOKEN'])
