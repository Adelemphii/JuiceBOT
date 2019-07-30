#The Official JuiceBOT Rewrite by Juice-chan
#Invite link: https://discordapp.com/api/oauth2/authorize?client_id=605404468254867457&permissions=67496000&scope=bot
#Type taskkill /F /IM python.exe /T to close out the bot code CMD.

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from itertools import cycle
import asyncio
import random

status = cycle(['JuiceBOT', 'By Juice-chan'])

owsup_list = ['Ana', 'Baptiste', 'Brigette', 'Lucio', 'Moira', 'Zenyatta']
owtank_list = ['D.va', 'Orisa', 'Reinhardt', 'Roadhog', 'Winston', 'Wrecking Ball', 'Zarya']
dps_list = ['Ashe', 'Bastion', 'Doomfist', 'Genji', 'Hanzo', 'Junkrat', 'Mcree', 'Mei', 'Pharah', 'Reaper', 'Soldier 76', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker']
def_list = ['Warden', 'Mozzie', 'Kaid', 'Clash', 'Maestro', 'Alibi', 'Vigil', 'Ela', 'Lesion', 'Echo', 'Mira', 'Caveira', 'Valkyrie', 'Frost', 'Mute', 'Smoke', 'Castle', 'Pulse', 'Doc', 'Rook', 'Jager', 'Bandit', 'Tachanka', 'Kapkan']
atk_list = ['Ash', 'Zofia', 'Glaz', 'Monty', 'NØkk', 'Gridlock', 'Nomad', 'Maverick', 'Lion', 'Finka', 'Dokkaebae', 'Zofia', 'Ying', 'Jackal', 'Hibana', 'Capitao', 'Blackbeard', 'Buck', 'Sledge', 'Thatcher', 'Thermite', 'Twitch', 'Blitz', 'IQ', 'Fuze', 'Glaz']
ow_list = ['Ana', 'Baptiste', 'Brigette', 'Lucio', 'Moira', 'Zenyatta', 'D.va', 'Orisa', 'Reinhardt', 'Roadhog', 'Winston', 'Wrecking Ball', 'Zarya', 'Ashe', 'Bastion', 'Doomfist', 'Genji', 'Hanzo', 'Junkrat', 'Mcree', 'Mei', 'Pharah', 'Reaper', 'Soldier 76', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker']
owe_list = ['Doomfist', 'Tracer', 'D.va', 'Orisa', 'Reinhardt', 'Wrecking Ball', 'Zarya', 'Bastion', 'Pharah', 'Tracer']

bot = commands.Bot(command_prefix='!')

TOKEN = 'yeet'

client = discord.Client()

@client.event
async def on_message(message):
#Embed Command
    embed = discord.Embed()
    title = 'Commands',
    description = 'This is the list of commands for this bot. For an explanation of what they do, do this:',
    colour = discord.Colour.blue()

    embed.set_footer(text='This is work in progress! By Juice-chan aka Birbl.')
    embed.set_image(url='https://cdn.discordapp.com/attachments/473186893711015966/605131851400609854/wawa.jpg')
    embed.set_thumbnail(url='')
    embed.set_author(name='JuiceBOT', icon_url='https://cdn.discordapp.com/attachments/473186893711015966/605131585850703877/birb.png')
    embed.add_field(name='Commands', value='This is the list of commands for this bot. For an explanation of what they do, do this:', inline=False)
    embed.add_field(name='Basic Commands', value='!hello, !ping, !kitten, @mega, disrespekt, and Yeet.', inline=False)
    embed.add_field(name='Rainbow Six: Siege Commands', value='!ATKR6 and !DEFR6.', inline=False)
    embed.add_field(name='Overwatch Commands', value='!OWEx and !Hero.', inline=False)
    if message.content.startswith('!commands'):
        await client.send_message(message.channel,embed=embed)

#Basic Commands
    if message.author == client.user:
        return
    if message.content.startswith('!!'):
        msg = '{0.author.mention} This is an invalid command! If you need help, type ``!commands`` for a list of valid commands!'.format(message)
        await client.send_message(message.channel,msg)
    if message.content.startswith('!test'):
        msg = 'This is indeed a test!'
        await client.send_message(message.channel,msg)
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!ping'):
        msg = '{0.author.mention} YEET, everyone uses "Pong" normally but I am DIFFERENT!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!kitten'):
        msg = 'We all know who the best around is, It is this little bugger right here! <:cbk1:473189857817133077>'
        await client.send_message(message.channel, msg)
    if ('yeet') in message.content:
        msg = '{0.author.mention} I believe the correct term is YEET, not just yeet. Get it right fam I do not have all day to just correct you! :thinking:'.format(message)
        await client.send_message(message.channel, msg)
    if ('Yeet') in message.content:
        msg = '{0.author.mention} I believe the correct term is YEET, not just Yeet. Get it right fam I do not have all day to just correct you! :thinking:'.format(message)
        await client.send_message(message.channel, msg)
    if ('@mega') in message.content:
        msg = 'mega is big gnat, do not talk to dis persun or u is not kool,,, u shidder,'
        await client.send_message(message.channel, msg)
    if ('disrespekt') in message.content:
        msg = 'that is desrepektful way 2 speek 2 ur elders young pidder, dun do that now.'
        await client.send_message(message.channel,msg)
    if message.content.startswith('!neko'): 
        msg = 'neko wus here, henlo fredn'
        await client.send_message(message.channel,msg)
    if ('JuiceStart') in message.content:
        msg = 'I am now online, Thank you for summoning me Master. I will make your day with my wonderful abilities!'
        await client.send_message(message.channel,msg)
    if ("i'm dad") in message.content.lower():
        msg = '**No dad jokes.**'
        await client.send_message(message.channel,msg)
        await client.delete_message(message)

#Gaming Commands: R6s
    if message.content.startswith('!ATKR6'):
        msg = (random.choice(atk_list))
        await client.send_message(message.channel,msg)
    if message.content.startswith('!DEFR6'):
        msg = (random.choice(def_list))
        await client.send_message(message.channel,msg)

#Gaming Commands: Overwatch
    if message.content.startswith('!OWEx'):
        msg = (random.choice(owe_list))
        await client.send_message(message.channel,msg)
    if message.content.startswith('!Hero'):
        msg = (random.choice(ow_list))
        await client.send_message(message.channel,msg)
    if message.content.startswith('!hero'):
        msg = (random.choice(ow_list))
        await client.send_message(message.channel,msg)


#Moderator Commands
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Test')
    await client.add_roles(member, role)



#Misc.
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(2)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('Ready to serve!')
    print('-----------------')

client.loop.create_task(change_status())
client.run('yeet')
