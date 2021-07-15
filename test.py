import random
import time
import asyncio
import discord
import math

from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='teko ')
client.remove_command('teko')
client.remove_command('help')

# client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.playing, name="teko help"))
    print('We have logged in as {0.user}'.format(client))


def check(author):
    def inner_check(message):
        return message.author == author

    return inner_check

command_usage=[]

@client.command()
async def size(ctx):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention+',end your current game to use another command.')
        return

    size = random.randint(1,21)
    string = "8"
    if size==21:
        string+="=================================================================================================="
    else:
        i=1
        while i <= size:
            string += "="
            i += 1
    string += "D"
    await ctx.send(string)

@client.command()
async def pp(ctx):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention+',end your current game to use another command.')
        return

    size = random.randint(1,20)
    string = "8"
    i=1
    while i <= size:
        string += "="
        i += 1
    string += "D"
    await ctx.send(string)

@client.command()
async def rps(ctx,arg0=None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention+',end your current game to use another command.')
        return

    z = random.randint(1, 3)
    if arg0==None:
        embed = discord.Embed(title='CORRECT COMMAND USAGE:',description="`teko rps [choice]`\nwhere `choice` = r,p or s.", color=0x7F00FF)
        embed.set_footer(text='Example : teko rps s.')
        await ctx.send(embed=embed)
    elif arg0.lower() == 'r':
        if z == 1:
            await ctx.send(embed=discord.Embed(description="**TEKO** also chose rock <:emoji_13:763360498132844544>.",color=0x7F00FF))
        elif z == 2:
            await ctx.send(embed=discord.Embed(description="**TEKO** chose paper 📃...**TEKO** won.", color=0x7F00FF))
        elif z == 3:
            await ctx.send(
                embed=discord.Embed(description="**TEKO** chose scissor ✂...**" + ctx.author.name + "** won.",color=0x7F00FF))
    elif arg0.lower() == 'p':
        if z == 1:
            await ctx.send(embed=discord.Embed(description="**TEKO** chose rock <:emoji_13:763360498132844544>...**" + ctx.author.name + "** won.",color=0x7F00FF))
        elif z == 2:
            await ctx.send(embed=discord.Embed(description="**TEKO** also chose paper 📃.", color=0x7F00FF))
        elif z == 3:
            await ctx.send(embed=discord.Embed(description="**TEKO** chose scissor ✂...**TEKO** won.", color=0x7F00FF))
    elif arg0.lower() == 's':
        if z == 1:
            await ctx.send(
                embed=discord.Embed(description="**TEKO** chose rock <:emoji_13:763360498132844544>...**TEKO** won.",color=0x7F00FF))
        elif z == 2:
            await ctx.send(embed=discord.Embed(description="**TEKO** chose paper 📃...**" + ctx.author.name + "** won.",color=0x7F00FF))
        elif z == 3:
            await ctx.send(embed=discord.Embed(description="**TEKO** also chose scissor ✂.", color=0x7F00FF))
    else:
        embed = discord.Embed(title='CORRECT COMMAND USAGE:',description="`teko rps [choice]`\nwhere `choice` = r,p or s.", color=0x7F00FF)
        embed.set_footer(text='Example : teko rps s.')
        await ctx.send(embed=embed)

@client.command()
async def rolldice(ctx):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention+',end your current game to use another command.')
        return

    string=await ctx.send(embed=discord.Embed(description='rolling dice <a:diceroll:855341301993701386>...',color=0x7F00FF))
    die=random.randint(1,6)
    time.sleep(2)
    if die==1:
        await string.edit(embed=discord.Embed(description='rolling dice <:dice1:855341427441139722>... it was 1',color=0x7F00FF))
    elif die==2:
        await string.edit(embed=discord.Embed(description='rolling dice <:dice2:855341381941329941>... it was 2',color=0x7F00FF))
    elif die==3:
        await string.edit(embed=discord.Embed(description='rolling dice <:dice3:855341405366386698>... it was 3',color=0x7F00FF))
    elif die==4:
        await string.edit(embed=discord.Embed(description='rolling dice <:dice4:855341364907737098>... it was 4',color=0x7F00FF))
    elif die==5:
        await string.edit(embed=discord.Embed(description='rolling dice <:dice5:855341344728547348>... it was 5',color=0x7F00FF))
    else:
        await string.edit(embed=discord.Embed(description='rolling dice <:dice6:855341325721665576>... it was 6',color=0x7F00FF))

@client.command()
async def cupid(ctx, arg0=None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention+',end your current game to use another command.')
        return
    percent=random.randint(0,100)
    string="------------------------------------------------\n**"+ctx.author.mention+"**\n"
    string+=":arrow_up_small:<a:blinkline:830102940315680868><a:blinkline:830102940315680868><a:blinkline:830102940315680868><a:blinkline:830102940315680868><a:blinkline:830102940315680868>("+str(percent)+"%)<a:blinkline:830102940315680868><a:blinkline:830102940315680868><a:blinkline:830102940315680868><a:blinkline:830102940315680868><a:blinkline:830102940315680868>:arrow_down_small:"
    if arg0==None:
        string+='\n**something**\n------------------------------------------------\n'
    else:
        string+='\n**'+arg0+'**\n------------------------------------------------\n'
        if percent==0:
            string+="<:iDubbbz:848245987025223701><:iDubbbz_hand:848249622009872385>\n*(that's ...)*"
        elif percent <=10:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's kinda small)*"
        elif percent<=20:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's kinda small)*"
        elif percent<=30:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's quite mediocre)*"
        elif percent<=40:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's quite mediocre)*"
        elif percent<=50:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's pretty good)*"
        elif percent<=60:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's pretty good)*"
        elif percent<=70:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's quite big)*"
        elif percent<=80:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's quite big)*"
        elif percent<=90:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's pretty huge)*"
        else:
            string += "<:iDubbbz:848245987025223701><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:string:848247397696274453><:iDubbbz_hand:848249622009872385>\n*(that's humongus)*"

    embed = discord.Embed(description=string, color=0x7F00FF)
    embed.set_author(name=ctx.author.display_name + "'s cupid", icon_url=ctx.author.avatar_url)
    if arg0==None:
        embed.set_footer(text='correct command usage : teko cupid happy,teko cupid @user,etc.')
    await ctx.send(embed=embed)

@client.command()
async def chopsticks(ctx, arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention+',end your current game to use another command.')
    elif arg1!=None and arg1._user.bot==True:
        await ctx.send(ctx.author.mention+",you can't play with bots!")
    elif arg1!=None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention+',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        command_usage.append(ctx.author.id)
        blh = brh = plh = prh = 1
        flag1 = 0
        fingers = ['', '↥', '↥↥', '↥↥↥', '↥↥↥↥']
        logs=''
        while flag1 >= 0:
            embed = discord.Embed(description="------------------------------------------------", color=0x7F00FF)
            embed.add_field(name='__TEKO__', value="LH : " + fingers[blh] + "   ,   RH : " + fingers[brh], inline=False)
            embed.add_field(name='__' + ctx.author.name + '__', value="LH : " + fingers[plh] + "   ,   RH : " + fingers[prh]+"\n------------------------------------------------\n"+logs, inline=False)
            embed.set_author(name='🥢 ' + ctx.author.name + ' vs TEKO 🥢')
            embed.set_footer(text="possible input = ll,lr,rr,rl | 'exit' to abort.")
            await ctx.send(embed=embed)
            if blh == 0 and brh == 0:
                flag1 = -1
                break
            elif plh == 0 and prh == 0:
                flag1 = -2
                break
            logs = '__**LOGS:**__\n>'
            t2=0
            while (1):
                try:
                    t1=time.time()
                    msg = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                except asyncio.TimeoutError:
                    await ctx.send('looks like you fell asleep **'+ctx.author.mention+'**.')
                    flag1 = -4
                    break
                uinput=msg.content.lower().split(' ')
                if msg.content.lower() == "lr" and brh != 0 and plh != 0:
                    brh += plh
                    logs += '**' + ctx.author.name + "** taps their __LEFT__ hand on **TEKO's** __RIGHT__ hand."
                    if brh == 5:
                        logs += '**' + ctx.author.name + "** eliminated **TEKO** __RIGHT__ hand."
                        brh = 0
                    break
                elif msg.content.lower() == "ll" and blh != 0 and plh != 0:
                    blh += plh
                    logs += '**' + ctx.author.name + "** taps their __LEFT__ hand on **TEKO's** __LEFT__ hand."
                    if blh == 5:
                        logs += '**' + ctx.author.name + "** eliminated **TEKO** __LEFT__ hand."
                        blh = 0
                    break
                elif msg.content.lower() == "rr" and brh != 0 and prh != 0:
                    brh += prh
                    logs += '**' + ctx.author.name + "** taps their __RIGHT__ hand on **TEKO's** __RIGHT__ hand."
                    if brh == 5:
                        logs += '**' + ctx.author.name + "** eliminated **TEKO** __RIGHT__ hand."
                        brh = 0
                    break
                elif msg.content.lower() == "rl" and blh != 0 and prh != 0:
                    blh += prh
                    logs += '**' + ctx.author.name + "** taps their __RIGHT__ hand on **TEKO's** __LEFT__ hand."
                    if blh == 5:
                        logs += '**' + ctx.author.name + "** eliminated **TEKO** __LEFT__ hand."
                        blh = 0
                    break
                elif msg.content.lower() == "split" and (prh == 0 or plh == 0):
                    if prh == 2 or plh == 2:
                        prh = plh = 1
                        logs += '**' + ctx.author.name + '** decided to split.'
                        break
                    elif prh == 4 or plh == 4:
                        prh = plh = 2
                        logs += '**' + ctx.author.name + '** decided to split.'
                        break
                    else:
                        await msg.add_reaction('\N{CROSS MARK}')
                elif len(uinput)==3 and plh != 0 and prh != 0 and uinput[0]=='split' and uinput[1] in ['0','1','2','3','4'] and uinput[2] in ['0','1','2','3','4'] and int(uinput[1]) + int(uinput[2]) == plh + prh:
                    if (plh==int(uinput[1]) and prh==int(uinput[2])) or (plh==int(uinput[2]) and prh==int(uinput[1])):
                        await msg.add_reaction('\N{CROSS MARK}')
                    else:
                        plh = int(uinput[1])
                        prh = int(uinput[2])
                        logs += '**' + ctx.author.name + '** decided to split.'
                        break
                elif msg.content.lower() == "exit":
                    await msg.add_reaction('\N{OCTAGONAL SIGN}')
                    flag1 = -3
                    break
                t2+=int(time.time()-t1)
            if flag1 == -4 or flag1 == -3:
                break
            if brh > 5:
                brh -= 5
            elif blh > 5:
                blh -= 5
            if blh == 0 and brh == 0:
                continue
            if plh == 0 and prh == 0:
                continue
            logs += '\n>'
            if blh + plh == 5:
                logs += "**TEKO** taps his __LEFT__ hand to **" + ctx.author.name + "'s** __LEFT__ hand and hence eliminate it."
                plh = 0
            elif blh + prh == 5:
                logs += "**TEKO** taps his __LEFT__ hand to **" + ctx.author.name + "'s** __RIGHT__ hand and hence eliminate it."
                prh = 0
            elif brh + plh == 5:
                logs += "**TEKO** taps his __RIGHT__ hand to **" + ctx.author.name + "'s** __LEFT__ hand and hence eliminate it."
                plh = 0
            elif brh + prh == 5:
                logs += "**TEKO** taps his __RIGHT__ hand to **" + ctx.author.name + "'s** __RIGHT__ hand and hence eliminate it."
                prh = 0
            elif brh == 0 and blh % 2 == 0:
                logs += "**TEKO** decided to split."
                brh = blh = int(blh / 2)
            elif blh == 0 and brh % 2 == 0:
                logs += "**TEKO** decided to split."
                brh = blh = int(brh / 2)
            else:
                if blh == 0:
                    if plh == 0:
                        bchoice = 4
                    elif prh == 0:
                        bchoice = 3
                    else:
                        bchoice = random.randint(3, 4)
                elif brh == 0:
                    if plh == 0:
                        bchoice = 2
                    elif prh == 0:
                        bcoice = 1
                    else:
                        bchoice = random.randint(1, 2)
                else:
                    if plh == 0:
                        bchoice = random.randrange(2, 5, 2)
                    elif prh == 0:
                        bchoice = random.randrange(1, 4, 2)
                    else:
                        bchoice = random.randint(1, 4)

                if bchoice == 1:
                    logs += "**TEKO** taps his __LEFT__ hand to **" + ctx.author.name + "'s** __LEFT__ hand."
                    plh = plh + blh
                elif bchoice == 2:
                    logs += "**TEKO** taps his __LEFT__ hand to **" + ctx.author.name + "'s** __RIGHT__ hand."
                    prh = prh + blh
                elif bchoice == 3:
                    logs += "**TEKO** taps his __RIGHT__ hand to **" + ctx.author.name + "'s** __LEFT__ hand."
                    plh = plh + brh
                else:
                    logs += "**TEKO** taps his __RIGHT__ hand to **" + ctx.author.name + "'s** __RIGHT__ hand."
                    prh = prh + brh
            if plh > 5:
                plh = plh - 5
            elif prh > 5:
                prh = prh - 5
            flag1 += 1

        if flag1 == -1:
            await ctx.send("👑 **" + ctx.author.name + "** won 👑")
        elif flag1 == -2:
            await ctx.send("👑 **TEKO** won 👑")
        command_usage.remove(ctx.author.id)
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision = t2=0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated")
        elif decision == 1:
            blh = brh = plh = prh = 1
            flag1 = 0
            fingers = ['', '↥', '↥↥', '↥↥↥', '↥↥↥↥']
            logs=''
            while 1:
                if plh == 0 and prh == 0:
                    title="👑 **{}** won 👑".format(arg1.display_name)
                elif blh == 0 and brh == 0:
                    title="👑 **" + str(ctx.author.name) + "** won 👑"
                elif decision%2!=0:
                    title='**' + ctx.author.name + '** turn:'
                else:
                    title='**{}** turn:'.format(arg1.display_name)
                embed = discord.Embed(title=title,description="------------------------------------------------", color=0x7F00FF)
                embed.add_field(name='__{}__'.format(arg1.display_name), value="LH : " + fingers[blh] + "   ,   RH : " + fingers[brh], inline=False)
                embed.add_field(name='__' + ctx.author.name + '__', value="LH : " + fingers[plh] + "   ,   RH : " + fingers[prh]+"\n------------------------------------------------\n"+logs, inline=False)
                embed.set_author(name='🥢 ' + ctx.author.name + ' vs {} 🥢'.format(arg1.display_name))
                embed.set_footer(text="possible input = ll,lr,rr,rl | 'exit' to abort.")
                await ctx.send(embed=embed)
                if plh == 0 and prh == 0:
                    break
                elif blh == 0 and brh == 0:
                    break
                if decision % 2 != 0:
                    logs = '__**LOGS:**__\n>'
                    t2=0
                    try:
                        while 1:
                            t1=time.time()
                            msg = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                            uinput=msg.content.lower().split(' ')
                            if msg.content.lower() == "lr" and brh != 0 and plh != 0:
                                brh += plh
                                if brh == 5:
                                    logs += '**' + str(ctx.author.name) + "** eliminated **{}**'s __RIGHT__ hand.".format(arg1.display_name)
                                    brh = 0
                                else:
                                    logs += '**' + ctx.author.name + "** taps their __LEFT__ hand on **{}**'s __RIGHT__ hand.".format(arg1.display_name)
                                break
                            elif msg.content.lower() == "ll" and blh != 0 and plh != 0:
                                blh += plh
                                if blh == 5:
                                    logs += '**' + str(ctx.author.name) + "** eliminated **{}** __LEFT__ hand.".format(arg1.display_name)
                                    blh = 0
                                else:
                                    logs += '**' + ctx.author.name + "** taps their __LEFT__ hand on **{}**'s __LEFT__ hand.".format(arg1.display_name)
                                break
                            elif msg.content.lower() == "rr" and brh != 0 and prh != 0:
                                brh += prh
                                if brh == 5:
                                    logs += '**' + str(ctx.author.name) + "** eliminated **{}** __RIGHT__ hand.".format(arg1.display_name)
                                    brh = 0
                                else:
                                    logs += '**' + ctx.author.name + "** taps their __RIGHT__ hand on **{}**'s __RIGHT__ hand.".format(arg1.display_name)
                                break
                            elif msg.content.lower() == "rl" and blh != 0 and prh != 0:
                                blh += prh
                                if blh == 5:
                                    logs += '**' + str(ctx.author.name) + "** eliminated **{}** __LEFT__ hand.".format(arg1.display_name)
                                    blh = 0
                                else:
                                    logs += '**' + ctx.author.name + "** taps their __RIGHT__ hand on **{}**'s __LEFT__ hand.".format(arg1.display_name)
                                break
                            elif msg.content.lower() == "split" and (prh == 0 or plh == 0):
                                if prh == 2 or plh == 2:
                                    prh = plh = 1
                                    logs += '**' + ctx.author.name + '** decided to split.'
                                    break
                                elif prh == 4 or plh == 4:
                                    prh = plh = 2
                                    logs += '**' + ctx.author.name + '** decided to split.'
                                    break
                                else:
                                    await msg.add_reaction('\N{CROSS MARK}')
                            elif len(uinput)==3 and plh != 0 and prh != 0 and uinput[0]=='split' and uinput[1] in ['0','1','2','3','4'] and uinput[2] in ['0','1','2','3','4'] and int(uinput[1]) + int(uinput[2]) == plh + prh:
                                if (plh == int(uinput[1]) and prh == int(uinput[2])) or (plh == int(uinput[2]) and prh == int(uinput[1])):
                                    await msg.add_reaction('\N{CROSS MARK}')
                                else:
                                    plh = int(uinput[1])
                                    prh = int(uinput[2])
                                    logs += '**' + ctx.author.name + '** decided to split.'
                                    break
                            elif msg.content.lower() == "exit":
                                await msg.add_reaction('\N{OCTAGONAL SIGN}')
                                flag1 = -3
                                break
                            t2+=int(time.time()-t1)
                    except asyncio.TimeoutError:
                        await ctx.send('looks like you fell asleep ' + ctx.author.mention + '.')
                        break
                    if flag1==-3:
                        break
                    elif brh > 5:
                        brh -= 5
                    elif blh > 5:
                        blh -= 5
                else:
                    logs += '\n>'
                    t2=0
                    try:
                        while 1:
                            t1=time.time()
                            msg = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                            uinput=msg.content.lower().split(' ')
                            if msg.content.lower() == "lr" and prh != 0 and blh != 0:
                                prh += blh
                                if prh == 5:
                                    logs += "**{}** eliminated **".format(arg1.display_name) + str(ctx.author.name) + "**'s __RIGHT__ hand."
                                    prh = 0
                                else:
                                    logs += "**{}** taps their __LEFT__ hand on **".format(arg1.display_name) + str(ctx.author.name) + "**'s __RIGHT__ hand."
                                break
                            elif msg.content.lower() == "ll" and plh != 0 and blh != 0:
                                plh += blh
                                if plh == 5:
                                    logs += "**{}** eliminated **".format(arg1.display_name) + str(ctx.author.name) + "**'s __LEFT__ hand."
                                    plh = 0
                                else:
                                    logs += "**{}** taps their __LEFT__ hand on **".format(arg1.display_name) + ctx.author.name + "**'s __LEFT__ hand."
                                break
                            elif msg.content.lower() == "rr" and prh != 0 and brh != 0:
                                prh += brh
                                if prh == 5:
                                    logs += "**{}** eliminated **".format(arg1.display_name) + str(ctx.author.name) + "** __RIGHT__ hand."
                                    prh = 0
                                else:
                                    logs += "**{}** taps their __RIGHT__ hand on **".format(arg1.display_name) + ctx.author.name + "**'s __RIGHT__ hand."
                                break
                            elif msg.content.lower() == "rl" and plh != 0 and brh != 0:
                                plh += brh
                                if plh == 5:
                                    logs += "**{}** eliminated **".format(arg1.display_name) + str(ctx.author.name) + "** __LEFT__ hand."
                                    plh = 0
                                else:
                                    logs += "**{}** taps their __RIGHT__ hand on **".format(arg1.display_name) + ctx.author.name + "**'s __LEFT__ hand."
                                break
                            elif msg.content.lower() == "split" and (brh == 0 or blh == 0):
                                if brh == 2 or blh == 2:
                                    brh = blh = 1
                                    logs += '**{}** decided to split.'.format(arg1.display_name)
                                    break
                                elif brh == 4 or blh == 4:
                                    brh = blh = 2
                                    logs += '**{}** decided to split.'.format(arg1.display_name)
                                    break
                                else:
                                    await msg.add_reaction('\N{CROSS MARK}')
                            elif len(uinput) == 3 and blh != 0 and brh != 0 and uinput[0] == 'split' and uinput[1] in ['0', '1', '2', '3', '4'] and uinput[2] in ['0', '1', '2', '3','4'] and int(uinput[1]) + int(uinput[2]) == blh + brh:
                                if (blh == int(uinput[1]) and brh == int(uinput[2])) or (blh == int(uinput[2]) and brh == int(uinput[1])):
                                    await msg.add_reaction('\N{CROSS MARK}')
                                else:
                                    blh = int(uinput[1])
                                    brh = int(uinput[2])
                                    logs += '**{}** decided to split.'.format(arg1.display_name)
                                    break
                            elif msg.content.lower() == "exit":
                                await msg.add_reaction('\N{OCTAGONAL SIGN}')
                                flag1 = -3
                                break
                            t2+=int(time.time()-t1)
                    except asyncio.TimeoutError:
                        await ctx.send('looks like you fell asleep {}.'.format(ctx.author.mention))
                        break
                    if flag1 == -3:
                        break
                    elif prh > 5:
                        prh -= 5
                    elif plh > 5:
                        plh -= 5
                decision += 1
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def tictactoe(ctx, arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        command_usage.append(ctx.author.id)
        mark = [':o:', ':x:']
        numbers=[':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']
        position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        win = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
        ppoint = []
        bpoint = []
        p = random.choice(mark)
        mark.remove(p)
        b = mark[0]
        flag1 = 0
        flag2 = 0
        while 1:

            bchoice = random.choice(position)
            position.remove(bchoice)
            bpoint.append(bchoice)
            i = 0
            k = 1

            string = "\n\n"
            while i < 3:
                j = 0
                while j < 3:
                    if k in bpoint:
                        string += str(b) + " | "
                    elif k in ppoint:
                        string += str(p) + " | "
                    else:
                        string += numbers[k-1] + " | "
                    k += 1
                    j += 1
                if k != 10:
                    string += "\n---------------\n"
                else:
                    string += "\n "
                i += 1

            for w in win:
                w = set(w)
                bpoint_set = set(bpoint)
                ppoint_set = set(ppoint)
                if w.issubset(bpoint_set) == True:
                    string+="\n👑 **TEKO won** 👑"
                    flag1 = 1
                    break
                elif w.issubset(ppoint_set) == True:
                    string+="👑 **" + str(ctx.author.name) + " won** 👑"
                    flag1 = 1
                    break
            if len(position) == 0:
                string+="draw"
            embed = discord.Embed(title="**" + str(ctx.author.name) + "** ~ " + str(p) + "** ** , **TEKO** ~ " + str(b) + "\n",description=string, color=0x7F00FF)
            embed.set_footer(text="choose number to mark their | 'exit' to abort.")
            await ctx.send(embed=embed)
            if flag1 == 1 or len(position) == 0:
                break
            try:
                t2=0
                while 1:
                    t1=time.time()
                    msg1 = await client.wait_for('message', check=check(ctx.author), timeout=60-t2)
                    msg = str(msg1.content)
                    if msg.lower() == "exit":
                        flag1 = 1
                        await msg1.add_reaction('\N{OCTAGONAL SIGN}')
                        break
                    if msg.isdigit():
                        pchoice = int(msg)
                        if pchoice in position:
                            position.remove(pchoice)
                            ppoint.append(pchoice)
                            break
                        elif pchoice > 0 and pchoice < 10 and pchoice not in position:
                            await msg1.add_reaction('\N{CROSS MARK}')
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send("looks like you fell asleep **" + ctx.author.mention + "**.")
                break
            for w in win:
                w = set(w)
                bpoint_set = set(bpoint)
                ppoint_set = set(ppoint)
                if w.issubset(bpoint_set) == True:
                    string = "\n\n"
                    while i < 3:
                        j = 0
                        while j < 3:
                            if k in bpoint:
                                string += str(b) + " | "
                            elif k in ppoint:
                                string += str(p) + " | "
                            else:
                                string += numbers[k-1] + " | "
                            k += 1
                            j += 1
                        if k != 10:
                            string += "\n---------------\n"
                        else:
                            string += "\n "
                        i += 1

                    embed = discord.Embed(title="**" + str(ctx.author.name) + "** ~ " + str(p) + "** ** , **TEKO** ~ " + str(b) + "\n",description=string+"\n**TEKO won**", color=0x7F00FF)
                    embed.set_footer(text="choose number to mark their | 'exit' to abort.")
                    await ctx.send(embed=embed)
                    flag1 = 1
                    break
                elif w.issubset(ppoint_set) == True:
                    i = 0
                    k = 1
                    string = "\n\n"
                    while i < 3:
                        j = 0
                        while j < 3:
                            if k in bpoint:
                                string += str(b) + " | "
                            elif k in ppoint:
                                string += str(p) + " | "
                            else:
                                string += numbers[k-1] + " | "
                            k += 1
                            j += 1
                        if k != 10:
                            string += "\n---------------\n"
                        else:
                            string += "\n "
                        i += 1

                    embed = discord.Embed(title="**" + str(ctx.author.name) + "** ~ " + str(p) + "** ** , **TEKO** ~ " + str(b) + "\n",description=string+"\n👑 **" + str(ctx.author.name) + " won** 👑", color=0x7F00FF)
                    embed.set_footer(text="choose number to mark their | 'exit' to abort.")
                    await ctx.send(embed=embed)
                    flag1 = 1
                    break
            if flag1 == 1:
                break
            else:
                flag2 += 1
        command_usage.remove(ctx.author.id)
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision =t2= 0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated")
        elif decision == 1:
            mark = [':o:', ':x:']
            numbers = [':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']
            position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            win = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
            ppoint = []
            bpoint = []
            p = random.choice(mark)
            mark.remove(p)
            b = mark[0]
            flag = 0
            while 1:
                i = 0
                k = 1
                string = "\n\n"
                while i < 3:
                    j = 0
                    while j < 3:
                        if k in bpoint:
                            string += str(b) + " | "
                        elif k in ppoint:
                            string += str(p) + " | "
                        else:
                            string += numbers[k-1] + " | "
                        k += 1
                        j += 1
                    if k != 10:
                        string += "\n---------------\n"
                    else:
                        string += "\n "
                    i += 1
                if decision % 2 != 0:
                    turn='**' + ctx.author.name + '** turn:'
                else:
                    turn='**{}** turn:'.format(arg1.display_name)
                for w in win:
                    w = set(w)
                    bpoint_set = set(bpoint)
                    ppoint_set = set(ppoint)
                    if w.issubset(bpoint_set) == True:
                        turn="👑 **{}** won 👑".format(arg1.display_name)
                        flag = 1
                        break
                    elif w.issubset(ppoint_set) == True:
                        turn="👑 **" + str(ctx.author.name) + "** won 👑"
                        flag = 1
                        break
                if len(position) == 0:
                    turn='draw.'
                embed = discord.Embed(title="**" + str(ctx.author.name) + "** ~ " + str(p) + "** ** , **{}** ~ ".format(arg1.display_name) + str(b) + "\n", description=string + '\n' + turn, color=0x7F00FF)
                embed.set_footer(text="choose number to mark their | 'exit' to abort.")
                await ctx.send(embed=embed)
                if flag == 1 or len(position) == 0:
                    break
                if decision % 2 != 0:
                    try:
                        t2=0
                        while 1:
                            t1=time.time()
                            msg1 = await client.wait_for('message', check=check(ctx.author), timeout=60-t2)
                            msg = str(msg1.content)
                            if msg.lower() == "exit":
                                flag = 1
                                await msg1.add_reaction('\N{OCTAGONAL SIGN}')
                                break
                            if msg.isdigit():
                                pchoice = int(msg)
                                if pchoice in position:
                                    position.remove(pchoice)
                                    ppoint.append(pchoice)
                                    break
                                elif pchoice > 0 and pchoice < 10 and pchoice not in position:
                                    await msg1.add_reaction('\N{CROSS MARK}')
                            t2+=int(time.time()-t1)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **" + ctx.author.name + "**.")
                        break
                else:
                    t2=0
                    try:
                        while 1:
                            t1=time.time()
                            msg1 = await client.wait_for('message', check=check(arg1._user), timeout=60-t2)
                            msg = str(msg1.content)
                            if msg.lower() == "exit":
                                flag = 1
                                await msg1.add_reaction('\N{OCTAGONAL SIGN}')
                                break
                            if msg.isdigit():
                                bchoice = int(msg)
                                if bchoice in position:
                                    position.remove(bchoice)
                                    bpoint.append(bchoice)
                                    break
                                elif bchoice > 0 and bchoice < 10 and bchoice not in position:
                                    await msg1.add_reaction('\N{CROSS MARK}')
                            t2+=int(time.time()-t1)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **{}**.".format(arg1.mention))
                        break
                if flag == 1:
                    break
                decision += 1
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def tictactoe2(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
        return
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
        return
    elif arg1==None:
        command_usage.append(ctx.author.id)
        decision=1
        filled_grid = []
        ppoint = []
        bpoint = []
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        win = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
        o = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        x = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        pos={}
        maze = {}
        flag = 0
        for i in range(9):
            maze[i] = [':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']
            pos[i+1]=[1,2,3,4,5,6,7,8,9]
        while 1:
            for i in range(0, 7, 3):
                if i == 0:
                    string = maze[i][0] + maze[i][1] + maze[i][2] + ':yellow_square:' + maze[i + 1][0] + maze[i + 1][1] + maze[i + 1][2] + ':yellow_square:' + maze[i + 2][0] + maze[i + 2][1] + maze[i + 2][2] + '\n'
                else:
                    string += ':yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:\n'
                    string += maze[i][0] + maze[i][1] + maze[i][2] + ':yellow_square:' + maze[i + 1][0] + maze[i + 1][1] + maze[i + 1][2] + ':yellow_square:' + maze[i + 2][0] + maze[i + 2][1] + maze[i + 2][2] + '\n'
                string += maze[i][3] + maze[i][4] + maze[i][5] + ':yellow_square:' + maze[i + 1][3] + maze[i + 1][4] +maze[i + 1][5] + ':yellow_square:' + maze[i + 2][3] + maze[i + 2][4] + maze[i + 2][5] + '\n'
                string += maze[i][6] + maze[i][7] + maze[i][8] + ':yellow_square:' + maze[i + 1][6] + maze[i + 1][7] +maze[i + 1][8] + ':yellow_square:' + maze[i + 2][6] + maze[i + 2][7] + maze[i + 2][8] + '\n'
            embed = discord.Embed(title="**" + str(ctx.author.name) + "** ~ :o: , **TEKO** ~ :x:",description=string, color=0x7F00FF)
            embed.set_author(name="ULTIMATE TIC-TAC-TOE")
            string = '\n'
            for i in range(3):
                for j in range(3):
                    if 3 * i + j + 1 in ppoint:
                        string += ':o:'
                    elif 3 * i + j + 1 in bpoint:
                        string += ':x:'
                    else:
                        string += ':blue_square:'
                    if i * 3 + j == 2 or i * 3 + j == 5:
                        string += '\n'
            if flag == 2:
                string += '\n:crown: **' + ctx.author.name + '** won :crown:\n'
            elif flag == 3:
                string += '\n:crown: **TEKO** won :crown:\n'
            elif (len(ppoint)+len(bpoint)==9) or (len(pos[1])+len(pos[2])+len(pos[3])+len(pos[4])+len(pos[5])+len(pos[6])+len(pos[7])+len(pos[8])+len(pos[9])==0):
                string += '\nIt was a tie\n'
                flag = 2
            else:
                string += '\n:small_blue_diamond: type `exit` to abort.'
            embed.add_field(name="ULTIMATE SCORE:", value=string, inline=False)
            if flag == 2 or flag == 3:
                await ctx.send(embed=embed)
                break
            if decision == 1 or (flag == 1 and decision % 2 != 0):
                embed.set_footer(text=ctx.author.name + ' turn:\ntype sub-grid number first then spot number like 13,49,etc.')
            else:
                embed.set_footer(text=ctx.author.name + ' turn (sub-grid ' + str(subgrid) + ') :\ntype spot number only (1-9).')
            if decision % 2 != 0:
                await ctx.send(embed=embed)
                try:
                    t2 = 0
                    while 1:
                        t1 = time.time()
                        msg = await client.wait_for('message', check=check(ctx.author), timeout=180 - t2)
                        msg1 = msg.content.lower()
                        if msg1 == 'exit':
                            await msg.add_reaction('\N{OCTAGONAL SIGN}')
                            flag = -1
                            break
                        elif (decision == 1 or flag == 1) and len(msg1) == 2 and msg1.isnumeric() == True and int(msg1[0]) != 0 and int(msg1[1]) != 0:
                            if maze[int(msg1[0]) - 1][int(msg1[1]) - 1] in [':one:', ':two:', ':three:', ':four:',':five:', ':six:', ':seven:', ':eight:',':nine:']:
                                maze[int(msg1[0]) - 1][int(msg1[1]) - 1] = ':o:'
                                o[int(msg1[0])].append(int(msg1[1]))
                                subgrid = int(msg1[1])
                                pos[int(msg1[0])].remove(int(msg1[1]))
                                flag = 0
                                break
                            else:
                                await msg.add_reaction('\N{CROSS MARK}')
                        elif flag != 1 and len(msg1) == 1 and msg1.isnumeric() == True and int(msg1) != 0:
                            if maze[subgrid - 1][int(msg1) - 1] in [':one:', ':two:', ':three:', ':four:', ':five:',':six:', ':seven:', ':eight:', ':nine:']:
                                maze[subgrid - 1][int(msg1) - 1] = ':o:'
                                o[subgrid].append(int(msg1))
                                pos[subgrid].remove(int(msg1))
                                subgrid = int(msg1)
                                break
                            else:
                                await msg.add_reaction('\N{CROSS MARK}')
                        t2+= int(time.time() - t1)
                except asyncio.TimeoutError:
                    await ctx.send('looks like you fell asleep,' + ctx.author.mention + '.')
                    break
            else:
                if flag==1:
                    subgrid=random.choice(list)
                    flag = 0
                spot = random.choice(pos[subgrid])
                pos[subgrid].remove(spot)
                maze[subgrid - 1][spot - 1] = ':x:'
                x[subgrid].append(spot)
                subgrid = spot
            if flag == -1:
                break
            for key in maze.keys():
                if (key + 1 not in filled_grid) and maze[key][0] != ':one:' and maze[key][1] != ':two:' and maze[key][2] != ':three:' and maze[key][3] != ':four:' and maze[key][4] != ':five:' and maze[key][5] != ':six:' and maze[key][6] != ':seven:' and maze[key][7] != ':eight:' and maze[key][8] != ':nine:':
                    filled_grid.append(key + 1)
                    list.remove(key+1)
            for key in o.keys():
                if len(o[key]) >= 3 and (key not in ppoint) and (key not in bpoint):
                    for w in win:
                        w = set(w)
                        point_set = set(o[key])
                        if w.issubset(point_set) == True:
                            ppoint.append(key)
                            for w in win:
                                w = set(w)
                                point_set = set(ppoint)
                                if w.issubset(point_set) == True:
                                    flag = 2
                                    break
                            if flag == 2:
                                break
                    if flag == 2:
                        break
            if flag == 2:
                continue
            for key in x.keys():
                if len(x[key]) >= 3 and (key not in bpoint) and (key not in ppoint):
                    for w in win:
                        w = set(w)
                        point_set = set(x[key])
                        if w.issubset(point_set) == True:
                            bpoint.append(key)
                            for w in win:
                                w = set(w)
                                point_set = set(bpoint)
                                if w.issubset(point_set) == True:
                                    flag = 3
                                    break
                            if flag == 3:
                                break
                    if flag == 3:
                        break
            if flag == 3:
                continue
            if subgrid in filled_grid:
                flag = 1
            decision += 1
        command_usage.remove(ctx.author.id)
        return
    command_usage.append(ctx.author.id)
    command_usage.append(arg1._user.id)
    decision = t2 = 0
    await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
    try:
        while 1:
            t1 = time.time()
            msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
            if msg.content.lower() == "yes" or msg.content.lower() == "y":
                decision = 1
                break
            elif msg.content.lower() == "no" or msg.content.lower() == "n":
                decision = -1
                break
            t2 += int(time.time() - t1)
    except asyncio.TimeoutError:
        await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    if decision == -1:
        await ctx.send("terminated")
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    filled_grid=[]
    ppoint=[]
    bpoint=[]
    win = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
    o={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    x={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    maze={}
    flag=0
    for i in range(9):
        maze[i]=[':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']
    while 1:
        for i in range(0,7,3):
            if i ==0:
                string=maze[i][0]+maze[i][1]+maze[i][2]+':yellow_square:'+maze[i+1][0]+maze[i+1][1]+maze[i+1][2]+':yellow_square:'+maze[i+2][0]+maze[i+2][1]+maze[i+2][2]+'\n'
            else:
                string += ':yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:\n'
                string += maze[i][0]+maze[i][1]+maze[i][2]+':yellow_square:'+maze[i+1][0]+maze[i+1][1]+maze[i+1][2]+':yellow_square:'+maze[i+2][0]+maze[i+2][1]+maze[i+2][2]+'\n'
            string+=maze[i][3]+maze[i][4]+maze[i][5]+':yellow_square:'+maze[i+1][3]+maze[i+1][4]+maze[i+1][5]+':yellow_square:'+maze[i+2][3]+maze[i+2][4]+maze[i+2][5]+'\n'
            string+=maze[i][6]+maze[i][7]+maze[i][8]+':yellow_square:'+maze[i+1][6]+maze[i+1][7]+maze[i+1][8]+':yellow_square:'+maze[i+2][6]+maze[i+2][7]+maze[i+2][8]+'\n'
        embed=discord.Embed(title="**" + str(ctx.author.name) + "** ~ :o: , **{}** ~ :x:".format(arg1.display_name),description=string, color=0x7F00FF)
        embed.set_author(name="ULTIMATE TIC-TAC-TOE")
        string='\n'
        for i in range(3):
            for j in range(3):
                if 3*i+j+1 in ppoint:
                    string+=':o:'
                elif 3*i+j+1 in bpoint:
                    string+=':x:'
                else:
                    string+=':blue_square:'
                if i*3+j==2 or i*3+j ==5:
                    string+='\n'
        if flag==2:
            string+='\n:crown: **'+ctx.author.name+'** won :crown:\n'
        elif flag==3:
            string += '\n:crown: **{}** won :crown:\n'.format(arg1.display_name)
        elif (len(x[1])+len(x[2])+len(x[3])+len(x[4])+len(x[5])+len(x[6])+len(x[7])+len(x[8])+len(x[9])+len(o[1])+len(o[2])+len(o[3])+len(o[4])+len(o[5])+len(o[6])+len(o[7])+len(o[8])+len(o[9])==81) or (len(ppoint)+len(bpoint)==9):
            string+='\nIt was a tie\n'
            flag=2
        else:
            string+='\n:small_blue_diamond: type `exit` to abort.'
        embed.add_field(name="ULTIMATE SCORE:", value=string, inline=False)
        if flag==2 or flag==3:
            await ctx.send(embed=embed)
            break
        if decision==1 or (flag==1 and decision%2!=0):
            embed.set_footer(text=ctx.author.name+' turn:\ntype sub-grid number first then spot number like 13,49,etc.')
        elif decision%2!=0:
            embed.set_footer(text=ctx.author.name + ' turn (sub-grid '+str(subgrid)+') :\ntype spot number only (1-9).')
        elif flag==1 and decision%2==0:
            embed.set_footer(text='{} turn:\ntype sub-grid number first then spot number like 13,49,etc.'.format(arg1.display_name))
        else:
            embed.set_footer(text='{} turn (sub-grid '.format(arg1.display_name)+str(subgrid)+') :\ntype spot number only (1-9).')
        await ctx.send(embed=embed)
        if decision%2!=0:
            t2=0
            try:
                while 1:
                    t1=time.time()
                    msg = await client.wait_for('message', check=check(ctx.author), timeout=180-t2)
                    msg1=msg.content.lower()
                    if msg1=='exit':
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        await ctx.send('aborted.')
                        flag=-1
                        break
                    elif (decision==1 or flag==1) and len(msg1)==2 and msg1.isnumeric()==True and int(msg1[0])!=0 and int(msg1[1])!=0:
                        if maze[int(msg1[0])-1][int(msg1[1])-1] in [':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']:
                            maze[int(msg1[0])-1][int(msg1[1])-1]=':o:'
                            o[int(msg1[0])].append(int(msg1[1]))
                            subgrid=int(msg1[1])
                            flag=0
                            break
                        else:
                            await msg.add_reaction('\N{CROSS MARK}')
                    elif flag!=1 and len(msg1)==1 and msg1.isnumeric()==True and int(msg1)!=0:
                        if maze[subgrid-1][int(msg1)-1] in [':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']:
                            maze[subgrid - 1][int(msg1) - 1]=':o:'
                            o[subgrid].append(int(msg1))
                            subgrid=int(msg1)
                            break
                        else:
                            await msg.add_reaction('\N{CROSS MARK}')
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send('looks like you fell asleep,'+ctx.author.mention+'.')
                break
        else:
            t2=0
            try:
                while 1:
                    t1=time.time()
                    msg = await client.wait_for('message', check=check(arg1._user), timeout=180-t2)
                    msg1=msg.content.lower()
                    if msg1=='exit':
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        await ctx.send('aborted.')
                        flag=-1
                        break
                    elif flag==1 and len(msg1)==2 and msg1.isnumeric()==True and int(msg1[0])!=0 and int(msg1[1])!=0:
                        if maze[int(msg1[0])-1][int(msg1[1])-1] in [':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']:
                            maze[int(msg1[0])-1][int(msg1[1])-1]=':x:'
                            x[int(msg1[0])].append(int(msg1[1]))
                            subgrid=int(msg1[1])
                            flag=0
                            break
                        else:
                            await msg.add_reaction('\N{CROSS MARK}')
                    elif flag!=1 and len(msg1)==1 and msg1.isnumeric()==True and int(msg1)!=0:
                        if maze[subgrid-1][int(msg1)-1] in [':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']:
                            maze[subgrid - 1][int(msg1) - 1]=':x:'
                            x[subgrid].append(int(msg1))
                            subgrid=int(msg1)
                            break
                        else:
                            await msg.add_reaction('\N{CROSS MARK}')
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send('looks like you fell asleep,{}.'.format(arg1.mention))
                break
        if flag==-1:
            break
        for key in maze.keys():
            if (key+1 not in filled_grid) and maze[key][0]!=':one:' and maze[key][1]!=':two:' and maze[key][2]!=':three:' and maze[key][3]!=':four:' and maze[key][4]!=':five:' and maze[key][5]!=':six:' and maze[key][6]!=':seven:' and maze[key][7]!=':eight:' and maze[key][8]!=':nine:':
                filled_grid.append(key+1)
        for key in o.keys():
            if len(o[key]) >=3 and (key not in ppoint) and (key not in bpoint):
                for w in win:
                    w = set(w)
                    point_set=set(o[key])
                    if w.issubset(point_set) == True:
                        ppoint.append(key)
                        for w in win:
                            w = set(w)
                            point_set = set(ppoint)
                            if w.issubset(point_set) == True:
                                flag=2
                                break
                        if flag==2:
                            break
                if flag==2:
                    break
        if flag==2:
            continue
        for key in x.keys():
            if len(x[key]) >=3 and (key not in bpoint) and (key not in ppoint):
                for w in win:
                    w = set(w)
                    point_set=set(x[key])
                    if w.issubset(point_set) == True:
                        bpoint.append(key)
                        for w in win:
                            w = set(w)
                            point_set = set(bpoint)
                            if w.issubset(point_set) == True:
                                flag=3
                                break
                        if flag==3:
                            break
                if flag==3:
                    break
        if flag==3:
            continue
        if subgrid in filled_grid:
            flag=1
        decision+=1
    command_usage.remove(ctx.author.id)
    command_usage.remove(arg1._user.id)

@client.command()
async def higherlower(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        command_usage.append(ctx.author.id)
        def check1(reaction,user):
            return ctx.author.id==user.id and reaction.emoji in ['⬆️', '⬇️', '❌']
        list = ['<:Ablack:797778470264242206>', '<:2black:797781010221760522>', '<:3black:797781317097095208>',
                '<:4black:797781687504601128>', '<:5black:797782123134058517>', '<:6black:797782962141528074>',
                '<:7black:797783957281570826>', '<:8black:797784212777336862>', '<:9black:797784475467382794>',
                '<:10black:797795657968123934>', '<:Jblack:797795699533807626>', '<:Qblack:797795786498637845>',
                '<:Kblack:797795814759202837>', '<:Ared:797796115659358208>', '<:2red:797796143600893993>',
                '<:3red:797796164963401748>', '<:4red:797796183804215327>', '<:5red:797796199955562506>',
                '<:6red:797796215722475570>', '<:7red:797796232994095144>', '<:8red:797796304767549441>',
                '<:9red:797796328838004747>', '<:10red:797796393838313482>', '<:Jred:797796421155029012>',
                '<:Qred:797796458069491732>', '<:Kred:797796484153475083>']
        random.shuffle(list)
        decision = 1
        flag1 = 0
        upoint = bpoint = 0
        prevcard = list.pop(-1)

        while len(list) != 0:

            if decision % 2 != 0:

                if len(list) == 2:
                    carddeck = '<:carddeck2:798031492164354058>'
                elif len(list) == 1:
                    carddeck = '<:carddeck1:798031461537415219>'
                elif len(list) >= 3:
                    carddeck = '<:carddeck3:798031475672088606>'

                string = "--------------------------------\n**" + ctx.author.name + "** score : " + str(upoint) + "\n**TEKO** score : " + str(bpoint) + "\n--------------------------------\n:small_blue_diamond: guess the number on next card.\n:small_blue_diamond: react :x: to abort.\n\n"
                if decision == 1:
                    string += ' '
                elif len(guess1) == 0:
                    string += guess2
                else:
                    string += guess1
                embed = discord.Embed(title=carddeck + "      " + prevcard, description=string, color=0x7F00FF)
                embed.set_footer(text=ctx.author.name + ' turn:')
                if decision == 1:
                    string1 = await ctx.send(embed=embed)
                    for emoji in ['⬆️', '⬇️', '❌']:
                        await string1.add_reaction(emoji)
                else:
                    await string1.edit(embed=embed)
                if prevcard[2] == 'A':
                    prevnum = 1
                elif prevcard[2] == 'J':
                    prevnum = 11
                elif prevcard[2] == 'Q':
                    prevnum = 12
                elif prevcard[2] == 'K':
                    prevnum = 13
                elif prevcard[2] == '1':
                    prevnum = 10
                else:
                    prevnum = int(prevcard[2])
                currcard = list.pop(-1)
                if currcard[2] == 'A':
                    currnum = 1
                elif currcard[2] == 'J':
                    currnum = 11
                elif currcard[2] == 'Q':
                    currnum = 12
                elif currcard[2] == 'K':
                    currnum = 13
                elif currcard[2] == '1':
                    currnum = 10
                else:
                    currnum = int(currcard[2])
                while flag1==0:
                    try:
                        reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                        if reaction.emoji== '❌':
                            await ctx.send('aborted')
                            flag1=-1
                        elif reaction.emoji in [ '⬆️', '⬇️']:
                            flag1=1
                        await string1.remove_reaction(reaction.emoji, ctx.author)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep," + ctx.author.mention + '.')
                        flag1 = -1
                        break
                if flag1 == -1:
                    break
                if currnum > prevnum:
                    ans = '⬆️'
                elif currnum < prevnum:
                    ans = '⬇️'
                else:
                    ans = 'equal'

                if ans == reaction.emoji:
                    upoint += 1
                    decision += 1
                    guess1 = "**CORRECT GUESS!!!** "
                elif ans != 'equal':
                    guess1 = "**WRONG GUESS!!! **"
                    guess2 = bchoice = ''
                else:
                    decision += 1
                prevcard = currcard
            else:
                if len(list) == 2:
                    carddeck = '<:carddeck2:798031492164354058>'
                elif len(list) == 1:
                    carddeck = '<:carddeck1:798031461537415219>'
                elif len(list) >= 3:
                    carddeck = '<:carddeck3:798031475672088606>'

                string = "--------------------------------\n**" + ctx.author.name + "** score : " + str(upoint) + "\n**TEKO** score : " + str(bpoint) + "\n--------------------------------\n:small_blue_diamond: guess the number on next card.\n:small_blue_diamond: react :x: to abort.\n\n"
                if len(guess2) == 0:
                    string += guess1
                else:
                    string += guess2
                embed = discord.Embed(title=carddeck + "      " + prevcard, description=string, color=0x7F00FF)
                embed.set_footer(text='TEKO turn:'+str(bchoice))
                await string1.edit(embed=embed)
                time.sleep(1)

                if prevcard[2] == 'A':
                    prevnum = 1
                elif prevcard[2] == 'J':
                    prevnum = 11
                elif prevcard[2] == 'Q':
                    prevnum = 12
                elif prevcard[2] == 'K':
                    prevnum = 13
                elif prevcard[2] == '1':
                    prevnum = 10
                else:
                    prevnum = int(prevcard[2])
                currcard = list.pop(-1)
                if currcard[2] == 'A':
                    currnum = 1
                elif currcard[2] == 'J':
                    currnum = 11
                elif currcard[2] == 'Q':
                    currnum = 12
                elif currcard[2] == 'K':
                    currnum = 13
                elif currcard[2] == '1':
                    currnum = 10
                else:
                    currnum = int(currcard[2])
                if prevnum > 10:
                    bchoice = "lower"
                    if currnum < prevnum:
                        guess2 = "**CORRECT GUESS!!!** "
                        bpoint += 1
                        decision += 1
                    elif currnum > prevnum:
                        guess2 = "**WRONG GUESS!!!**"
                        guess1 = ''
                    else:
                        decision += 1
                elif prevnum < 5:
                    bchoice = "higher"
                    if currnum > prevnum:
                        guess2 = "**CORRECT GUESS!!! **"
                        bpoint += 1
                        decision += 1
                    elif currnum < prevnum:
                        guess2 = "**WRONG GUESS!!!**"
                        guess1 = ''
                    else:
                        decision += 1
                else:
                    bchoice = random.choice(['higher', 'lower'])
                    if bchoice == 'higher':
                        if currnum > prevnum:
                            guess2 = "**CORRECT GUESS!!!** "
                            bpoint += 1
                            decision += 1
                        elif currnum < prevnum:
                            guess2 = "**WRONG GUESS!!!**"
                            guess1 = ''
                        else:
                            decision += 1
                    else:
                        if currnum < prevnum:
                            guess2 = "**CORRECT GUESS!!!** "
                            bpoint += 1
                            decision += 1
                        elif currnum > prevnum:
                            guess2 = "**WRONG GUESS!!!**"
                            guess1 = ''
                        else:
                            decision += 1
                prevcard = currcard
                time.sleep(1)
            decision += 1
            flag1 = 0
        if flag1 != -1:
            string = "--------------------------------\n**" + ctx.author.name + "** score : " + str(upoint) + "\n**TEKO** score : " + str(bpoint) + "\n--------------------------------\n"
            if upoint > bpoint:
                string+=":crown: **" + ctx.author.name + "** won :crown:"
            elif upoint < bpoint:
                string+=":crown: **TEKO** won :crown:"
            else:
                string+="tie"
            embed = discord.Embed(title='**' + ctx.author.name + '** vs  **TEKO**', description=string, color=0x7F00FF)
            await string1.edit(embed=embed)
        command_usage.remove(ctx.author.id)
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision =t2= 0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated")
        elif decision == 1:
            def check1(reaction, user):
                return (ctx.author.id == user.id and reaction.emoji in ['⬆️', '⬇️', '❌']) or (arg1._user.id == user.id and reaction.emoji=='❌')
            def check2(reaction, user):
                return (arg1._user.id == user.id and reaction.emoji in ['⬆️', '⬇️', '❌']) or (ctx.author.id == user.id and reaction.emoji=='❌')
            list = ['<:Ablack:797778470264242206>', '<:2black:797781010221760522>', '<:3black:797781317097095208>',
                    '<:4black:797781687504601128>', '<:5black:797782123134058517>', '<:6black:797782962141528074>',
                    '<:7black:797783957281570826>', '<:8black:797784212777336862>',
                    '<:9black:797784475467382794>', '<:10black:797795657968123934>', '<:Jblack:797795699533807626>',
                    '<:Qblack:797795786498637845>', '<:Kblack:797795814759202837>', '<:Ared:797796115659358208>',
                    '<:2red:797796143600893993>', '<:3red:797796164963401748>', '<:4red:797796183804215327>',
                    '<:5red:797796199955562506>', '<:6red:797796215722475570>', '<:7red:797796232994095144>',
                    '<:8red:797796304767549441>', '<:9red:797796328838004747>', '<:10red:797796393838313482>',
                    '<:Jred:797796421155029012>', '<:Qred:797796458069491732>', '<:Kred:797796484153475083>']
            random.shuffle(list)
            flag = 0
            upoint = bpoint = 0
            prevcard = list.pop(-1)

            while len(list) != 0:

                if decision % 2 != 0:

                    if len(list) == 2:
                        carddeck = '<:carddeck2:798031492164354058>'
                    elif len(list) == 1:
                        carddeck = '<:carddeck1:798031461537415219>'
                    elif len(list) >= 3:
                        carddeck = '<:carddeck3:798031475672088606>'

                    string = "--------------------------------\n**" + ctx.author.name + "** score : " + str(upoint) + "\n**{}** score : ".format(arg1.display_name) + str(bpoint) + "\n--------------------------------\n:small_blue_diamond: guess the number on next card.\n:small_blue_diamond: react :x: to abort.\n\n"
                    if decision == 1:
                        string += ' '
                    elif len(guess1) == 0:
                        string += guess2
                    else:
                        string += guess1
                    embed = discord.Embed(title=carddeck + "      " + prevcard, description=string, color=0x7F00FF)
                    embed.set_footer(text='**' + ctx.author.name + '** turn:')
                    if decision == 1:
                        string1 = await ctx.send(embed=embed)
                        for emoji in ['⬆️', '⬇️', '❌']:
                            await string1.add_reaction(emoji)
                    else:
                        await string1.edit(embed=embed)
                    if prevcard[2] == 'A':
                        prevnum = 1
                    elif prevcard[2] == 'J':
                        prevnum = 11
                    elif prevcard[2] == 'Q':
                        prevnum = 12
                    elif prevcard[2] == 'K':
                        prevnum = 13
                    elif prevcard[2] == '1':
                        prevnum = 10
                    else:
                        prevnum = int(prevcard[2])
                    currcard = list.pop(-1)
                    if currcard[2] == 'A':
                        currnum = 1
                    elif currcard[2] == 'J':
                        currnum = 11
                    elif currcard[2] == 'Q':
                        currnum = 12
                    elif currcard[2] == 'K':
                        currnum = 13
                    elif currcard[2] == '1':
                        currnum = 10
                    else:
                        currnum = int(currcard[2])

                    while flag1 == 0:
                        try:
                            reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                            if reaction.emoji == '❌':
                                await ctx.send('aborted')
                                flag1 = -1
                            elif reaction.emoji in ['⬆️', '⬇️']:
                                flag1 = 1
                            await string1.remove_reaction(reaction.emoji, ctx.author)
                        except asyncio.TimeoutError:
                            await ctx.send("looks like you fell asleep," + ctx.author.mention + '.')
                            flag1 = -1
                            break
                    if flag == -1:
                        break
                    if currnum > prevnum:
                        ans = '⬆️'
                    elif currnum < prevnum:
                        ans = '⬇️'
                    else:
                        ans = 'equal'

                    if ans == reaction.emoji:
                        upoint += 1
                        decision += 1
                        guess1 = "**CORRECT GUESS!!!** "
                    elif ans != 'equal':
                        guess1 = "**WRONG GUESS!!!**"
                        guess2 = ''
                    else:
                        decision += 1
                    prevcard = currcard
                else:
                    if len(list) == 2:
                        carddeck = '<:carddeck2:798031492164354058>'
                    elif len(list) == 1:
                        carddeck = '<:carddeck1:798031461537415219>'
                    elif len(list) >= 3:
                        carddeck = '<:carddeck3:798031475672088606>'

                    string = "--------------------------------\n**" + ctx.author.name + "** score : " + str(upoint) + "\n**{}** score : ".format(arg1.display_name) + str(bpoint) + "\n--------------------------------\n:small_blue_diamond: guess the number on next card.\n:small_blue_diamond: react :x: to abort.\n\n"
                    if len(guess2) == 0:
                        string += guess1
                    else:
                        string += guess2
                    embed = discord.Embed(title=carddeck + "      " + prevcard, description=string, color=0x7F00FF)
                    embed.set_footer(text='**{}** turn:'.format(arg1.display_name))
                    await string1.edit(embed=embed)

                    if prevcard[2] == 'A':
                        prevnum = 1
                    elif prevcard[2] == 'J':
                        prevnum = 11
                    elif prevcard[2] == 'Q':
                        prevnum = 12
                    elif prevcard[2] == 'K':
                        prevnum = 13
                    elif prevcard[2] == '1':
                        prevnum = 10
                    else:
                        prevnum = int(prevcard[2])
                    currcard = list.pop(-1)
                    if currcard[2] == 'A':
                        currnum = 1
                    elif currcard[2] == 'J':
                        currnum = 11
                    elif currcard[2] == 'Q':
                        currnum = 12
                    elif currcard[2] == 'K':
                        currnum = 13
                    elif currcard[2] == '1':
                        currnum = 10
                    else:
                        currnum = int(currcard[2])

                    while flag1 == 0:
                        try:
                            reaction, user = await client.wait_for('reaction_add', check=check2, timeout=60)
                            if reaction.emoji == '❌':
                                await ctx.send('aborted')
                                flag1 = -1
                            elif reaction.emoji in ['⬆️', '⬇️']:
                                flag1 = 1
                            await string1.remove_reaction(reaction.emoji, ctx.author)
                        except asyncio.TimeoutError:
                            await ctx.send("looks like you fell asleep,{}.".format(arg1.display_name))
                            flag1 = -1
                            break
                    if flag == -1:
                        break
                    if currnum > prevnum:
                        ans = '⬆️'
                    elif currnum < prevnum:
                        ans = '⬇️'
                    else:
                        ans = 'equal'

                    if ans == reaction.emoji:
                        bpoint += 1
                        decision += 1
                        guess2 = "**CORRECT GUESS!!! **"
                    elif ans != 'equal':
                        guess2 = "**WRONG GUESS!!! **"
                        guess1 = ''
                    else:
                        decision += 1
                    prevcard = currcard
                flag = 0
                decision += 1
            if flag != -1:
                string = "--------------------------------\n**" + ctx.author.name + "** score : " + str(upoint) + "\n**{}** score : ".format(arg1.display_name) + str(bpoint) + "\n--------------------------------"
                if upoint > bpoint:
                    string+=":crown: **" + ctx.author.name + "** won :crown:"
                elif upoint < bpoint:
                    string+=":crown: **{}** won :crown:".format(arg1.display_name)
                else:
                    string+="tie"
                await string1.edit(embed=discord.Embed(title="                 " + prevcard, description=string, color=0x7F00FF))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def gtn(ctx):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    command_usage.append(ctx.author.id)
    bnum = random.randint(1, 100)
    await ctx.send("I am thinking of number ?? in betweeen 1 to 100.\nCan you guess it? (`exit` to abort)")
    count = 0
    flag1 = int(count)
    try:
        t2=0
        while flag1 == 0:
            t1=time.time()
            msg1 = await client.wait_for('message', check=check(ctx.author), timeout=60-t2)
            msg = msg1.content.lower()
            if msg == 'exit':
                await msg1.add_reaction('\N{OCTAGONAL SIGN}')
                break
            if msg.isdigit():
                msg = int(msg)
                if msg in range(1, 101):
                    flag1 = 1
            t2+=int(time.time()-t1)
    except asyncio.TimeoutError:
        await ctx.send("looks like you fell asleep **" + ctx.author.name + "**.")

    while flag1 == 1 and msg != bnum:
        if msg - bnum in range(11):
            await ctx.send("my number is little lesser than " + str(msg))
        elif msg - bnum in range(11, 21):
            await ctx.send("my number is lesser than " + str(msg))
        elif msg - bnum in range(21, 99):
            await ctx.send("my number is way lesser than " + str(msg))
        elif bnum - msg in range(11):
            await ctx.send("my number is little greater than " + str(msg))
        elif bnum - msg in range(11, 21):
            await ctx.send("my number is greater than " + str(msg))
        elif bnum - msg in range(21, 99):
            await ctx.send("my number is way greater than " + str(msg))
        flag1 = 0
        try:
            t2=0
            while flag1 == 0:
                t1=time.time()
                msg1 = await client.wait_for('message', check=check(ctx.author), timeout=60-t2)
                msg = msg1.content.lower()
                if msg == 'exit':
                    await msg1.add_reaction('\N{OCTAGONAL SIGN}')
                    break
                if msg.isdigit():
                    msg = int(msg)
                    if msg in range(1, 101):
                        flag1 = 1
                t2+=int(time.time()-t1)
        except asyncio.TimeoutError:
            await ctx.send("looks like you fell asleep **" + ctx.author.name + "**.")
        count += 1
    if flag1 == 1:
        if count == 0:
            await ctx.send(
                embed=discord.Embed(title='PERFECT! You guessed in first try **' + str(ctx.author.name) + '**.',color=0x7F00FF))
        else:
            await ctx.send(embed=discord.Embed(title='CORRECT GUESS ' + str(ctx.author.name) + '!',description="Tries : " + str(count + 1), color=0x7F00FF))
    command_usage.remove(ctx.author.id)

@client.command()
async def quickbattle(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1 == None:
        command_usage.append(ctx.author.id)
        def check1(reaction,user):
            return ctx.author.id==user.id and reaction.emoji in ['🇦','🇧','🆎','❌']
        embed = discord.Embed(title=ctx.author.name + ',choose one weapon crate (A/B/C)', color=0x7F00FF)
        embed.set_image(url='https://i.imgur.com/C9TTdyZ.png')
        embed.set_footer(text="type 'exit' to abort.")
        await ctx.send(embed=embed)
        flag0 = t2=0
        try:
            while flag0 == 0:
                t1=time.time()
                msg = await client.wait_for('message', check=check(ctx.author), timeout=60-t2)
                msg = msg.content.lower()
                if msg == 'exit':
                    await msg.add_reaction('\N{OCTAGONAL SIGN}')
                    await ctx.send('aborted.')
                    break
                if msg == 'a' or msg == 'b' or msg == "c":
                    flag0 = 1
                t2+=int(time.time()-t1)
        except asyncio.TimeoutError:
            await ctx.send("looks like you fell asleep **" + ctx.author.name + "**.")

        if flag0 == 1:
            attack = ["steel sword", "dragon's axe", "eternal wand", "demonic axe", "inferno sabre"]
            defense = ["wooden armor", "silver armor", "cursed armor", "horned shield", "devils head"]
            at_emoji = ['<:steel_sword:846613638629425172>', '<:dragons_axe:846638164428718121>',
                        '<:eternal_wand:846693813496971275>', '<:demonic_axe:846721643216371762>',
                        '<:inferno_sabre:846731022518583308>']
            def_emoji = ['<:wooden_armor:846796698570588180>', '<:silver_armor:846987110320832513>',
                         '<:cursed_shield:847059204791599134>', '<:horned_shield:847075416077631539>',
                         '<:devils_head:847088212106412042>']
            p1_health = p2_health = 200

            if msg == 'a':
                choice = random.choice(['C', 'B'])
            elif msg == 'b':
                choice = random.choice(['A', 'C'])
            else:
                choice = random.choice(['A', 'B'])

            chance = random.randint(1, 101)
            if chance <= 42:
                p1_at = attack[0]
                a1_emoji = at_emoji[0]
                a1i = 20
                a1j = 31
            elif chance <= 64:
                p1_at = attack[1]
                a1_emoji = at_emoji[1]
                a1i = 20
                a1j = 41
            elif chance <= 81:
                p1_at = attack[2]
                a1_emoji = at_emoji[2]
                a1i = 30
                a1j = 41
            elif chance <= 93:
                p1_at = attack[3]
                a1_emoji = at_emoji[3]
                a1i = 30
                a1j = 51
            else:
                p1_at = attack[4]
                a1_emoji = at_emoji[4]
                a1i = 40
                a1j = 61

            chance = random.randint(1, 101)
            if chance <= 42:
                p1_def = defense[0]
                d1_emoji = def_emoji[0]
                d1i = 2
                d1j = 6
            elif chance <= 64:
                p1_def = defense[1]
                d1_emoji = def_emoji[1]
                d1i = 5
                d1j = 10
            elif chance <= 81:
                p1_def = defense[2]
                d1_emoji = def_emoji[2]
                d1i = 10
                d1j = 17
            elif chance <= 93:
                p1_def = defense[3]
                d1_emoji = def_emoji[3]
                d1i = 12
                d1j = 21
            else:
                p1_def = defense[4]
                d1_emoji = def_emoji[4]
                d1i = 15
                d1j = 26
            chance = random.randint(1, 101)
            if chance <= 42:
                p2_at = attack[0]
                a2_emoji = at_emoji[0]
                a2i = 20
                a2j = 31
            elif chance <= 64:
                p2_at = attack[1]
                a2_emoji = at_emoji[1]
                a2i = 20
                a2j = 41
            elif chance <= 81:
                p2_at = attack[2]
                a2_emoji = at_emoji[2]
                a2i = 30
                a2j = 41
            elif chance <= 93:
                p2_at = attack[3]
                a2_emoji = at_emoji[3]
                a2i = 30
                a2j = 51
            else:
                p2_at = attack[4]
                a2_emoji = at_emoji[4]
                a2i = 40
                a2j = 61

            chance = random.randint(1, 101)
            if chance <= 42:
                p2_def = defense[0]
                d2_emoji = def_emoji[0]
                d2i = 2
                d2j = 6
            elif chance <= 64:
                p2_def = defense[1]
                d2_emoji = def_emoji[1]
                d2i = 5
                d2j = 10
            elif chance <= 81:
                p2_def = defense[2]
                d2_emoji = def_emoji[2]
                d2i = 10
                d2j = 17
            elif chance <= 93:
                p2_def = defense[3]
                d2_emoji = def_emoji[3]
                d2i = 12
                d2j = 21
            else:
                p2_def = defense[4]
                d2_emoji = def_emoji[4]
                d2i = 15
                d2j = 26

            string = '**' + ctx.author.name + '** chosen ' + msg.upper() + ' while **TEKO** chosen ' + choice + '.\n\n<a:crate_opening:847360093560242196> (opening crate **' + msg.upper() + '**)...'
            msg1 = await ctx.send(embed=discord.Embed(description=string, color=0x7F00FF))
            time.sleep(3)
            string = '**' + ctx.author.name + '** chosen ' + msg.upper() + ' while **TEKO** chosen ' + choice + '.\n\n<:open_crate:847354402334703617> (crate **' + msg.upper() + '** opened) : \n**' + ctx.author.name + "** got __" + p1_at + "__ [" + a1_emoji + "] and __" + p1_def + "__ [" + d1_emoji + '].'
            string += '\n\n<a:crate_opening:847360093560242196> (opening crate **' + choice + '**)...'
            await msg1.edit(embed=discord.Embed(description=string, color=0x7F00FF))
            time.sleep(3)
            string = '**' + ctx.author.name + '** chosen ' + msg.upper() + ' while **TEKO** chosen ' + choice + '.\n\n<:open_crate:847354402334703617> (crate **' + msg.upper() + '** opened) : \n**' + ctx.author.name + "** got __" + p1_at + "__ [" + a1_emoji + "] and __" + p1_def + "__ [" + d1_emoji + '].'
            string += '\n\n<:open_crate:847354402334703617> (crate **' + choice + '** opened):\n**TEKO** got __' + p2_at + "__ [" + a2_emoji + "] and __" + p2_def + "__ [" + d2_emoji + '].'
            await msg1.edit(embed=discord.Embed(description=string, color=0x7F00FF))
            time.sleep(1)
            flag1 = flag0 = 0
            while flag1 >= 0:
                if p1_health < 0:
                    p1_health = 0
                if p2_health < 0:
                    p2_health = 0
                if flag1 == 0:
                    ubar = '**' + ctx.author.name + '**\n<:green_front:851765622832627732>'
                    bbar = '**TEKO**\n<:green_front:851765622832627732>'
                    for i in range(10):
                        ubar += '<:green_bar:851761532664938507>'
                        bbar += '<:green_bar:851761532664938507>'
                    ubar += '<:green_end:851761504276447242> ' + str(p1_health) + ' HP\n\n'
                    bbar += '<:green_end:851761504276447242> ' + str(p2_health) + ' HP'
                    string = "🇦 -> to attack the opponent with sword.\n🇧 -> to block opponent's attack with armor.\n🆎 -> to attack while blocking opponent's attack."
                    embed = discord.Embed(title=':boom: ' + ctx.author.name + ' vs TEKO :boom:',description=string + '\n\n' + ubar + bbar, color=0x7F00FF)
                    embed.set_footer(text=ctx.author.name+" turn:")
                    msg = await ctx.send(embed=embed)
                    for emoji in ['🇦','🇧','🆎','❌']:
                        await msg.add_reaction(emoji)
                else:
                    if p1_health <= 36:
                        ubar = '**' + ctx.author.name + '**\n'
                        if p1_health == 0:
                            ubar += '<:black_front:851761853461954591>'
                            for i in range(10):
                                ubar += '<:black_bar:851772206820491282>'
                        elif p1_health >= 18:
                            ubar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                            for i in range(9):
                                ubar += '<:black_bar:851772206820491282>'
                        else:
                            ubar += '<:red_end:851761608614215690>'
                            for i in range(10):
                                ubar += '<:black_bar:851772206820491282>'
                        ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                    elif p1_health <= 100:
                        ubar = '**' + ctx.author.name + '**\n<:yellow_end:851765642088284190>'
                        for i in range(int(p1_health / 18) - 1):
                            ubar += '<:yellow_bar:851761551416229898>'
                        for i in range(11 - int(p1_health / 18)):
                            ubar += '<:black_bar:851772206820491282>'
                        ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                    elif p1_health < 200:
                        ubar = '**' + ctx.author.name + '**\n<:green_front:851765622832627732>'
                        for i in range(int(p1_health / 18) - 1):
                            ubar += '<:green_bar:851761532664938507>'
                        for i in range(11 - int(p1_health / 18)):
                            ubar += '<:black_bar:851772206820491282>'
                        ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'

                    if p2_health <= 36:
                        bbar = '**TEKO**\n'
                        if p2_health == 0:
                            bbar += '<:black_front:851761853461954591>'
                            for i in range(10):
                                bbar += '<:black_bar:851772206820491282>'
                        elif p2_health >= 18:
                            bbar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                            for i in range(9):
                                bbar += '<:black_bar:851772206820491282>'
                        else:
                            bbar += '<:red_end:851761608614215690>'
                            for i in range(10):
                                bbar += '<:black_bar:851772206820491282>'
                        bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                    elif p2_health <= 100:
                        bbar = '**TEKO**\n<:yellow_end:851765642088284190>'
                        for i in range(int(p2_health / 18) - 1):
                            bbar += '<:yellow_bar:851761551416229898>'
                        for i in range(11 - int(p2_health / 18)):
                            bbar += '<:black_bar:851772206820491282>'
                        bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                    elif p2_health < 200:
                        bbar = '**TEKO**\n<:green_front:851765622832627732>'
                        for i in range(int(p2_health / 18) - 1):
                            bbar += '<:green_bar:851761532664938507>'
                        for i in range(11 - int(p2_health / 18)):
                            bbar += '<:black_bar:851772206820491282>'
                        bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                    embed = discord.Embed(title=':boom: ' + ctx.author.name + ' vs TEKO :boom:',description=string + '\n\n' + ubar + bbar, color=0x7F00FF)
                    embed.set_footer(text=ctx.author.name+" turn:")
                    await msg.edit(embed=embed)
                if p1_health == 0 or p2_health == 0:
                    break

                try:
                    while flag0 == 0:
                        reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                        if reaction.emoji == '❌':
                            await ctx.send('aborted.')
                            break
                        elif reaction.emoji=='🇦':
                            flag0 = 1
                            p1_choice='a'
                        elif reaction.emoji=='🇧':
                            flag0 = 1
                            p1_choice = 'b'
                        elif reaction.emoji=='🆎':
                            flag0 = 1
                            p1_choice = 'ab'
                        await msg.remove_reaction(reaction.emoji, ctx.author)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep **" + ctx.author.mention + "**.")
                    flag0 = 0

                if flag0 == 0:
                    break
                if p1_choice == 'a':
                    damage = random.randint(a1i, a1j)
                    p2_choice = random.choice(['a', 'b', 'ab'])
                    if p2_choice == 'a':
                        string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to attack , **TEKO** also attacked but failed.__**TEKO** lost " + str(
                            damage) + ' HP.__'
                        p2_health = p2_health - damage
                    elif p2_choice == 'b':
                        damage = damage - int(damage * random.randint(d2i, d2j) * 0.01)
                        string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to attack but **TEKO** blocked.__**TEKO** lost " + str(
                            damage) + ' HP.__'
                        p2_health = p2_health - damage
                    else:
                        damage = random.randint(a2i, a2j)
                        string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to attack but **TEKO** decided to attack while blocking.__**" + ctx.author.name + '** lost ' + str(
                            damage) + ' HP.__'
                        p1_health = p1_health - damage
                elif p1_choice == 'b':
                    p2_choice = random.choice(['a', 'b', 'ab'])
                    if p2_choice == 'a':
                        damage = random.randint(a2i, a2j)
                        if (p1_def == defense[2] and p2_at == attack[1]) or (p1_def == defense[4] and p2_at == attack[3]):
                            damage = damage - 2 * int(damage * random.randint(d1i, d1j) * 0.01)
                        else:
                            damage = damage - int(damage * random.randint(d1i, d1j) * 0.01)
                        string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to block while **TEKO** attacked.__**" + ctx.author.name + "** lost " + str(
                            damage) + " HP.__"
                        p1_health = p1_health - damage
                    elif p2_choice == 'b':
                        if p1_def == defense[3]:
                            damage = int(0.5 * random.randint(a1i, a1j))
                            string = "__**LOGS**__\n>**" + ctx.author.name + '** decided to block,**TEKO** also blocked but **' + ctx.author.name + '** managed to give some damage with their horned shield.__**TEKO** lost ' + str(
                                damage) + " HP.__"
                            p2_health = p2_health - damage
                        else:
                            string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to block ,**TEKO** also blocked.__Nothing happened.__'
                    else:
                        damage = random.randint(a2i, a2j)
                        string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to block while **TEKO** decided to attack while block but hurt themselves.__**TEKO** lost ' + str(
                            damage) + " HP.__"
                        p2_health = p2_health - damage
                else:
                    damage = random.randint(a1i, a1j)
                    p2_choice = random.choice(['a', 'b', 'ab'])
                    if p2_choice == 'a':
                        string = '__**LOGS**__\n>**' + ctx.author.name + '** decide to attack while block while **TEKO** decided to attack but failed.__**TEKO** lost ' + str(
                            damage) + " HP.__"
                        p2_health = p2_health - damage
                    elif p2_choice == 'b':
                        string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to attack while block but **TEKO** decided to block and hence **' + ctx.author.name + '** hurt themselves.__**' + ctx.author.name + '** lost ' + str(
                            damage) + " HP.__"
                        p1_health = p1_health - damage
                    else:
                        damage = damage - int(0.005 * damage * random.randint(d2i, d2j))
                        string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to attack while block , **TEKO** did the same but **' + ctx.author.name + '** attack was more aggressive.__**TEKO** lost ' + str(
                            damage) + " HP.__"
                        p2_health = p2_health - damage
                if p1_health < 0:
                    p1_health = 0
                if p2_health < 0:
                    p2_health = 0

                if p1_health <= 36:
                    ubar = '**' + ctx.author.name + '**\n'
                    if p1_health == 0:
                        ubar += '<:black_front:851761853461954591>'
                        for i in range(10):
                            ubar += '<:black_bar:851772206820491282>'
                    elif p1_health >= 18:
                        ubar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                        for i in range(9):
                            ubar += '<:black_bar:851772206820491282>'
                    else:
                        ubar += '<:red_end:851761608614215690>'
                        for i in range(10):
                            ubar += '<:black_bar:851772206820491282>'
                    ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                elif p1_health <= 100:
                    ubar = '**' + ctx.author.name + '**\n<:yellow_end:851765642088284190>'
                    for i in range(int(p1_health / 18) - 1):
                        ubar += '<:yellow_bar:851761551416229898>'
                    for i in range(11 - int(p1_health / 18)):
                        ubar += '<:black_bar:851772206820491282>'
                    ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                elif p1_health < 200:
                    ubar = '**' + ctx.author.name + '**\n<:green_front:851765622832627732>'
                    for i in range(int(p1_health / 18) - 1):
                        ubar += '<:green_bar:851761532664938507>'
                    for i in range(11 - int(p1_health / 18)):
                        ubar += '<:black_bar:851772206820491282>'
                    ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'

                if p2_health <= 36:
                    bbar = '**TEKO**\n'
                    if p2_health == 0:
                        bbar += '<:black_front:851761853461954591>'
                        for i in range(10):
                            bbar += '<:black_bar:851772206820491282>'
                    elif p2_health >= 18:
                        bbar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                        for i in range(9):
                            bbar += '<:black_bar:851772206820491282>'
                    else:
                        bbar += '<:red_end:851761608614215690>'
                        for i in range(10):
                            bbar += '<:black_bar:851772206820491282>'
                    bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                elif p2_health <= 100:
                    bbar = '**TEKO**\n<:yellow_end:851765642088284190>'
                    for i in range(int(p2_health / 18) - 1):
                        bbar += '<:yellow_bar:851761551416229898>'
                    for i in range(11 - int(p2_health / 18)):
                        bbar += '<:black_bar:851772206820491282>'
                    bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                elif p2_health < 200:
                    bbar = '**TEKO**\n<:green_front:851765622832627732>'
                    for i in range(int(p2_health / 18) - 1):
                        bbar += '<:green_bar:851761532664938507>'
                    for i in range(11 - int(p2_health / 18)):
                        bbar += '<:black_bar:851772206820491282>'
                    bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                embed = discord.Embed(title=':boom: ' + ctx.author.name + ' vs TEKO :boom:',description=string + '\n\n' + ubar + bbar, color=0x7F00FF)
                embed.set_footer(text="TEKO turn:")
                await msg.edit(embed=embed)

                if p1_health == 0 or p2_health == 0:
                    break
                time.sleep(1)
                p2_choice = random.choice(['a', 'b', 'ab', 'a', 'ab'])
                if p2_choice == 'a':
                    damage = random.randint(a2i, a2j)
                    p1_choice = random.choice(['a', 'b', 'ab'])
                    if p1_choice == 'a':
                        string += "\n>**TEKO** decided to attack , **" + ctx.author.name + "** also attacked but failed.__**" + ctx.author.name + "** lost " + str(
                            damage) + ' HP.__'
                        p1_health = p1_health - damage
                    elif p1_choice == 'b':
                        damage = damage - int(damage * random.randint(d1i, d1j) * 0.01)
                        string += "\n>**TEKO** decided to attack but **" + ctx.author.name + "** blocked.__**" + ctx.author.name + "** lost " + str(
                            damage) + ' HP.__'
                        p1_health = p1_health - damage
                    else:
                        damage = random.randint(a1i, a1j)
                        string += '\n>**TEKO** decided to attack but **' + ctx.author.name + '** decided to attack while blocking.__**TEKO** lost ' + str(
                            damage) + ' HP.__'
                        p2_health = p2_health - damage
                elif p2_choice == 'b':
                    p1_choice = random.choice(['a', 'b', 'ab'])
                    if p1_choice == 'a':
                        damage = random.randint(a1i, a1j)
                        if (p2_def == defense[2] and p1_at == attack[1]) or (
                                p2_def == defense[4] and p1_at == attack[3]):
                            damage = damage - 2 * int(damage * random.randint(d2i, d2j) * 0.01)
                        else:
                            damage = damage - int(damage * random.randint(d2i, d2j) * 0.01)
                        string += "\n>**TEKO** decided to block while **" + ctx.author.name + "** attacked.__**TEKO** lost " + str(
                            damage) + " HP.__"
                        p2_health = p2_health - damage
                    elif p1_choice == 'b':
                        if p2_def == defense[3]:
                            damage = int(0.5 * random.randint(a2i, a2j))
                            string += '\n>**TEKO** decided to block,**' + ctx.author.name + '** also blocked but **TEKO** managed to give some damage with their horned shield.__**' + ctx.author.name + '** lost ' + str(
                                damage) + " HP.__"
                            p1_health = p1_health - damage
                        else:
                            string += '\n>**TEKO** decided to block ,**' + ctx.author.name + '** also blocked.__Nothing happened.__'
                    else:
                        damage = random.randint(a1i, a1j)
                        string += '\n>**TEKO** decided to block while **' + ctx.author.name + '** decided to attack while block but hurt themselves.__**' + ctx.author.name + '** lost ' + str(
                            damage) + " HP.__"
                        p1_health = p1_health - damage
                else:
                    damage = random.randint(a2i, a2j)
                    p1_choice = random.choice(['a', 'b', 'ab'])
                    if p1_choice == 'a':
                        string += '\n>**TEKO** decide to attack while block while **' + ctx.author.name + '** decided to attack but failed.__**' + ctx.author.name + '** lost ' + str(
                            damage) + " HP.__"
                        p1_health = p1_health - damage
                    elif p1_choice == 'b':
                        string += '\n>**TEKO** decided to attack while block but **' + ctx.author.name + '** decided to block and hence **TEKO** hurt themselves.__**TEKO** lost ' + str(
                            damage) + " HP.__"
                        p2_health = p2_health - damage
                    else:
                        damage = damage - int(0.005 * damage * random.randint(d1i, d1j))
                        string += '\n>**TEKO** decided to attack while block , **' + ctx.author.name + '** did the same but **TEKO** attack was more aggressive.__**' + ctx.author.name + '** lost ' + str(
                            damage) + " HP.__"
                        p1_health = p1_health - damage
                flag1 = flag1 + 1
                flag0 = 0
            if p2_health == 0:
                await ctx.send(":crown: **" + ctx.author.name + "** won :crown:")
            elif p1_health == 0:
                await ctx.send(":crown: **TEKO** won :crown:")
        command_usage.remove(ctx.author.id)
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision =t2= 0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated.")
        elif decision == 1:
            def check1(reaction, user):
                return (ctx.author.id == user.id and reaction.emoji in ['🇦', '🇧', '🆎', '❌']) or (arg1._user.id==user.id and reaction.emoji=='❌')
            def check2(reaction, user):
                return (arg1._user.id == user.id and reaction.emoji in ['🇦', '🇧', '🆎', '❌']) or (ctx.author.id==user.id and reaction.emoji=='❌')
            embed = discord.Embed(title=ctx.author.name + ',choose one weapon crate (A/B/C)', color=0x7F00FF)
            embed.set_image(url='https://i.imgur.com/C9TTdyZ.png')
            embed.set_footer(text="type 'exit' to abort.")
            await ctx.send(embed=embed)
            flag = 0
            p1_choice = p2_choice = 'x'
            try:
                t2=0
                while flag <= 1:
                    t1=time.time()
                    msg = await client.wait_for('message', timeout=60-t2)

                    if (msg.author == ctx.author or msg.author == arg1._user) and msg.content.lower() == 'exit':
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        await ctx.send('aborted.')
                        flag = 0
                        break
                    if msg.author == ctx.author and (
                            msg.content.lower() == 'a' or msg.content.lower() == 'b' or msg.content.lower() == "c") and p1_choice == 'x':
                        if p2_choice == 'x' or (p2_choice != 'x' and p2_choice != msg.content.upper()):
                            p1_choice = msg.content.upper()
                            flag = flag + 1

                    if msg.author == arg1._user and (
                            msg.content.lower() == 'a' or msg.content.lower() == 'b' or msg.content.lower() == "c") and p2_choice == 'x':
                        if p1_choice == 'x' or (p1_choice != 'x' and p1_choice != msg.content.upper()):
                            p2_choice = msg.content.upper()
                            flag = flag + 1
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send("terminated.")
                flag = 0

            if flag != 0:
                attack = ["steel sword", "dragon's axe", "eternal wand", "demonic axe", "inferno sabre"]
                defense = ["wooden armor", "silver armor", "cursed armor", "horned shield", "devils head"]
                at_emoji = ['<:steel_sword:846613638629425172>', '<:dragons_axe:846638164428718121>',
                            '<:eternal_wand:846693813496971275>', '<:demonic_axe:846721643216371762>',
                            '<:inferno_sabre:846731022518583308>']
                def_emoji = ['<:wooden_armor:846796698570588180>', '<:silver_armor:846987110320832513>',
                             '<:cursed_shield:847059204791599134>', '<:horned_shield:847075416077631539>',
                             '<:devils_head:847088212106412042>']
                p1_health = p2_health = 200

                chance = random.randint(1, 101)
                if chance <= 42:
                    p1_at = attack[0]
                    a1_emoji = at_emoji[0]
                    a1i = 20
                    a1j = 31
                elif chance <= 64:
                    p1_at = attack[1]
                    a1_emoji = at_emoji[1]
                    a1i = 20
                    a1j = 41
                elif chance <= 81:
                    p1_at = attack[2]
                    a1_emoji = at_emoji[2]
                    a1i = 30
                    a1j = 41
                elif chance <= 93:
                    p1_at = attack[3]
                    a1_emoji = at_emoji[3]
                    a1i = 30
                    a1j = 51
                else:
                    p1_at = attack[4]
                    a1_emoji = at_emoji[4]
                    a1i = 40
                    a1j = 61

                chance = random.randint(1, 101)
                if chance <= 42:
                    p1_def = defense[0]
                    d1_emoji = def_emoji[0]
                    d1i = 2
                    d1j = 6
                elif chance <= 64:
                    p1_def = defense[1]
                    d1_emoji = def_emoji[1]
                    d1i = 5
                    d1j = 10
                elif chance <= 81:
                    p1_def = defense[2]
                    d1_emoji = def_emoji[2]
                    d1i = 10
                    d1j = 17
                elif chance <= 93:
                    p1_def = defense[3]
                    d1_emoji = def_emoji[3]
                    d1i = 12
                    d1j = 21
                else:
                    p1_def = defense[4]
                    d1_emoji = def_emoji[4]
                    d1i = 15
                    d1j = 26
                chance = random.randint(1, 101)
                if chance <= 42:
                    p2_at = attack[0]
                    a2_emoji = at_emoji[0]
                    a2i = 20
                    a2j = 31
                elif chance <= 64:
                    p2_at = attack[1]
                    a2_emoji = at_emoji[1]
                    a2i = 20
                    a2j = 41
                elif chance <= 81:
                    p2_at = attack[2]
                    a2_emoji = at_emoji[2]
                    a2i = 30
                    a2j = 41
                elif chance <= 93:
                    p2_at = attack[3]
                    a2_emoji = at_emoji[3]
                    a2i = 30
                    a2j = 51
                else:
                    p2_at = attack[4]
                    a2_emoji = at_emoji[4]
                    a2i = 40
                    a2j = 61

                chance = random.randint(1, 101)
                if chance <= 42:
                    p2_def = defense[0]
                    d2_emoji = def_emoji[0]
                    d2i = 2
                    d2j = 6
                elif chance <= 64:
                    p2_def = defense[1]
                    d2_emoji = def_emoji[1]
                    d2i = 5
                    d2j = 10
                elif chance <= 81:
                    p2_def = defense[2]
                    d2_emoji = def_emoji[2]
                    d2i = 10
                    d2j = 17
                elif chance <= 93:
                    p2_def = defense[3]
                    d2_emoji = def_emoji[3]
                    d2i = 12
                    d2j = 21
                else:
                    p2_def = defense[4]
                    d2_emoji = def_emoji[4]
                    d2i = 15
                    d2j = 26

                string = '**' + ctx.author.name + '** chosen ' + p1_choice + ' while **{}** chosen '.format(
                    arg1.display_name) + p2_choice + '.\n\n<a:crate_opening:847360093560242196> (opening crate **' + p1_choice + '**)...'
                msg1 = await ctx.send(embed=discord.Embed(description=string, color=0x7F00FF))
                time.sleep(3)
                string = '**' + ctx.author.name + '** chosen ' + p1_choice + ' while **{}** chosen '.format(
                    arg1.display_name) + p2_choice + '.\n\n<:open_crate:847354402334703617> (crate **' + p1_choice + '** opened) : \n**' + ctx.author.name + "** got __" + p1_at + "__ [" + a1_emoji + "] and __" + p1_def + "__ [" + d1_emoji + '].'
                string += '\n\n<a:crate_opening:847360093560242196> (opening crate **' + p2_choice + '**)...'
                await msg1.edit(embed=discord.Embed(description=string, color=0x7F00FF))
                time.sleep(3)
                string = '**' + ctx.author.name + '** chosen ' + p1_choice + ' while **TEKO** chosen ' + p2_choice + '.\n\n<:open_crate:847354402334703617> (crate **' + p1_choice + '** opened) : \n**' + ctx.author.name + "** got __" + p1_at + "__ [" + a1_emoji + "] and __" + p1_def + "__ [" + d1_emoji + '].'
                string += '\n\n<:open_crate:847354402334703617> (crate **' + p2_choice + '** opened):\n**{}** got __'.format(
                    arg1.display_name) + p2_at + "__ [" + a2_emoji + "] and __" + p2_def + "__ [" + d2_emoji + '].'
                await msg1.edit(embed=discord.Embed(description=string, color=0x7F00FF))
                time.sleep(1)
                flag1 = flag = 0
                while flag1 >= 0:
                    if p1_health < 0:
                        p1_health = 0
                    if p2_health < 0:
                        p2_health = 0
                    if flag1 == 0:
                        ubar = '**' + ctx.author.name + '**\n<:green_front:851765622832627732>'
                        bbar = '**TEKO**\n<:green_front:851765622832627732>'
                        for i in range(10):
                            ubar += '<:green_bar:851761532664938507>'
                            bbar += '<:green_bar:851761532664938507>'
                        ubar += '<:green_end:851761504276447242> ' + str(p1_health) + ' HP\n\n'
                        bbar += '<:green_end:851761504276447242> ' + str(p2_health) + ' HP'
                        string = "a -> to attack the opponent with sword.\nb -> to block opponent's attack with armor.\nab -> to attack while blocking opponent's attack."
                        embed = discord.Embed( title=':boom: ' + ctx.author.name + ' vs {} :boom:'.format(arg1.display_name),description=string + '\n\n' + ubar + bbar.format(arg1.display_name), color=0x7F00FF)
                        embed.set_footer(text=ctx.author.name+" turn:")
                        msg = await ctx.send(embed=embed)
                        for emoji in ['🇦', '🇧', '🆎', '❌']:
                            await msg.add_reaction(emoji)
                    else:
                        if p1_health <= 36:
                            ubar = '**' + ctx.author.name + '**\n'
                            if p1_health == 0:
                                ubar += '<:black_front:851761853461954591>'
                                for i in range(10):
                                    ubar += '<:black_bar:851772206820491282>'
                            elif p1_health >= 18:
                                ubar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                                for i in range(9):
                                    ubar += '<:black_bar:851772206820491282>'
                            else:
                                ubar += '<:red_end:851761608614215690>'
                                for i in range(10):
                                    ubar += '<:black_bar:851772206820491282>'
                            ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                        elif p1_health <= 100:
                            ubar = '**' + ctx.author.name + '**\n<:yellow_end:851765642088284190>'
                            for i in range(int(p1_health / 18) - 1):
                                ubar += '<:yellow_bar:851761551416229898>'
                            for i in range(11 - int(p1_health / 18)):
                                ubar += '<:black_bar:851772206820491282>'
                            ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                        elif p1_health < 200:
                            ubar = '**' + ctx.author.name + '**\n<:green_front:851765622832627732>'
                            for i in range(int(p1_health / 18) - 1):
                                ubar += '<:green_bar:851761532664938507>'
                            for i in range(11 - int(p1_health / 18)):
                                ubar += '<:black_bar:851772206820491282>'
                            ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'

                        if p2_health <= 36:
                            bbar = '**{}**\n'.format(arg1.display_name)
                            if p2_health == 0:
                                bbar += '<:black_front:851761853461954591>'
                                for i in range(10):
                                    bbar += '<:black_bar:851772206820491282>'
                            elif p2_health >= 18:
                                bbar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                                for i in range(9):
                                    bbar += '<:black_bar:851772206820491282>'
                            else:
                                bbar += '<:red_end:851761608614215690>'
                                for i in range(10):
                                    bbar += '<:black_bar:851772206820491282>'
                            bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                        elif p2_health <= 100:
                            bbar = '**{}**\n<:yellow_end:851765642088284190>'.format(arg1.display_name)
                            for i in range(int(p2_health / 18) - 1):
                                bbar += '<:yellow_bar:851761551416229898>'
                            for i in range(11 - int(p2_health / 18)):
                                bbar += '<:black_bar:851772206820491282>'
                            bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                        elif p2_health < 200:
                            bbar = '**{}**\n<:green_front:851765622832627732>'.format(arg1.display_name)
                            for i in range(int(p2_health / 18) - 1):
                                bbar += '<:green_bar:851761532664938507>'
                            for i in range(11 - int(p2_health / 18)):
                                bbar += '<:black_bar:851772206820491282>'
                            bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                        embed = discord.Embed(
                            title=':boom: ' + ctx.author.name + ' vs {} :boom:'.format(arg1.display_name),
                            description=string + '\n\n' + ubar + bbar, color=0x7F00FF)
                        embed.set_footer(text=ctx.author.name+" turn:")
                        await msg.edit(embed=embed)
                    if p1_health == 0 or p2_health == 0:
                        break

                    try:
                        while flag == 0:
                            reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                            if reaction.emoji == '❌':
                                await ctx.send('aborted.')
                                break
                            elif reaction.emoji == '🇦':
                                flag = 1
                                p1_choice = 'a'
                            elif reaction.emoji == '🇧':
                                flag = 1
                                p1_choice = 'b'
                            elif reaction.emoji == '🆎':
                                flag = 1
                                p1_choice = 'ab'
                            await msg.remove_reaction(reaction.emoji, ctx.author)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **" + ctx.author.mention + "**.")
                        flag = 0

                    if flag == 0:
                        break
                    if p1_choice == 'a':
                        damage = random.randint(a1i, a1j)
                        p2_choice = random.choice(['a', 'b', 'ab'])
                        if p2_choice == 'a':
                            string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to attack , **{}** also attacked but failed.".format(
                                arg1.display_name) + "__**{}** lost ".format(arg1.display_name) + str(damage) + ' HP.__'
                            p2_health = p2_health - damage
                        elif p2_choice == 'b':
                            damage = damage - int(damage * random.randint(d2i, d2j) * 0.01)
                            string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to attack but **{}** blocked.".format(
                                arg1.display_name) + "__**{}** lost ".format(arg1.display_name) + str(
                                damage) + ' HP.__'
                            p2_health = p2_health - damage
                        else:
                            damage = random.randint(a2i, a2j)
                            string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to attack but **{}** decided to attack while blocking.__**".format(
                                arg1.display_name) + ctx.author.name + '** lost ' + str(damage) + ' HP.__'
                            p1_health = p1_health - damage
                    elif p1_choice == 'b':
                        p2_choice = random.choice(['a', 'b', 'ab'])
                        if p2_choice == 'a':
                            damage = random.randint(a2i, a2j)
                            if (p1_def == defense[2] and p2_at == attack[1]) or (
                                    p1_def == defense[4] and p2_at == attack[3]):
                                damage = damage - 2 * int(damage * random.randint(d1i, d1j) * 0.01)
                            else:
                                damage = damage - int(damage * random.randint(d1i, d1j) * 0.01)
                            string = "__**LOGS**__\n>**" + ctx.author.name + "** decided to block while **{}** attacked.__**".format(
                                arg1.display_name) + ctx.author.name + "** lost " + str(damage) + " HP.__"
                            p1_health = p1_health - damage
                        elif p2_choice == 'b':
                            if p1_def == defense[3]:
                                damage = int(0.5 * random.randint(a1i, a1j))
                                string = "__**LOGS**__\n>**" + ctx.author.name + '** decided to block,**{}** also blocked but **'.format(
                                    arg1.display_name) + ctx.author.name + '** managed to give some damage with their horned shield.__**{}** lost '.format(
                                    arg1.display_name) + str(damage) + " HP.__"
                                p2_health = p2_health - damage
                            else:
                                string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to block ,**{}** also blocked.__Nothing happened.__'.format(
                                    arg1.display_name)
                        else:
                            damage = random.randint(a2i, a2j)
                            string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to block while **{}** decided to attack while block but hurt themselves.'.format(
                                arg1.display_name) + '__**{}** lost '.format(arg1.display_name) + str(
                                damage) + " HP.__"
                            p2_health = p2_health - damage
                    else:
                        damage = random.randint(a1i, a1j)
                        p2_choice = random.choice(['a', 'b', 'ab'])
                        if p2_choice == 'a':
                            string = '__**LOGS**__\n>**' + ctx.author.name + '** decide to attack while block while **{}** decided to attack but failed.'.format(
                                arg1.display_name) + '__**{}** lost '.format(arg1.display_name) + str(
                                damage) + " HP.__"
                            p2_health = p2_health - damage
                        elif p2_choice == 'b':
                            string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to attack while block but **{}** decided to block and hence **'.format(
                                arg1.display_name) + ctx.author.name + '** hurt themselves.__**' + ctx.author.name + '** lost ' + str(
                                damage) + " HP.__"
                            p1_health = p1_health - damage
                        else:
                            damage = damage - int(0.005 * damage * random.randint(d2i, d2j))
                            string = '__**LOGS**__\n>**' + ctx.author.name + '** decided to attack while block , **{}** did the same but **'.format(
                                arg1.display_name) + ctx.author.name + '** attack was more aggressive.__**{}** lost '.format(
                                arg1.display_name) + str(damage) + " HP.__"
                            p2_health = p2_health - damage
                    if p1_health < 0:
                        p1_health = 0
                    if p2_health < 0:
                        p2_health = 0
                    if p1_health <= 36:
                        ubar = '**' + ctx.author.name + '**\n'
                        if p1_health == 0:
                            ubar += '<:black_front:851761853461954591>'
                            for i in range(10):
                                ubar += '<:black_bar:851772206820491282>'
                        elif p1_health >= 18:
                            ubar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                            for i in range(9):
                                ubar += '<:black_bar:851772206820491282>'
                        else:
                            ubar += '<:red_end:851761608614215690>'
                            for i in range(10):
                                ubar += '<:black_bar:851772206820491282>'
                        ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                    elif p1_health <= 100:
                        ubar = '**' + ctx.author.name + '**\n<:yellow_end:851765642088284190>'
                        for i in range(int(p1_health / 18) - 1):
                            ubar += '<:yellow_bar:851761551416229898>'
                        for i in range(11 - int(p1_health / 18)):
                            ubar += '<:black_bar:851772206820491282>'
                        ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'
                    elif p1_health < 200:
                        ubar = '**' + ctx.author.name + '**\n<:green_front:851765622832627732>'
                        for i in range(int(p1_health / 18) - 1):
                            ubar += '<:green_bar:851761532664938507>'
                        for i in range(11 - int(p1_health / 18)):
                            ubar += '<:black_bar:851772206820491282>'
                        ubar += '<:black_end:851761876974829598> ' + str(p1_health) + ' HP\n\n'

                    if p2_health <= 36:
                        bbar = '**{}**\n'.format(arg1.display_name)
                        if p2_health == 0:
                            bbar += '<:black_front:851761853461954591>'
                            for i in range(10):
                                bbar += '<:black_bar:851772206820491282>'
                        elif p2_health >= 18:
                            bbar += '<:red_end:851761608614215690><:red_bar:851761581012418570>'
                            for i in range(9):
                                bbar += '<:black_bar:851772206820491282>'
                        else:
                            bbar += '<:red_end:851761608614215690>'
                            for i in range(10):
                                bbar += '<:black_bar:851772206820491282>'
                        bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                    elif p2_health <= 100:
                        bbar = '**{}**\n<:yellow_end:851765642088284190>'.format(arg1.display_name)
                        for i in range(int(p2_health / 18) - 1):
                            bbar += '<:yellow_bar:851761551416229898>'
                        for i in range(11 - int(p2_health / 18)):
                            bbar += '<:black_bar:851772206820491282>'
                        bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                    elif p2_health < 200:
                        bbar = '**{}**\n<:green_front:851765622832627732>'.format(arg1.display_name)
                        for i in range(int(p2_health / 18) - 1):
                            bbar += '<:green_bar:851761532664938507>'
                        for i in range(11 - int(p2_health / 18)):
                            bbar += '<:black_bar:851772206820491282>'
                        bbar += '<:black_end:851761876974829598> ' + str(p2_health) + ' HP'
                    embed = discord.Embed(
                        title=':boom: ' + ctx.author.name + ' vs {} :boom:'.format(arg1.display_name),
                        description=string + '\n\n' + ubar + bbar, color=0x7F00FF)
                    embed.set_footer(text="{} turn:".format(arg1.display_name))
                    await msg.edit(embed=embed)

                    if p1_health == 0 or p2_health == 0:
                        break

                    flag = 0
                    try:
                        while flag == 0:
                            reaction, user = await client.wait_for('reaction_add', check=check2, timeout=60)
                            if reaction.emoji == '❌':
                                await ctx.send('aborted.')
                                break
                            elif reaction.emoji == '🇦':
                                flag = 1
                                p2_choice = 'a'
                            elif reaction.emoji == '🇧':
                                flag = 1
                                p2_choice = 'b'
                            elif reaction.emoji == '🆎':
                                flag = 1
                                p2_choice = 'ab'
                            await msg.remove_reaction(reaction.emoji, arg1._user)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **{}**.".format(arg1.mention))
                        flag = 0

                    if flag == 0:
                        break
                    if p2_choice == 'a':
                        damage = random.randint(a2i, a2j)
                        p1_choice = random.choice(['a', 'b', 'ab'])
                        if p1_choice == 'a':
                            string += "\n>**{}** decided to attack , **".format(
                                arg1.display_name) + ctx.author.name + "** also attacked but failed.__**" + ctx.author.name + "** lost " + str(
                                damage) + ' HP.__'
                            p1_health = p1_health - damage
                        elif p1_choice == 'b':
                            damage = damage - int(damage * random.randint(d1i, d1j) * 0.01)
                            string += "\n>**{}** decided to attack but **".format(
                                arg1.display_name) + ctx.author.name + "** blocked.__**" + ctx.author.name + "** lost " + str(
                                damage) + ' HP.__'
                            p1_health = p1_health - damage
                        else:
                            damage = random.randint(a1i, a1j)
                            string += '\n>**{}** decided to attack but **'.format(
                                arg1.display_name) + ctx.author.name + '** decided to attack while blocking.__**{}** lost '.format(
                                arg1.display_name) + str(damage) + ' HP.__'
                            p2_health = p2_health - damage
                    elif p2_choice == 'b':
                        p1_choice = random.choice(['a', 'b', 'ab'])
                        if p1_choice == 'a':
                            damage = random.randint(a1i, a1j)
                            if (p2_def == defense[2] and p1_at == attack[1]) or ( p2_def == defense[4] and p1_at == attack[3]):
                                damage = damage - 2 * int(damage * random.randint(d2i, d2j) * 0.01)
                            else:
                                damage = damage - int(damage * random.randint(d2i, d2j) * 0.01)
                            string += "\n>**{}** decided to block while **".format(
                                arg1.display_name) + ctx.author.name + "** attacked.__**{}** lost ".format(
                                arg1.display_name) + str(damage) + " HP.__"
                            p2_health = p2_health - damage
                        elif p1_choice == 'b':
                            if p2_def == defense[3]:
                                damage = int(0.5 * random.randint(a2i, a2j))
                                string += '\n>**{}** decided to block,**'.format(
                                    arg1.display_name) + ctx.author.name + '** also blocked but **{}** managed to give some damage with their horned shield.__**'.format(
                                    arg1.display_name) + ctx.author.name + '** lost ' + str(damage) + " HP.__"
                                p1_health = p1_health - damage
                            else:
                                string += '\n>**{}** decided to block ,**'.format(
                                    arg1.display_name) + ctx.author.name + '** also blocked.__Nothing happened.__'
                        else:
                            damage = random.randint(a1i, a1j)
                            string += '\n>**{}** decided to block while **'.format(
                                arg1.display_name) + ctx.author.name + '** decided to attack while block but hurt themselves.__**' + ctx.author.name + '** lost ' + str(
                                damage) + " HP.__"
                            p1_health = p1_health - damage
                    else:
                        damage = random.randint(a2i, a2j)
                        p1_choice = random.choice(['a', 'b', 'ab'])
                        if p1_choice == 'a':
                            string += '\n>**{}** decide to attack while block while **'.format(
                                arg1.display_name) + ctx.author.name + '** decided to attack but failed.__**' + ctx.author.name + '** lost ' + str(
                                damage) + " HP.__"
                            p1_health = p1_health - damage
                        elif p1_choice == 'b':
                            string += '\n>**{}** decided to attack while block but **'.format(
                                arg1.display_name) + ctx.author.name + '** decided to block and hence **{}** hurt themselves.'.format(
                                arg1.display_name) + '__**{}** lost '.format(arg1.display_name) + str(
                                damage) + " HP.__"
                            p2_health = p2_health - damage
                        else:
                            damage = damage - int(0.005 * damage * random.randint(d1i, d1j))
                            string += '\n>**{}** decided to attack while block , **'.format(
                                arg1.display_name) + ctx.author.name + '** did the same but **{}** attack was more aggressive.__**'.format(
                                arg1.display_name) + ctx.author.name + '** lost ' + str(damage) + " HP.__"
                            p1_health = p1_health - damage
                    flag1 = flag1 + 1
                    flag = 0

                if p2_health == 0:
                    await ctx.send(":crown: **" + ctx.author.name + "** won :crown:")
                elif p1_health == 0:
                    await ctx.send(":crown: **{}** won :crown:".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def spellbind(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko spellbind @user`',color=0x7F00FF))
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision = t2=0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** did'nt replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated")
        elif decision == 1:
            cards = ['<:RED_CARD:792356986410893342>', '<:BLUE_CARD:792358450155749376>','<:GREEN_CARD:792358469500010497>', '<:YELLOW_CARD:792673264266641408>']
            spell = ['<:nature_call:848110745165758475>', '<:blessing:848108213752299550>','<:stoneskin:848099608609816597>', '<:Deflect_shield:848101470133682186>','<:fireball:848090622820220938>', '<:ice_spear:848092801639645224>','<:lightning:848096066330689567>', '<:Bleeding:848104514963898388>','<:deathlock:848122972911829003>']
            uhealth = bhealth = 5
            bdef = udef = uhealcurse = udamagecurse = bhealcurse = bdamagecurse = 0

            while 1:
                user = []
                cardspawn = []
                flag1 = 0
                if random.randint(1, 250) == 55 or random.randint(1, 250) == 125:
                    cardspawn.append('<:RARE_CARD:792661062008700968>')
                    cardspawn.append('<:RARE_CARD:792661062008700968>')
                    i = 0
                    while i < 6:
                        cardspawn.append(random.choice(cards))
                        i += 1
                else:
                    i = 0
                    while i < 8:
                        cardspawn.append(random.choice(cards))
                        i += 1
                random.shuffle(cardspawn)

                string = " "
                i = 0
                while i < 8:
                    string += str(i + 1) + "-{ " + str(cardspawn[i]) + " }     "
                    if i == 3:
                        string += "\n\n"
                    i += 1
                string += "\n---------------------------------------\n**" + ctx.author.name + "** : ❤ " + str(
                    uhealth) + " , 🛡️ " + str(udef) + "\n"
                if udamagecurse != 0:
                    if uhealcurse == 0:
                        string += "   damage curse : " + str(udamagecurse) + "\n"
                    else:
                        string += "   damage curse : " + str(udamagecurse) + " ,"
                if uhealcurse != 0:
                    string += "   heal curse : " + str(uhealcurse) + "\n"
                string += "**{}** : ❤ ".format(arg1.display_name) + str(bhealth) + " , 🛡️ " + str(bdef) + "\n"
                if bdamagecurse != 0:
                    if bhealcurse == 0:
                        string += "   damage curse : " + str(bdamagecurse) + "\n"
                    else:
                        string += "   damage curse : " + str(bdamagecurse) + ","
                if bhealcurse != 0:
                    string += "   heal curse : " + str(bhealcurse) + "\n"
                string += "---------------------------------------\n"

                if decision % 2 != 0:
                    embed = discord.Embed(title=':crystal_ball: ' + str(ctx.author.name) + " vs {}".format(arg1.display_name) + ' :crystal_ball:',description=string + "**" + ctx.author.name + "** turn,choose two/three cards:\n",color=0x7F00FF)
                    embed.set_footer(text="choose cards like 14,75,268,etc | 'exit' to abort.")
                    await ctx.send(embed=embed)
                    if uhealth == 0:
                        await ctx.send("👑 **{}** won 👑".format(arg1.display_name))
                        break
                    elif bhealth == 0:
                        await ctx.send("👑 **" + str(ctx.author) + "** won 👑")
                        break
                    try:
                        t2=0
                        while 1:
                            t1=time.time()
                            msg1 = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                            msg = str(msg1.content)
                            if msg.lower() == 'exit':
                                await msg1.add_reaction('\N{OCTAGONAL SIGN}')
                                flag1 = -1
                                break
                            elif (len(msg)==2 and msg[0] in ['1','2','3','4','5','6','7','8'] and msg[1] in ['1','2','3','4','5','6','7','8'] and msg[0]!=msg[1]) or (len(msg)==3 and msg[0] in ['1','2','3','4','5','6','7','8'] and msg[1] in ['1','2','3','4','5','6','7','8'] and msg[2] in ['1','2','3','4','5','6','7','8'] and msg[0]!=msg[1] and msg[1]!=msg[2] and msg[0]!=msg[2]):
                                m=len(msg)
                                i = 0
                                while i < m:
                                    if cardspawn[int(msg[i]) - 1] == '<:RED_CARD:792356986410893342>':
                                        if random.randint(1, 20) != 10:
                                            user.append(random.choice(
                                                ['<:fireball:848090622820220938>', '<:ice_spear:848092801639645224>','<:lightning:848096066330689567>']))
                                        else:
                                            user.append(random.choice(spell))
                                    elif cardspawn[int(msg[i]) - 1] == '<:BLUE_CARD:792358450155749376>':
                                        if random.randint(1, 20) != 10:
                                            user.append(random.choice(['<:stoneskin:848099608609816597>','<:Deflect_shield:848101470133682186>']))
                                        else:
                                            user.append(random.choice(spell))
                                    elif cardspawn[int(msg[i]) - 1] == '<:GREEN_CARD:792358469500010497>':
                                        if random.randint(1, 20) != 10:
                                            user.append(random.choice(['<:nature_call:848110745165758475>', '<:blessing:848108213752299550>']))
                                        else:
                                            user.append(random.choice(spell))
                                    elif cardspawn[int(msg[i]) - 1] == '<:YELLOW_CARD:792673264266641408>':
                                        if random.randint(1, 10) != 9:
                                            user.append(random.choice(['<:Bleeding:848104514963898388>', '<:deathlock:848122972911829003>']))
                                        else:
                                            user.append(random.choice(spell))
                                    else:
                                        if random.randint(1, 10) <= 9:
                                            user.append('<:xoppelganger:848118346154508288>')
                                        else:
                                            user.append(random.choice(spell))
                                    i += 1
                                string = "**" + str(ctx.author.name) + "** got " + str(user[0]) + " " + str(user[1])
                                if m == 3:
                                    string += " " + str(user[2])
                                flag1 = 1
                                break
                            t2 += int(time.time() - t1)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **" + ctx.author.mention + "**.")
                        flag1 = -1
                        break

                    if flag1 == 1:

                        if m == 2:
                            if user[0][2] == user[1][2]:
                                if user[0][2] == 'f':
                                    string += " and casted **__fireball__**"
                                    if udamagecurse == 0:
                                        if bdef != 0:
                                            bdef -= 1
                                        else:
                                            bhealth -= 2
                                        string += " (2 damage)"
                                    else:
                                        string += " (but of no use)"
                                elif user[0][2] == 'i':
                                    string += " and casted **__ice spear__**"
                                    if udamagecurse == 0:
                                        if bdef != 0:
                                            bdef -= 1
                                        else:
                                            bhealth -= 2
                                        string += " (2 damage)"
                                    else:
                                        string += " (but of no use)"
                                elif user[0][2] == 'l':
                                    string += " and casted **__lightning__**"
                                    if udamagecurse == 0:
                                        if bdef != 0:
                                            bdef -= 1
                                        else:
                                            bhealth -= 2
                                        string += " (2 damage)"
                                    else:
                                        string += " (but of no use)"
                                elif user[0][2] == 's':
                                    string += " and casted **__stoneskin__** (+1 defense)"
                                    udef += 1
                                elif user[0][2] == 'D':
                                    string += " and casted **__deflect shield__** (+1 defense)"
                                    udef += 1
                                elif user[0][2] == 'n':
                                    string += " and casted **__nature call__**"
                                    if uhealcurse == 0:
                                        uhealth += 1
                                        string += " (+1 health)"
                                    else:
                                        string += " (but of no use)"
                                elif user[0][2] == 'b':
                                    string += " and casted **__blessing__** (curse removed)"
                                    uhealcurse = udamagecurse = 0
                                elif user[0][2] == 'B':
                                    string += " and casted **__bleeding__**"
                                    if udef != 0:
                                        bhealcurse += 2
                                        udef -= 1
                                        string += " (opponent heal blocked for next two turns)"
                                    else:
                                        uhealcurse += 3
                                        string += " on themself (heal blocked for next two turns)"
                                elif user[0][2] == 'd':
                                    string += " and casted **__deathlock__** "
                                    if udef != 0:
                                        bdamagecurse += 2
                                        udef -= 1
                                        string += " (opponent attack blocked for next two turns)"
                                    else:
                                        udamagecurse += 3
                                        string += " on themself (attack blocked for next two turns)"
                                else:
                                    string += " and casted **__doppleganger__** ("
                                    if udamagecurse == 0:
                                        if bdef != 0:
                                            bdef -= 1
                                        else:
                                            bhealth -= 2
                                        string += "2 damage,"
                                    udef += 1
                                    string += "+1 defense"
                                    if uhealcurse == 0:
                                        uhealth += 1
                                        string += ",+1 health"
                                    string += ")"
                            else:
                                string += " (spell mismatch)"
                        else:
                            string1 = str(user[0][2]) + str(user[1][2]) + str(user[2][2])
                            if string1 == 'ffl' or string1 == 'flf' or string1 == 'lff':
                                string += " and casted **__meteorite__**"
                                if udamagecurse == 0:
                                    if bdef != 0:
                                        bdef -= 1
                                    else:
                                        bhealth -= 3
                                    string += " (3 damage)"
                                else:
                                    string += " (but of no use)"
                            elif string1 == "iil" or string1 == "ili" or string1 == "lii":
                                string += " and casted **__ice rain__**"
                                if udamagecurse == 0:
                                    if bdef != 0:
                                        bdef -= 1
                                    else:
                                        bhealth -= 3
                                    string += " (3 damage)"
                                else:
                                    string += " (but of no use)"
                            elif string1 == "lln" or string1 == "lnl" or string1 == "nll":
                                string += " and casted **__storm__** ("
                                if udamagecurse == 0:
                                    if bdef != 0:
                                        bdef -= 1
                                    else:
                                        bhealth -= 3
                                    string += "3 damage,"
                                uhealcurse = udamagecurse = 0
                                string += "curse removed)"
                            elif string1 == "fss" or string1 == "ssf" or string1 == "sfs":
                                string += " and casted **__burning shield__** (+3 defense)"
                                udef += 3
                            elif string1 == "nnd" or string1 == "ndn" or string1 == "dnn":
                                string += " and casted **__phantom__** ("
                                if uhealcurse == 0:
                                    uhealth += 3
                                    string += "+3 health,"
                                bdef = 0
                                string += "opponent defense resetted)"
                            elif string1 == "nBD" or string1 == "BnD" or string1 == "nBD" or string1 == "nDB" or string1 == "DnB" or string1 == "nBD":
                                string += " and casted **__vampire__** ("
                                if udamagecurse == 0:
                                    if bdef != 0:
                                        bdef -= 1
                                    else:
                                        bhealth -= 4
                                    string += "4 damage,"
                                if uhealcurse == 0:
                                    uhealth += 3
                                    string += "+3 health)"
                                if string[-1] == "(":
                                    string += "but of no use)"
                            elif string1 == "xlx" or string1 == "xxl" or string1 == "lxx":
                                string += " and casted **__soul abruption__** ("
                                if udamagecurse == 0:
                                    if bdef != 0:
                                        bdef -= 1
                                    else:
                                        bhealth -= 5
                                    string += "5 damage,"
                                bhealcurse += 2
                                bdamagecurse += 2
                                string += "healing and damage blocked for next two turns)"
                            else:
                                string += " (spell mismatch)"

                        await ctx.send(string)
                    elif flag1 == -1:
                        break
                    if uhealcurse != 0:
                        uhealcurse -= 1
                    if udamagecurse != 0:
                        udamagecurse -= 1
                else:
                    embed = discord.Embed(title=':crystal_ball: ' + str(ctx.author.name) + " vs {}".format(arg1.display_name) + ' :crystal_ball:',description=string + '**{}** turn,choose two/three cards :\n'.format(arg1.display_name), color=0x7F00FF)
                    embed.set_footer(text="choose cards like 14,75,268,etc | 'exit' to abort.")
                    await ctx.send(embed=embed)
                    if uhealth == 0:
                        await ctx.send("👑 **{}** won 👑".format(arg1.display_name))
                        break
                    elif bhealth == 0:
                        await ctx.send("👑 **" + str(ctx.author) + "** won 👑")
                        break
                    try:
                        t2=0
                        while 1:
                            t1=time.time()
                            msg1 = await client.wait_for('message', check=check(arg1._user), timeout=120-t2)
                            msg = str(msg1.content)
                            if msg.lower() == 'exit':
                                await msg1.add_reaction('\N{OCTAGONAL SIGN}')
                                flag1 = -1
                                break
                            elif (len(msg) == 2 and msg[0] in ['1', '2', '3', '4', '5', '6', '7', '8'] and msg[1] in ['1', '2', '3', '4', '5', '6', '7', '8'] and msg[0] != msg[1]) or (len(msg) == 3 and msg[0] in ['1', '2', '3', '4', '5', '6', '7', '8'] and msg[1] in ['1', '2', '3', '4', '5', '6', '7', '8'] and msg[2] in ['1', '2', '3', '4', '5', '6','7', '8'] and msg[0] != msg[1] and msg[1] != msg[2] and msg[0] != msg[2]):
                                m=len(msg)
                                i = 0
                                while i < m:
                                    if cardspawn[int(msg[i]) - 1] == '<:RED_CARD:792356986410893342>':
                                        if random.randint(1, 20) != 10:
                                            user.append(random.choice(['<:fireball:848090622820220938>', '<:ice_spear:848092801639645224>','<:lightning:848096066330689567>']))
                                        else:
                                            user.append(random.choice(spell))
                                    elif cardspawn[int(msg[i]) - 1] == '<:BLUE_CARD:792358450155749376>':
                                        if random.randint(1, 20) != 10:
                                            user.append(random.choice(['<:stoneskin:848099608609816597>','<:Deflect_shield:848101470133682186>']))
                                        else:
                                            user.append(random.choice(spell))
                                    elif cardspawn[int(msg[i]) - 1] == '<:GREEN_CARD:792358469500010497>':
                                        if random.randint(1, 20) != 10:
                                            user.append(random.choice(['<:nature_call:848110745165758475>', '<:blessing:848108213752299550>']))
                                        else:
                                            user.append(random.choice(spell))
                                    elif cardspawn[int(msg[i]) - 1] == '<:YELLOW_CARD:792673264266641408>':
                                        if random.randint(1, 10) != 9:
                                            user.append(random.choice( ['<:Bleeding:848104514963898388>', '<:deathlock:848122972911829003>']))
                                        else:
                                            user.append(random.choice(spell))
                                    else:
                                        if random.randint(1, 10) <= 9:
                                            user.append('<:xoppelganger:848118346154508288>')
                                        else:
                                            user.append(random.choice(spell))
                                    i += 1
                                string = "**{}** got ".format(arg1.display_name) + str(user[0]) + " " + str(user[1])
                                if m == 3:
                                    string += " " + str(user[2])
                                flag1 = 1
                                break
                            t2 += int(time.time() - t1)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **{}**.".format(arg1.mention))
                        flag1 = -1
                        break

                    if flag1 == 1:
                        if m == 2:
                            if user[0][2] == user[1][2]:
                                if user[0][2] == 'f':
                                    string += " and casted **__fireball__**"
                                    if bdamagecurse == 0:
                                        if udef != 0:
                                            udef -= 1
                                        else:
                                            uhealth -= 2
                                        string += " (2 damage)"
                                    else:
                                        string += " (but of no use)"
                                elif user[0][2] == 'i':
                                    string += " and casted **__ice spear__**"
                                    if bdamagecurse == 0:
                                        if udef != 0:
                                            udef -= 1
                                        else:
                                            uhealth -= 2
                                        string += " (2 damage)"
                                    else:
                                        string += " (but of no use)"
                                elif user[0][2] == 'l':
                                    string += " and casted **__lightning__**"
                                    if bdamagecurse == 0:
                                        if udef != 0:
                                            udef -= 1
                                        else:
                                            uhealth -= 2
                                        string += " (2 damage)"
                                    else:
                                        string += " (but of no use)"
                                elif user[0][2] == 's':
                                    string += " and casted **__stoneskin__** (+1 defense)"
                                    bdef += 1
                                elif user[0][2] == 'D':
                                    string += " and casted **__deflect shield__** (+1 defense)"
                                    bdef += 1
                                elif user[0][2] == 'n':
                                    string += " and casted **__nature call__**"
                                    if bhealcurse == 0:
                                        bhealth += 1
                                        string += " (+1 health)"
                                    else:
                                        string += " but of no use."
                                elif user[0][2] == 'b':
                                    string += " and casted **__blessing__** (curse removed)"
                                    bhealcurse = bdamagecurse = 0
                                elif user[0][2] == 'B':
                                    string += " and casted **__bleeding__**"
                                    if bdef != 0:
                                        uhealcurse += 2
                                        bdef -= 1
                                        string += " (opponent heal blocked for next two turns)"
                                    else:
                                        bhealcurse += 3
                                        string += " on themself (heal blocked for next two turns)"
                                elif user[0][2] == 'd':
                                    string += " and casted **__deathlock__**"
                                    if bdef != 0:
                                        udamagecurse += 2
                                        bdef = - 1
                                        string += " (opponent attack blocked for next two turns)"
                                    else:
                                        bdamagecurse += 3
                                        string += " on themself (attack blocked for next two turns)"
                                else:
                                    string += " and casted **__doppleganger__** ("
                                    if bdamagecurse == 0:
                                        if udef != 0:
                                            udef -= 1
                                        else:
                                            uhealth -= 2
                                        string += "2 damage,"
                                    bdef += 1
                                    string += "+1 defense"
                                    if bhealcurse == 0:
                                        bhealth += 1
                                        string += ",+1 health"
                                    string += ")"
                            else:
                                string += " (spell mismatch)"
                        else:
                            string1 = str(user[0][2]) + str(user[1][2]) + str(user[2][2])
                            if string1 == 'ffl' or string1 == 'flf' or string1 == 'lff':
                                string += " and casted **__meteorite__**"
                                if bdamagecurse == 0:
                                    if udef != 0:
                                        udef -= 1
                                    else:
                                        uhealth -= 3
                                    string += " (3 damage)"
                                else:
                                    string += " (but of no use)"
                            elif string1 == "iil" or string1 == "ili" or string1 == "lii":
                                string += " and casted **__ice rain__**"
                                if bdamagecurse == 0:
                                    if udef != 0:
                                        udef -= 1
                                    else:
                                        uhealth -= 3
                                    string += " (3 damage)"
                                else:
                                    string += " (but of no use)"
                            elif string1 == "lln" or string1 == "lnl" or string1 == "nll":
                                string += " and casted **__storm__** ("
                                if bdamagecurse == 0:
                                    if udef != 0:
                                        udef -= 1
                                    else:
                                        uhealth -= 3
                                    string += "3 damage,"
                                bhealcurse = bdamagecurse = 0
                                string += "curse removed)"
                            elif string1 == "fss" or string1 == "ssf" or string1 == "sfs":
                                string += " and casted **__burning shield__** (+3 defense)"
                                bdef += 3
                            elif string1 == "nnd" or string1 == "ndn" or string1 == "dnn":
                                string += " and casted **__phantom__** ("
                                if bhealcurse == 0:
                                    bhealth += 3
                                    string += "+3 health,"
                                udef = 0
                                string += "opponent defense resetted)"
                            elif string1 == "nBD" or string1 == "BnD" or string1 == "nBD" or string1 == "nDB" or string1 == "DnB" or string1 == "nBD":
                                string += " and casted **__vampire__** ("
                                if bdamagecurse == 0:
                                    if udef != 0:
                                        udef -= 1
                                    else:
                                        uhealth -= 4
                                    string += "4 damage,"
                                if bhealcurse == 0:
                                    bhealth += 3
                                    string += "+3 health)"
                                if string[-1] == "(":
                                    string += "but of no use)"
                            elif string1 == "xlx" or string1 == "xxl" or string1 == "lxx":
                                string += " and casted **__soul abruption__** ("
                                if bdamagecurse == 0:
                                    if udef != 0:
                                        udef -= 1
                                    else:
                                        uhealth -= 5
                                    string += "5 damage,"
                                uhealcurse += 2
                                udamagecurse += 2
                                string += "healing and damage blocked for next two turns)"
                            else:
                                string += " (spell mismatch)"

                        await ctx.send(string)
                    elif flag1 == -1:
                        break
                    if bhealcurse != 0:
                        bhealcurse -= 1
                    if bdamagecurse != 0:
                        bdamagecurse -= 1
                if uhealth < 0:
                    uhealth = 0
                elif uhealth > 6:
                    uhealth = 6
                if bhealth < 0:
                    bhealth = 0
                elif bhealth > 6:
                    bhealth = 6
                if udef > 3:
                    udef = 3
                if bdef > 3:
                    bdef = 3
                decision += 1
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def duel(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))

    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko duel @user`',color=0x7F00FF))
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision =t2= 0
        await ctx.send("**{}**,do you accept the duel? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated.")
        elif decision == 1:
            p1_health = p2_health = 3
            health = ['', '<:game_heart:848505744063332392>','<:game_heart:848505744063332392> <:game_heart:848505744063332392>','<:game_heart:848505744063332392> <:game_heart:848505744063332392> <:game_heart:848505744063332392>']
            flag = 0
            while 1:
                embed = discord.Embed(description='**' + ctx.author.name + "** : " + str(health[p1_health] + '\n**{}** : '.format(arg1.display_name) + str(health[p2_health])),color=0x7F00FF)
                embed.set_image(url='https://i.imgur.com/3Cu6VDZ.png')
                embed.set_footer(text="type 'x' to shoot when camera flashes | 'exit' to abort.")
                embed.set_author(name=ctx.author.display_name + "'s challenge", icon_url=ctx.author.avatar_url)

                if decision == 1:
                    await ctx.send(embed=embed)
                    time.sleep(3)
                else:
                    time.sleep(3)
                    await string.edit(embed=embed)

                string1 = await ctx.send(':camera:')
                time.sleep(random.randint(2, 11))
                await string1.edit(content=':camera_with_flash:')
                flag = 0

                try:
                    t2=0
                    while flag == 0:
                        t1=time.time()
                        msg = await client.wait_for('message', timeout=10-t2)
                        if (msg.author == ctx.author or msg.author == arg1._user) and msg.content.lower() == 'exit':
                            await msg.add_reaction('\N{OCTAGONAL SIGN}')
                            break
                        if msg.author == ctx.author and msg.content.lower() == 'x':
                            await msg.add_reaction('\N{COLLISION SYMBOL}')
                            link = 'https://i.imgur.com/QzjGmc0.png'
                            desc = '**' + ctx.author.name + '** hit while **{}** missed.'.format(arg1.display_name)
                            flag = 1
                            p2_health -= 1
                        elif msg.author == arg1._user and msg.content.lower() == 'x':
                            await msg.add_reaction('\N{COLLISION SYMBOL}')
                            link = 'https://i.imgur.com/mCNPIaE.png'
                            desc = '**{}** hit while **'.format(arg1.display_name) + ctx.author.name + '** missed.'
                            flag = 2
                            p1_health -= 1
                        t2+=int(time.time()-t1)
                except asyncio.TimeoutError:
                    await string1.edit(content="No one shot.Both gunslingers decided to end the fight in peace :flag_white:.")
                    break
                if flag == 0:
                    break
                embed = discord.Embed(description='**' + ctx.author.name + "** : " + str(health[p1_health]) + '\n**{}** : '.format(arg1.display_name) + str(health[p2_health]) + '\n\n:gun: ' + desc, color=0x7F00FF)
                embed.set_image(url=link)
                embed.set_author(name=ctx.author.display_name + "'s challenge", icon_url=ctx.author.avatar_url)
                string = await ctx.send(embed=embed)

                if p2_health == 0:
                    await ctx.send(":crown: **" + ctx.author.name + "** is the __fastest hand in the west__ :crown:")
                    break
                elif p1_health == 0:
                    await ctx.send(":crown: **{}** is the __fastest hand in the west__ :crown:".format(arg1.display_name))
                    break
                decision += 1
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def aduhuli(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko aduhule @user`',color=0x7F00FF))
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision =t2= 0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated.")
        elif decision == 1:
            animal = [':pig:', ':cow:', ':monkey_face:', ':boar:', ':deer:']
            temp_animal = ['p', 'c', 'm', 'b', 'd']
            ani_pos = [-1, -1, -1, -1, -1]
            cattle = [':pig:', ':cow:', ':monkey_face:', ':boar:', ':deer:']
            dead_cattle = ['<:pig_dead:848968239442427914>', '<:cow_dead:848968264012267524>','<:monke_dead:848968285689348177>', '<:boar_dead:848968329502916618>','<:deer_dead:848968305217372240>']
            tiger = 0
            pos = [':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:',':white_large_square:', ':white_large_square:', ':white_large_square:', ':white_large_square:',':white_large_square:', ':white_large_square:']
            while 1:
                if decision == 1:
                    pos[0] = ':tiger:'
                    tiger_pos = 0

                string = ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:' + pos[0] + ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::no_entry::zero:\n'
                string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::arrow_lower_left::arrow_down::arrow_lower_right::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::no_entry:\n'
                string += ':black_large_square::black_large_square::black_large_square::black_large_square:' + pos[1] + ':left_right_arrow:' + pos[2] + ':left_right_arrow:' + pos[3] + ':black_large_square::black_large_square::black_large_square::black_large_square::no_entry::one::two::three:\n'
                string += ':black_large_square::black_large_square::black_large_square::arrow_lower_left::black_large_square::black_large_square::arrow_down::black_large_square::black_large_square::arrow_lower_right::black_large_square::black_large_square::black_large_square::no_entry:\n'
                string += ':black_large_square::black_large_square:' + pos[4] + ':left_right_arrow::left_right_arrow::left_right_arrow:' + pos[5] + ':left_right_arrow::left_right_arrow::left_right_arrow:' + pos[6] + ':black_large_square::black_large_square::no_entry::four::five::six:\n'
                string += ':black_large_square::arrow_lower_left::black_large_square::black_large_square::black_large_square::black_large_square::arrow_down::black_large_square::black_large_square::black_large_square::black_large_square::arrow_lower_right::black_large_square::no_entry:\n'
                string += pos[7] + ':left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow:' + pos[8] + ':left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow:' + pos[9] + ':no_entry::seven::eight::nine:'
                embed = discord.Embed(title='{} turn :'.format(arg1.display_name),description=string + "\n\n**" + ctx.author.name + "** : " + str(tiger) + "/2\n**{}** cattle : ".format(arg1.display_name) + cattle[0] +cattle[1] + cattle[2] + cattle[3] + cattle[4], color=0x7F00FF)
                embed.set_footer(text="type input like b4,c9,etc | 'exit' to abort.")
                flag = 0
                await ctx.send(embed=embed)

                if tiger == 2:
                    await ctx.send(':crown: **' + ctx.author.name + '** won. :crown:')
                    break
                # ---------------taking p2 input----------------
                try:
                    t2=0
                    while flag == 0:
                        t1=time.time()
                        msg = await client.wait_for('message', check=check(arg1._user), timeout=120-t2)
                        msg1 = msg.content.lower()
                        if msg1 == 'exit':
                            await msg.add_reaction('\N{OCTAGONAL SIGN}')
                            break
                        elif decision <= 5 and len(msg1) == 2 and msg1[0].isalpha() == True and msg1[1].isdigit() == True:
                            for ani in temp_animal:
                                if msg1[0] == ani:
                                    if int(msg1[1]) in range(0, 10):
                                        if pos[int(msg1[1])] == ':white_large_square:':
                                            flag = 1
                                            temp_animal.remove(msg1[0])
                                            break
                        elif decision > 5 and len(msg1) == 2 and msg1[0].isalpha() == True and msg1[1].isdigit() == True:
                            i = 0
                            for ani in animal:
                                if msg1[0] == ani[1]:
                                    if int(msg1[1]) in range(0, 10):
                                        if pos[int(msg1[1])] == ':white_large_square:':
                                            if int(msg1[1]) == 0 and (ani_pos[i] == 1 or ani_pos[i] == 2 or ani_pos[i] == 3):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 1 and (ani_pos[i] == 0 or ani_pos[i] == 2 or ani_pos[i] == 4):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 2 and (ani_pos[i] == 0 or ani_pos[i] == 1 or ani_pos[i] == 3 or ani_pos[i] == 5):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 3 and (ani_pos[i] == 0 or ani_pos[i] == 2 or ani_pos[i] == 6):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 4 and (ani_pos[i] == 1 or ani_pos[i] == 5 or ani_pos[i] == 7):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 5 and (ani_pos[i] == 2 or ani_pos[i] == 4 or ani_pos[i] == 6 or ani_pos[i] == 8):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 6 and (ani_pos[i] == 3 or ani_pos[i] == 5 or ani_pos[i] == 9):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 7 and (ani_pos[i] == 4 or ani_pos[i] == 8):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 8 and (ani_pos[i] == 5 or ani_pos[i] == 7 or ani_pos[i] == 9):
                                                flag = 2
                                                break
                                            elif int(msg1[1]) == 9 and (ani_pos[i] == 6 or ani_pos[i] == 8):
                                                flag = 2
                                                break
                                i += 1
                        t2+=int(time.time()-t1)
                except asyncio.TimeoutError:
                    await ctx.send("**{}** didn't replied.".format(arg1.mention))
                if flag == 0:
                    break
                # ---------------for first 5 decisions-----------------
                if flag == 1:
                    for ani in animal:
                        if ani[1] == msg1[0]:
                            if ani[1] == 'p':
                                ani_pos[0] = int(msg1[1])
                            elif ani[1] == 'c':
                                ani_pos[1] = int(msg1[1])
                            elif ani[1] == 'm':
                                ani_pos[2] = int(msg1[1])
                            elif ani[1] == 'b':
                                ani_pos[3] = int(msg1[1])
                            elif ani[1] == 'd':
                                ani_pos[4] = int(msg1[1])
                            pos[int(msg1[1])] = ani

                # -------------for animal movement------------
                elif flag == 2:
                    pos[int(msg1[1])] = animal[i]
                    pos[ani_pos[i]] = ':white_large_square:'
                    ani_pos[i] = int(msg1[1])
                string = ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:' + pos[0] + ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::no_entry::zero:\n'
                string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::arrow_lower_left::arrow_down::arrow_lower_right::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::no_entry:\n'
                string += ':black_large_square::black_large_square::black_large_square::black_large_square:' + pos[1] + ':left_right_arrow:' + pos[2] + ':left_right_arrow:' + pos[3] + ':black_large_square::black_large_square::black_large_square::black_large_square::no_entry::one::two::three:\n'
                string += ':black_large_square::black_large_square::black_large_square::arrow_lower_left::black_large_square::black_large_square::arrow_down::black_large_square::black_large_square::arrow_lower_right::black_large_square::black_large_square::black_large_square::no_entry:\n'
                string += ':black_large_square::black_large_square:' + pos[4] + ':left_right_arrow::left_right_arrow::left_right_arrow:' + pos[5] + ':left_right_arrow::left_right_arrow::left_right_arrow:' + pos[6] + ':black_large_square::black_large_square::no_entry::four::five::six:\n'
                string += ':black_large_square::arrow_lower_left::black_large_square::black_large_square::black_large_square::black_large_square::arrow_down::black_large_square::black_large_square::black_large_square::black_large_square::arrow_lower_right::black_large_square::no_entry:\n'
                string += pos[7] + ':left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow:' + pos[8] + ':left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow:' + pos[9] + ':no_entry::seven::eight::nine:'
                embed = discord.Embed(title=ctx.author.name + ' turn :',description=string + "\n\n**" + ctx.author.name + "** : " + str(tiger) + "/2\n**{}** cattle : ".format(arg1.display_name) + cattle[0] +cattle[1] + cattle[2] + cattle[3] + cattle[4], color=0x7F00FF)
                embed.set_footer(text="type input 0-9 | 'exit' to abort.")
                await ctx.send(embed=embed)

                if tiger_pos == 9 and pos[3] != ':white_large_square:' and pos[6] != ':white_large_square:' and pos[7] != ':white_large_square:' and pos[8] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 7 and pos[1] != ':white_large_square:' and pos[4] != ':white_large_square:' and pos[8] != ':white_large_square:' and pos[9] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 8 and pos[2] != ':white_large_square:' and pos[5] != ':white_large_square:' and pos[7] != ':white_large_square:' and pos[9] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 4 and pos[7] != ':white_large_square:' and pos[5] != ':white_large_square:' and pos[6] != ':white_large_square:' and pos[1] != ':white_large_square:' and pos[0] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 5 and pos[2] != ':white_large_square:' and pos[4] != ':white_large_square:' and pos[6] != ':white_large_square:' and pos[8] != ':white_large_square:' and pos[0] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 6 and pos[3] != ':white_large_square:' and pos[0] != ':white_large_square:' and pos[4] != ':white_large_square:' and pos[5] != ':white_large_square:' and pos[9] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 3 and pos[0] != ':white_large_square:' and pos[1] != ':white_large_square:' and pos[2] != ':white_large_square:' and pos[6] != ':white_large_square:' and pos[9] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 2 and pos[3] != ':white_large_square:' and pos[0] != ':white_large_square:' and pos[1] != ':white_large_square:' and pos[5] != ':white_large_square:' and pos[8] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                elif tiger_pos == 1 and pos[0] != ':white_large_square:' and pos[3] != ':white_large_square:' and pos[2] != ':white_large_square:' and pos[4] != ':white_large_square:' and pos[7] != ':white_large_square:':
                    await ctx.send(':crown: **{}** :crown:'.format(arg1.display_name))
                    break
                # --------------taking p1 input------------
                flag = 0
                try:
                    t2=0
                    while flag == 0:
                        t1=time.time()
                        msg = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                        if msg.content.lower() == 'exit':
                            await msg.add_reaction('\N{OCTAGONAL SIGN}')
                            break
                        if msg.content.isdigit():
                            msg1 = int(msg.content)
                        else:
                            continue
                        if msg1 in range(0, 10):
                            if msg1 == tiger_pos:
                                continue
                            if pos[msg1] == ':white_large_square:':
                                if msg1 == 0 and (tiger_pos == 1 or tiger_pos == 2 or tiger_pos == 3):
                                    flag = 1
                                elif msg1 == 1 and (tiger_pos == 0 or tiger_pos == 2 or tiger_pos == 4):
                                    flag = 1
                                elif msg1 == 2 and (tiger_pos == 0 or tiger_pos == 1 or tiger_pos == 3 or tiger_pos == 5):
                                    flag = 1
                                elif msg1 == 3 and (tiger_pos == 0 or tiger_pos == 2 or tiger_pos == 6):
                                    flag = 1
                                elif msg1 == 4 and (tiger_pos == 1 or tiger_pos == 5 or tiger_pos == 7):
                                    flag = 1
                                elif msg1 == 5 and (tiger_pos == 2 or tiger_pos == 4 or tiger_pos == 6 or tiger_pos == 8):
                                    flag = 1
                                elif msg1 == 6 and (tiger_pos == 3 or tiger_pos == 5 or tiger_pos == 9):
                                    flag = 1
                                elif msg1 == 7 and (tiger_pos == 4 or tiger_pos == 8):
                                    flag = 1
                                elif msg1 == 8 and (tiger_pos == 5 or tiger_pos == 7 or tiger_pos == 9):
                                    flag = 1
                                elif msg1 == 9 and (tiger_pos == 6 or tiger_pos == 8):
                                    flag = 1
                            elif pos[msg1] != ':white_large_square:':
                                if msg1 == 0 or msg1 == 7 or msg1 == 9:
                                    continue
                                if msg1 == 1:
                                    if tiger_pos == 0 and pos[4] == ':white_large_square:':
                                        flag = 2
                                        i = 4
                                    elif tiger_pos == 4 and pos[0] == ':white_large_square:':
                                        i = 0
                                        flag = 2
                                elif msg1 == 2:
                                    if tiger_pos == 0 and pos[5] == ':white_large_square:':
                                        i = 5
                                        flag = 2
                                    elif tiger_pos == 5 and pos[0] == ':white_large_square:':
                                        i = 0
                                        flag = 2
                                    elif tiger_pos == 1 and pos[3] == ':white_large_square:':
                                        i = 3
                                        flag = 2
                                    elif tiger_pos == 3 and pos[1] == ':white_large_square:':
                                        i = 1
                                        flag = 2
                                elif msg1 == 3:
                                    if tiger_pos == 0 and pos[6] == ':white_large_square:':
                                        i = 6
                                        flag = 2
                                    elif tiger_pos == 6 and pos[0] == ':white_large_square:':
                                        i = 0
                                        flag = 2
                                elif msg1 == 4:
                                    if tiger_pos == 1 and pos[7] == ':white_large_square:':
                                        i = 7
                                        flag = 2
                                    elif tiger_pos == 7 and pos[1] == ':white_large_square:':
                                        i = 1
                                        flag = 2
                                elif msg1 == 5:
                                    if tiger_pos == 2 and pos[8] == ':white_large_square:':
                                        i = 8
                                        flag = 2
                                    elif tiger_pos == 8 and pos[2] == ':white_large_square:':
                                        i = 2
                                        flag = 2
                                    elif tiger_pos == 4 and pos[6] == ':white_large_square:':
                                        i = 6
                                        flag = 2
                                    elif tiger_pos == 6 and pos[4] == ':white_large_square:':
                                        i = 4
                                        flag = 2
                                elif msg1 == 6:
                                    if tiger_pos == 3 and pos[9] == ':white_large_square:':
                                        i = 9
                                        flag = 2
                                    elif tiger_pos == 9 and pos[3] == ':white_large_square:':
                                        i = 3
                                        flag = 2
                                elif msg1 == 8:
                                    if tiger_pos == 7 and pos[9] == ':white_large_square:':
                                        i = 9
                                        flag = 2
                                    elif tiger_pos == 9 and pos[7] == ':white_large_square:':
                                        i = 7
                                        flag = 2
                        t2+=int(time.time()-t1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention + " didn't replied.")
                if flag == 0:
                    break
                # -------------tiger moving in empty pos------------
                if flag == 1:
                    pos[msg1] = ':tiger:'
                    pos[tiger_pos] = ':white_large_square:'
                    tiger_pos = msg1
                # -----------------------tiger killing cattle-----------------------------
                elif flag == 2:
                    pos[tiger_pos] = ':white_large_square:'
                    pos[i] = ':tiger:'
                    tiger_pos = i
                    i = 0
                    for ani in animal:
                        if ani == pos[msg1]:
                            animal[i] = 'xx'
                            ani_pos[i] = -1
                            cattle[i] = dead_cattle[i]
                        i += 1
                    pos[msg1] = ':white_large_square:'
                    tiger += 1
                decision += 1
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def connect4(ctx, arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko connect4 @user`',color=0x7F00FF))
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision =t2= 0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** did'nt replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated.")
        elif decision == 1:
            bscore = pscore = 0
            win = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [8, 9, 10, 11], [9, 10, 11, 12],
                   [10, 11, 12, 13], [11, 12, 13, 14], [15, 16, 17, 18], [16, 17, 18, 19], [17, 18, 19, 20],
                   [18, 19, 20, 21], [22, 23, 24, 25], [23, 24, 25, 26], [24, 25, 26, 27], [25, 26, 27, 28],
                   [29, 30, 31, 32], [30, 31, 32, 33], [31, 32, 33, 34], [32, 33, 34, 35], [36, 37, 38, 39],
                   [37, 38, 39, 40], [38, 39, 40, 41], [39, 40, 41, 42], [1, 8, 15, 22], [8, 15, 22, 29],
                   [15, 22, 29, 36], [2, 9, 16, 23], [9, 16, 23, 30], [16, 23, 30, 37], [3, 10, 17, 24],
                   [10, 17, 24, 31], [17, 24, 31, 38], [4, 11, 18, 25], [11, 18, 25, 32], [18, 25, 32, 39],
                   [5, 12, 19, 26], [12, 19, 26, 33], [19, 26, 33, 40], [6, 13, 20, 27], [13, 20, 27, 34],
                   [20, 27, 34, 41], [7, 14, 21, 28], [14, 21, 28, 35], [21, 28, 35, 42], [1, 9, 17, 25],
                   [2, 10, 18, 26], [3, 11, 19, 27], [4, 12, 20, 28], [8, 16, 24, 32], [9, 17, 25, 33],
                   [10, 18, 26, 34], [11, 19, 27, 35], [15, 23, 31, 39], [16, 24, 32, 40], [17, 25, 33, 41],
                   [18, 26, 34, 42], [7, 13, 19, 25], [6, 12, 18, 24], [5, 11, 17, 23], [4, 10, 16, 22],
                   [14, 20, 26, 32], [13, 19, 25, 31], [12, 18, 24, 30], [11, 17, 23, 29], [21, 27, 33, 39],
                   [20, 26, 32, 38], [19, 25, 31, 37], [18, 24, 30, 36]]
            maze = []
            for i in range(43):
                maze.append(' ')
            ppoint = []
            bpoint = []
            flag = 0
            round=1
            while 1:
                pblink = []
                bblink = []
                for w in win:
                    w0 = set(w)
                    bpoint_set = set(bpoint)
                    ppoint_set = set(ppoint)
                    if w0.issubset(bpoint_set) == True:
                        bblink = w
                        break
                    elif w0.issubset(ppoint_set) == True:
                        pblink = w
                        break
                string = '__**ROUND '+str(round)+'**__\n**' + ctx.author.name + ' score** : ' + str(pscore) + '\n**{} score** : '.format(arg1.display_name) + str(bscore) + '\n'
                string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
                k = 1
                for i in range(6):
                    for j in range(7):
                        if k in pblink:
                            string += '<a:blue_blink:852461887349325866>'
                            maze[k] = ':blue_circle:'
                        elif k in bblink:
                            string += '<a:red_blink:852461867681972255>'
                            maze[k] = ':red_circle:'
                        elif k in ppoint:
                            maze[k] = ':blue_circle:'
                            string += ':blue_circle:'
                        elif k in bpoint:
                            maze[k] = ':red_circle:'
                            string += ':red_circle:'
                        else:
                            maze[k] = ':white_circle:'
                            string += ':white_circle:'
                        k += 1
                    string += '\n'
                string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n:one::two::three::four::five::six::seven:'
                embed = discord.Embed(title="**" + str(ctx.author.name) + "** ~ :blue_circle: , **{}** ~ :red_circle:".format(arg1.display_name), description=string, color=0x7F00FF)
                if decision%2!=0:
                    embed.set_footer(text=str(ctx.author.name) + " turn:\nchoose from 1-7 | 'exit' to abort.")
                else:
                    embed.set_footer(text="{} turn:\nchoose from 1-7 | 'exit' to abort.".format(arg1.display_name))
                await ctx.send(embed=embed)

                for w in win:
                    w = set(w)
                    bpoint_set = set(bpoint)
                    ppoint_set = set(ppoint)
                    if w.issubset(bpoint_set) == True:
                        bscore += 1
                        if bscore == 3:
                            await ctx.send("**{}** scored.".format(arg1.display_name) + "\n👑 **{}** won 👑".format(arg1.display_name))
                            flag = 1
                            break
                        else:
                            await ctx.send("**{}** scored.".format(arg1.display_name))
                            time.sleep(2)
                            maze = []
                            for i in range(43):
                                maze.append(' ')
                            ppoint = []
                            bpoint = []
                            decision = 1
                            flag = -1
                            break
                    elif w.issubset(ppoint_set) == True:
                        pscore += 1
                        if pscore == 3:
                            await ctx.send("**" + ctx.author.name + "** scored.\n👑 **" + ctx.author.name + "** won 👑")
                            flag = 1
                            break
                        else:
                            await ctx.send("**" + ctx.author.name + "** scored.")
                            time.sleep(2)
                            maze = []
                            for i in range(43):
                                maze.append(' ')
                            ppoint = []
                            bpoint = []
                            decision = 1
                            flag = -1
                            break
                if flag == 1:
                    break
                elif flag == -1:
                    round += 1
                    flag = 0
                    continue
                if maze[1] != ':white_circle:' and maze[2] != ':white_circle:' and maze[3] != ':white_circle:' and maze[4] != ':white_circle:' and maze[5] != ':white_circle:' and maze[6] != ':white_circle:' and maze[7] != ':white_circle:':
                    await ctx.send("draw.")
                    time.sleep(2)
                    maze = []
                    for i in range(43):
                        maze.append(' ')
                    ppoint = []
                    bpoint = []
                    decision = 1
                    flag = 0
                    round += 1
                    continue

                if decision % 2 != 0:
                    try:
                        t2=0
                        while 1:
                            t1=time.time()
                            msg = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                            if msg.content.lower() == "exit":
                                flag = 1
                                await msg.add_reaction('\N{OCTAGONAL SIGN}')
                                break
                            elif msg.content.isdigit() == True and int(msg.content) >= 1 and int(msg.content) <= 7:
                                if int(msg.content) == 1:
                                    if maze[36] == ':white_circle:':
                                        ppoint.append(36)
                                    elif maze[29] == ':white_circle:':
                                        ppoint.append(29)
                                    elif maze[22] == ':white_circle:':
                                        ppoint.append(22)
                                    elif maze[15] == ':white_circle:':
                                        ppoint.append(15)
                                    elif maze[8] == ':white_circle:':
                                        ppoint.append(8)
                                    elif maze[1] == ':white_circle:':
                                        ppoint.append(1)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 2:
                                    if maze[37] == ':white_circle:':
                                        ppoint.append(37)
                                    elif maze[30] == ':white_circle:':
                                        ppoint.append(30)
                                    elif maze[23] == ':white_circle:':
                                        ppoint.append(23)
                                    elif maze[16] == ':white_circle:':
                                        ppoint.append(16)
                                    elif maze[9] == ':white_circle:':
                                        ppoint.append(9)
                                    elif maze[2] == ':white_circle:':
                                        ppoint.append(2)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 3:
                                    if maze[38] == ':white_circle:':
                                        ppoint.append(38)
                                    elif maze[31] == ':white_circle:':
                                        ppoint.append(31)
                                    elif maze[24] == ':white_circle:':
                                        ppoint.append(24)
                                    elif maze[17] == ':white_circle:':
                                        ppoint.append(17)
                                    elif maze[10] == ':white_circle:':
                                        ppoint.append(10)
                                    elif maze[3] == ':white_circle:':
                                        ppoint.append(3)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 4:
                                    if maze[39] == ':white_circle:':
                                        ppoint.append(39)
                                    elif maze[32] == ':white_circle:':
                                        ppoint.append(32)
                                    elif maze[25] == ':white_circle:':
                                        ppoint.append(25)
                                    elif maze[18] == ':white_circle:':
                                        ppoint.append(18)
                                    elif maze[11] == ':white_circle:':
                                        ppoint.append(11)
                                    elif maze[4] == ':white_circle:':
                                        ppoint.append(4)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 5:
                                    if maze[40] == ':white_circle:':
                                        ppoint.append(40)
                                    elif maze[33] == ':white_circle:':
                                        ppoint.append(33)
                                    elif maze[26] == ':white_circle:':
                                        ppoint.append(26)
                                    elif maze[19] == ':white_circle:':
                                        ppoint.append(19)
                                    elif maze[12] == ':white_circle:':
                                        ppoint.append(12)
                                    elif maze[5] == ':white_circle:':
                                        ppoint.append(5)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 6:
                                    if maze[41] == ':white_circle:':
                                        ppoint.append(41)
                                    elif maze[34] == ':white_circle:':
                                        ppoint.append(34)
                                    elif maze[27] == ':white_circle:':
                                        ppoint.append(27)
                                    elif maze[20] == ':white_circle:':
                                        ppoint.append(20)
                                    elif maze[13] == ':white_circle:':
                                        ppoint.append(13)
                                    elif maze[6] == ':white_circle:':
                                        ppoint.append(6)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 7:
                                    if maze[42] == ':white_circle:':
                                        ppoint.append(42)
                                    elif maze[35] == ':white_circle:':
                                        ppoint.append(35)
                                    elif maze[28] == ':white_circle:':
                                        ppoint.append(28)
                                    elif maze[21] == ':white_circle:':
                                        ppoint.append(21)
                                    elif maze[14] == ':white_circle:':
                                        ppoint.append(14)
                                    elif maze[7] == ':white_circle:':
                                        ppoint.append(7)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                break
                            t2+=int(time.time()-t1)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **" + ctx.author.mention + "**.")
                        break
                else:
                    try:
                        t2=0
                        while 1:
                            t1=time.time()
                            msg = await client.wait_for('message', check=check(arg1._user), timeout=120-t2)
                            if msg.content.lower() == "exit":
                                flag = 1
                                await msg.add_reaction('\N{OCTAGONAL SIGN}')
                                break
                            elif msg.content.isdigit() == True and int(msg.content) >= 1 and int(msg.content) <= 7:
                                if int(msg.content) == 1:
                                    if maze[36] == ':white_circle:':
                                        bpoint.append(36)
                                    elif maze[29] == ':white_circle:':
                                        bpoint.append(29)
                                    elif maze[22] == ':white_circle:':
                                        bpoint.append(22)
                                    elif maze[15] == ':white_circle:':
                                        bpoint.append(15)
                                    elif maze[8] == ':white_circle:':
                                        bpoint.append(8)
                                    elif maze[1] == ':white_circle:':
                                        bpoint.append(1)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 2:
                                    if maze[37] == ':white_circle:':
                                        bpoint.append(37)
                                    elif maze[30] == ':white_circle:':
                                        bpoint.append(30)
                                    elif maze[23] == ':white_circle:':
                                        bpoint.append(23)
                                    elif maze[16] == ':white_circle:':
                                        bpoint.append(16)
                                    elif maze[9] == ':white_circle:':
                                        bpoint.append(9)
                                    elif maze[2] == ':white_circle:':
                                        bpoint.append(2)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 3:
                                    if maze[38] == ':white_circle:':
                                        bpoint.append(38)
                                    elif maze[31] == ':white_circle:':
                                        bpoint.append(31)
                                    elif maze[24] == ':white_circle:':
                                        bpoint.append(24)
                                    elif maze[17] == ':white_circle:':
                                        bpoint.append(17)
                                    elif maze[10] == ':white_circle:':
                                        bpoint.append(10)
                                    elif maze[3] == ':white_circle:':
                                        bpoint.append(3)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 4:
                                    if maze[39] == ':white_circle:':
                                        bpoint.append(39)
                                    elif maze[32] == ':white_circle:':
                                        bpoint.append(32)
                                    elif maze[25] == ':white_circle:':
                                        bpoint.append(25)
                                    elif maze[18] == ':white_circle:':
                                        bpoint.append(18)
                                    elif maze[11] == ':white_circle:':
                                        bpoint.append(11)
                                    elif maze[4] == ':white_circle:':
                                        bpoint.append(4)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 5:
                                    if maze[40] == ':white_circle:':
                                        bpoint.append(40)
                                    elif maze[33] == ':white_circle:':
                                        bpoint.append(33)
                                    elif maze[26] == ':white_circle:':
                                        bpoint.append(26)
                                    elif maze[19] == ':white_circle:':
                                        bpoint.append(19)
                                    elif maze[12] == ':white_circle:':
                                        bpoint.append(12)
                                    elif maze[5] == ':white_circle:':
                                        bpoint.append(5)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 6:
                                    if maze[41] == ':white_circle:':
                                        bpoint.append(41)
                                    elif maze[34] == ':white_circle:':
                                        bpoint.append(34)
                                    elif maze[27] == ':white_circle:':
                                        bpoint.append(27)
                                    elif maze[20] == ':white_circle:':
                                        bpoint.append(20)
                                    elif maze[13] == ':white_circle:':
                                        bpoint.append(13)
                                    elif maze[6] == ':white_circle:':
                                        bpoint.append(6)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                elif int(msg.content) == 7:
                                    if maze[42] == ':white_circle:':
                                        bpoint.append(42)
                                    elif maze[35] == ':white_circle:':
                                        bpoint.append(35)
                                    elif maze[28] == ':white_circle:':
                                        bpoint.append(28)
                                    elif maze[21] == ':white_circle:':
                                        bpoint.append(21)
                                    elif maze[14] == ':white_circle:':
                                        bpoint.append(14)
                                    elif maze[7] == ':white_circle:':
                                        bpoint.append(7)
                                    else:
                                        await msg.add_reaction('\N{CROSS MARK}')
                                        continue
                                break
                            t2+=int(time.time()-t1)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep **{}**.".format(arg1.mention))
                        break
                decision += 1
                if flag == 1:
                    break
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def cf(ctx, arg0=None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    z = random.randint(1, 2)
    if arg0==None:
        embed = discord.Embed(title='CORRECT COMMAND USAGE:',description="`teko cf [choice]`\nwhere `choice` = h or t.", color=0x7F00FF)
        embed.set_footer(text='Example : teko cf h.')
        await ctx.send(embed=embed)
    elif arg0.lower() == 'h':
        msg = await ctx.send(embed=discord.Embed(description="tossing coin <a:coin_flip:852110422370680842>...", color=0x7F00FF))

        await asyncio.sleep(3)
        if z == 1:
            await msg.edit(embed=discord.Embed(title="it was **heads**", description="you won.", color=0x7F00FF))

        else:
            await msg.edit(embed=discord.Embed(title="it was **tails**", description="you lost.", color=0x7F00FF))

    elif arg0.lower() == 't':
        msg = await ctx.send(embed=discord.Embed(description="tossing coin <a:coin_flip:852110422370680842>...", color=0x7F00FF))
        time.sleep(3)
        if z == 2:
            await msg.edit(embed=discord.Embed(title="it was **tails**", description="you won.", color=0x7F00FF))
        else:
            await msg.edit(embed=discord.Embed(title="it was **heads**", description="you lost.", color=0x7F00FF))
    else:
        embed = discord.Embed(title='CORRECT COMMAND USAGE:',description="`teko cf [choice]`\nwhere `choice` = h or t.", color=0x7F00FF)
        embed.set_footer(text='Example : teko cf h.')
        await ctx.send(embed=embed)
        
@client.command()
async def coinflip(ctx, arg0=None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    z = random.randint(1, 2)
    if arg0==None:
        embed = discord.Embed(title='CORRECT COMMAND USAGE:',description="`teko cf [choice]`\nwhere `choice` = h or t.", color=0x7F00FF)
        embed.set_footer(text='Example : teko cf h.')
        await ctx.send(embed=embed)
    elif arg0.lower() == 'h':
        msg = await ctx.send(embed=discord.Embed(description="tossing coin <a:coin_flip:852110422370680842>...", color=0x7F00FF))

        await asyncio.sleep(3)
        if z == 1:
            await msg.edit(embed=discord.Embed(title="it was **heads**", description="you won.", color=0x7F00FF))

        else:
            await msg.edit(embed=discord.Embed(title="it was **tails**", description="you lost.", color=0x7F00FF))

    elif arg0.lower() == 't':
        msg = await ctx.send(embed=discord.Embed(description="tossing coin <a:coin_flip:852110422370680842>...", color=0x7F00FF))
        time.sleep(3)
        if z == 2:
            await msg.edit(embed=discord.Embed(title="it was **tails**", description="you won.", color=0x7F00FF))
        else:
            await msg.edit(embed=discord.Embed(title="it was **heads**", description="you lost.", color=0x7F00FF))
    else:
        embed = discord.Embed(title='CORRECT COMMAND USAGE:',description="`teko cf [choice]`\nwhere `choice` = h or t.", color=0x7F00FF)
        embed.set_footer(text='Example : teko cf h.')
        await ctx.send(embed=embed)
    
@client.command()
async def sumo(ctx, arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko sumo @user',color=0x7F00FF))
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision =t2= 0
        await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** did'nt replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated.")
        elif decision == 1:
            no_response = 0
            ring = [4, 5, 6, 7, 8, 9, 15, 22, 26, 35, 37, 48, 50, 59, 63, 70, 76, 77, 78, 79, 80, 81]
            alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
            ppos = 42
            bpos = 43
            flag = 0
            pscore = bscore = ppotential = bpotential = pstreak = bstreak = 0
            pbar = [':black_medium_square:', ':black_medium_square:', ':black_medium_square:', ':black_medium_square:',':black_medium_square:']
            bbar = [':black_medium_square:', ':black_medium_square:', ':black_medium_square:', ':black_medium_square:',':black_medium_square:']
            movement = 'horizontal'
            while 1:
                for i in range(5):
                    if i < ppotential:
                        pbar[i] = ':black_square_button:'
                    else:
                        pbar[i] = ':black_medium_square:'
                    if i < bpotential:
                        bbar[i] = ':black_square_button:'
                    else:
                        bbar[i] = ':black_medium_square:'
                string = '<:sumo1:852926778782515252> potential : '
                for i in range(5):
                    string += pbar[i]
                string += '\n<:sumo2:852926801394270249> potential : '
                for i in range(5):
                    string += bbar[i]
                string += '\n'
                k = 1
                for i in range(7):
                    for j in range(12):
                        if k == ppos:
                            string += '<:sumo1:852926778782515252>'
                        elif k == bpos:
                            string += '<:sumo2:852926801394270249>'
                        elif k in ring:
                            string += ':red_square:'
                        else:
                            string += ':black_large_square:'
                        k += 1
                    string += '\n'
                embed = discord.Embed(title='**' + ctx.author.name + '** <:sumo1side:852926755835478078> ' + str(pscore) + '/' + str(bscore) + ' <:sumo2side:852936504165531718> **{}**'.format(arg1.display_name), description=string,color=0x7F00FF)
                embed.set_footer(text="type displayed text quickly | 'exit' to abort.")
                if decision == 1:
                    string1 = await ctx.send(embed=embed)
                    time.sleep(2)
                else:
                    await string1.edit(embed=embed)
                if no_response == 4:
                    await msg1.edit(content='no one responding,aborted.')
                    break
                if bpos in ring:
                    pscore += 1
                    if pscore == 2:
                        await msg1.edit(content=':crown: **' + ctx.author.name + '** won. :crown:')
                        break
                    else:
                        await msg1.edit(content='**' + ctx.author.name + '** won this round.')
                        flag = -1
                elif ppos in ring:
                    bscore += 1
                    if bscore == 2:
                        await msg1.edit(content=':crown: **{}** won. :crown:'.format(arg1.display_name))
                        break
                    else:
                        await msg1.edit(content='**{}** won this round.'.format(arg1.display_name))
                        flag = -1
                if flag == -1:
                    flag = 0
                    ppotential = bpotential = pstreak = bstreak = 0
                    pbar = [':black_medium_square:', ':black_medium_square:', ':black_medium_square:',':black_medium_square:', ':black_medium_square:']
                    bbar = [':black_medium_square:', ':black_medium_square:', ':black_medium_square:',':black_medium_square:', ':black_medium_square:']
                    movement = 'horizontal'
                    ppos = 42
                    bpos = 43
                    decision = 1
                    continue
                if decision <= 11:
                    cd = 3.1 - 0.1 * decision
                else:
                    cd = 2
                if decision % 2 != 0:
                    if decision == 1:
                        msg1 = await ctx.send('**' + ctx.author.name + '** turn:')
                    else:
                        await msg1.edit(content='**' + ctx.author.name + '** turn:')
                    alphabet = ''
                    for i in range(random.randint(3, 5)):
                        alphabet += random.choice(alphabets)
                    time.sleep(2)
                    await msg1.edit(content='**' + ctx.author.name + '** turn:\ntype `' + alphabet + '`')
                    time.sleep(0.8)
                    await msg1.edit(content='**' + ctx.author.name + '** turn:')
                    try:
                        while 1:
                            msg = await client.wait_for('message', check=check(ctx.author), timeout=cd)
                            if msg.content.lower() == 'exit':
                                flag = 1
                                await msg.add_reaction('\N{OCTAGONAL SIGN}')
                                await msg1.edit(content='aborted.')
                                break
                            elif msg.content.lower() == alphabet:
                                if pstreak == 2:
                                    bstreak = 0
                                    pstreak = 0
                                    movement = random.choice(['up', 'down'])
                                    if movement == 'up':
                                        if ppos == 40:
                                            bpos = 28
                                        elif ppos == 41:
                                            bpos = 29
                                        elif ppos == 42:
                                            bpos = 30
                                        elif ppos == 43:
                                            bpos = 31
                                        elif ppos == 44:
                                            bpos = 32
                                        elif ppos == 45:
                                            bpos = 33
                                        elif ppos == 46:
                                            bpos = 34
                                    elif movement == 'down':
                                        if ppos == 40:
                                            bpos = 52
                                        elif ppos == 41:
                                            bpos = 53
                                        elif ppos == 42:
                                            bpos = 54
                                        elif ppos == 43:
                                            bpos = 55
                                        elif ppos == 44:
                                            bpos = 56
                                        elif ppos == 45:
                                            bpos = 57
                                        elif ppos == 46:
                                            bpos = 58
                                elif movement == 'up':
                                    if ppotential == 5:
                                        ppos -= 24
                                        bpos -= 24
                                        ppotential = -1
                                    else:
                                        ppos -= 12
                                        bpos -= 12
                                elif movement == 'down':
                                    if ppotential == 5:
                                        ppos += 24
                                        bpos += 24
                                        ppotential = -1
                                    else:
                                        ppos += 12
                                        bpos += 12
                                elif movement == 'horizontal':
                                    pstreak += 1
                                    if ppotential == 5:
                                        ppos += 2
                                        bpos += 2
                                        ppotential = -1
                                    else:
                                        ppos += 1
                                        bpos += 1
                                ppotential += 1
                            else:
                                await msg.add_reaction('\N{CROSS MARK}')
                                pstreak = 0
                                if movement == 'horizontal':
                                    ppos -= 1
                                    bpos -= 1
                                elif movement == 'up':
                                    ppos += 12
                                    bpos += 12
                                elif movement == 'down':
                                    ppos -= 12
                                    bpos -= 12
                            await msg.delete()
                            no_response = 0
                            break
                    except asyncio.TimeoutError:
                        await msg1.edit(content=ctx.author.mention + ' missed their turn.')
                        if ppotential != 0:
                            ppotential -= 1
                        no_response += 1
                        pstreak = 0
                    if ppos == 4 or ppos == 5 or ppos == 6 or ppos == 7 or ppos == 8 or ppos == 9 or ppos == 22:
                        ppos += 12
                        bpos += 12
                    elif ppos == 76 or ppos == 77 or ppos == 78 or ppos == 79 or ppos == 80 or ppos == 81 or ppos == 70:
                        ppos -= 12
                        bpos -= 12
                else:
                    await msg1.edit(content='**{}** turn:'.format(arg1.display_name))
                    alphabet = ''
                    for i in range(random.randint(3, 5)):
                        alphabet += random.choice(alphabets)
                    time.sleep(2)
                    await msg1.edit(content='**{}** turn:\ntype `'.format(arg1.display_name) + alphabet + '`')
                    time.sleep(0.8)
                    await msg1.edit(content='**{}** turn:'.format(arg1.display_name))
                    try:
                        while 1:
                            msg = await client.wait_for('message', check=check(arg1._user), timeout=cd)
                            if msg.content.lower() == 'exit':
                                flag = 1
                                await msg.add_reaction('\N{OCTAGONAL SIGN}')
                                await msg1.edit(content='aborted.')
                                break
                            elif msg.content.lower() == alphabet:
                                if bstreak == 3:
                                    pstreak = 0
                                    bstreak = 0
                                    movement = random.choice(['up', 'down'])
                                    if movement == 'up':
                                        if bpos == 45:
                                            ppos = 57
                                        elif bpos == 44:
                                            ppos = 56
                                        elif bpos == 43:
                                            ppos = 55
                                        elif bpos == 42:
                                            ppos = 54
                                        elif bpos == 41:
                                            ppos = 53
                                        elif bpos == 40:
                                            ppos = 52
                                        elif bpos == 39:
                                            ppos = 51
                                    elif movement == 'down':
                                        if bpos == 45:
                                            ppos = 33
                                        elif bpos == 44:
                                            ppos = 32
                                        elif bpos == 43:
                                            ppos = 31
                                        elif bpos == 42:
                                            ppos = 30
                                        elif bpos == 41:
                                            ppos = 29
                                        elif bpos == 40:
                                            ppos = 28
                                        elif bpos == 39:
                                            ppos = 27
                                elif movement == 'up':
                                    if bpotential == 5:
                                        ppos += 24
                                        bpos += 24
                                        bpotential = -1
                                    else:
                                        ppos += 12
                                        bpos += 12
                                elif movement == 'down':
                                    if bpotential == 5:
                                        ppos -= 24
                                        bpos -= 24
                                        bpotential = -1
                                    else:
                                        ppos -= 12
                                        bpos -= 12
                                elif movement == 'horizontal':
                                    bstreak += 1
                                    if bpotential == 5:
                                        ppos -= 2
                                        bpos -= 2
                                        bpotential = -1
                                    else:
                                        ppos -= 1
                                        bpos -= 1
                                bpotential += 1
                            else:
                                await msg.add_reaction('\N{CROSS MARK}')
                                bstreak = 0
                                if movement == 'horizontal':
                                    ppos += 1
                                    bpos += 1
                                elif movement == 'up':
                                    ppos -= 12
                                    bpos -= 12
                                elif movement == 'down':
                                    ppos += 12
                                    bpos += 12
                            await msg.delete()
                            no_response = 0
                            break
                    except asyncio.TimeoutError:
                        await msg1.edit(content='{} missed their turn.'.format(arg1.mention))
                        if bpotential != 0:
                            bpotential -= 1
                        no_response += 1
                        bstreak = 0
                    if bpos == 63 or bpos == 76 or bpos == 77 or bpos == 78 or bpos == 79 or bpos == 80:
                        bpos -= 12
                        ppos -= 12
                    elif bpos == 15 or bpos == 5 or bpos == 4 or bpos == 6 or bpos == 7 or bpos == 8:
                        bpos += 12
                        ppos += 12
                decision += 1
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def ques(ctx, *,arg):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    string = "   "
    ans = random.randint(1, 105)
    if ans == 1:
        string += "yes."
    elif ans == 2:
        string += "no."
    elif ans == 3:
        string += "maybe."
    elif ans == 4:
        string += "statistically yes."
    elif ans == 5:
        string += "perhaps no."
    elif ans == 6:
        string += "i have to politely disagree."
    elif ans == 7:
        string += "it's Jesus."
    elif ans == 8:
        string += "area 51."
    elif ans == 9:
        string += "aliens did it."
    elif ans == 10:
        string += "you will never know."
    elif ans == 11:
        string += "dark chocolates."
    elif ans == 12:
        string += "is that really a question?"
    elif ans == 13:
        string += "i hope not."
    elif ans == 14:
        string += "yeah."
    elif ans == 15:
        string += "hentai."
    elif ans == 16:
        string += "potato potato."
    elif ans == 17:
        string += "it is what it is."
    elif ans == 18:
        string += "possiblities are high."
    elif ans == 19:
        string += "according to the laws of physics,no."
    elif ans == 20:
        string += "drugs."
    elif ans == 21:
        string += "so watermelon of you."
    elif ans == 22:
        string += "i hate to say this but yes."
    elif ans == 23:
        string += "some questions can never be answered."
    elif ans == 24:
        string += "*hides the body.*"
    elif ans == 25:
        string += "*runs away.*"
    elif ans == 26:
        string += "skip."
    elif ans == 27:
        string += "god's plan."
    elif ans == 28:
        string += "brain diarrhea."
    elif ans == 29:
        string += "let us assume it's true."
    elif ans == 30:
        string += "your ex."
    elif ans == 31:
        string += "girls."
    elif ans == 32:
        string += "boys."
    elif ans == 33:
        string += "procastination."
    elif ans == 34:
        string += "XO"
    elif ans == 35:
        string += "most likely not."
    elif ans == 36:
        string += "..."
    elif ans == 37:
        string += "R.I.P"
    elif ans == 38:
        string += "33°C."
    elif ans == 39:
        string += "imagine asking to bot."
    elif ans == 40:
        string += "😳."
    elif ans == 41:
        string += "sacrifice is the only way."
    elif ans == 42:
        string += "you wouldn't get it."
    elif ans == 43:
        string += "fidget spinner."
    elif ans == 44:
        string += "**FBI OPEN UP**."
    elif ans == 45:
        string += "potassium cyanide."
    elif ans == 46:
        string += "just go with the flow."
    elif ans == 47:
        string += "i don't know."
    elif ans == 48:
        string += "another one."
    elif ans == 49:
        string += "it's real."
    elif ans == 50:
        string += "they are coming."
    elif ans == 51:
        string += "all about money."
    elif ans == 52:
        string += "i know,right."
    elif ans == 53:
        string += "i guess so."
    elif ans == 54:
        string += "*sighs*."
    elif ans == 55:
        string += "studies say no."
    elif ans == 56:
        string += "100mL."
    elif ans == 57:
        string += "not now."
    elif ans == 58:
        string += "you are right."
    elif ans == 59:
        string += "yeah,i saw that."
    elif ans == 60:
        string += "*cocks gun*."
    elif ans == 61:
        string += "it ain't worth a try."
    elif ans == 62:
        string += "tomorrow."
    elif ans == 63:
        string += "you already know."
    elif ans == 64:
        string += "*stares suspiciously*."
    elif ans == 65:
        string += "mankind."
    elif ans == 66:
        string += "you exposed it!!!"
    elif ans == 67:
        string += "who knows."
    elif ans == 68:
        string += "yeah,i heard it on the radio."
    elif ans == 69:
        string += "what if i say no."
    elif ans == 70:
        string += "yes and that's a factual."
    elif ans == 71:
        string += "lol?"
    elif ans == 72:
        string += "peace is the answer."
    elif ans == 73:
        string += "that's why mom doesn't love you."
    elif ans == 74:
        string += "planet earth."
    elif ans == 75:
        string += "the closet."
    elif ans == 76:
        string += "actually no."
    elif ans == 77:
        string += "wait for monsoon."
    elif ans == 78:
        string += "1/4 chance."
    elif ans == 79:
        string += "spaghetti."
    elif ans == 80:
        string += "elaborate."
    elif ans == 81:
        string += "911."
    elif ans == 82:
        string += "69."
    elif ans == 83:
        string += ":no_entry_sign: :billed_cap: but idk."
    elif ans == 84:
        string += "sometimes yes but sometimes no."
    elif ans == 85:
        string += "k."
    elif ans == 86:
        string += "Keanu Reeves."
    elif ans == 87:
        string += "odds are high."
    elif ans == 88:
        string += "hmm."
    elif ans == 89:
        string += "look in the mirror."
    elif ans == 90:
        string += "it's an old story."
    elif ans == 91:
        string += "29th feb."
    elif ans == 92:
        string += "ignore it."
    elif ans == 93:
        string += "*thinking*."
    elif ans == 94:
        string += "that's why she left you."
    elif ans == 95:
        string += "don't trust me."
    elif ans == 96:
        string += "maths."
    elif ans == 97:
        string += "a handful of salt."
    elif ans == 98:
        string += "wtf."
    elif ans == 99:
        string += "*twin towers left the chat*."
    elif ans == 100:
        string += "i-"
    elif ans == 101:
        string += "don't worry,one day sun will explode and everything will erase :)"
    elif ans == 102:
        string +="a beta simp in gigachad body."
    elif ans == 103:
        string+="cause nuns don't work on sunday."
    elif ans==104:
        string+="*dramatic orchestral music plays*"
    else:
        string += "you are so much smarter when you don't speak."
    await ctx.send(embed=discord.Embed(title="**Q . " + str(arg) + "**", description=string, color=0x7F00FF))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.author.bot:
        return
    if "gn " in msg.content.lower():
        await msg.add_reaction("<a:emoji_11:763348543146295329>")
    elif " gn" in msg.content.lower():
        await msg.add_reaction("<a:emoji_11:763348543146295329>")
    elif "gn." in msg.content.lower():
        await msg.add_reaction("<a:emoji_11:763348543146295329>")
    elif "gn " in msg.content.lower():
        await msg.add_reaction("<a:emoji_11:763348543146295329>")
    elif "good night" in msg.content.lower():
        await msg.add_reaction("<a:emoji_11:763348543146295329>")

    if "gm" in msg.content.lower():
        await msg.add_reaction("<a:emoji_12:763351577159139330>")
    elif " gm" in msg.content.lower():
        await msg.add_reaction("<a:emoji_12:763351577159139330>")
    elif "gm " in msg.content.lower():
        await msg.add_reaction("<a:emoji_12:763351577159139330>")
    elif "gm." in msg.content.lower():
        await msg.add_reaction("<a:emoji_12:763351577159139330>")
    elif "good morning" in msg.content.lower():
        await msg.add_reaction("<a:emoji_12:763351577159139330>")
    if "teko" in msg.content.lower():
        if "fuck" in msg.content.lower():
            await msg.add_reaction("<a:no_u:764894207755812904>")

    await client.process_commands(msg)


@client.command()
async def wam(ctx, arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1==None:
        command_usage.append(ctx.author.id)
        flag=0
        score = pts=0
        digits = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '❌']
        holes = ['<:hole1:852852344600526908>', '<:hole2:852852365027573780>', '<:hole3:852852386102902784>','<:hole4:852852423478345738>', '<:hole5:852852443099693087>', '<:hole6:852852463596732456>','<:hole7:852852485903089704>']
        embed = discord.Embed(title='<:hole1:852852344600526908>  <:hole2:852852365027573780>  <:hole3:852852386102902784>  <:hole4:852852423478345738>\n       <:hole5:852852443099693087>  <:hole6:852852463596732456>  <:hole7:852852485903089704> ',description=":small_blue_diamond: **SCORE** = " + str(score) + '\n:small_blue_diamond: react :x: to abort',color=0x7F00FF)
        embed.set_author(name=ctx.author.display_name + "'s whack-a-mole")
        embed.set_footer(text='press corresponding emoji when mole hops.')
        string1 = await ctx.send(embed=embed)
        for emoji in digits:
            await string1.add_reaction(emoji)

        def check1(reaction, user):
            return user.id == ctx.author.id and str(reaction.emoji) in digits
        mole=prev_mole=-1
        t1 = time.time()
        while 1:
            string = ''
            while mole==prev_mole:
                mole = random.randint(0, 6)
            for i in range(7):
                if i == 4:
                    string += '\n       '
                if i == mole:
                    string += '<:mole:852848674479931423>  '
                else:
                    string += holes[i] + '  '
            if time.time()-t1>60:
                flag=-1
                string='GAME OVER!'
            embed = discord.Embed(title=string, description=":small_blue_diamond: **SCORE** = " + str(score) + '\n:small_blue_diamond: react :x: to abort', color=0x7F00FF)
            embed.set_author(name=ctx.author.display_name + "'s whack-a-mole",icon_url=ctx.author.avatar_url)
            embed.set_footer(text='press corresponding emoji when mole hops.')
            await string1.edit(embed=embed)
            if flag==-1:
                break
            try:
                reaction, user = await client.wait_for('reaction_add', check=check1, timeout=3)
            except asyncio.TimeoutError:
                prev_mole = mole
                continue
            else:
                if str(reaction.emoji) == digits[7]:
                    await ctx.send('aborted.')
                    break
                elif str(reaction.emoji) == digits[mole]:
                    pts += 0.5
                    score=int(math.exp(pts))
            await string1.remove_reaction(reaction.emoji, ctx.author)
            prev_mole=mole
        command_usage.remove(ctx.author.id)
    else:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        flag = 0
        score1 = pts1 = score2 = pts2 =0
        digits = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '❌']
        holes = ['<:hole1:852852344600526908>', '<:hole2:852852365027573780>', '<:hole3:852852386102902784>',
                 '<:hole4:852852423478345738>', '<:hole5:852852443099693087>', '<:hole6:852852463596732456>',
                 '<:hole7:852852485903089704>']
        embed = discord.Embed(title='<:hole1:852852344600526908>  <:hole2:852852365027573780>  <:hole3:852852386102902784>  <:hole4:852852423478345738>\n       <:hole5:852852443099693087>  <:hole6:852852463596732456>  <:hole7:852852485903089704> ',description=":small_blue_diamond: **"+ctx.author.name+" SCORE** = " + str(score1) + '\n:small_blue_diamond: **{} SCORE** = '.format(arg1.display_name)+str(score2)+'\n:small_blue_diamond: react :x: to abort',color=0x7F00FF)
        embed.set_author(name="WHACK-A-MOLE")
        embed.set_footer(text='press corresponding emoji when mole hops.')
        string1 = await ctx.send(embed=embed)
        for emoji in digits:
            await string1.add_reaction(emoji)

        def check1(reaction, user):
            return (user.id == ctx.author.id or user.id==arg1._user.id) and str(reaction.emoji) in digits

        mole = prev_mole = -1
        t1 = time.time()
        while 1:
            string = ''
            while mole==prev_mole:
                mole = random.randint(0, 6)
            for i in range(7):
                if i == 4:
                    string += '\n       '
                if i == mole:
                    string += '<:mole:852848674479931423>  '
                else:
                    string += holes[i] + '  '
            if time.time()-t1>90:
                flag=-1
                string='GAME OVER!,'
                if score2>score1:
                    string+=',**{}** won.'.format(arg1.display_name)
                elif score1>score2:
                    string+='**'+ctx.author.name+'** won.'
                else:
                    string+='draw.'
            embed = discord.Embed(title=string, description=":small_blue_diamond: **"+ctx.author.name+" SCORE** = " + str(score1) + '\n:small_blue_diamond: **{} SCORE** = '.format(arg1.display_name)+str(score2)+'\n:small_blue_diamond: react :x: to abort', color=0x7F00FF)
            embed.set_author(name=ctx.author.display_name + "'s whack-a-mole",icon_url=ctx.author.avatar_url)
            embed.set_footer(text='press corresponding emoji when mole hops.')
            await string1.edit(embed=embed)
            if flag==-1:
                break
            try:
                reaction, user = await client.wait_for('reaction_add', check=check1, timeout=3)
            except asyncio.TimeoutError:
                prev_mole = mole
                continue
            else:
                if str(reaction.emoji) == digits[7]:
                    await ctx.send('aborted.')
                    break
                elif user.id == ctx.author.id and str(reaction.emoji) == digits[mole]:
                    pts1 += 0.5
                    score1 = int(math.exp(pts1))
                elif user.id == arg1._user.id and str(reaction.emoji) == digits[mole]:
                    pts2 += 0.5
                    score2 = int(math.exp(pts2))
            await string1.remove_reaction(reaction.emoji, ctx.author)
            await string1.remove_reaction(reaction.emoji, arg1._user)
            prev_mole = mole
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)

@client.command()
async def av(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1==None:
        embed = discord.Embed(color=0x7F00FF)
        embed.set_author(name=ctx.author.display_name + "'s avatar")
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=0x7F00FF)
        embed.set_author(name="{}'s avatar".format(arg1.display_name))
        embed.set_image(url=arg1._user.avatar_url)
        await ctx.send(embed=embed)

@client.command()
async def avatar(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1==None:
        embed = discord.Embed(color=0x7F00FF)
        embed.set_author(name=ctx.author.display_name + "'s avatar")
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=0x7F00FF)
        embed.set_author(name="{}'s avatar".format(arg1.display_name))
        embed.set_image(url=arg1._user.avatar_url)
        await ctx.send(embed=embed)

@client.command()
async def kuromasu(ctx):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    command_usage.append(ctx.author.id)
    flag=-1
    blue_num=['','<:blue1:853560159091294220>','<:blue2:853560179718881290>','<:blue3:853560199925989377>','<:blue4:853560218008682496>','<:blue5:853560235717427221>','<:blue6:853560257744994364>']
    while flag==-1:
        maze_orig = []
        index = []
        flag = 1
        for i in range(16):
            dot=random.choice([':red_circle:',':blue_circle:'])
            maze_orig.append(dot)
            if dot==':blue_circle:':
                index.append(i)
        for i in range(16):
            if i ==0 and maze_orig[i]==':blue_circle:':
                if maze_orig[1]==':red_circle:' and maze_orig[4]==':red_circle:':
                    flag=-1
                    break
            elif i==3 and maze_orig[i]==':blue_circle:':
                if maze_orig[2]==':red_circle:' and maze_orig[7]==':red_circle:':
                    flag=-1
                    break
            elif i==12 and maze_orig[i]==':blue_circle:':
                if maze_orig[8]==':red_circle:' and maze_orig[13]==':red_circle:':
                    flag=-1
                    break
            elif i==15 and maze_orig[i]==':blue_circle:':
                if maze_orig[11]==':red_circle:' and maze_orig[14]==':red_circle:':
                    flag=-1
                    break
            elif (i==1 or i==2) and maze_orig[i]==':blue_circle:':
                if maze_orig[i-1]==':red_circle:' and maze_orig[i+4]==':red_circle:' and maze_orig[i+1]==':red_circle:':
                    flag=-1
                    break
            elif (i==13 or i==14) and maze_orig[i]==':blue_circle:':
                if maze_orig[i-1]==':red_circle:' and maze_orig[i-4]==':red_circle:' and maze_orig[i+1]==':red_circle:':
                    flag=-1
                    break
            elif (i==4 or i==8) and maze_orig[i]==':blue_circle:':
                if maze_orig[i-4]==':red_circle:' and maze_orig[i+4]==':red_circle:' and maze_orig[i+1]==':red_circle:':
                    flag=-1
                    break
            elif (i==7 or i==11) and maze_orig[i]==':blue_circle:':
                if maze_orig[i-1]==':red_circle:' and maze_orig[i+4]==':red_circle:' and maze_orig[i-4]==':red_circle:':
                    flag=-1
                    break
            elif (i==5 or i==6 or i==9 or i==10) and maze_orig[i]==':blue_circle:':
                if maze_orig[i-1]==':red_circle:' and maze_orig[i+4]==':red_circle:' and maze_orig[i+1]==':red_circle:' and maze_orig[i-4]==':red_circle:':
                    flag=-1
                    break

    random.shuffle(index)
    display_blue=[]
    list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for j in range(random.randint(3,5)):
        surround=0
        pos=index[j]
        if pos in [0,4,8,12]:
            for i in range(1,4):
                if maze_orig[pos+i] ==':blue_circle:' or (maze_orig[pos+i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [1,5,9,13]:
            for i in range(1,3):
                if maze_orig[pos+i] ==':blue_circle:' or (maze_orig[pos+i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [2,6,10,14]:
            if maze_orig[pos + 1] == ':blue_circle:' or (maze_orig[pos + 1] in blue_num):
                surround += 1
        if pos in [3,7,11,15]:
            for i in range(1,4):
                if maze_orig[pos-i] ==':blue_circle:' or (maze_orig[pos-i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [2,6,10,14]:
            for i in range(1,3):
                if maze_orig[pos-i] ==':blue_circle:' or (maze_orig[pos-i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [1,5,9,13]:
            if maze_orig[pos - 1] == ':blue_circle:' or (maze_orig[pos - 1] in blue_num):
                surround += 1
        if pos in [0,1,2,3]:
            for i in range(4,16,4):
                if maze_orig[pos+i]==':blue_circle:' or (maze_orig[pos+i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [4,5,6,7]:
            for i in range(4,12,4):
                if maze_orig[pos+i]==':blue_circle:' or (maze_orig[pos+i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [8,9,10,11]:
            if maze_orig[pos + 4] == ':blue_circle:' or (maze_orig[pos + 4] in blue_num):
                surround += 1
        if pos in [12,13,14,15]:
            for i in range(4,16,4):
                if maze_orig[pos-i]==':blue_circle:' or (maze_orig[pos-i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [8,9,10,11]:
            for i in range(4,12,4):
                if maze_orig[pos-i]==':blue_circle:' or (maze_orig[pos-i] in blue_num):
                    surround+=1
                else:
                    break
        elif pos in [4,5,6,7]:
            if maze_orig[pos - 4] == ':blue_circle:' or (maze_orig[pos - 4] in blue_num):
                surround += 1
        maze_orig[pos]=blue_num[surround]
        display_blue.append(pos)
    maze = []
    for element in display_blue:
        list.remove(element)
    display=random.randint(5-len(display_blue),8-len(display_blue))+len(display_blue)
    random.shuffle(list)
    list=list[:display-len(display_blue)]
    positions=[]
    for i in range(16):
        if i in display_blue or i in list:
            maze.append(maze_orig[i])
        else:
            maze.append('<:blank:853646489191579648>')
            positions.append(i+1)
    pos=''
    for element in positions:
        pos+=str(element)+','
    pos=pos[:-1]+'.'
    turns=0
    maze1=maze.copy()
    flag=-1
    while 1:
        progress = 0
        string = ''
        for i in range(4):
            for j in range(4):
                if maze[j+4*i]==maze_orig[j+4*i]:
                    progress+=6.25
                elif maze[j+4*i]!='<:blank:853646489191579648>':
                    progress-=6.25
                string += maze[j + 4 * i]+' '
            string+='  :no_entry:  '
            for j in range(4):
                string += maze1[j + 4 * i]+' '
            string += '\n'
        if progress<0:
            progress=0
        if flag==2:
            embed = discord.Embed(title='SOLUTION :',description=string + '\n:small_blue_diamond: Progress : ' + str(progress) + '%\n:small_blue_diamond: Available positions : ' + pos + '\n:small_blue_diamond: The right side puzzle is only to show the fixed dots in your original puzzle' + '\n:small_blue_diamond: type `restart` to restart the puzzle.\n:small_blue_diamond: type `exit` to abort/reveal solution.',color=0x7F00FF)
        else:
            embed = discord.Embed(description=string+'\n:small_blue_diamond: Progress : '+str(progress)+'%\n:small_blue_diamond: Available positions : '+pos+'\n:small_blue_diamond: The right side puzzle is only to show the fixed dots in your original puzzle'+'\n:small_blue_diamond: type `restart` to restart the puzzle.\n:small_blue_diamond: type `exit` to abort/reveal solution.', color=0x7F00FF)
        embed.set_author(name=ctx.author.display_name + "'s puzzle:", icon_url=ctx.author.avatar_url)
        embed.set_footer(text="enter dot in empty positions like 2r,11b,etc.")
        await ctx.send(embed=embed)

        if flag==2:
            break
        elif maze_orig == maze:
            await ctx.send('GG **'+ctx.author.name+'** , you completed the puzzle in '+str(turns)+' turns.')
            flag=3
            break
        flag = -1
        try:
            t2=0
            while 1:
                t1=time.time()
                msg = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                msg1 = msg.content.lower()
                if msg.content.lower()=='exit':
                    await msg.add_reaction('\N{OCTAGONAL SIGN}')
                    flag = 2
                    maze = maze_orig.copy()
                    break
                elif msg.content.lower()=='restart':
                    maze=maze1.copy()
                    flag=0
                elif len(msg1)==2 and msg1[1].isalpha()==True and msg1[0].isdigit()==True:

                    if int(msg1[0]) in positions:
                        if msg1[1]=='r':
                            maze[int(msg1[0])-1]=':red_circle:'
                            flag=0
                        elif msg1[1]=='b':
                            maze[int(msg1[0])-1]=':blue_circle:'
                            flag=0
                elif len(msg1) == 3 and msg1[2].isalpha()==True and msg1[0].isdigit()==True and msg1[1].isdigit()==True:
                    num=msg1[0]+msg1[1]
                    num=int(num)
                    if num in positions:
                        if msg1[2] == 'r':
                            maze[num-1] = ':red_circle:'
                            flag = 0
                        elif msg1[2] == 'b':
                            maze[num-1] = ':blue_circle:'
                            flag = 0
                if flag in [0,1,2]:
                    break
                t2+=int(time.time()-t1)
        except asyncio.TimeoutError:
            await ctx.send("looks like you fell asleep **" + ctx.author.mention + "**.")
            break
        turns+=1
    command_usage.remove(ctx.author.id)

@client.command()
async def colorix(ctx):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    command_usage.append(ctx.author.id)
    maze=[]
    pos1=pos2=-1
    turns=score=0
    while pos1==pos2:
        pos1=random.randint(0,15)
        pos2=random.randint(0,15)
    for i in range(4):
        for j in range(4):
            if j+4*i == pos1 or j+4*i == pos2:
                maze.append('<:0th:853875973416943617>')
            else:
                maze.append('<:empty:853875902316412968>')
    positions=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    def check1(reaction, user):
        return user.id == ctx.author.id and str(reaction.emoji) in ['⬅️','➡️','⬆️','⬇️','❌']
    while 1:
        string=''
        for i in range(4):
            for j in range(4):
                string+=maze[j+4*i]
            string+='\n'
        embed=discord.Embed(title='**'+ctx.author.name+',CAN YOU REACH PINK!**',description=string+'\n:small_blue_diamond: **SCORE** : '+str(score)+'\n:small_blue_diamond: color order :\n<:0th:853875973416943617> < <:1st:853876013184319519> < <:2nd:853876034008252456> < <:3rd:853876056737054720> < <:4th:853876087192289340> < <:5th:853876194591113227> < <:6th:853876228121165824> < <:7th:853876250292256810> < <:8th:853876268785598474> < <:9th:853876289483177984> < <:tenth:853876310279847986>\n:small_blue_diamond: react :x: to abort.', color=0x7F00FF)
        embed.set_author(name=ctx.author.display_name + "'s colorix", icon_url=ctx.author.avatar_url)
        embed.set_footer(text='react required emoji to swipe in that direction. ')
        if turns==0:
            string1=await ctx.send(embed=embed)
            for emoji in ['⬅️','➡️','⬆️','⬇️','❌']:
                await string1.add_reaction(emoji)
        elif '<:tenth:853876310279847986>' in maze:
            embed = discord.Embed(title='GG **'+ctx.author.name+'**, you reached pink in '+str(turns)+' turns.',description=string + '\n:small_blue_diamond: **SCORE** : ' + str(score), color=0x7F00FF)
            embed.set_author(name=ctx.author.display_name + "'s colorix", icon_url=ctx.author.avatar_url)
            await string1.edit(embed=embed)
            break
        elif '<:empty:853875902316412968>' not in maze:
            flag=0
            for i in range(15):
                if (maze[i]==maze[i+1]) or (i <12 and maze[i]==maze[i+4]):
                    flag=1
                    break
            if flag==0:
                embed = discord.Embed(title='GAME OVER **'+ctx.author.name+'**',description=string + '\n:small_blue_diamond: **SCORE** : ' + str(score), color=0x7F00FF)
                embed.set_author(name=ctx.author.display_name + "'s colorix", icon_url=ctx.author.avatar_url)
                await string1.edit(embed=embed)
                break
        else:
            await string1.edit(embed=embed)
        maze1 = maze.copy()
        try:
            reaction, user = await client.wait_for('reaction_add', check=check1, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("looks like you fell asleep **" + ctx.author.mention + "**.")
            break
        else:
            if reaction.emoji=='❌':
                await ctx.send('aborted.')
                break
            elif reaction.emoji=='⬅️':
                for i in range(0,13,4):
                    color=[]
                    for j in range(4):
                        if maze[i+j]!='<:empty:853875902316412968>':
                            color.append(maze[i+j])
                    pos=0
                    while len(color)!=0:
                        if len(color)!=1:
                            if color[0]==color[1]:
                                if color[0]=='<:0th:853875973416943617>':
                                    score+=4
                                    maze[pos+i]='<:1st:853876013184319519>'
                                elif color[0]=='<:1st:853876013184319519>':
                                    score += 8
                                    maze[pos+i]='<:2nd:853876034008252456>'
                                elif color[0]=='<:2nd:853876034008252456>':
                                    score += 16
                                    maze[pos+i]='<:3rd:853876056737054720>'
                                elif color[0]=='<:3rd:853876056737054720>':
                                    score += 32
                                    maze[pos+i]='<:4th:853876087192289340>'
                                elif color[0]=='<:4th:853876087192289340>':
                                    score += 64
                                    maze[pos+i]='<:5th:853876194591113227>'
                                elif color[0]=='<:5th:853876194591113227>':
                                    score += 128
                                    maze[pos+i]='<:6th:853876228121165824>'
                                elif color[0]=='<:6th:853876228121165824>':
                                    score+=256
                                    maze[pos+i]='<:7th:853876250292256810>'
                                elif color[0]=='<:7th:853876250292256810>':
                                    score+=512
                                    maze[pos+i]='<:8th:853876268785598474>'
                                elif color[0]=='<:8th:853876268785598474>':
                                    score+=1024
                                    maze[pos+i]='<:9th:853876289483177984>'
                                elif color[0]=='<:9th:853876289483177984>':
                                    score+=2048
                                    maze[pos+i]='<:tenth:853876310279847986>'
                                color.pop(0)
                            else:
                                maze[pos+i]=color[0]
                            pos+=1
                            color.pop(0)
                        else:
                            maze[pos+i] = color[0]
                            color.pop(0)
                            pos+=1
                    while pos <=3:
                        maze[pos+i]='<:empty:853875902316412968>'
                        pos+=1
                await string1.remove_reaction(reaction.emoji, ctx.author)
            elif reaction.emoji == '➡️':
                for i in range(3, 16, 4):
                    color = []
                    for j in range(4):
                        if maze[i - j] != '<:empty:853875902316412968>':
                            color.append(maze[i - j])
                    pos = 0
                    while len(color) != 0:
                        if len(color) != 1:
                            if color[0] == color[1]:
                                if color[0] == '<:0th:853875973416943617>':
                                    score += 4
                                    maze[i-pos] = '<:1st:853876013184319519>'
                                elif color[0] == '<:1st:853876013184319519>':
                                    score += 8
                                    maze[i-pos] = '<:2nd:853876034008252456>'
                                elif color[0] == '<:2nd:853876034008252456>':
                                    score += 16
                                    maze[i-pos] = '<:3rd:853876056737054720>'
                                elif color[0] == '<:3rd:853876056737054720>':
                                    score += 32
                                    maze[i-pos] = '<:4th:853876087192289340>'
                                elif color[0] == '<:4th:853876087192289340>':
                                    score += 64
                                    maze[i-pos] = '<:5th:853876194591113227>'
                                elif color[0] == '<:5th:853876194591113227>':
                                    score += 128
                                    maze[i-pos] = '<:6th:853876228121165824>'
                                elif color[0] == '<:6th:853876228121165824>':
                                    score += 256
                                    maze[i-pos] = '<:7th:853876250292256810>'
                                elif color[0] == '<:7th:853876250292256810>':
                                    score += 512
                                    maze[i-pos] = '<:8th:853876268785598474>'
                                elif color[0] == '<:8th:853876268785598474>':
                                    score += 1024
                                    maze[i-pos] = '<:9th:853876289483177984>'
                                elif color[0] == '<:9th:853876289483177984>':
                                    score += 2048
                                    maze[i-pos] = '<:tenth:853876310279847986>'
                                color.pop(0)
                            else:
                                maze[i-pos] = color[0]
                            pos += 1
                            color.pop(0)
                        else:
                            maze[i-pos] = color[0]
                            color.pop(0)
                            pos += 1
                    while pos <= 3:
                        maze[i-pos] = '<:empty:853875902316412968>'
                        pos += 1
                await string1.remove_reaction(reaction.emoji, ctx.author)
            elif reaction.emoji == '⬆️':
                for i in range(4):
                    color = []
                    for j in range(0,13,4):
                        if maze[i +j] != '<:empty:853875902316412968>':
                            color.append(maze[i + j])
                    pos = 0
                    while len(color) != 0:
                        if len(color) != 1:
                            if color[0] == color[1]:
                                if color[0] == '<:0th:853875973416943617>':
                                    score += 4
                                    maze[i+4*pos] = '<:1st:853876013184319519>'
                                elif color[0] == '<:1st:853876013184319519>':
                                    score += 8
                                    maze[i+4*pos] = '<:2nd:853876034008252456>'
                                elif color[0] == '<:2nd:853876034008252456>':
                                    score += 16
                                    maze[i+4*pos] = '<:3rd:853876056737054720>'
                                elif color[0] == '<:3rd:853876056737054720>':
                                    score += 32
                                    maze[i+4*pos] = '<:4th:853876087192289340>'
                                elif color[0] == '<:4th:853876087192289340>':
                                    score += 64
                                    maze[i+4*pos] = '<:5th:853876194591113227>'
                                elif color[0] == '<:5th:853876194591113227>':
                                    score += 128
                                    maze[i+4*pos] = '<:6th:853876228121165824>'
                                elif color[0] == '<:6th:853876228121165824>':
                                    score += 256
                                    maze[i+4*pos] = '<:7th:853876250292256810>'
                                elif color[0] == '<:7th:853876250292256810>':
                                    score += 512
                                    maze[i+4*pos] = '<:8th:853876268785598474>'
                                elif color[0] == '<:8th:853876268785598474>':
                                    score += 1024
                                    maze[i+4*pos] = '<:9th:853876289483177984>'
                                elif color[0] == '<:9th:853876289483177984>':
                                    score += 2048
                                    maze[i+4*pos] = '<:tenth:853876310279847986>'
                                color.pop(0)
                            else:
                                maze[i+4*pos] = color[0]
                            pos += 1
                            color.pop(0)
                        else:
                            maze[i+4*pos] = color[0]
                            color.pop(0)
                            pos += 1
                    while pos <= 3:
                        maze[i+4*pos] = '<:empty:853875902316412968>'
                        pos += 1
            elif reaction.emoji == '⬇️':
                for i in range(12,16):
                    color = []
                    for j in range(0,13,4):
                        if maze[i -j] != '<:empty:853875902316412968>':
                            color.append(maze[i - j])
                    pos = 0
                    while len(color) != 0:
                        if len(color) != 1:
                            if color[0] == color[1]:
                                if color[0] == '<:0th:853875973416943617>':
                                    score += 4
                                    maze[i-4*pos] = '<:1st:853876013184319519>'
                                elif color[0] == '<:1st:853876013184319519>':
                                    score += 8
                                    maze[i-4*pos] = '<:2nd:853876034008252456>'
                                elif color[0] == '<:2nd:853876034008252456>':
                                    score += 16
                                    maze[i-4*pos] = '<:3rd:853876056737054720>'
                                elif color[0] == '<:3rd:853876056737054720>':
                                    score += 32
                                    maze[i-4*pos] = '<:4th:853876087192289340>'
                                elif color[0] == '<:4th:853876087192289340>':
                                    score += 64
                                    maze[i-4*pos] = '<:5th:853876194591113227>'
                                elif color[0] == '<:5th:853876194591113227>':
                                    score += 128
                                    maze[i-4*pos] = '<:6th:853876228121165824>'
                                elif color[0] == '<:6th:853876228121165824>':
                                    score += 256
                                    maze[i-4*pos] = '<:7th:853876250292256810>'
                                elif color[0] == '<:7th:853876250292256810>':
                                    score += 512
                                    maze[i-4*pos] = '<:8th:853876268785598474>'
                                elif color[0] == '<:8th:853876268785598474>':
                                    score += 1024
                                    maze[i-4*pos] = '<:9th:853876289483177984>'
                                elif color[0] == '<:9th:853876289483177984>':
                                    score += 2048
                                    maze[i-4*pos] = '<:tenth:853876310279847986>'
                                color.pop(0)
                            else:
                                maze[i-4*pos] = color[0]
                            pos += 1
                            color.pop(0)
                        else:
                            maze[i-4*pos] = color[0]
                            color.pop(0)
                            pos += 1
                    while pos <= 3:
                        maze[i-4*pos] = '<:empty:853875902316412968>'
                        pos += 1
            await string1.remove_reaction(reaction.emoji, ctx.author)
            if maze==maze1:
                continue
            random.shuffle(positions)
            for i in positions:
                if maze[i]=='<:empty:853875902316412968>':
                    r=random.randint(1,100)
                    if r == 1:
                        maze[i]='<:2nd:853876034008252456>'
                    elif r<=10:
                        maze[i]='<:1st:853876013184319519>'
                    else:
                        maze[i]='<:0th:853875973416943617>'
                    break
        turns+=1
    command_usage.remove(ctx.author.id)

@client.command()
async def svk(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
    elif arg1!=None:
        command_usage.append(ctx.author.id)
        command_usage.append(arg1._user.id)
        decision=t2 = 0
        await ctx.send("**{}**,do you want to start (as a survivor)? [ **y** / **n** ]".format(arg1.display_name))
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                if msg.content.lower() == "yes" or msg.content.lower() == "y":
                    decision = 1
                    break
                elif msg.content.lower() == "no" or msg.content.lower() == "n":
                    decision = -1
                    break
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            await ctx.send("**{}** did'nt replied.".format(arg1.display_name))
        if decision == -1:
            await ctx.send("terminated.")
        elif decision == 1:
            characters=['🧛','🧙','<:detective:854262739928612894>','🧝','🧟','🥷']
            survivors=5
            flag=0
            pos=0
            killer=random.choice(characters)
            random.shuffle(characters)
            await ctx.author.send('your killer character is '+killer+" (don't reveal it)")
            for r in characters:
                if r==killer:
                    break
                pos+=1
            def check1(reaction, user):
                return (user.id == ctx.author.id and str(reaction.emoji) in characters) or ((user.id == ctx.author.id or user.id == arg1._user.id) and str(reaction.emoji) == '❌')
            def check2(reaction, user):
                return (user.id == arg1._user.id and str(reaction.emoji) in characters) or ((user.id == ctx.author.id or user.id == arg1._user.id) and str(reaction.emoji) == '❌')
            def check3(reaction, user):
                return (user.id == ctx.author.id or user.id == arg1._user.id) and (reaction.emoji=='🏃' or reaction.emoji=='🔪')

            await ctx.send(ctx.author.mention+',your killer character is sent in your DM (make sure your DMs are open to everyone). ')
            string = "\n**__NIGHT 1__**\n------------------------------------------------\n"
            string+=':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:'+characters[0]+':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_lower_left::black_large_square::arrow_lower_right::black_large_square::black_large_square:\n'
            string += ':black_large_square:'+characters[1]+':black_large_square::black_large_square::black_large_square:'+characters[2]+':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::black_large_square::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:'+characters[3]+':black_large_square::black_large_square::black_large_square:'+characters[4]+':black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_upper_left::black_large_square::arrow_upper_right::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:'+characters[5]+':black_large_square::black_large_square::black_large_square:\n'
            string+=':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 5/5\n:small_blue_diamond: react :x: to abort."
            embed=discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:',description=string, color=0x7F00FF)
            embed.set_footer(text=ctx.author.name+',react the person whom you want to kill.(only in adjacent or opposite corner)')
            string1=await ctx.send(embed=embed)
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep " + ctx.author.mention + ".")
                    flag=-1
                    break
                else:
                    if reaction.emoji=='❌':
                        await ctx.send('aborted.')
                        flag=-1
                        break
                    if (pos == 0 or pos == 3 or pos==4) and str(reaction.emoji) in [characters[1],characters[2],characters[5]]:
                        break
                    elif (pos == 1 or pos==2 or pos==5) and str(reaction.emoji) in [characters[0],characters[3],characters[4]]:
                        break
                    await string1.remove_reaction(reaction.emoji, ctx.author)
            if flag==-1:
                command_usage.remove(ctx.author.id)
                command_usage.remove(arg1._user.id)
                return
            pos=0
            for c in characters:
                if c==str(reaction.emoji):
                    characters[pos]=':skull:'
                    break
                pos+=1
            survivors-=1
            string = "\n**__NIGHT 1__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[0] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_lower_left::black_large_square::arrow_lower_right::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[1] + ':black_large_square::black_large_square::black_large_square:' + characters[2] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::black_large_square::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[3] + ':black_large_square::black_large_square::black_large_square:' + characters[4] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_upper_left::black_large_square::arrow_upper_right::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[5] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n"+str(reaction.emoji)+" was killed!\n\n:small_blue_diamond: **SURVIVORS REMAINING** : 4/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text='{},react the person you find suspicious.'.format(arg1.display_name))
            string1=await ctx.send(embed=embed)
            characters.remove(':skull:')
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check2, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep ,{}.".format(arg1.mention))
                    flag=-1
                    break
                else:
                    if reaction.emoji=='❌':
                        await ctx.send('aborted.')
                        flag=-1
                    elif reaction.emoji==killer:
                        await ctx.send('survivors decided to eliminate '+str(reaction.emoji)+' (and he was **the killer**)\n:crown: **{}** won:crown:'.format(arg1.display_name))
                        flag=-1
                    else:
                        await ctx.send('survivors decided to eliminate ' + str(reaction.emoji) + ' (but he was **not the killer**)')
                        survivors-=1
                    break
            if flag==-1:
                command_usage.remove(arg1._user.id)
                command_usage.remove(ctx.author.id)
                return
            characters.remove(reaction.emoji)
            random.shuffle(characters)
            string = "\n**__NIGHT 2__**\n------------------------------------------------\n"
            string+=':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string+=':black_large_square:'+characters[0]+':left_right_arrow:'+characters[1]+':black_large_square:\n'
            string+=':black_large_square::arrow_up_down::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:'+characters[2] + ':left_right_arrow:' + characters[3]+':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 3/5\n:small_blue_diamond: react :x: to abort."
            embed=discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text=ctx.author.name+',react the person whom you want to kill.(only in adjacent or opposite corner)')
            string1=await ctx.send(embed=embed)
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction ('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep " + ctx.author.mention + ".")
                    flag=-1
                    break
                else:
                    if str(reaction.emoji)=='❌':
                        await ctx.send('aborted.')
                        flag=-1
                        break
                    elif str(reaction.emoji)!=killer:
                        break
                await string1.remove_reaction(reaction.emoji, ctx.author)
            if flag==-1:
                command_usage.remove(ctx.author.id)
                command_usage.remove(arg1._user.id)
                return
            pos = 0
            for c in characters:
                if c == str(reaction.emoji):
                    characters[pos] = ':skull:'
                    break
                pos += 1
            survivors -= 1
            string = "\n**__NIGHT 2__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[0] + ':left_right_arrow:' + characters[1] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[2] + ':left_right_arrow:' + characters[3] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n"+str(reaction.emoji)+" was killed!\n\n:small_blue_diamond: **SURVIVORS REMAINING** : 2/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text='{},react the person you find suspicious.'.format(arg1.display_name))
            string1=await ctx.send(embed=embed)
            characters.remove(':skull:')
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check2, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep ,{}.".format(arg1.mention))
                    flag = -1
                    break
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aborted.')
                        flag = -1
                    elif reaction.emoji == killer:
                        await ctx.send('survivors decided to eliminate ' + str(reaction.emoji) + ' (and he was **the killer**)\n:crown: **{}** won:crown:'.format(arg1.display_name))
                        flag = -1
                    else:
                        await ctx.send('survivors decided to eliminate ' + str(reaction.emoji) + ' (but he was **not the killer**)')
                        survivors -= 1
                    break
            if flag==-1:
                command_usage.remove(arg1._user.id)
                command_usage.remove(ctx.author.id)
                return
            characters.remove(reaction.emoji)
            random.shuffle(characters)
            string = "\n**__NIGHT 3__**\n------------------------------------------------\n"
            string+=':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string+=':black_large_square:'+characters[0]+':left_right_arrow:'+characters[1]+':black_large_square:\n'
            string+=':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 1/5"
            embed=discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            string1=await ctx.send(embed=embed)
            msg=await ctx.send(ctx.author.mention+',react in your DM.')
            msg1=await ctx.author.send('What will you do?\n🏃 : run away.\n🔪 : attack')
            for emoji in ['🏃','🔪']:
                await msg1.add_reaction(emoji)
            try:
                reaction, user = await client.wait_for('reaction_add', check=check3, timeout=30)
            except asyncio.TimeoutError:
                await msg.edit(content="looks like the killer ran away.\n:crown: **{}** won :crown:".format(arg1.display_name))
                flag = -1
            else:
                if reaction.emoji=='🔪':
                    choice1='attack each other'
                elif reaction.emoji=='🏃':
                    choice1='run away'
            await msg.edit(content='{},react in your DM.'.format(arg1.mention))
            msg1 = await arg1._user.send('What will you do?\n🏃 : run away.\n🔪 : attack')
            for emoji in ['🏃', '🔪']:
                await msg1.add_reaction(emoji)
            try:
                reaction, user = await client.wait_for('reaction_add', check=check3, timeout=30)
            except asyncio.TimeoutError:
                await msg.edit(content="looks like the last survivor already got killed.\n:crown: **"+ctx.author.name+"** won :crown:")
            else:
                if reaction.emoji=='🔪':
                    choice2='attack each other'
                elif reaction.emoji=='🏃':
                    choice2='run away'
            if characters[0]==killer:
                survivor=characters[1]
            else:
                survivor=characters[0]
            if choice1==choice2:
                if choice1[0]=='a':
                    await msg.edit(content="Killer("+killer+") decided to __attack__ ,but "+survivor+" somehow managed to snatch his knife and killed him.\n:crown: **{}** won :crown:".format(arg1.display_name))
                else:
                    await msg.edit(content="Killer ("+killer+") accidently lost his knife.Both decided to __run away__,but killer got caught by police.\n:crown: **{}** won :crown:".format(arg1.display_name))
            elif choice1[0]=='a':
                await msg.edit(content='Killer('+killer+') decided to __attack__ while '+survivor+' decided to __run away__ but failed.\n:crown: **'+ctx.author.name+'** won :crown:')
            else:
                await msg.edit(content='Killer('+killer+') accidently droppped his knife.'+survivor+' grabbed it and tried to attack him but suddendly police arrived and suspected '+survivor+' as murderer.\n:crown: **'+ctx.author.name+'** won :crown:')
        if ctx.author.id in command_usage:
            command_usage.remove(ctx.author.id)
        if arg1._user.id in command_usage:
            command_usage.remove(arg1._user.id)
    else:
        command_usage.append(ctx.author.id)
        await ctx.send('Do you want to play as `killer/k` or `survivors/s` ?')
        t2=0
        try:
            while 1:
                t1=time.time()
                msg = await client.wait_for('message',check=check(ctx.author),timeout=30-t2)
                if msg.content.lower()=='k' or msg.content.lower()=='killer':
                    flag=1
                    break
                elif msg.content.lower() == 's' or msg.content.lower()=='survivor' or msg.content.lower()=='survivors':
                    flag=2
                    break
                elif msg.content.lower()=='exit':
                    await msg.add_reaction('\N{OCTAGONAL SIGN}')
                    flag=0
                    break
                t2+=int(time.time()-t1)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention+" didn't replied,aborted.")
            command_usage.remove(ctx.author.id)
            return
        if flag==0:
            command_usage.remove(ctx.author.id)
            return
        if flag==1:
            characters = ['🧛', '🧙', '<:detective:854262739928612894>', '🧝', '🧟', '🥷']
            def check1(reaction, user):
                return (user.id == ctx.author.id) and (str(reaction.emoji) in characters or str(reaction.emoji)=='❌')
            def check3(reaction, user):
                return (user.id == ctx.author.id ) and (reaction.emoji=='🏃' or reaction.emoji=='🔪')
            flag = 0
            pos = 0
            killer = random.choice(characters)
            random.shuffle(characters)
            for r in characters:
                if r == killer:
                    break
                pos += 1
            string = "\n**__NIGHT 1__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[0] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_lower_left::black_large_square::arrow_lower_right::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[1] + ':black_large_square::black_large_square::black_large_square:' + characters[2] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::black_large_square::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[3] + ':black_large_square::black_large_square::black_large_square:' + characters[4] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_upper_left::black_large_square::arrow_upper_right::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[5] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n"+ctx.author.mention+",your killer character is "+killer+".\n\n:small_blue_diamond: **SURVIVORS REMAINING** : 5/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text=ctx.author.name + ',react the person whom you want to kill.(only in adjacent or opposite corner)')
            string1 = await ctx.send(embed=embed)
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep " + ctx.author.mention + ".")
                    flag = -1
                    break
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aborted.')
                        flag = -1
                        break
                    if (pos == 0 or pos == 3 or pos == 4) and str(reaction.emoji) in [characters[1], characters[2],characters[5]]:
                        suspect=random.choice([characters[0],characters[3],characters[4]])
                        break
                    elif (pos == 1 or pos == 2 or pos == 5) and str(reaction.emoji) in [characters[0], characters[3],characters[4]]:
                        suspect = random.choice([characters[1], characters[2], characters[5]])
                        break
                    await string1.remove_reaction(reaction.emoji, ctx.author)
            if flag == -1:
                command_usage.remove(ctx.author.id)
                return
            pos = 0
            for c in characters:
                if c == str(reaction.emoji):
                    characters[pos] = ':skull:'
                    break
                pos += 1
            string = "\n**__NIGHT 1__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[0] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_lower_left::black_large_square::arrow_lower_right::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[1] + ':black_large_square::black_large_square::black_large_square:' + characters[2] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::black_large_square::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[3] + ':black_large_square::black_large_square::black_large_square:' + characters[4] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_upper_left::black_large_square::arrow_upper_right::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[5] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n" + str(reaction.emoji) + " was killed!\n\n:small_blue_diamond: **SURVIVORS REMAINING** : 4/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            await string1.edit(embed=embed)
            characters.remove(':skull:')
            if suspect==killer:
                await ctx.send('Survivors decided to eliminate '+suspect+' (and he was **the killer**)\n:crown: **TEKO** won:crown:')
                command_usage.remove(ctx.author.id)
                return
            else:
                await ctx.send('Survivors decided to eliminate ' + suspect + ' (but he was **not the killer**)')
            characters.remove(suspect)
            random.shuffle(characters)
            string = "\n**__NIGHT 2__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[0] + ':left_right_arrow:' + characters[1] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[2] + ':left_right_arrow:' + characters[3] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 3/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text=ctx.author.name + ',react the person whom you want to kill.(only in adjacent or opposite corner)')
            string1 = await ctx.send(embed=embed)
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep " + ctx.author.mention + ".")
                    flag = -1
                    break
                else:
                    if str(reaction.emoji) == '❌':
                        await ctx.send('aborted.')
                        flag = -1
                        break
                    elif str(reaction.emoji) != killer:
                        break
                await string1.remove_reaction(reaction.emoji, ctx.author)
            if flag == -1:
                command_usage.remove(ctx.author.id)
                return
            pos = 0
            for c in characters:
                if c == str(reaction.emoji):
                    characters[pos] = ':skull:'
                    break
                pos += 1
            string = "\n**__NIGHT 2__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[0] + ':left_right_arrow:' + characters[1] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[2] + ':left_right_arrow:' + characters[3] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n" + str(reaction.emoji) + " was killed!\n\n:small_blue_diamond: **SURVIVORS REMAINING** : 2/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            await string1.edit(embed=embed)
            characters.remove(':skull:')
            suspect=random.choice(characters)
            if suspect==killer:
                await ctx.send('Survivors decided to eliminate '+suspect+' (and he was **the killer**)\n:crown: **TEKO** won:crown:')
                command_usage.remove(ctx.author.id)
                return
            else:
                await ctx.send('Survivors decided to eliminate ' + suspect + ' (but he was **not the killer**)')
            characters.remove(suspect)
            random.shuffle(characters)
            string = "\n**__NIGHT 3__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[0] + ':left_right_arrow:' + characters[1] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 1/5"
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text=ctx.author.name+",what will you do? 'run away' or 'attack'.")
            string1=await ctx.send(embed=embed)
            for emoji in ['🏃','🔪']:
                await string1.add_reaction(emoji)
            try:
                reaction, user = await client.wait_for('reaction_add', check=check3, timeout=30)
            except asyncio.TimeoutError:
                await msg.edit(content="looks like the killer ran away.\n:crown: **TEKO** won :crown:")
                command_usage.remove(ctx.author.id)
                return
            if characters[0]==killer:
                survivor=characters[1]
            else:
                survivor=characters[0]
            choice2=random.choice(['🔪','🏃'])
            if str(reaction.emoji) == choice2:
                if choice2 == '🔪':
                    await ctx.send("Killer(" + killer + ") decided to __attack__ ,but " + survivor + " somehow managed to snatch his knife and killed him.\n:crown: **TEKO** won :crown:")
                else:
                    await ctx.send("Killer (" + killer + ") accidently lost his knife.Both decided to __run away__,but killer got caught by police.\n:crown: **TEKO** won :crown:")
            elif choice2 == '🔪':
                await ctx.send('Killer(' + killer + ') decided to __attack__ while ' + survivor + ' decided to __run away__ but failed.\n:crown: **' + ctx.author.name + '** won :crown:')
            else:
                await ctx.send('Killer(' + killer + ') accidently droppped his knife.' + survivor + ' grabbed it and tried to attack him but suddendly police arrived and suspected ' + survivor + ' as murderer.\n:crown: **' + ctx.author.name + '** won :crown:')
        else:
            characters = ['🧛', '🧙', '<:detective:854262739928612894>', '🧝', '🧟', '🥷']
            def check1(reaction, user):
                return (user.id == ctx.author.id) and (str(reaction.emoji) in characters or str(reaction.emoji)=='❌')
            def check3(reaction, user):
                return (user.id == ctx.author.id) and (reaction.emoji == '🏃' or reaction.emoji == '🔪')
            flag = 0
            pos = 0
            killer = random.choice(characters)
            random.shuffle(characters)
            for r in characters:
                if r == killer:
                    break
                pos += 1
            string = "\n**__NIGHT 1__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[0] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_lower_left::black_large_square::arrow_lower_right::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[1] + ':black_large_square::black_large_square::black_large_square:' + characters[2] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::black_large_square::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[3] + ':black_large_square::black_large_square::black_large_square:' + characters[4] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_upper_left::black_large_square::arrow_upper_right::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[5] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 5/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            string1 = await ctx.send(embed=embed)
            time.sleep(2)
            if (pos == 0 or pos == 3 or pos == 4):
                killed=random.choice([characters[1], characters[2],characters[5]])
            elif (pos == 1 or pos == 2 or pos == 5):
                killed=random.choice([characters[0], characters[3],characters[4]])
            pos = 0
            for c in characters:
                if c == killed:
                    characters[pos] = ':skull:'
                    break
                pos += 1
            string = "\n**__NIGHT 1__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[0] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_lower_left::black_large_square::arrow_lower_right::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[1] + ':black_large_square::black_large_square::black_large_square:' + characters[2] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::black_large_square::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[3] + ':black_large_square::black_large_square::black_large_square:' + characters[4] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::arrow_upper_left::black_large_square::arrow_upper_right::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square:' + characters[5] + ':black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n" + str(killed) + " was killed!\n\n:small_blue_diamond: **SURVIVORS REMAINING** : 4/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text=ctx.author.name+',react the person you find suspicious.')
            await string1.edit(embed=embed)
            characters.remove(':skull:')
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep ,"+ctx.author.mention)
                    flag = -1
                    break
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aborted.')
                        flag = -1
                    elif reaction.emoji == killer:
                        await ctx.send('survivors decided to eliminate ' + str(reaction.emoji) + ' (and he was **the killer**)\n:crown: **'+ctx.author.name+'** won:crown:')
                        flag = -1
                    else:
                        await ctx.send('survivors decided to eliminate ' + str(reaction.emoji) + ' (but he was **not the killer**)')
                    break
            if flag == -1:
                command_usage.remove(ctx.author.id)
                return
            characters.remove(str(reaction.emoji))
            random.shuffle(characters)
            string = "\n**__NIGHT 2__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[0] + ':left_right_arrow:' + characters[1] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[2] + ':left_right_arrow:' + characters[3] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 3/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            string1 = await ctx.send(embed=embed)
            killed=killer
            while killed==killer:
                killed=random.choice(characters)
            time.sleep(2)
            pos = 0
            for c in characters:
                if c == killed:
                    characters[pos] = ':skull:'
                    break
                pos += 1
            string = "\n**__NIGHT 2__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[0] + ':left_right_arrow:' + characters[1] + ':black_large_square:\n'
            string += ':black_large_square::arrow_up_down::black_large_square::arrow_up_down::black_large_square:\n'
            string += ':black_large_square:' + characters[2] + ':left_right_arrow:' + characters[3] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n"+killed+" was killed!\n\n:small_blue_diamond: **SURVIVORS REMAINING** : 3/5\n:small_blue_diamond: react :x: to abort."
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text=ctx.author.name + ',react the person you find suspicious.')
            await string1.edit(embed=embed)
            characters.remove(':skull:')
            for emoji in characters:
                await string1.add_reaction(emoji)
            await string1.add_reaction('❌')
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep ,"+ctx.author.name)
                    flag = -1
                    break
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aborted.')
                        flag = -1
                    elif reaction.emoji == killer:
                        await ctx.send('survivors decided to eliminate ' + str(reaction.emoji) + ' (and he was **the killer**)\n:crown: **'+ctx.author.name+'** won:crown:')
                        flag = -1
                    else:
                        await ctx.send('survivors decided to eliminate ' + str(reaction.emoji) + ' (but he was **not the killer**)')
                    break
            if flag==-1:
                command_usage.remove(ctx.author.id)
                return
            characters.remove(str(reaction.emoji))
            random.shuffle(characters)
            string = "\n**__NIGHT 3__**\n------------------------------------------------\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:\n'
            string += ':black_large_square:' + characters[0] + ':left_right_arrow:' + characters[1] + ':black_large_square:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:'
            string += "\n------------------------------------------------\n:small_blue_diamond: **SURVIVORS REMAINING** : 1/5"
            embed = discord.Embed(title=':person_running: **SURVIVORS vs KILLER** :knife:', description=string,color=0x7F00FF)
            embed.set_footer(text=ctx.author.name + ",what will you do? 'run away' or 'attack'.")
            string1 = await ctx.send(embed=embed)
            for emoji in ['🏃', '🔪']:
                await string1.add_reaction(emoji)
            try:
                reaction, user = await client.wait_for('reaction_add', check=check3, timeout=30)
            except asyncio.TimeoutError:
                await msg.edit(content="looks like the last survivor already got killed.\n:crown: **TEKO** won :crown:")
                command_usage.remove(ctx.author.id)
                return
            if characters[0] == killer:
                survivor = characters[1]
            else:
                survivor = characters[0]
            choice2 = random.choice(['🔪', '🏃'])
            if str(reaction.emoji) == choice2:
                if choice2 == '🔪':
                    await ctx.send("Killer(" + killer + ") decided to __attack__ ,but " + survivor + " somehow managed to snatch his knife and killed him.\n:crown: **"+ctx.author.name+"** won :crown:")
                else:
                    await ctx.send("Killer (" + killer + ") accidently lost his knife.Both decided to __run away__,but killer got caught by police.\n:crown: **"+ctx.author.name+"** won :crown:")
            elif choice2 == '🔪':
                await ctx.send('Killer(' + killer + ') decided to __attack__ while ' + survivor + ' decided to __run away__ but failed.\n:crown: **TEKO** won :crown:')
            else:
                await ctx.send('Killer(' + killer + ') accidently droppped his knife.' + survivor + ' grabbed it and tried to attack him but suddendly police arrived and suspected ' + survivor + ' as murderer.\n:crown: **TEKO** won :crown:')
        if ctx.author.id in command_usage:
            command_usage.remove(ctx.author.id)

@client.command()
async def treasurehunt(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
        return
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
        return
    elif arg1==None:
        command_usage.append(ctx.author.id)
        def check1(reaction, user):
            return user.id == ctx.author.id and str(reaction.emoji) in ['⬅️', '➡️', '⬆️', '⬇️', '❌']
        decision=1
        pscore = bscore = pblock = bblock = 0
        maze = []
        for i in range(7):
            for j in range(11):
                maze.append(':blue_square:')
        maze[0] = '<:ship1:854787284012367913>'
        maze[76] = '<:ship2:854786423777001513>'
        ppos = 0
        bpos = 76
        flag = -2
        activity = '**' + ctx.author.name + '** turn:'
        pstring = '<:no_treasure:855123476192821248><:no_treasure:855123476192821248><:no_treasure:855123476192821248>'
        bstring = pstring[:]
        while 1:
            if flag == -2:
                bchoice = ['u', 'd', 'l', 'r']
                index = []
                for i in range(77):
                    index.append(i)
                index.remove(bpos)
                index.remove(ppos)
                treasure = random.choice(index)
                index.remove(treasure)
                cyclone = []
                map = []
                dragon = []
                for i in range(random.randint(2, 3)):
                    cyclone.append(random.choice(index))
                    index.remove(cyclone[i])
                for i in range(random.randint(3, 4)):
                    map.append(random.choice(index))
                    index.remove(map[i])
                for i in range(random.randint(2, 3)):
                    dragon.append(random.choice(index))
                    index.remove(dragon[i])
                it = int(treasure / 11)
                jt = treasure % 11
                flag = 0

            if pblock == 0:
                maze[ppos] = '<:ship1:854787284012367913>'
            if bblock == 0:
                maze[bpos] = '<:ship2:854786423777001513>'
            string = '<:ship1_land:855124044705955901> __' + ctx.author.name + '__ : ' + str(pstring) + '\n<:ship2_land:855123926299574302> __TEKO__ : ' + str(bstring) + '\n\n'
            for i in range(7):
                for j in range(11):
                    string += maze[i * 11 + j]
                string += '\n'
            embed = discord.Embed(title=':pirate_flag: **TREASURE HUNT** :pirate_flag:\n',description=string, color=0x7F00FF)
            embed.add_field(name='OBJECTIVE:',value=':small_blue_diamond: first one to find three treasures win\n:small_blue_diamond: react :x: to abort.\n-------------------------------------\n' + activity,inline=False)
            embed.set_thumbnail(url='https://i.imgur.com/nfcH5mw.png')
            embed.set_footer(text='react specific emoji to move in that direction.')
            if decision == 1 and pscore == 0 and bscore == 0:
                string1 = await ctx.send(embed=embed)
                for emoji in ['⬅️', '➡️', '⬆️', '⬇️', '❌']:
                    await string1.add_reaction(emoji)
            else:
                await string1.edit(embed=embed)
            if bscore == 3 or pscore == 3:
                break
            if decision % 2 != 0 and pblock == 0:
                activity = ''
                while 1:
                    try:
                        reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                    except asyncio.TimeoutError:
                        await ctx.send("looks like you fell asleep," + ctx.author.mention + '.')
                        flag = -1
                        break
                    old_pos = ppos
                    maze[ppos] = ':blue_square:'
                    if reaction.emoji == '❌':
                        await ctx.send('aborted.')
                        flag = -1
                    elif reaction.emoji == '➡️':
                        if ppos in [10, 21, 32, 43, 54, 65, 76]:
                            ppos -= 10
                        else:
                            ppos += 1
                    elif reaction.emoji == '⬅️':
                        if ppos in [0, 11, 22, 33, 44, 55, 66]:
                            ppos += 10
                        else:
                            ppos -= 1
                    elif reaction.emoji == '⬇️':
                        if ppos in range(66, 77):
                            ppos -= 66
                        else:
                            ppos += 11
                    elif reaction.emoji == '⬆️':
                        if ppos in range(0, 10):
                            ppos += 66
                        else:
                            ppos -= 11
                    await string1.remove_reaction(reaction.emoji, ctx.author)
                    if ppos == bpos:
                        ppos = old_pos
                    else:
                        break
                if flag == -1:
                    break
                if ppos in cyclone:
                    pblock = 3
                    bblock = 0
                    activity = '*' + ctx.author.name + ' got stucked in cyclone :cyclone:*'
                    maze[ppos] = '<a:ship1_cyclone:855123637622669352>'
                elif ppos in dragon:
                    pblock = 4
                    bblock = 0
                    activity = '*' + ctx.author.name + ' got caught by sea dragon :dragon:*'
                    maze[ppos] = '<a:ship1_dragon:855123596224757860>'
                elif ppos in map:
                    i = int(ppos / 11)
                    j = ppos % 11
                    map.remove(ppos)
                    if i == it:
                        if j < jt:
                            direction = 'east'
                        else:
                            direction = 'west'
                    elif i < it:
                        if j < jt:
                            direction = 'south-east'
                        elif j > jt:
                            direction = 'south-west'
                        else:
                            direction = 'south'
                    else:
                        if j < jt:
                            direction = 'north-east'
                        elif j > jt:
                            direction = 'north-west'
                        else:
                            direction = 'north'
                    activity = '*' + ctx.author.name + ' found a map piece <:map:854786538175856670>.*'
                    await ctx.author.send('according to map piece <:map:854786538175856670> , treasure is somewhere in ' + direction + '.')
                elif ppos == treasure:
                    pscore += 1
                    flag = -2
                    pstring = ''
                    for i in range(3):
                        if i < pscore:
                            pstring += '<:treasure:855718827220008980>'
                        else:
                            pstring += '<:no_treasure:855123476192821248>'
                    activity = '*' + ctx.author.name + ' found the treasure <:treasure:855718827220008980>*.\n'
                    if pscore == 3:
                        activity += ':crown: **' + ctx.author.name + '** won :crown:'
                        continue
                if bblock > 0:
                    bblock -= 1
                if bblock == 0:
                    activity += '\n**TEKO** turn:'
                else:
                    activity += '\n**' + ctx.author.name + '** turn:'
            elif decision % 2 == 0 and bblock == 0:
                time.sleep(1)
                activity = ''
                while 1:
                    old_pos = bpos
                    maze[bpos] = ':blue_square:'
                    choose=random.choice(bchoice)
                    if choose=='r':
                        if bpos in [10, 21, 32, 43, 54, 65, 76]:
                            bpos -= 10
                        else:
                            bpos += 1
                    elif choose=='l':
                        if bpos in [0, 11, 22, 33, 44, 55, 66]:
                            bpos += 10
                        else:
                            bpos -= 1
                    elif choose=='d':
                        if bpos in range(66, 77):
                            bpos -= 66
                        else:
                            bpos += 11
                    elif choose=='u':
                        if bpos in range(0, 10):
                            bpos += 66
                        else:
                            bpos -= 11
                    if bpos == ppos:
                        bpos = old_pos
                    else:
                        break
                if bpos in cyclone:
                    bblock = 3
                    pblock = 0
                    activity = '*TEKO got stucked in cyclone :cyclone:*'
                    maze[bpos] = '<a:ship2_cyclone:855123690895573023>'
                elif bpos in dragon:
                    bblock = 4
                    pblock = 0
                    activity = '*TEKO got caught by sea dragon :dragon:*'
                    maze[bpos] = '<a:ship2_dragon:855123615431393361>'
                elif bpos in map:
                    i = int(bpos / 11)
                    j = bpos % 11
                    map.remove(bpos)
                    if i == it:
                        if j < jt:
                            bchoice=['r']
                        else:
                            bchoice=['l']
                    elif i < it:
                        if j < jt:
                            bchoice=['r','d']
                        elif j > jt:
                            bchoice=['l','d']
                        else:
                            bchoice=['d']
                    else:
                        if j < jt:
                            bchoice=['u','r']
                        elif j > jt:
                            bchoice=['l','u']
                        else:
                            bchoice=['u']
                    activity = '*TEKO found a map piece <:map:854786538175856670>.*'
                elif bpos == treasure:
                    bscore += 1
                    flag = -2
                    bstring = ''
                    for i in range(3):
                        if i < bscore:
                            bstring += '<:treasure:855718827220008980>'
                        else:
                            bstring += '<:no_treasure:855123476192821248>'
                    activity = '*TEKO found the treasure <:treasure:855718827220008980>*.\n'.format(arg1.display_name)
                    if bscore == 3:
                        activity += ':crown: **TEKO** won :crown:'
                        continue
                if pblock > 0:
                    pblock -= 1
                if pblock == 0:
                    activity += '\n**' + ctx.author.name + '** turn:'
                else:
                    activity += '\n**TEKO** turn:'
            if bblock == 0 and pblock == 0:
                for i in range(7):
                    for j in range(11):
                        if (j + i * 11 == bpos and i * 11 + j + 1 == ppos) or (i * 11 + j == ppos and i * 11 + j + 1 == bpos):
                            flag = 1
                    if flag == 1:
                        break
                if flag != 1:
                    for j in range(11):
                        for i in range(j, j + 66, 11):
                            if (i + j == bpos and i + 11 + j == ppos) or (i + j == ppos and i + j + 11 == bpos):
                                flag = 1
                        if flag == 1:
                            break
                if flag == 1:
                    if random.choice(['p', 'b']) == 'p':
                        activity += '\n:warning: both pirates got into clash and **' + ctx.author.name + '** died :warning:'
                        maze[ppos] = ':blue_square:'
                        ppos = 0
                        time.sleep(1)
                    else:
                        activity += '\n:warning: both pirates got into clash and **TEKO** died :warning:'
                        maze[bpos] = ':blue_square:'
                        bpos = 76
                        time.sleep(1)
                    flag = 0
            decision += 1
        command_usage.remove(ctx.author.id)
        return
    command_usage.append(ctx.author.id)
    command_usage.append(arg1._user.id)
    decision = t2=0
    await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
    try:
        while 1:
            t1 = time.time()
            msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
            if msg.content.lower() == "yes" or msg.content.lower() == "y":
                decision = 1
                break
            elif msg.content.lower() == "no" or msg.content.lower() == "n":
                decision = -1
                await ctx.send('aborted.')
                break
            t2 += int(time.time() - t1)
    except asyncio.TimeoutError:
        await ctx.send("**{}** did'nt replied.".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    if decision!=1:
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    def check1(reaction, user):
        return user.id == ctx.author.id and str(reaction.emoji) in ['⬅️','➡️','⬆️','⬇️','❌']
    def check2(reaction, user):
        return user.id == arg1._user.id and str(reaction.emoji) in ['⬅️','➡️','⬆️','⬇️','❌']
    pscore=bscore=pblock=bblock=0
    maze=[]
    for i in range(7):
        for j in range(11):
            maze.append(':blue_square:')
    maze[0]='<:ship1:854787284012367913>'
    maze[76]='<:ship2:854786423777001513>'
    ppos=0
    bpos=76
    flag=-2
    activity = '**' + ctx.author.name + '** turn:'
    pstring='<:no_treasure:855123476192821248><:no_treasure:855123476192821248><:no_treasure:855123476192821248>'
    bstring=pstring[:]
    while 1:
        if flag==-2:
            index = []
            for i in range(77):
                index.append(i)
            index.remove(bpos)
            index.remove(ppos)
            treasure=random.choice(index)
            index.remove(treasure)
            cyclone=[]
            map=[]
            dragon=[]
            for i in range(random.randint(2,3)):
                cyclone.append(random.choice(index))
                index.remove(cyclone[i])
            for i in range(random.randint(3,4)):
                map.append(random.choice(index))
                index.remove(map[i])
            for i in range(random.randint(2,3)):
                dragon.append(random.choice(index))
                index.remove(dragon[i])
            it = int(treasure / 11)
            jt = treasure % 11
            flag=0

        if pblock==0:
            maze[ppos]='<:ship1:854787284012367913>'
        if bblock==0:
            maze[bpos]='<:ship2:854786423777001513>'
        string=''
        for i in range(7):
            for j in range(11):
                string+=maze[i*11+j]
            string += '\n'
        embed=discord.Embed(title=':pirate_flag: **TREASURE HUNT** :pirate_flag:\n',description='<:ship1_land:855124044705955901> __'+ctx.author.name+'__ : '+str(pstring)+'\n<:ship2_land:855123926299574302> __{}__ : '.format(arg1.display_name)+str(bstring)+'\n\n'+string,color=0x7F00FF)
        embed.add_field(name='OBJECTIVE:',value=':small_blue_diamond: first one to find three treasures win.\n:small_blue_diamond: react :x: to abort.\n-------------------------------------\n'+activity, inline=False)
        embed.set_thumbnail(url='https://i.imgur.com/nfcH5mw.png')
        embed.set_footer(text='react specific emoji to move in that direction.')
        if decision==1 and pscore==0 and bscore==0:
            string1 = await ctx.send(embed=embed)
            for emoji in ['⬅️','➡️','⬆️','⬇️','❌']:
                await string1.add_reaction(emoji)
        else:
            await string1.edit(embed=embed)
        if bscore==3 or pscore==3:
            break
        if decision%2!=0 and pblock==0:
            activity=''
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep,"+ctx.author.mention+'.')
                    flag=-1
                    break
                old_pos=ppos
                maze[ppos]=':blue_square:'
                if reaction.emoji=='❌':
                    await ctx.send('aborted.')
                    flag=-1
                elif reaction.emoji=='➡️':
                    if ppos in [10,21,32,43,54,65,76]:
                        ppos-=10
                    else:
                        ppos+=1
                elif reaction.emoji=='⬅️':
                    if ppos in [0,11,22,33,44,55,66]:
                        ppos+=10
                    else:
                        ppos-=1
                elif reaction.emoji=='⬇️':
                    if ppos in range(66,77):
                        ppos-=66
                    else:
                        ppos+=11
                elif reaction.emoji=='⬆️':
                    if ppos in range(0,10):
                        ppos+=66
                    else:
                        ppos-=11
                await string1.remove_reaction(reaction.emoji, ctx.author)
                if ppos==bpos:
                    ppos=old_pos
                else:
                    break
            if flag==-1:
                break
            if ppos in cyclone:
                pblock=3
                bblock=0
                activity='*'+ctx.author.name+' got stucked in cyclone :cyclone:*'
                maze[ppos]='<a:ship1_cyclone:855123637622669352>'
            elif ppos in dragon:
                pblock=4
                bblock=0
                activity = '*' + ctx.author.name + ' got caught by sea dragon :dragon:*'
                maze[ppos]='<a:ship1_dragon:855123596224757860>'
            elif ppos in map:
                i = int(ppos / 11)
                j = ppos % 11
                map.remove(ppos)
                if i == it:
                    if j<jt:
                        direction='east'
                    else:
                        direction='west'
                elif i<it:
                    if j<jt:
                        direction='south-east'
                    elif j>jt:
                        direction='south-west'
                    else:
                        direction='south'
                else:
                    if j<jt:
                        direction='north-east'
                    elif j>jt:
                        direction='north-west'
                    else:
                        direction='north'
                activity='*'+ctx.author.name+' found a map piece <:map:854786538175856670>.*'
                await ctx.author.send('according to map piece <:map:854786538175856670> , treasure is somewhere in '+direction+'.')
            elif ppos == treasure:
                pscore+=1
                flag=-2
                pstring=''
                for i in range(3):
                    if i<pscore:
                        pstring+='<:treasure:855718827220008980>'
                    else:
                        pstring+='<:no_treasure:855123476192821248>'
                activity='*'+ctx.author.name+' found the treasure <:treasure:855718827220008980>*.\n'
                if pscore==3:
                    activity+=':crown: **'+ctx.author.name+'** won :crown:'
                    continue
            if bblock>0:
                bblock-=1
            if bblock==0:
                activity+='\n**{}** turn:'.format(arg1.display_name)
            else:
                activity += '\n**' + ctx.author.name + '** turn:'
        elif decision%2==0 and bblock==0:
            activity=''
            while 1:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check2, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep,{}.".format(arg1.mention))
                    flag=-1
                    break
                old_pos=bpos
                maze[bpos]=':blue_square:'
                if reaction.emoji=='❌':
                    await ctx.send('aborted.')
                    flag=-1
                elif reaction.emoji=='➡️':
                    if bpos in [10,21,32,43,54,65,76]:
                        bpos-=10
                    else:
                        bpos+=1
                elif reaction.emoji=='⬅️':
                    if bpos in [0,11,22,33,44,55,66]:
                        bpos+=10
                    else:
                        bpos-=1
                elif reaction.emoji=='⬇️':
                    if bpos in range(66,77):
                        bpos-=66
                    else:
                        bpos+=11
                elif reaction.emoji=='⬆️':
                    if bpos in range(0,10):
                        bpos+=66
                    else:
                        bpos-=11
                await string1.remove_reaction(reaction.emoji, arg1._user)
                if bpos==ppos:
                    bpos=old_pos
                else:
                    break
            if flag==-1:
                break
            if bpos in cyclone:
                bblock=3
                pblock=0
                activity='*{} got stucked in cyclone :cyclone:*'.format(arg1.display_name)
                maze[bpos]='<a:ship2_cyclone:855123690895573023>'
            elif bpos in dragon:
                bblock=4
                pblock=0
                activity = '*{} got caught by sea dragon :dragon:*'.format(arg1.display_name)
                maze[bpos]='<a:ship2_dragon:855123615431393361>'
            elif bpos in map:
                i = int(bpos / 11)
                j =bpos % 11
                map.remove(bpos)
                if i == it:
                    if j<jt:
                        direction='east'
                    else:
                        direction='west'
                elif i<it:
                    if j<jt:
                        direction='south-east'
                    elif j>jt:
                        direction='south-west'
                    else:
                        direction='south'
                else:
                    if j<jt:
                        direction='north-east'
                    elif j>jt:
                        direction='north-west'
                    else:
                        direction='north'
                activity='*{} found a map piece .*'.format(arg1.display_name)
                await arg1._user.send('according to map piece <:map:854786538175856670> , treasure is somewhere in '+direction+'.')
            elif bpos == treasure:
                bscore+=1
                flag=-2
                bstring = ''
                for i in range(3):
                    if i < bscore:
                        bstring += '<:treasure:855718827220008980>'
                    else:
                        bstring += '<:no_treasure:855123476192821248>'
                activity='*{} found the treasure <:treasure:855718827220008980>*.\n'.format(arg1.display_name)
                if bscore==3:
                    activity+=':crown: **{}** won :crown:'.format(arg1.display_name)
                    continue
            if pblock>0:
                pblock-=1
            if pblock==0:
                activity+='\n**'+ctx.author.name+'** turn:'
            else:
                activity += '\n**{}** turn:'.format(arg1.display_name)
        if bblock==0 and pblock==0:
            for i in range(7):
                for j in range(11):
                    if (j+i*11 == bpos and i*11+j+1==ppos) or (i*11+j==ppos and i*11+j+1==bpos):
                        flag=1
                if flag==1:
                    break
            if flag!=1:
                for j in range(11):
                    for i in range(j,j+66,11):
                        if (i+j == bpos and i+11+j == ppos) or (i+j == ppos and i+j+11==bpos):
                            flag=1
                    if flag==1:
                        break
            if flag==1:
                if random.choice(['p','b'])=='p':
                    activity+='\n:warning: both pirates got into clash and **'+ctx.author.name+'** died :warning:'
                    maze[ppos]=':blue_square:'
                    ppos=0
                    time.sleep(1)
                else:
                    activity += '\n:warning: both pirates got into clash and **{}** died :warning:'.format(arg1.display_name)
                    maze[bpos] = ':blue_square:'
                    bpos=76
                    time.sleep(1)
                flag=0
        decision+=1
    command_usage.remove(ctx.author.id)
    command_usage.remove(arg1._user.id)

@client.command()
async def bankrob(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
        return
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
        return
    elif arg1==None:
        command_usage.append(ctx.author.id)
        def check1(reaction,user):
            return ctx.author.id==user.id and reaction.emoji in ['🔵','🔴','🟤','🟣','🟢','🟡','❌']
        decision=stage=1
        pscore=tries=0
        while 1:
            if decision==1:
                color = ['🔵', '🔴', '🟤', '🟣', '🟢', '🟡']
                random.shuffle(color)
                color_code = []
                for i in range(4):
                    color_code.append(color[i])
                road = ''
                string="__BANK "+str(stage)+"__\n\n"
                for i in range(12-stage):
                    road+=':bridge_at_night:'
                road += ":police_car:"
                embed=discord.Embed(title=":bank:_"+road,description=string+"react in a particular order to make your 4-space color code."+"\n\n:small_blue_diamond: **"+ctx.author.name+"**'s pocket = "+str(pscore)+" :coin:\n:small_blue_diamond: correct dots in right position - :small_red_triangle:.\n:small_blue_diamond: correct dots in wrong position - :small_red_triangle_down:.\n:small_blue_diamond: react :x: to abort/reveal code.",color=0x7F00FF)
                embed.set_author(name=ctx.author.display_name + ",steal the money before police arrive!", icon_url=ctx.author.avatar_url)
                embed.set_footer(text="guesses made : "+str(decision-1))
                string1=await ctx.send(embed=embed)
                for emoji in ['🔵','🔴','🟤','🟣','🟢','🟡','❌']:
                    await string1.add_reaction(emoji)
            flag=0
            user_code=[]
            while flag!=4:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=180)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep,"+ctx.author.mention+".")
                    flag=-1
                    break
                else:
                    if reaction.emoji =='❌':
                        string='aborted (the code was '
                        for i in range(4):
                            string+=color_code[i]
                        await ctx.send(string+').')
                        flag=-1
                        break
                    elif reaction.emoji in ['🔵','🔴','🟤','🟣','🟢','🟡'] and reaction.emoji not in user_code:
                        user_code.append(str(reaction.emoji))
                        string+=str(reaction.emoji)
                        flag+=1
                        embed = discord.Embed(title=":bank:_"+road,description=string + "\n\n:small_blue_diamond: **"+ctx.author.name+"**'s pocket = "+str(pscore)+" :coin:\n:small_blue_diamond: correct dots in right position - :small_red_triangle:.\n:small_blue_diamond: correct dots in wrong position - :small_red_triangle_down:.\n:small_blue_diamond: react :x: to abort/reveal code.",color=0x7F00FF)
                        embed.set_author(name=ctx.author.display_name + ",steal the money before police arrive!",icon_url=ctx.author.avatar_url)
                        embed.set_footer(text="guesses made : " + str(decision - 1))
                        await string1.edit(embed=embed)
            if flag==-1:
                break
            string+='  ------>  '
            for i in range(4):
                if color_code[i]==user_code[i]:
                    string+=':small_red_triangle:'
                elif user_code[i] in color_code:
                    flag+=1
            for i in range(4,flag):
                string+=':small_red_triangle_down:'
            string+='\n'
            if user_code==color_code:
                if decision==1:
                    score=500000
                else:
                    score=1.90+0.10*decision
                    score=int(100/score)*random.randint(9990-decision*818,10000-decision*818)
                string+="\n**"+ctx.author.name+"** successfully break into the vault and robbed  "+str(score)+" :coin:."
                pscore+=score
            decision+=1
            road=''
            for i in range(13-stage):
                if i==13-decision-stage:
                    road+=':police_car:'
                else:
                    road += ':bridge_at_night:'
            embed = discord.Embed(title=":bank:_"+road,description=string + "\n\n:small_blue_diamond: **"+ctx.author.name+"**'s pocket = "+str(pscore)+" :coin:\n:small_blue_diamond: correct dots in right position - :small_red_triangle:.\n:small_blue_diamond: correct dots in wrong position - :small_red_triangle_down:.\n:small_blue_diamond: react :x: to abort/reveal code.",color=0x7F00FF)
            embed.set_author(name=ctx.author.display_name + ",steal the money before police arrive!",icon_url=ctx.author.avatar_url)
            embed.set_footer(text="guesses made : " + str(decision - 1))
            await string1.edit(embed=embed)
            if user_code==color_code:
                tries+=decision
                decision=1
                stage+=1
            elif 13-decision-stage==0:
                embed=discord.embed(title=":rotating_light: **"+ctx.author.name+"** got arrested for bank robbery :rotating_light:.\n__**GAME OVER!**__",description=":small_blue_diamond: Bank robbed : "+str(stage)+"\n:small_bllue_diamond: Money stole : "+str(pscore)+" :coin:\n:small_blue_diamond: total tries : "+str(tries))
                embed.set_author(name=ctx.author.display_name + "'s bankrob",icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                break
            for emoji in user_code:
                await string1.remove_reaction(emoji,ctx.author)
        command_usage.remove(ctx.author.id)
        return
    command_usage.append(ctx.author.id)
    command_usage.append(arg1._user.id)
    decision = t2 = 0
    await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
    try:
        while 1:
            t1 = time.time()
            msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
            if msg.content.lower() == "yes" or msg.content.lower() == "y":
                decision = 1
                break
            elif msg.content.lower() == "no" or msg.content.lower() == "n":
                decision = -1
                await ctx.send('aborted.')
                break
            t2 += int(time.time() - t1)
    except asyncio.TimeoutError:
        await ctx.send("**{}** did'nt replied.".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    if decision != 1:
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    def check1(reaction, user):
        return ctx.author.id == user.id and reaction.emoji in ['🔵', '🔴', '🟤', '🟣', '🟢', '🟡', '❌']
    def check2(reaction, user):
        return arg1._user.id == user.id and reaction.emoji in ['🔵', '🔴', '🟤', '🟣', '🟢', '🟡', '❌']
    stage=1
    pscore=bscore=0
    while 1:
        flag = 0
        user_code = []
        if decision==1:
            color = ['🔵', '🔴', '🟤', '🟣', '🟢', '🟡']
            random.shuffle(color)
            color_code = []
            for i in range(4):
                color_code.append(color[i])
        if decision%2!=0:
            if decision == 1:
                road=''
                string = "__BANK "+str(stage)+"__ : :lock::lock::lock::lock:\n\n"
                for i in range(12-stage):
                    road+=':bridge_at_night:'
                road += ":police_car:"
                embed = discord.Embed(title=":bank:_"+road,description=string+"react in a particular order to make your 4-space color code." + "\n\n:small_blue_diamond: **"+ctx.author.name+"**'s pocket = "+str(pscore)+" :coin:\n:small_blue_diamond: **{}**'s pocket = ".format(arg1.display_name)+str(bscore)+" :coin:\n:small_blue_diamond: correct dots in right position - :small_red_triangle:.\n:small_blue_diamond: correct dots in wrong position - :small_red_triangle_down:.\n:small_blue_diamond: react :x: to abort/reveal code.",color=0x7F00FF)
                embed.set_footer(text=ctx.author.name+" turn:")
                string1 = await ctx.send(embed=embed)
                for emoji in ['🔵', '🔴', '🟤', '🟣', '🟢', '🟡', '❌']:
                    await string1.add_reaction(emoji)
            while flag != 4:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check1, timeout=180)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep," + ctx.author.mention + ".")
                    flag = -1
                    break
                else:
                    if reaction.emoji == '❌':
                        string = 'aborted (the code was '
                        for i in range(4):
                            string += color_code[i]
                        await ctx.send(string + ').')
                        flag = -1
                        break
                    elif reaction.emoji in ['🔵', '🔴', '🟤', '🟣', '🟢', '🟡'] and reaction.emoji not in user_code:
                        user_code.append(str(reaction.emoji))
                        string += str(reaction.emoji)
                        flag += 1
                        embed = discord.Embed(title=":bank:_"+road+":police_car:",description=string + "\n\n:small_blue_diamond: **"+ctx.author.name+"**'s pocket = "+str(pscore)+" :coin:\n:small_blue_diamond: **{}**'s pocket = ".format(arg1.display_name)+str(bscore)+" :coin:\n:small_blue_diamond: correct dots in right position - :small_red_triangle:.\n:small_blue_diamond: correct dots in wrong position - :small_red_triangle_down:.\n:small_blue_diamond: react :x: to abort/reveal code.",color=0x7F00FF)
                        embed.set_footer(text=ctx.author.name+" turn:")
                        await string1.edit(embed=embed)
        else:
            while flag != 4:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check2, timeout=180)
                except asyncio.TimeoutError:
                    await ctx.send("looks like you fell asleep,{}.".format(arg1.mention))
                    flag = -1
                    break
                else:
                    if reaction.emoji == '❌':
                        string = 'aborted (the code was '
                        for i in range(4):
                            string += color_code[i]
                        await ctx.send(string + ').')
                        flag = -1
                        break
                    elif reaction.emoji in ['🔵', '🔴', '🟤', '🟣', '🟢', '🟡'] and reaction.emoji not in user_code:
                        user_code.append(str(reaction.emoji))
                        string += str(reaction.emoji)
                        flag += 1
                        embed = discord.Embed(title=":bank:_"+road+":police_car:",description=string + "\n\n:small_blue_diamond: **"+ctx.author.name+"**'s pocket = "+str(pscore)+" :coin:\n:small_blue_diamond: **{}**'s pocket = ".format(arg1.display_name)+str(bscore)+" :coin:\n:small_blue_diamond: correct dots in right position - :small_red_triangle:.\n:small_blue_diamond: correct dots in wrong position - :small_red_triangle_down:.\n:small_blue_diamond: react :x: to abort/reveal code.",color=0x7F00FF)
                        embed.set_footer(text="{} turn:".format(arg1.display_name))
                        await string1.edit(embed=embed)
        if flag == -1:
            break
        string += '  ------>  '
        for i in range(4):
            if color_code[i] == user_code[i]:
                string += ':small_red_triangle:'
            elif user_code[i] in color_code:
                flag += 1
        for i in range(4, flag):
            string += ':small_red_triangle_down:'
        string += '\n'
        if user_code == color_code and decision%2!=0:
            if decision==1:
                score=500000
            else:
                score=2.00+0.10*(int(decision/2))
                score=int(100/score)*random.randint(9990-decision*818,10000-decision*818)
            string+="\n**"+ctx.author.name+"** successfully break into the vault and robbed "+str(score)+" :coin:."
            pscore+=score
        elif user_code == color_code:
            if decision==1:
                score=500000
            else:
                score=1.90+0.10*(int(decision/2))
                score=int(100/score)*random.randint(9990-decision*818,10000-decision*818)
            string+="\n**{}** successfully break into the vault and robbed ".format(arg1.display_name)+str(score)+" :coin:."
            bscore+=score
        road = ''
        for i in range(13 - stage):
            if i == 13 - decision - stage:
                road += ':police_car:'
            else:
                road += ':bridge_at_night:'
        embed = discord.Embed(title=":bank:_"+road+":police_car:",description=string + "\n\n:small_blue_diamond: **"+ctx.author.name+"**'s pocket = "+str(pscore)+" :coin:\n:small_blue_diamond: **{}**'s pocket = ".format(arg1.display_name)+str(bscore)+" :coin:\n:small_blue_diamond: correct dots in right position - :small_red_triangle:.\n:small_blue_diamond: correct dots in wrong position - :small_red_triangle_down:.\n:small_blue_diamond: react :x: to abort/reveal code.",color=0x7F00FF)
        if decision%2!=0:
            embed.set_footer(text="{} turn:".format(arg1.display_name))
        else:
            embed.set_footer(text=ctx.author.name + " turn:")
        await string1.edit(embed=embed)
        if user_code == color_code:
            time.sleep(1)
            decision=1
            stage+=1
        elif 13 - stage - decision == 0:
            if pscore>bscore:
                await ctx.send("**GAME OVER!**\n:crown: **"+ctx.author.name+"** won :crown:")
            elif pscore<bscore:
                await ctx.send("**GAME OVER!**\n:crown: **{}** won :crown:".format(arg1.display_name))
            else:
                await ctx.send("**GAME OVER!**\nIt was a tie.")
            break
        elif decision % 2 == 0:
            for emoji in user_code:
                await string1.remove_reaction(emoji, arg1._user)
            decision+=1
        else:
            for emoji in user_code:
                await string1.remove_reaction(emoji, ctx.author)
            decision+=1
    command_usage.remove(ctx.author.id)
    command_usage.remove(arg1._user.id)

@client.command()
async def sos(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
        return
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
        return
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko sos @user`',color=0x7F00FF))
        return
    command_usage.append(ctx.author.id)
    command_usage.append(arg1._user.id)
    decision = t2=0
    await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
    try:
        while 1:
            t1=time.time()
            msg = await client.wait_for('message', check=check(arg1._user), timeout=30-t2)
            if msg.content.lower() == "yes" or msg.content.lower() == "y":
                decision = 1
                break
            elif msg.content.lower() == "no" or msg.content.lower() == "n":
                decision = -1
                break
            t2+=int(time.time()-t1)
    except asyncio.TimeoutError:
        await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    if decision == -1:
        await ctx.send("terminated.")
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    win={1:[0,2],2:[1,3],3:[2,4],5:[0,10],9:[4,14],10:[5,15],14:[9,19],15:[10,20],19:[14,24],21:[20,22],22:[21,23],23:[22,24]}
    for i in [6,7,8,11,12,13,16,17,18]:
        win[i]=[i-1,i+1,i-5,i+5,i-6,i+6,i-4,i+4]
    maze=[]
    o=[]
    spot=[]
    for i in range(25):
        maze.append(":black_large_square:")
        spot.append(i)
    decision=1
    flag=0
    while 1:
        string = ":blue_square::one::two::three::four::five:\n"
        for i in range(5):
            if i == 0:
                string += ':one:'
            elif i == 1:
                string += ':two:'
            elif i == 2:
                string += ':three:'
            elif i == 3:
                string += ':four:'
            else:
                string += ':five:'
            for j in range(5):
                string += maze[5 * i + j]
            string += '\n'
        if decision%2!=0 and flag==1:
            string+="\n\n:crown: {} won :crown:".format(arg1.display_name)
        elif flag==1:
            string+="\n\n:crown: "+ctx.author.name+" won :crown:"
        elif len(spot)==0:
            string+='\n\ntie.'
            flag=1
        if decision%2!=0:
            embed = discord.Embed(title="**" + ctx.author.name + "** turn:", description=string, color=0x7F00FF)
        else:
            embed = discord.Embed(title="**{}** turn:".format(arg1.display_name), description=string, color=0x7F00FF)
        embed.set_author(name='first one to make SOS wins!')
        embed.set_footer(text="type input like 14s,32o,etc | 'exit' to abort.")
        await ctx.send(embed=embed)
        if flag==1:
            break
        flag=t2=0
        if decision%2!=0:
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(ctx.author), timeout=180-t2)
                    msg1=msg.content.lower()
                    if msg.content.lower()=='exit':
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        flag=-1
                        break
                    elif len(msg1)==3 and msg1[0].isnumeric()==True and msg1[1].isnumeric()==True and msg1[2].isalpha()==True and (int(msg1[0]) in range(1,6)) and (int(msg1[1]) in range(1,6)) and (msg1[2] in ['s','o']):
                        if 5*(int(msg1[0])-1)+(int(msg1[1])-1) in spot:
                            if msg1[2]=='s':
                                maze[5*(int(msg1[0])-1)+(int(msg1[1])-1)]=':regional_indicator_s:'
                            else:
                                maze[5 * (int(msg1[0]) - 1) + (int(msg1[1]) - 1)] = ':o:'
                                o.append(5 * (int(msg1[0]) - 1) + (int(msg1[1]) - 1))
                            spot.remove(5 * (int(msg1[0]) - 1) + (int(msg1[1]) - 1))
                            break
                        else:
                            await msg.add_reaction('\N{CROSS MARK}')
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send("looks like you fell asleep,"+ctx.author.mention+".")
                break
            if flag==-1:
                break
        else:
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(arg1._user), timeout=180-t2)
                    msg1=msg.content.lower()
                    if msg.content.lower()=='exit':
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        flag=-1
                        break
                    elif len(msg1)==3 and msg1[0].isnumeric()==True and msg1[1].isnumeric()==True and msg1[2].isalpha()==True and (int(msg1[0]) in range(1,6)) and (int(msg1[1]) in range(1,6)) and (msg1[2] in ['s','o']):
                        if 5*(int(msg1[0])-1)+(int(msg1[1])-1) in spot:
                            if msg1[2]=='s':
                                maze[5*(int(msg1[0])-1)+(int(msg1[1])-1)]=':regional_indicator_s:'
                            else:
                                maze[5 * (int(msg1[0]) - 1) + (int(msg1[1]) - 1)] = ':o:'
                                o.append(5 * (int(msg1[0]) - 1) + (int(msg1[1]) - 1))
                            spot.remove(5 * (int(msg1[0]) - 1) + (int(msg1[1]) - 1))
                            break
                        else:
                            await msg.add_reaction('\N{CROSS MARK}')
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send("looks like you fell asleep,{}.".format(arg1.mention))
                break
            if flag==-1:
                break
        for pos in o:
            for key in win.keys():
                if key==pos:
                    for i in range(0, len(win[key]), 2):
                        if maze[win[key][i]]==':regional_indicator_s:' and maze[win[key][i+1]]==':regional_indicator_s:':
                            flag=1
                            break
                    if flag==1:
                        break
            if flag==1:
                break
        decision+=1
    command_usage.remove(ctx.author.id)
    command_usage.remove(arg1._user.id)

@client.command()
async def battleship(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
        return
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
        return
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko battleship @user`',color=0x7F00FF))
        return
    command_usage.append(ctx.author.id)
    command_usage.append(arg1._user.id)
    decision = t2=0
    await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
    try:
        while 1:
            t1=time.time()
            msg = await client.wait_for('message', check=check(arg1._user), timeout=30-t2)
            if msg.content.lower() == "yes" or msg.content.lower() == "y":
                decision = 1
                break
            elif msg.content.lower() == "no" or msg.content.lower() == "n":
                decision = -1
                break
            t2+=int(time.time()-t1)
    except asyncio.TimeoutError:
        await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    if decision == -1:
        await ctx.send("terminated.")
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    for k in range(2):
        pos=[]
        carrier_pos_hori=[]
        battleship_pos_hori=[]
        battleship_pos_vert=[]
        carrier_pos_vert=[]
        cruiser_pos_vert=[]
        cruiser_pos_hori=[]
        for i in range(10):
            for j in range(10):
                pos.append(10*i+j)
                if j in range(6):
                    carrier_pos_hori.append(10*i+j)
                    battleship_pos_hori.append(10*i+j)
                if j==6:
                    battleship_pos_hori.append(10 * i + j)
                if i in range(6):
                    carrier_pos_vert.append(10*i+j)
                    battleship_pos_vert.append(10 * i + j)
                if i==6:
                    battleship_pos_vert.append(10 * i + j)
                if i!=9 and i!=8:
                    cruiser_pos_vert.append(10*i+j)
                if j!=9 and j!=8:
                    cruiser_pos_hori.append(10 * i + j)

        carrier=[]
        battleship1=[]
        battleship2=[]
        cruiser1=[]
        cruiser2=[]
        cruiser3=[]
        submarine1=[]
        submarine2=[]
        submarine3=[]
        submarine4=[]
        direction=random.choice(['h','v'])
        if direction=='h':
            spot=random.choice(carrier_pos_hori)
            for i in [spot,spot+1,spot+2,spot+3,spot+4]:
                carrier.append(i)
                for j in [battleship_pos_hori,battleship_pos_vert,cruiser_pos_vert,cruiser_pos_hori,pos]:
                    if i in j:
                        j.remove(i)
        else:
            spot = random.choice(carrier_pos_vert)
            for i in [spot, spot + 10,spot + 20,spot + 30, spot + 40]:
                carrier.append(i)
                for j in [battleship_pos_hori,battleship_pos_vert,cruiser_pos_vert,cruiser_pos_hori,pos]:
                    if i in j:
                        j.remove(i)
        direction=random.choice(['h','v'])
        if direction=='h':
            while 1:
                spot=random.choice(battleship_pos_hori)
                for i in [spot,spot+1,spot+2,spot+3]:
                    if i in carrier:
                        i=-1
                        break
                    else:
                        battleship1.append(i)
                battleship_pos_hori.remove(spot)
                if i==-1:
                    battleship1=[]
                    continue
                else:
                    break
        else:
            while 1:
                spot=random.choice(battleship_pos_vert)
                for i in [spot,spot+10,spot+20,spot+30]:
                    if i in carrier:
                        i=-1
                        break
                    else:
                        battleship1.append(i)
                battleship_pos_vert.remove(spot)
                if i==-1:
                    battleship1=[]
                    continue
                else:
                    break
        for i in battleship1:
            for j in [battleship_pos_hori,battleship_pos_vert,cruiser_pos_vert,cruiser_pos_hori,pos]:
                if i in j:
                    j.remove(i)
        direction = random.choice(['h', 'v'])
        if direction == 'h':
            while 1:
                spot = random.choice(battleship_pos_hori)
                for i in [spot, spot + 1, spot + 2, spot + 3]:
                    for j in [carrier,battleship1]:
                        if i in j:
                            i = -1
                            break
                    if i==-1:
                        break
                    else:
                        battleship2.append(i)
                battleship_pos_hori.remove(spot)
                if i == -1:
                    battleship2 = []
                    continue
                else:
                    break
        else:
            while 1:
                spot = random.choice(battleship_pos_vert)
                for i in [spot, spot + 10, spot + 20, spot + 30]:
                    for j in [carrier,battleship1]:
                        if i in j:
                            i = -1
                            break
                    if i==-1:
                        break
                    else:
                        battleship2.append(i)
                battleship_pos_vert.remove(spot)
                if i == -1:
                    battleship2 = []
                    continue
                else:
                    break
        for i in battleship2:
            for j in [cruiser_pos_vert,cruiser_pos_hori,pos]:
                if i in j:
                    j.remove(i)
        direction = random.choice(['h', 'v'])
        if direction == 'h':
            while 1:
                spot = random.choice(cruiser_pos_hori)
                for i in [spot, spot + 1, spot + 2]:
                    for j in [carrier,battleship1,battleship2]:
                        if i in j:
                            i = -1
                            break
                    if i==-1:
                        break
                    else:
                        cruiser1.append(i)
                cruiser_pos_hori.remove(spot)
                if i == -1:
                    cruiser1 = []
                    continue
                else:
                    break
        else:
            while 1:
                spot = random.choice(cruiser_pos_vert)
                for i in [spot, spot + 10, spot + 20]:
                    for j in [carrier,battleship1,battleship2]:
                        if i in j:
                            i = -1
                            break
                    if i==-1:
                        break
                    else:
                        cruiser1.append(i)
                cruiser_pos_vert.remove(spot)
                if i == -1:
                    cruiser1 = []
                    continue
                else:
                    break
        for i in cruiser1:
            for j in [cruiser_pos_vert,cruiser_pos_hori,pos]:
                if i in j:
                    j.remove(i)
        direction = random.choice(['h', 'v'])
        if direction == 'h':
            while 1:
                spot = random.choice(cruiser_pos_hori)
                for i in [spot, spot + 1, spot + 2]:
                    for j in [carrier, battleship1, battleship2,cruiser1]:
                        if i in j:
                            i = -1
                            break
                    if i == -1:
                        break
                    else:
                        cruiser2.append(i)
                cruiser_pos_hori.remove(spot)
                if i == -1:
                    cruiser2 = []
                    continue
                else:
                    break
        else:
            while 1:
                spot = random.choice(cruiser_pos_vert)
                for i in [spot, spot + 10, spot + 20]:
                    for j in [carrier, battleship1, battleship2,cruiser1]:
                        if i in j:
                            i = -1
                            break
                    if i == -1:
                        break
                    else:
                        cruiser2.append(i)
                cruiser_pos_vert.remove(spot)
                if i == -1:
                    cruiser2 = []
                    continue
                else:
                    break
        for i in cruiser2:
            for j in [cruiser_pos_vert,cruiser_pos_hori,pos]:
                if i in j:
                    j.remove(i)
        direction = random.choice(['h', 'v'])
        if direction == 'h':
            while 1:
                spot = random.choice(cruiser_pos_hori)
                for i in [spot, spot + 1, spot + 2]:
                    for j in [carrier, battleship1, battleship2, cruiser1,cruiser2]:
                        if i in j:
                            i = -1
                            break
                    if i == -1:
                        break
                    else:
                        cruiser3.append(i)
                cruiser_pos_hori.remove(spot)
                if i == -1:
                    cruiser3 = []
                    continue
                else:
                    break
        else:
            while 1:
                spot = random.choice(cruiser_pos_vert)
                for i in [spot, spot + 10, spot + 20]:
                    for j in [carrier, battleship1, battleship2, cruiser1,cruiser2]:
                        if i in j:
                            i = -1
                            break
                    if i == -1:
                        break
                    else:
                        cruiser3.append(i)
                cruiser_pos_vert.remove(spot)
                if i == -1:
                    cruiser3 = []
                    continue
                else:
                    break
        for i in cruiser3:
            if i in pos:
                pos.remove(i)
        submarine=[]
        for i in range(4):
            submarine.append(random.choice(pos))
            pos.remove(submarine[i])
        powerup = []
        powerup_display=[]
        tier1 = ['bomber', 'radar', 'sea_mine']
        tier2 = ['nukeplane', 'torpedo', 'defense_system']
        if random.randint(1, 101) <= 94:
            length = 2
            t1_chance = 50
            t2_chance = 40
        else:
            length = 3
            t1_chance = 60
            t2_chance = 30
        t3_chance = 10
        chance = random.randint(1, 101)
        if chance < t3_chance:
            powerup.append(random.choice(['striker', 'ufo']))
            if powerup[0] == 'striker':
                powerup_display.append(':helicopter:')
            elif powerup[0] == 'ufo':
                powerup_display.append(':flying_saucer:')
            t3_chance = 0
            t2_chance -= 20
            t1_chance += 30
        elif chance <= t3_chance + t2_chance:
            powerup.append(random.choice(tier2))
            tier2.remove(powerup[0])
            if powerup[0] == 'nukeplane':
                powerup_display.append(':airplane:')
            elif powerup[0] == 'torpedo':
                powerup_display.append('<:torpedo:859668485440405515>')
            elif powerup[0] == 'defense_system':
                powerup_display.append('<:defense_system:858895078532317194>')
            t2_chance -= 4
            t1_chance += 4
        else:
            powerup.append(random.choice(tier1))
            tier1.remove(powerup[0])
            if powerup[0] == 'bomber':
                powerup_display.append(':airplane_small:')
            elif powerup[0] == 'radar':
                powerup_display.append('<:radar:858895009569570847>')
            else:
                powerup_display.append('<:sea_mine:858894878230052884>')
            t2_chance += 8
            t1_chance -= 8
        chance = random.randint(1, 101)
        if chance < t3_chance:
            powerup.append(random.choice(['striker', 'ufo']))
            if powerup[1] == 'striker':
                powerup_display.append(':helicopter:')
            elif powerup[1] == 'ufo':
                powerup_display.append(':flying_saucer:')
            t3_chance = 0
            t2_chance -= 20
            t1_chance += 30
        elif chance <= t3_chance + t2_chance:
            powerup.append(random.choice(tier2))
            tier2.remove(powerup[1])
            if powerup[1] == 'nukeplane':
                powerup_display.append(':airplane:')
            elif powerup[1] == 'torpedo':
                powerup_display.append('<:torpedo:859668485440405515>')
            elif powerup[1] == 'defense_system':
                powerup_display.append('<:defense_system:858895078532317194>')
            t2_chance -= 4
            t1_chance += 4
        else:
            powerup.append(random.choice(tier1))
            tier1.remove(powerup[1])
            if powerup[1] == 'bomber':
                powerup_display.append(':airplane_small:')
            elif powerup[1] == 'radar':
                powerup_display.append('<:radar:858895009569570847>')
            else:
                powerup_display.append('<:sea_mine:858894878230052884>')
            t2_chance += 8
            t1_chance -= 8
        if length == 3:
            chance = random.randint(1, 101)
            if chance < t3_chance:
                powerup.append(random.choice(['striker', 'ufo']))
                if powerup[2] == 'striker':
                    powerup_display.append(':helicopter:')
                elif powerup[2] == 'ufo':
                    powerup_display.append(':flying_saucer:')
            elif chance <= t3_chance + t2_chance:
                powerup.append(random.choice(tier2))
                if powerup[3] == 'nukeplane':
                    powerup_display.append(':airplane:')
                elif powerup[3] == 'torpedo':
                    powerup_display.append('<:torpedo:859668485440405515>')
                elif powerup[3] == 'defense_system':
                    powerup_display.append('<:defense_system:858895078532317194>')
            else:
                powerup.append(random.choice(tier1))
                if powerup[2] == 'bomber':
                    powerup_display.append(':airplane_small:')
                elif powerup[2] == 'radar':
                    powerup_display.append('<:radar:858895009569570847>')
                else:
                    powerup_display.append('<:sea_mine:858894878230052884>')
        if k==0:
            pcarrier=carrier.copy()
            pbattleship1=battleship1.copy()
            pbattleship2 = battleship2.copy()
            pcruiser1=cruiser1.copy()
            pcruiser2 = cruiser2.copy()
            pcruiser3 = cruiser3.copy()
            psubmarine=submarine.copy()
            ppowerup=powerup.copy()
            ppowerup_display=powerup_display.copy()
    bcarrier = carrier.copy()
    bbattleship1 = battleship1.copy()
    bbattleship2 = battleship2.copy()
    bcruiser1 = cruiser1.copy()
    bcruiser2 = cruiser2.copy()
    bcruiser3 = cruiser3.copy()
    bsubmarine = submarine.copy()
    bpowerup = powerup.copy()
    bpowerup_display = powerup_display.copy()
    pblasted=[[],[],[],[],[],[],[]]
    bblasted = [[], [], [], [], [], [], []]
    pmaze=[]
    for i in range(100):
        pmaze.append(':blue_square:')
    bmaze=pmaze.copy()
    fleet1 = [
        '[:white_medium_square::white_medium_square::white_medium_square::white_medium_square::white_medium_square:>',
        '[:white_medium_square::white_medium_square::white_medium_square::white_medium_square:>',
        '[:white_medium_square::white_medium_square::white_medium_square::white_medium_square:>',
        '[:white_medium_square::white_medium_square::white_medium_square:>',
        '[:white_medium_square::white_medium_square::white_medium_square:>',
        '[:white_medium_square::white_medium_square::white_medium_square:>', '[:white_medium_square:>',
        '[:white_medium_square:>', '[:white_medium_square:>', '[:white_medium_square:>']
    fleet2 = fleet1.copy()
    spot={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
    positions=[':regional_indicator_a:',':regional_indicator_b:',':regional_indicator_c:',':regional_indicator_d:',':regional_indicator_e:',':regional_indicator_f:',':regional_indicator_g:',':regional_indicator_h:',':regional_indicator_i:',':regional_indicator_j:']
    # sea mine ---------------------------------------------------------------
    pdefense_line=bdefense_line=-1
    mine_spot=[]
    pmine_spot=[]
    bmine_spot=[]
    for i in range(100):
        mine_spot.append(i)
    random.shuffle(mine_spot)
    if 'sea_mine' in ppowerup:
        pmine_spot.append(mine_spot[0])
        pmine_spot.append(mine_spot[1])
        pmine_spot.append(mine_spot[2])
        pmine_spot.append(mine_spot[3])
    if 'sea_mine' in bpowerup:
        bmine_spot.append(mine_spot[4])
        bmine_spot.append(mine_spot[5])
        bmine_spot.append(mine_spot[6])
        bmine_spot.append(mine_spot[7])
    #defense system-------------------------------------------------------
    if 'defense_system' in ppowerup:
        pdefense_line=random.randint(0,10)
    if 'defense_system' in bpowerup:
        bdefense_line=random.randint(0,10)
    while 1 :
        flag=0
        #p1 turn-------------------------------------------------
        if decision%2!=0:
            string=':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
            for i in range(10):
                string+='\n'+positions[i]
                for j in range(10):
                    string+=bmaze[10*i+j]
            embed = discord.Embed(title=ctx.author.name+" turn:",description=string+'\n:boom: - hit , :x: - miss', color=0x7F00FF)
            embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
            string='**Powerup** : '
            for k in ppowerup_display:
                string+= k
            embed.add_field(name=':ship: '+ctx.author.name+"'s fleet:", value=fleet1[0]+'\n'+fleet1[1]+'\n'+fleet1[2]+'\n'+fleet1[3]+'\n'+fleet1[4]+'\n'+fleet1[5]+'\n'+fleet1[6]+'    '+fleet1[7]+'    '+fleet1[8]+'    '+fleet1[9]+'\n'+string, inline=True)
            string = '**Powerup** : '
            for k in bpowerup_display:
                string += k
            embed.add_field(name=":ship: {}'s fleet:".format(arg1.display_name), value=fleet2[0]+'\n'+fleet2[1]+'\n'+fleet2[2]+'\n'+fleet2[3]+'\n'+fleet2[4]+'\n'+fleet2[5]+'\n'+fleet2[6]+'    '+fleet2[7]+'    '+fleet2[8]+'    '+fleet2[9]+'\n'+string, inline=True)
            embed.set_footer(text="type input like a5,f3,etc | 'exit' to abort.")
            string1=await ctx.send(embed=embed)
            if len(pblasted[0])+len(pblasted[1])+len(pblasted[2])+len(pblasted[3])+len(pblasted[4])+len(pblasted[5])+len(pblasted[6])==26:
                await ctx.send(":crown: **{}** won :crown:".format(arg1.display_name))
                break
            elif len(bblasted[0])+len(bblasted[1])+len(bblasted[2])+len(bblasted[3])+len(bblasted[4])+len(bblasted[5])+len(bblasted[6])==26:
                await ctx.send(":crown: **"+ctx.author.name+"** won :crown:")
                break
            action=''
            t2=0
            try:
                while 1:
                    t1=time.time()
                    msg = await client.wait_for('message', check=check(ctx.author), timeout=120-t2)
                    msg1=msg.content.lower()
                    if msg1=='exit':
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        flag=-1
                        break
                    elif 'radar' in ppowerup and len(msg1)==8 and msg1[:5]=='radar' and msg1[5]==' ' and msg1[6].isalpha()==True and (msg1[6] in ['b','c','d','e','f','g','h','i']) and msg1[7].isnumeric()==True and (int(msg1[7]) in range(2,10)):
                        choice = 10 * spot[msg1[6]] + (int(msg1[7]) - 1)
                        await msg.add_reaction('<:radar:858895009569570847>')
                        action='radar'
                        break
                    elif 'torpedo' in ppowerup and len(msg1)==9 and msg1[:7]=='torpedo' and msg1[7]==' ' and msg1[8].isalpha()==True and (msg1[8] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
                        choice=10*spot[msg1[8]]
                        action = 'torpedo'
                        await msg.add_reaction('<:torpedo:859668485440405515>')
                        break
                    elif msg1 in ppowerup and msg1=='striker':
                        choice=random.choice([44,45,54,55])
                        action = 'striker'
                        await msg.add_reaction('\N{HELICOPTER}')
                        break
                    elif 'ufo' in ppowerup and msg1=='ufo':
                        choice=random.choice([44,45,54,55])
                        action = 'ufo'
                        await msg.add_reaction('🛸')
                        break
                    elif 'nukeplane' in ppowerup and len(msg1)==12 and msg1[:9]=='nukeplane' and msg1[9]==' ' and msg1[10].isalpha()==True and (msg1[10] in ['b','c','d','e','f','g','h','i']) and msg1[11].isnumeric()==True and (int(msg1[11]) in range(2,10)):
                        choice = 10 * spot[msg1[10]] + (int(msg1[11]) - 1)
                        await msg.add_reaction('\N{AIRPLANE}')
                        action='nukeplane'
                        break
                    elif 'bomber' in ppowerup and msg1[:6] == 'bomber' and msg1[6] == ' ':
                        i = j = 7
                        marks = []
                        for alpha in msg1[7:]:
                            if alpha == ' ':
                                marks.append(msg1[i:j])
                                i += len(marks[-1]) + 1
                            j += 1
                        marks.append(msg1[i:j])
                        if len(marks) == 3 and (len(marks[0]) == 2 or len(marks[0]) == 3) and (len(marks[1]) == 2 or len(marks[1]) == 3) and (len(marks[2]) == 2 or len(marks[2]) == 3) and ( marks[0][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and (marks[1][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and (marks[2][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
                            if len(marks[0]) == 2 and marks[0][1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                marks.append(10 * spot[marks[0][0]] + (int(marks[0][1]) - 1))
                            elif len(marks[0]) == 3 and marks[0][1] == '1' and marks[0][2] == '0':
                                marks.append(10 * spot[marks[0][0]] + 9)
                            if len(marks[1]) == 2 and marks[1][1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                marks.append(10 * spot[marks[1][0]] + (int(marks[1][1]) - 1))
                            elif len(marks[1]) == 3 and marks[1][1] == '1' and marks[1][2] == '0':
                                marks.append(10 * spot[marks[1][0]] + 9)
                            if len(marks[2]) == 2 and marks[2][1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                marks.append(10 * spot[marks[2][0]] + (int(marks[2][1]) - 1))
                            elif len(marks[2]) == 3 and marks[2][1] == '1' and marks[2][2] == '0':
                                marks.append(10 * spot[marks[2][0]] + 9)
                            if (marks[3]!=None and marks[4]!=None and marks[5]!=None) and marks[3] in range(0, 99) and marks[4] in range(0, 99) and marks[5] in range(0, 99):
                                action='bomber'
                                break
                    elif len(msg1)==2 and msg1[0].isalpha()==True and msg1[1].isnumeric()==True and (msg1[0] in ['a','b','c','d','e','f','g','h','i','j']) and (int(msg1[1]) in range(1,10)):
                        choice=10*spot[msg1[0]]+(int(msg1[1])-1)
                        if bmaze[choice] ==':blue_square:':
                            break
                        else:
                            await msg.add_reaction('\N{NO ENTRY SIGN}')
                    elif len(msg1)==3 and msg1[0].isalpha()==True and msg1[1].isnumeric()==True and msg1[2].isnumeric()==True and (msg1[0] in ['a','b','c','d','e','f','g','h','i','j']) and int(msg1[1])==1 and int(msg1[2])==0:
                        choice=10*spot[msg1[0]]+9
                        if bmaze[choice] == ':blue_square:':
                            break
                        else:
                            await msg.add_reaction('\N{NO ENTRY SIGN}')
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send('looks like you fell asleep,'+ctx.author.name+'.')
                break
            if flag==-1:
                break
            #striker,ufo,nukeplane--------------------------------------------
            if action=='striker' or action == 'ufo' or action=='nukeplane':
                chance='n'
                if action=='striker':
                    list=[choice+11,choice+22,choice+33,choice+9,choice+18,choice+27,choice-11,choice-22,choice-33,choice-9,choice-18,choice-27]
                    title=ctx.author.name + ' released __FRACTAL STRIKER__ :helicopter:'
                    destroyer=':helicopter:'
                elif action=='nukeplane':
                    list=[choice - 11, choice - 10, choice - 9, choice - 1, choice + 1,choice + 11, choice + 10, choice + 9]
                    title = ctx.author.name + ' released __NUKEPLANE__ :airplane:'
                    destroyer=':airplane:'
                else:
                    list=[choice-30,choice-19,choice-8,choice+3,choice-21,choice-12,choice-3,choice+30,choice+19,choice+8,choice+21,choice+12]
                    title=ctx.author.name + ' released __UFO__ :flying_saucer:'
                    destroyer=':flying_saucer:'
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        if 10 * i + j in list:
                            string += '<a:impact:858999640158371861>'
                        elif 10 * i + j == choice:
                            string+=destroyer
                        else:
                            string += bmaze[10 * i + j]
                embed = discord.Embed(title=title, description=string,color=0x7F00FF)
                embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(3)
                if choice % 10 != bdefense_line:
                    for mark in list:
                        if mark % 10 == bdefense_line:
                            continue
                        j=0
                        for k in [bcarrier, bbattleship1, bbattleship2, bcruiser1, bcruiser2, bcruiser3, bsubmarine]:
                            if mark in k and bmaze[mark] != ':boom:' and bmaze[mark] != 'fire':
                                bmaze[mark] = ':boom:'
                                bblasted[j].append(mark)
                                chance = 'y'
                                flag = 1
                                break
                            j+=1
                        if flag != 1:
                            bmaze[mark] = ':x:'
                        flag = 0
                        if mark in bmine_spot:
                            bmine_spot.remove(mark)
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        string += bmaze[10 * i + j]
                if choice % 10 == bdefense_line:
                    string += "\n\nUnfortunately,"+destroyer+"got destroyed by **{}**'s defense system <:defense_system:858895078532317194>.".format(arg1.display_name)
                embed = discord.Embed(title=title, description=string,color=0x7F00FF)
                embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
                await string1.edit(embed=embed)
                if chance == 'y':
                    decision += 1
                ppowerup.remove(action)
                ppowerup_display.remove(destroyer)
            #torpedo---------------------------------------------
            elif action=='torpedo':
                chance='n'
                destroyed=''
                for mark in reversed(range(choice,choice+10)):
                    string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                    for i in range(10):
                        string += '\n' + positions[i]
                        for j in range(10):
                            if 10 * i + j == mark:
                                string += '<:torpedo:859668485440405515>'
                            else:
                                string += bmaze[10 * i + j]
                    embed = discord.Embed(title=ctx.author.name + ' released __TORPEDO__ <:torpedo:859668485440405515>',description=string, color=0x7F00FF)
                    embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
                    await string1.edit(embed=embed)
                    time.sleep(1)
                    if mark%10==bdefense_line or len(destroyed)!=0:
                        break
                    j=0
                    for k in [bcarrier, bbattleship1, bbattleship2, bcruiser1, bcruiser2, bcruiser3,bsubmarine]:
                        if mark in k:
                            if bmaze[mark]!=':boom:' and bmaze[mark]!='fire':
                                bmaze[mark]=':boom:'
                                bblasted[j].append(mark)
                                destroyed=bmaze[mark]
                                chance='y'
                            flag=1
                            break
                        j+=1
                    if flag!=1:
                        bmaze[mark]=':x:'
                    flag=0
                    if mark in bmine_spot:
                        bmine_spot.remove(mark)
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        string += bmaze[10 * i + j]
                if mark % 10 == bdefense_line:
                    string += "\n\nUnfortunately,<:torpedo:859668485440405515> got destroyed by **{}**'s defense system <:defense_system:858895078532317194>.".format(arg1.display_name)
                embed = discord.Embed(title=ctx.author.name + ' released __TORPEDO__ <:torpedo:859668485440405515>',description=string, color=0x7F00FF)
                embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(1)
                if chance == 'y':
                    decision += 1
                ppowerup.remove(action)
                ppowerup_display.remove('<:torpedo:859668485440405515>')
            #bomber-----------------------
            elif action=='bomber':
                chance='n'
                await msg.add_reaction('\N{SMALL AIRPLANE}')
                for mark in [marks[3],marks[4],marks[5]]:
                    string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                    for i in range(10):
                        string += '\n' + positions[i]
                        for j in range(10):
                            if 10*i+j == mark:
                                string+='<a:impact:858999640158371861>'
                            else:
                                string+=bmaze[10*i+j]
                    embed = discord.Embed(title=ctx.author.name +' released __BOMBER__ :airplane_small:',description=string, color=0x7F00FF)
                    embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
                    await string1.edit(embed=embed)
                    time.sleep(2)
                    if mark%10==bdefense_line:
                        break
                    j=0
                    for k in [bcarrier, bbattleship1, bbattleship2, bcruiser1, bcruiser2, bcruiser3,bsubmarine]:
                        if mark in k:
                            if bmaze[mark]!=':boom:' and bmaze[mark]!='fire':
                                bmaze[mark]=':boom:'
                                bblasted[j].append(mark)
                                chance='y'
                            flag=1
                            break
                        j+=1
                    if flag!=1:
                        bmaze[mark]=':x:'
                    flag=0
                    if mark in bmine_spot:
                        bmine_spot.remove(mark)
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        string += bmaze[10 * i + j]
                if mark%10==bdefense_line:
                    string += "\n\nUnfortunately,:airplane_small: got destroyed by **{}**'s defense system <:defense_system:858895078532317194>.".format(arg1.display_name)
                embed = discord.Embed(title=ctx.author.name + ' released __BOMBER__ :airplane_small:',description=string, color=0x7F00FF)
                embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(1)
                if chance=='y':
                    decision+=1
                ppowerup.remove('bomber')
                ppowerup_display.remove(':airplane_small:')
            #radar---------------------------
            elif action=='radar':
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        if 10 * i + j in [choice-11,choice-10,choice-9,choice-1,choice,choice+1,choice+11,choice+10,choice+9]:
                            for k in [bcarrier, bbattleship1, bbattleship2, bcruiser1, bcruiser2, bcruiser3,bsubmarine]:
                                if 10*i+j in k:
                                    string+='<a:scan_red:858999681400963102>'
                                    flag=1
                                    break
                            if flag==0:
                                string+='<a:scan_green:858999663247360001>'
                            flag=0
                        else:
                            string += bmaze[10 * i + j]
                embed = discord.Embed(title=ctx.author.name+' used __RADAR__ <:radar:858895009569570847>',description=string, color=0x7F00FF)
                embed.set_author(name="{}'s region:".format(arg1.display_name), icon_url=arg1._user.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(3)
                ppowerup.remove('radar')
                ppowerup_display.remove('<:radar:858895009569570847>')
            #mine------------------------------
            elif choice in bmine_spot:
                await msg.add_reaction('<:sea_mine:858894878230052884>')
                await ctx.send('**'+ctx.author.name+"** got caught by __SEA MINE__ <:sea_mine:858894878230052884> and hit in their own region.")
                j = 0
                for i in [pcarrier, pbattleship1, pbattleship2, pcruiser1, pcruiser2, pcruiser3, psubmarine]:
                    if choice in i and pmaze[choice]!=':fire:' and pmaze[choice]!=':boom:':
                        pmaze[choice] = ':boom:'
                        pblasted[j].append(choice)
                        flag = 1
                        break
                    j += 1
                if flag != 1:
                    pmaze[choice] = ':x:'
                if len(pblasted[0]) == 5 and pmaze[pcarrier[0]] != ':fire:':
                    for i in pcarrier:
                        pmaze[i] = ':fire:'
                    fleet1[0] = '[:red_square::red_square::red_square::red_square::red_square:>'
                if len(pblasted[1]) == 4 and pmaze[pbattleship1[0]] != ':fire:':
                    for i in pbattleship1:
                        pmaze[i] = ':fire:'
                    fleet1[1] = '[:red_square::red_square::red_square::red_square:>'
                if len(pblasted[2]) == 4 and pmaze[pbattleship2[0]] != ':fire:':
                    for i in pbattleship2:
                        pmaze[i] = ':fire:'
                    fleet1[2] = '[:red_square::red_square::red_square::red_square:>'
                if len(pblasted[3]) == 3 and pmaze[pcruiser1[0]] != ':fire:':
                    for i in pcruiser1:
                        pmaze[i] = ':fire:'
                    fleet1[3] = '[:red_square::red_square::red_square:>'
                if len(pblasted[4]) == 3 and pmaze[pcruiser2[0]] != ':fire:':
                    for i in pcruiser2:
                        pmaze[i] = ':fire:'
                    fleet1[4] = '[:red_square::red_square::red_square:>'
                if len(pblasted[5]) == 3 and pmaze[pcruiser3[0]] != ':fire:':
                    for i in pcruiser3:
                        pmaze[i] = ':fire:'
                    fleet1[5] = '[:red_square::red_square::red_square:>'
                if len(pblasted[6]) >= 1 and pmaze[pblasted[6][0]] != ':fire:':
                    pmaze[pblasted[6][0]] = ':fire:'
                    fleet1[6] = '[:red_square:>'
                if len(pblasted[6]) >= 2 and pmaze[pblasted[6][1]] != ':fire:':
                    pmaze[pblasted[6][1]] = ':fire:'
                    fleet1[7] = '[:red_square:>'
                if len(pblasted[6]) >= 3 and pmaze[pblasted[6][2]] != ':fire:':
                    pmaze[pblasted[6][2]] = ':fire:'
                    fleet1[8] = '[:red_square:>'
                if len(pblasted[6]) == 4 and pmaze[pblasted[6][3]] != ':fire:':
                    pmaze[pblasted[6][3]] = ':fire:'
                    fleet1[9] = '[:red_square:>'
                bmine_spot.remove(choice)
            #hit or miss----------------------------------------------
            else:
                j=0
                for i in [bcarrier, bbattleship1, bbattleship2, bcruiser1, bcruiser2, bcruiser3,bsubmarine]:
                    if choice in i:
                        bmaze[choice] = ':boom:'
                        await msg.add_reaction('\N{COLLISION SYMBOL}')
                        bblasted[j].append(choice)
                        decision+=1
                        flag=1
                        break
                    j+=1
                if flag != 1:
                    bmaze[choice] = ':x:'
                    await msg.add_reaction('\N{CROSS MARK}')
            if len(bblasted[0])==5 and bmaze[bcarrier[0]]!=':fire:':
                for i in bcarrier:
                    bmaze[i]=':fire:'
                fleet2[0]='[:red_square::red_square::red_square::red_square::red_square:>'
            elif len(bblasted[1])==4 and bmaze[bbattleship1[0]]!=':fire:':
                for i in bbattleship1:
                    bmaze[i]=':fire:'
                fleet2[1]='[:red_square::red_square::red_square::red_square:>'
            elif len(bblasted[2])==4 and bmaze[bbattleship2[0]]!=':fire:':
                for i in bbattleship2:
                    bmaze[i]=':fire:'
                fleet2[2]='[:red_square::red_square::red_square::red_square:>'
            elif len(bblasted[3])==3 and bmaze[bcruiser1[0]]!=':fire:':
                for i in bcruiser1:
                    bmaze[i]=':fire:'
                fleet2[3]='[:red_square::red_square::red_square:>'
            elif len(bblasted[4])==3 and bmaze[bcruiser2[0]]!=':fire:':
                for i in bcruiser2:
                    bmaze[i]=':fire:'
                fleet2[4] = '[:red_square::red_square::red_square:>'
            elif len(bblasted[5])==3 and bmaze[bcruiser3[0]]!=':fire:':
                for i in bcruiser3:
                    bmaze[i]=':fire:'
                fleet2[5] = '[:red_square::red_square::red_square:>'
            if len(bblasted[6])>=1 and bmaze[bblasted[6][0]]!=':fire:':
                bmaze[bblasted[6][0]]=':fire:'
                fleet2[6] = '[:red_square:>'
            if len(bblasted[6])>=2 and bmaze[bblasted[6][1]]!=':fire:':
                bmaze[bblasted[6][1]]=':fire:'
                fleet2[7] = '[:red_square:>'
            if len(bblasted[6])>=3 and bmaze[bblasted[6][2]]!=':fire:':
                bmaze[bblasted[6][2]]=':fire:'
                fleet2[8] = '[:red_square:>'
            if len(bblasted[6])==4 and bmaze[bblasted[6][3]]!=':fire:':
                bmaze[bblasted[6][3]]=':fire:'
                fleet2[9] = '[:red_square:>'
            if len(bmine_spot) == 0 and 'sea_mine' in bpowerup:
                bpowerup.remove('sea_mine')
                bpowerup_display.remove('<:sea_mine:858894878230052884>')
        else:
            #p2 turn-------------------------
            string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
            for i in range(10):
                string += '\n' + positions[i]
                for j in range(10):
                    string += pmaze[10 * i + j]
            embed = discord.Embed(title="{} turn:".format(arg1.display_name), description=string+'\n:boom: - hit , :x: - miss', color=0x7F00FF)
            embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
            string = '**Powerup** : '
            for k in ppowerup_display:
                string += k
            embed.add_field(name=':ship: ' + ctx.author.name + "'s fleet:",value=fleet1[0] + '\n' + fleet1[1] + '\n' + fleet1[2] + '\n' + fleet1[3] + '\n' + fleet1[4] + '\n' + fleet1[5] + '\n' + fleet1[6] + '    ' + fleet1[7] + '    ' + fleet1[8] + '    ' + fleet1[9]+'\n'+string, inline=True)
            string = '**Powerup** : '
            for k in bpowerup_display:
                string += k
            embed.add_field(name=":ship: {}'s fleet:".format(arg1.display_name),value=fleet2[0] + '\n' + fleet2[1] + '\n' + fleet2[2] + '\n' + fleet2[3] + '\n' + fleet2[4] + '\n' + fleet2[5] + '\n' + fleet2[6] + '    ' + fleet2[7] + '    ' + fleet2[8] + '    ' + fleet2[9]+'\n'+string, inline=True)
            embed.set_footer(text="type input like a5,f3,etc | 'exit' to abort.")
            string1=await ctx.send(embed=embed)
            if len(pblasted[0])+len(pblasted[1])+len(pblasted[2])+len(pblasted[3])+len(pblasted[4])+len(pblasted[5])+len(pblasted[6])==26:
                await ctx.send(":crown: **{}** won :crown:".format(arg1.display_name))
                break
            elif len(bblasted[0])+len(bblasted[1])+len(bblasted[2])+len(bblasted[3])+len(bblasted[4])+len(bblasted[5])+len(bblasted[6])==26:
                await ctx.send(":crown: **"+ctx.author.name+"** won :crown:")
                break
            action=''
            t2=0
            try:
                while 1:
                    t1=time.time()
                    msg = await client.wait_for('message', check=check(arg1._user), timeout=120-t2)
                    msg1 = msg.content.lower()
                    if msg1 == 'exit':
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        flag = -1
                        break
                    elif 'radar' in bpowerup and msg1[:5]=='radar' and msg1[5]==' ' and msg1[6].isalpha()==True and (msg1[6] in ['b','c','d','e','f','g','h','i']) and msg1[7].isnumeric()==True and (int(msg1[7]) in range(2,10)):
                        choice = 10 * spot[msg1[6]] + (int(msg1[7]) - 1)
                        await msg.add_reaction('<:radar:858895009569570847>')
                        action='radar'
                        break
                    elif 'torpedo' in bpowerup and len(msg1)==9 and msg1[:7]=='torpedo' and msg1[7]==' ' and msg1[8].isalpha()==True and (msg1[8] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
                        choice=10*spot[msg1[8]]
                        await msg.add_reaction('<:torpedo:859668485440405515>')
                        action = 'torpedo'
                        break
                    elif msg1 in bpowerup and msg1=='striker':
                        choice=random.choice([44,45,54,55])
                        action='striker'
                        await msg.add_reaction('\N{HELICOPTER}')
                        break
                    elif msg1 in bpowerup and msg1=='ufo':
                        choice=random.choice([44,45,54,55])
                        action='ufo'
                        await msg.add_reaction('\N{FLYING SAUCER}')
                        break
                    elif 'nukeplane' in bpowerup and len(msg1)==12 and msg1[:9]=='nukeplane' and msg1[9]==' ' and msg1[10].isalpha()==True and (msg1[10] in ['b','c','d','e','f','g','h','i']) and msg1[11].isnumeric()==True and (int(msg1[11]) in range(2,10)):
                        choice = 10 * spot[msg1[10]] + (int(msg1[11]) - 1)
                        await msg.add_reaction('\N{AIRPLANE}')
                        action='nukeplane'
                        break
                    elif 'bomber' in bpowerup and msg1[:6] == 'bomber' and msg1[6] == ' ':
                        i = j = 7
                        marks = []
                        for alpha in msg1[7:]:
                            if alpha == ' ':
                                marks.append(msg1[i:j])
                                i += len(marks[-1]) + 1
                            j += 1
                        marks.append(msg1[i:j])
                        if len(marks) == 3 and (len(marks[0]) == 2 or len(marks[0]) == 3) and (len(marks[1]) == 2 or len(marks[1]) == 3) and (len(marks[2]) == 2 or len(marks[2]) == 3) and ( marks[0][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and (marks[1][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and (marks[2][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
                            if len(marks[0]) == 2 and marks[0][1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                marks.append(10 * spot[marks[0][0]] + (int(marks[0][1]) - 1))
                            elif len(marks[0]) == 3 and marks[0][1] == '1' and marks[0][2] == '0':
                                marks.append(10 * spot[marks[0][0]] + 9)
                            if len(marks[1]) == 2 and marks[1][1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                marks.append(10 * spot[marks[1][0]] + (int(marks[1][1]) - 1))
                            elif len(marks[1]) == 3 and marks[1][1] == '1' and marks[1][2] == '0':
                                marks.append(10 * spot[marks[1][0]] + 9)
                            if len(marks[2]) == 2 and marks[2][1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                marks.append(10 * spot[marks[2][0]] + (int(marks[2][1]) - 1))
                            elif len(marks[2]) == 3 and marks[2][1] == '1' and marks[2][2] == '0':
                                marks.append(10 * spot[marks[2][0]] + 9)
                            if (marks[3]!=None and marks[4]!=None and marks[5]!=None) and marks[3] in range(0, 99) and marks[4] in range(0, 99) and marks[5] in range(0, 99):
                                action='bomber'
                                break
                    elif len(msg1) == 2 and msg1[0].isalpha() == True and msg1[1].isnumeric() == True and (msg1[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and (int(msg1[1]) in range(1, 10)):
                        choice = 10 * spot[msg1[0]] + (int(msg1[1]) - 1)
                        if pmaze[choice] == ':blue_square:':
                            break
                        else:
                            await msg.add_reaction('\N{NO ENTRY SIGN}')
                    elif len(msg1) == 3 and msg1[0].isalpha() == True and msg1[1].isnumeric() == True and msg1[2].isnumeric() == True and (msg1[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and int(msg1[1]) == 1 and int(msg1[2]) == 0:
                        choice = 10 * spot[msg1[0]] + 9
                        if pmaze[choice] == ':blue_square:':
                            break
                        else:
                            await msg.add_reaction('\N{NO ENTRY SIGN}')
                    t2+=int(time.time()-t1)
            except asyncio.TimeoutError:
                await ctx.send('looks like you fell asleep,{}.'.format(arg1.display_name))
                break
            if flag == -1:
                break
            # striker,ufo,nukeplane--------------------------------------------
            if action in ['ufo','nukeplane','striker']:
                chance = 'n'
                if action == 'striker':
                    list = [choice + 11, choice + 22, choice + 33, choice + 9, choice + 18, choice + 27,choice - 11, choice - 22, choice - 33, choice - 9, choice - 18, choice - 27]
                    title ='{} released __FRACTAL STRIKER__ :helicopter:'.format(arg1.display_name)
                    destroyer = ':helicopter:'
                elif action == 'nukeplane':
                    list = [choice - 11, choice - 10, choice - 9, choice - 1, choice + 1, choice + 11, choice + 10,choice + 9]
                    title ='{} released __NUKEPLANE__ :airplane:'.format(arg1.display_name)
                    destroyer = ':airplane:'
                else:
                    list = [choice - 30, choice - 19, choice - 8, choice + 3, choice - 21, choice - 12, choice - 3,choice + 30, choice + 19, choice + 8, choice + 21, choice + 12]
                    title ='{} released __UFO__ :flying_saucer:'.format(arg1.display_name)
                    destroyer = ':flying_saucer:'
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        if 10 * i + j in list:
                            string += '<a:impact:858999640158371861>'
                        elif 10 * i + j == choice:
                            string+=destroyer
                        else:
                            string += pmaze[10 * i + j]
                embed = discord.Embed(title=title, description=string, color=0x7F00FF)
                embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(3)
                if choice % 10 != pdefense_line:
                    for mark in list:
                        if mark % 10 == pdefense_line:
                            continue
                        j=0
                        for k in [pcarrier, pbattleship1, pbattleship2, pcruiser1, pcruiser2, pcruiser3, psubmarine]:
                            if mark in k and pmaze[mark] != ':boom:' and pmaze[mark] != 'fire':
                                pmaze[mark] = ':boom:'
                                pblasted[j].append(mark)
                                chance = 'y'
                                flag = 1
                                break
                            j+=1
                        if flag != 1:
                            pmaze[mark] = ':x:'
                        flag = 0
                        if mark in pmine_spot:
                            pmine_spot.remove(mark)
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        string += pmaze[10 * i + j]
                if choice % 10 == pdefense_line:
                    string += "\n\nUnfortunately," + destroyer + "got destroyed by **"+ctx.author.name+"**'s defense system <:defense_system:858895078532317194>."
                embed = discord.Embed(title=title, description=string, color=0x7F00FF)
                embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
                await string1.edit(embed=embed)
                if chance == 'y':
                    decision += 1
                bpowerup.remove(action)
                bpowerup_display.remove(destroyer)
            # torpedo---------------------------------------------
            elif action == 'torpedo':
                chance = 'n'
                destroyed = ''
                for mark in reversed(range(choice, choice + 10)):
                    string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                    for i in range(10):
                        string += '\n' + positions[i]
                        for j in range(10):
                            if 10 * i + j == mark:
                                string += '<:torpedo:859668485440405515>'
                            else:
                                string += pmaze[10 * i + j]
                    embed = discord.Embed(title='{} released __TORPEDO__ <:torpedo:859668485440405515>'.format(arg1.display_name),description=string, color=0x7F00FF)
                    embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
                    await string1.edit(embed=embed)
                    time.sleep(1)
                    if mark % 10 == pdefense_line or len(destroyed) != 0:
                        break
                    j=0
                    for k in [pcarrier, pbattleship1, pbattleship2, pcruiser1, pcruiser2, pcruiser3, psubmarine]:
                        if mark in k:
                            if pmaze[mark] != ':boom:' and pmaze[mark] != 'fire':
                                pmaze[mark] = ':boom:'
                                pblasted[j].append(mark)
                                destroyed = pmaze[mark]
                                chance = 'y'
                            flag = 1
                            break
                        j+=1
                    if flag != 1:
                        pmaze[mark] = ':x:'
                    flag = 0
                    if mark in pmine_spot:
                        pmine_spot.remove(mark)
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        string += pmaze[10 * i + j]
                if mark % 10 == pdefense_line:
                    string += "\n\nUnfortunately,<:torpedo:859668485440405515> got destroyed by **"+ctx.author.name+"**'s defense system <:defense_system:858895078532317194>."
                embed = discord.Embed(title='{} released __TORPEDO__ <:torpedo:859668485440405515>'.format(arg1.display_name), description=string,color=0x7F00FF)
                embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(1)
                if chance == 'y':
                    decision += 1
                bpowerup.remove(action)
                bpowerup_display.remove('<:torpedo:859668485440405515>')
            # bomber-----------------------
            elif action== 'bomber':
                chance = 'n'
                await msg.add_reaction('\N{SMALL AIRPLANE}')
                for mark in [marks[3], marks[4], marks[5]]:
                    string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                    for i in range(10):
                        string += '\n' + positions[i]
                        for j in range(10):
                            if 10 * i + j == mark:
                                string += '<a:impact:858999640158371861>'
                            else:
                                string += pmaze[10 * i + j]
                    embed = discord.Embed(title='{} released __BOMBER__ :airplane_small:'.format(arg1.display_name),description=string, color=0x7F00FF)
                    embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
                    await string1.edit(embed=embed)
                    time.sleep(2)
                    if mark%10==pdefense_line:
                        break
                    j=0
                    for k in [pcarrier, pbattleship1, pbattleship2, pcruiser1, pcruiser2, pcruiser3, psubmarine]:
                        if mark in k:
                            if pmaze[mark] != ':boom:' and pmaze[mark]!=':fire:':
                                pmaze[mark] = ':boom:'
                                pblasted[j].append(mark)
                                chance = 'y'
                            flag = 1
                            break
                        j+=1
                    if flag != 1:
                        pmaze[mark] = ':x:'
                    flag = 0
                    if mark in pmine_spot:
                        pmine_spot.remove(mark)
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        string += pmaze[10 * i + j]
                if mark%10==pdefense_line:
                    string += "\n\nUnfortunately,:airplane_small: got destroyed by **"+ctx.author.name+"**'s defense system <:defense_system:858895078532317194>."
                embed = discord.Embed(title='{} released __BOMBER__ :airplane_small:'.format(arg1.display_name),description=string, color=0x7F00FF)
                embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(1)
                if chance == 'y':
                    decision += 1
                bpowerup.remove(action)
                bpowerup_display.remove(':airplane_small:')
            # radar---------------------------
            elif action == 'radar':
                string = ':black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:'
                for i in range(10):
                    string += '\n' + positions[i]
                    for j in range(10):
                        if 10 * i + j in [choice - 11, choice - 10, choice - 9, choice - 1, choice, choice + 1,choice + 11, choice + 10, choice + 9]:
                            for k in [pcarrier, pbattleship1, pbattleship2, pcruiser1, pcruiser2, pcruiser3,psubmarine]:
                                if 10 * i + j in k:
                                    string += '<a:scan_red:858999681400963102>'
                                    flag = 1
                                    break
                            if flag == 0:
                                string += '<a:scan_green:858999663247360001>'
                            flag = 0
                        else:
                            string += pmaze[10 * i + j]
                embed = discord.Embed(title='{} used __RADAR__ <:radar:858895009569570847>'.format(arg1.display_name),description=string, color=0x7F00FF)
                embed.set_author(name=ctx.author.name+"'s region:", icon_url=ctx.author.avatar_url)
                await string1.edit(embed=embed)
                time.sleep(3)
                bpowerup.remove(action)
                bpowerup_display.remove('<:radar:858895009569570847>')
            #mine----------------------------------------
            elif choice in pmine_spot:
                await msg.add_reaction('<:sea_mine:858894878230052884>')
                await ctx.send("**{}** got caught by __SEA MINE__ <:sea_mine:858894878230052884> and hit in their own region.".format(arg1.display_name))
                j = 0
                for i in [bcarrier, bbattleship1, bbattleship2, bcruiser1, bcruiser2, bcruiser3, bsubmarine]:
                    if choice in i and bmaze[choice] == ':fire:' and bmaze[choice] == ':boom:':
                        bmaze[choice] = ':boom:'
                        bblasted[j].append(choice)
                        flag = 1
                        break
                    j += 1
                if flag != 1:
                    bmaze[choice] = ':x:'
                if len(bblasted[0]) == 5 and bmaze[bcarrier[0]] != ':fire:':
                    for i in bcarrier:
                        bmaze[i] = ':fire:'
                    fleet2[0] = '[:red_square::red_square::red_square::red_square::red_square:>'
                if len(bblasted[1]) == 4 and bmaze[bbattleship1[0]] != ':fire:':
                    for i in bbattleship1:
                        bmaze[i] = ':fire:'
                    fleet2[1] = '[:red_square::red_square::red_square::red_square:>'
                if len(bblasted[2]) == 4 and bmaze[bbattleship2[0]] != ':fire:':
                    for i in bbattleship2:
                        bmaze[i] = ':fire:'
                    fleet2[2] = '[:red_square::red_square::red_square::red_square:>'
                if len(bblasted[3]) == 3 and bmaze[bcruiser1[0]] != ':fire:':
                    for i in bcruiser1:
                        bmaze[i] = ':fire:'
                    fleet2[3] = '[:red_square::red_square::red_square:>'
                if len(bblasted[4]) == 3 and bmaze[bcruiser2[0]] != ':fire:':
                    for i in bcruiser2:
                        bmaze[i] = ':fire:'
                    fleet2[4] = '[:red_square::red_square::red_square:>'
                if len(bblasted[5]) == 3 and bmaze[bcruiser3[0]] != ':fire:':
                    for i in bcruiser3:
                        bmaze[i] = ':fire:'
                    fleet2[5] = '[:red_square::red_square::red_square:>'
                if len(bblasted[6]) >= 1 and bmaze[bblasted[6][0]] != ':fire:':
                    bmaze[bblasted[6][0]] = ':fire:'
                    fleet2[6] = '[:red_square:>'
                if len(bblasted[6]) >= 2 and bmaze[bblasted[6][1]] != ':fire:':
                    bmaze[bblasted[6][1]] = ':fire:'
                    fleet2[7] = '[:red_square:>'
                if len(bblasted[6]) >= 3 and bmaze[bblasted[6][2]] != ':fire:':
                    bmaze[bblasted[6][2]] = ':fire:'
                    fleet2[8] = '[:red_square:>'
                if len(bblasted[6]) == 4 and bmaze[bblasted[6][3]] != ':fire:':
                    bmaze[bblasted[6][3]] = ':fire:'
                    fleet2[9] = '[:red_square:>'
                pmine_spot.remove(choice)
            #hit or miss-------------------------------
            else:
                j=0
                for i in [pcarrier, pbattleship1, pbattleship2, pcruiser1, pcruiser2, pcruiser3, psubmarine]:
                    if choice in i:
                        pmaze[choice] = ':boom:'
                        await msg.add_reaction('\N{COLLISION SYMBOL}')
                        pblasted[j].append(choice)
                        decision += 1
                        flag = 1
                        break
                    j += 1
                if flag != 1:
                    pmaze[choice] = ':x:'
                    await msg.add_reaction('\N{CROSS MARK}')
            if len(pblasted[0]) == 5 and pmaze[pcarrier[0]] != ':fire:':
                for i in pcarrier:
                    pmaze[i] = ':fire:'
                fleet1[0] = '[:red_square::red_square::red_square::red_square::red_square:>'
            if len(pblasted[1]) == 4 and pmaze[pbattleship1[0]] != ':fire:':
                for i in pbattleship1:
                    pmaze[i] = ':fire:'
                fleet1[1] = '[:red_square::red_square::red_square::red_square:>'
            if len(pblasted[2]) == 4 and pmaze[pbattleship2[0]] != ':fire:':
                for i in pbattleship2:
                    pmaze[i] = ':fire:'
                fleet1[2] = '[:red_square::red_square::red_square::red_square:>'
            if len(pblasted[3]) == 3 and pmaze[pcruiser1[0]] != ':fire:':
                for i in pcruiser1:
                    pmaze[i] = ':fire:'
                fleet1[3] = '[:red_square::red_square::red_square:>'
            if len(pblasted[4]) == 3 and pmaze[pcruiser2[0]] != ':fire:':
                for i in pcruiser2:
                    pmaze[i] = ':fire:'
                fleet1[4] = '[:red_square::red_square::red_square:>'
            if len(pblasted[5]) == 3 and pmaze[pcruiser3[0]] != ':fire:':
                for i in pcruiser3:
                    pmaze[i] = ':fire:'
                fleet1[5] = '[:red_square::red_square::red_square:>'
            if len(pblasted[6]) == 1 and pmaze[pblasted[6][0]] != ':fire:':
                pmaze[pblasted[6][0]] = ':fire:'
                fleet1[6] = '[:red_square:>'
            if len(pblasted[6]) == 2 and pmaze[pblasted[6][1]] != ':fire:':
                pmaze[pblasted[6][1]] = ':fire:'
                fleet1[7] = '[:red_square:>'
            if len(pblasted[6]) == 3 and pmaze[pblasted[6][2]] != ':fire:':
                pmaze[pblasted[6][2]] = ':fire:'
                fleet1[8] = '[:red_square:>'
            if len(pblasted[6]) == 4 and pmaze[pblasted[6][3]] != ':fire:':
                pmaze[pblasted[6][3]] = ':fire:'
                fleet1[9] = '[:red_square:>'
            if len(pmine_spot) == 0 and 'sea_mine' in ppowerup:
                ppowerup.remove('sea_mine')
                ppowerup_display.remove('<:sea_mine:858894878230052884>')
        decision+=1
    command_usage.remove(ctx.author.id)
    command_usage.remove(arg1._user.id)

@client.command()
async def blindrun(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
        return
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
        return
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko blindrun @user`',color=0x7F00FF))
        return
    command_usage.append(ctx.author.id)
    command_usage.append(arg1._user.id)
    decision = t2=0
    await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
    try:
        while 1:
            t1=time.time()
            msg = await client.wait_for('message', check=check(arg1._user), timeout=30-t2)
            if msg.content.lower() == "yes" or msg.content.lower() == "y":
                decision = 1
                break
            elif msg.content.lower() == "no" or msg.content.lower() == "n":
                decision = -1
                break
            t2+=int(time.time()-t1)
    except asyncio.TimeoutError:
        await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    if decision == -1:
        await ctx.send("terminated.")
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    pcrystals = ['<:blue_gem:860432007901478922>', '<:green_gem:860432031610699807>', '<:red_gem:860431888396845076>']
    bcrystals = ['<:blue_gem:860432007901478922>', '<:green_gem:860432031610699807>', '<:red_gem:860431888396845076>']
    random.shuffle(pcrystals)
    random.shuffle(bcrystals)
    pscore = ['<:no_gem:860441522801344522>', '<:no_gem:860441522801344522>', '<:no_gem:860441522801344522>']
    bscore = ['<:no_gem:860441522801344522>', '<:no_gem:860441522801344522>', '<:no_gem:860441522801344522>']
    pultsolution = []
    bultsolution = []
    turnmissed = 0
    pwin = 0
    bwin = 0

    def maze(solution, crystals, emoji):
        maze_up = [emoji]
        maze_down = [':yellow_square:']
        for i in range(7 - len(crystals)):
            if solution[i] == 'down':
                maze_up.append('<:spike:860432293919195146>')
                maze_down.append(':yellow_square:')
            elif solution[i] == 'up':
                maze_up.append(':black_large_square:')
                maze_down.append(':black_large_square:')
            else:
                maze_up.append('<:skeleton:860416488753987594>')
                maze_down.append(':yellow_square:')
            maze_down.append(':yellow_square:')
            if i == 6 - len(crystals):
                maze_up.append(crystals[0])
            else:
                maze_up.append(':black_large_square:')
        return maze_up, maze_down

    def ult_maze(solution, emoji):
        maze_up = [emoji]
        maze_down = [':yellow_square:']
        for i in range(6):
            if solution[i] == 'down':
                maze_up.append('<:spike:860432293919195146>')
                maze_down.append(':yellow_square:')
            elif solution[i] == 'up':
                maze_up.append(':black_large_square:')
                maze_down.append(':black_large_square:')
            if i == 5 or i == 3:
                maze_up.append('<:door:860432271877210132>')
            else:
                maze_up.append(':black_large_square:')
            maze_down.append(':yellow_square:')
        return maze_up, maze_down

    def maze_hidden(maze_up, crystals, ultsolution):
        string = maze_up[0]
        if len(ultsolution) == 0:
            for i in range(13 - 2 * len(crystals)):
                string += ':question:'
            string += crystals[0] + '\n:yellow_square:'
            for i in range(13 - 2 * len(crystals)):
                string += ':grey_question:'
            string += ':yellow_square:'
        else:
            for i in range(11):
                if i == 7:
                    string += '<:door:860432271877210132>'
                else:
                    string += ':question:'
            string += '<:door:860432271877210132>\n:yellow_square:'
            for i in range(11):
                if i == 7:
                    string += ':yellow_square:'
                else:
                    string += ':grey_question:'
            string += ':yellow_square:'
        return string

    bdoor = pdoor = -1
    while 1:
        psolution = []
        bsolution = []
        if pwin != 3 and len(pultsolution) == 0:
            for i in range(7 - len(pcrystals)):
                psolution.append(random.choice(['up', 'down', 'right']))
            pmaze_up, pmaze_down = maze(psolution, pcrystals, '<:knight1:860412559445458954>')
        elif len(pultsolution) == 0:
            for i in range(6):
                pultsolution.append(random.choice(['up', 'down']))
            pdoor = random.choice([8, 12])
        if len(pultsolution) != 0:
            pmaze_up, pmaze_down = ult_maze(pultsolution, '<:knight1:860412559445458954>')
        if bwin != 3 and len(bultsolution) == 0:
            for i in range(7 - len(bcrystals)):
                bsolution.append(random.choice(['up', 'down', 'right']))
            bmaze_up, bmaze_down = maze(bsolution, bcrystals, '<:knight2:860410717735747614>')
        elif len(bultsolution) == 0:
            for i in range(6):
                bultsolution.append(random.choice(['up', 'down']))
            bdoor = random.choice([8, 12])
        if len(bultsolution) != 0:
            bmaze_up, bmaze_down = ult_maze(bultsolution, '<:knight2:860410717735747614>')
        pstring = maze_hidden(pmaze_up, pcrystals, pultsolution)
        bstring = "\n\n**{}'s journey [".format(arg1.display_name) + bscore[0] + bscore[1] + bscore[2] + "]**\n" + maze_hidden(bmaze_up, bcrystals, bultsolution)
        string1 = await ctx.send(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=pstring + bstring, color=0x7F00FF))
        time.sleep(2)
        string = ''
        if pwin == 0:
            for step in pmaze_up:
                string += step
            string += '\n'
            for step in pmaze_down:
                string += step
            await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=string + bstring, color=0x7F00FF))
            time.sleep(0.3)
        elif pwin == 1:
            for i in range(2):
                if i == 0:
                    for step in pmaze_up:
                        string += step
                    string += '\n:yellow_square::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::yellow_square:'
                else:
                    string = pmaze_up[0] + ':question::question::question::question::question::question::question::question::question:' + pcrystals[0] + '\n'
                    for step in pmaze_down:
                        string += step
                await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=string + bstring, color=0x7F00FF))
                time.sleep(0.3)
        elif pwin == 2:
            list = [1, 3, 5, 7, 9, 11]
            random.shuffle(list)
            for l in list:
                string_up = pmaze_up[0]
                string_down = ':yellow_square:'
                for i in range(1, 12):
                    if l == i:
                        string_up += pmaze_up[l]
                        string_down += pmaze_down[l]
                    else:
                        string_up += ':question:'
                        string_down += ':grey_question:'
                string_up += pcrystals[0]
                string_down += ':yellow_square:'
                await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=string_up + '\n' + string_down + bstring, color=0x7F00FF))
                time.sleep(0.3)

        await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=pstring + bstring, color=0x7F00FF))
        if len(psolution) == 0:
            time.sleep(2)
        if bwin == 0:
            string = "\n\n**{}'s journey [".format(arg1.display_name) + bscore[0] + bscore[1] + bscore[2] + "]**\n"
            for step in bmaze_up:
                string += step
            string += '\n'
            for step in bmaze_down:
                string += step
            await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=pstring + string, color=0x7F00FF))
            time.sleep(0.3)
        elif bwin == 1:
            for i in range(2):
                string = "\n\n**{}'s journey [".format(arg1.display_name) + bscore[0] + bscore[1] + bscore[2] + "]**\n"
                if i == 0:
                    for step in bmaze_up:
                        string += step
                    string += '\n:yellow_square::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::grey_question::yellow_square:'
                else:
                    string += bmaze_up[0] + ':question::question::question::question::question::question::question::question::question:' + bcrystals[0] + '\n'
                    for step in bmaze_down:
                        string += step
                await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=pstring + string, color=0x7F00FF))
                time.sleep(0.3)
        elif bwin == 2:
            list = [1, 3, 5, 7, 9, 11]
            random.shuffle(list)
            for l in list:
                string_up = bmaze_up[0]
                string_down = ':yellow_square:'
                for i in range(1, 12):
                    if l == i:
                        string_up += bmaze_up[l]
                        string_down += bmaze_down[l]
                    else:
                        string_up += ':question:'
                        string_down += ':grey_question:'
                string_up += bcrystals[0]
                string_down += ':yellow_square:'
                await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=pstring + "\n\n**{}'s journey [".format(arg1.display_name) + bscore[0] + bscore[1] +bscore[2] + "]**\n" + string_up + '\n' + string_down, color=0x7F00FF))
                time.sleep(0.3)
        embed = discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=pstring + bstring, color=0x7F00FF)
        embed.set_footer(text="'exit' to abort.")
        await string1.edit(embed=embed)
        if len(pultsolution) == 0:
            await ctx.send(ctx.author.mention + ' turn:\nmake ' + str(7 - len(pcrystals)) + '-moves combination using `up`/`u` , `down`/`d` , `right`/`r` (within 30 seconds)')
        else:
            await ctx.send(ctx.author.mention + ' turn:\nmake 4 or 6-moves combination using `up`/`u` , `down`/`d` (within 30 seconds)')
        t2 = flag = 0
        value = ''
        moves = []
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(ctx.author), timeout=30 - t2)
                msg1 = msg.content.lower()
                msg1 = msg1.split(' ')
                if msg.content.lower() == 'exit':
                    flag = -1
                    await msg.add_reaction('\N{OCTAGONAL SIGN}')
                    break
                elif len(pultsolution) != 0 and len(msg1) in [4, 6]:
                    for choice in msg1:
                        if choice not in ['up', 'u', 'down', 'd']:
                            flag = 1
                            break
                    if flag != 1:
                        await msg.add_reaction('\N{THUMBS UP SIGN}')
                        turnmissed = 0
                        moves.append(msg1)
                        break
                    flag = 0
                elif len(msg1) == len(psolution):
                    for choice in msg1:
                        if choice not in ['right', 'r', 'up', 'u', 'down', 'd']:
                            flag = 1
                            break
                    if flag != 1:
                        await msg.add_reaction('\N{THUMBS UP SIGN}')
                        turnmissed = 0
                        moves.append(msg1)
                        break
                    flag = 0
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            turnmissed += 1
            moves.append([])
            value = ctx.author.mention + ' missed their turn.\n'
        if flag==-1:
            break
        elif turnmissed == 4:
            await ctx.send('looks like both players fell asleep,aborted.')
            break
        if len(bultsolution) == 0:
            await ctx.send(value + "{} turn:\nmake ".format(arg1.mention) + str(7 - len(bcrystals)) + '-moves combination using `up`/`u` , `down`/`d` , `right`/`r` (within 30 seconds)')
        else:
            await ctx.send(value + "{} turn:\nmake ".format(arg1.mention) + '4 or 6-moves combination using `up`/`u` , `down`/`d` (within 30 seconds)')
        t2 = flag = 0
        try:
            while 1:
                t1 = time.time()
                msg = await client.wait_for('message', check=check(arg1._user), timeout=30 - t2)
                msg1 = msg.content.lower()
                msg1 = msg1.split(' ')
                if msg.content.lower() == 'exit':
                    flag = -1
                    await msg.add_reaction('\N{OCTAGONAL SIGN}')
                    break
                elif len(bultsolution) != 0 and len(msg1) in [4, 6]:
                    for choice in msg1:
                        if choice not in ['up', 'u', 'down', 'd']:
                            flag = 1
                            break
                    if flag != 1:
                        await msg.add_reaction('\N{THUMBS UP SIGN}')
                        turnmissed = 0
                        moves.append(msg1)
                        break
                    flag = 0
                elif len(msg1) == len(bsolution):
                    for choice in msg1:
                        if choice not in ['right', 'r', 'up', 'u', 'down', 'd']:
                            flag = 1
                            break
                    if flag != 1:
                        await msg.add_reaction('\N{THUMBS UP SIGN}')
                        turnmissed = 0
                        moves.append(msg1)
                        break
                    flag = 0
                t2 += int(time.time() - t1)
        except asyncio.TimeoutError:
            turnmissed += 1
            moves.append([])
            await ctx.send('{} missed their turn.\n'.format(arg1.mention))
        if flag==-1:
            break
        elif turnmissed == 4:
            await ctx.send('looks like both players fell asleep,aborted.')
            break
        string = ''
        if len(pultsolution) == 0:
            for step in pmaze_up:
                string += step
            string += '\n'
            for step in pmaze_down:
                string += step
        else:
            string += pstring
        string += '\n__Movement__ :\n'
        for i in range(len(moves[0])):
            if moves[0][i] == 'u':
                moves[0][i] = 'up'
            elif moves[0][i] == 'd':
                moves[0][i] = 'down'
            elif moves[0][i] == 'r':
                moves[0][i] = 'right'
            string += moves[0][i] + ' '
        if len(bultsolution) == 0:
            string += "\n\n**{}'s journey [".format(arg1.display_name) + bscore[0] + bscore[1] + bscore[2] + "]**\n"
            for step in bmaze_up:
                string += step
            string += '\n'
            for step in bmaze_down:
                string += step
        else:
            string += bstring
        string += '\n__Movement__ :\n'
        for i in range(len(moves[1])):
            if moves[1][i] == 'u':
                moves[1][i] = 'up'
            elif moves[1][i] == 'd':
                moves[1][i] = 'down'
            elif moves[1][i] == 'r':
                moves[1][i] = 'right'
            string += moves[1][i] + ' '
        string1 = await ctx.send(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=string, color=0x7F00FF))
        ppos = bpos = j = 0
        time.sleep(0.5)
        while 1:
            time.sleep(0.5)
            if len(pultsolution) == 0 and j < len(moves[0]) and pmaze_up[ppos] != ':skull_crossbones:' and moves[0][j] == psolution[j]:
                pmaze_up[ppos + 2] = pmaze_up[ppos]
                pmaze_up[ppos] = ':black_large_square:'
                if pmaze_up[ppos + 1] == '<:skeleton:860416488753987594>':
                    pmaze_up[ppos + 1] = '<:skeleton_dead:860483733936275555>'
                elif pmaze_up[ppos + 1] == '<:spike:860432293919195146>':
                    pmaze_up[ppos + 1] = '<:spike_down:860484864905838612>'
                ppos += 2
                moves[0][j] = '~~' + psolution[j] + '~~'
                if ppos == len(pmaze_up) - 1:
                    pscore[pwin] = pcrystals[0]
                    pcrystals.remove(pcrystals[0])
                    pwin += 1
            elif len(pultsolution) != 0 and j < len(moves[0]) and pmaze_up[ppos] != ':skull_crossbones:' and moves[0][j] == pultsolution[j]:
                pmaze_up[ppos + 2] = pmaze_up[ppos]
                pmaze_up[ppos] = ':black_large_square:'
                if pmaze_up[ppos + 1] == '<:spike:860432293919195146>':
                    pmaze_up[ppos + 1] = '<:spike_down:860484864905838612>'
                ppos += 2
                moves[0][j] = '~~' + pultsolution[j] + '~~'
                if ppos == 8 and len(moves[0]) == 4:
                    if pdoor == 8:
                        pwin += 1
                elif ppos == 12 and len(moves[0]) == 6:
                    if pdoor == 12:
                        pwin += 1
            elif len(pultsolution) != 0 and j < len(moves[0]) and pmaze_up[ppos] != ':skull_crossbones:' and moves[0][j] != pultsolution[j]:
                pmaze_up[ppos] = ':skull_crossbones:'
            elif len(pultsolution) == 0 and j < len(moves[0]) and pmaze_up[ppos] != ':skull_crossbones:' and moves[0][j] != psolution[j]:
                pmaze_up[ppos] = ':skull_crossbones:'
            if len(bultsolution) == 0 and j < len(moves[1]) and bmaze_up[bpos] != ':skull_crossbones:' and moves[1][j] == bsolution[j]:
                bmaze_up[bpos + 2] = bmaze_up[bpos]
                bmaze_up[bpos] = ':black_large_square:'
                if bmaze_up[bpos + 1] == '<:skeleton:860416488753987594>':
                    bmaze_up[bpos + 1] = '<:skeleton_dead:860483733936275555>'
                elif bmaze_up[bpos + 1] == '<:spike:860432293919195146>':
                    bmaze_up[bpos + 1] = '<:spike_down:860484864905838612>'
                bpos += 2
                moves[1][j] = '~~' + bsolution[j] + '~~'
                if bpos == len(bmaze_up) - 1:
                    bscore[bwin] = bcrystals[0]
                    bcrystals.remove(bcrystals[0])
                    bwin += 1
            elif len(bultsolution) != 0 and j < len(moves[1]) and bmaze_up[bpos] != ':skull_crossbones:' and moves[1][j] == bultsolution[j]:
                bmaze_up[bpos + 2] = bmaze_up[bpos]
                bmaze_up[bpos] = ':black_large_square:'
                if bmaze_up[bpos + 1] == '<:spike:860432293919195146>':
                    bmaze_up[bpos + 1] = '<:spike_down:860484864905838612>'
                bpos += 2
                moves[1][j] = '~~' + bultsolution[j] + '~~'
                if bpos == 8 and len(moves[1]) == 4:
                    if bdoor == 8:
                        bwin += 1
                elif bpos == 12 and len(moves[1]) == 6:
                    if bdoor == 12:
                        bwin += 1
            elif len(bultsolution) != 0 and j < len(moves[1]) and bmaze_up[bpos] != ':skull_crossbones:' and moves[1][j] != bultsolution[j]:
                bmaze_up[bpos] = ':skull_crossbones:'
            elif len(bultsolution) == 0 and j < len(moves[1]) and bmaze_up[bpos] != ':skull_crossbones:' and moves[1][j] != bsolution[j]:
                bmaze_up[bpos] = ':skull_crossbones:'
            if ppos == 0 and pmaze_up[ppos] == '<:knight1:860412559445458954>':
                pmaze_up[ppos] = ':skull_crossbones:'
            if bpos == 0 and bmaze_up[bpos] == '<:knight2:860410717735747614>':
                bmaze_up[bpos] = ':skull_crossbones:'
            string = ''
            if len(pultsolution) == 0:
                for step in pmaze_up:
                    string += step
                string += '\n'
                for step in pmaze_down:
                    string += step
            else:
                string_up = ''
                string_down = ''
                for i in range(0, ppos + 1):
                    string_up += pmaze_up[i]
                    string_down += pmaze_down[i]
                for k in range(i + 1, 13):
                    if k in [8, 12]:
                        string_up += '<:door:860432271877210132>'
                        string_down += ':yellow_square:'
                    else:
                        string_up += ':question:'
                        string_down += ':grey_question:'
                string += string_up + '\n' + string_down
            string += '\n__Movement__ :\n'
            for move in moves[0]:
                string += move + ' '
            string += "\n\n**{}'s journey [".format(arg1.display_name) + bscore[0] + bscore[1] + bscore[2] + "]**\n"
            if len(bultsolution) == 0:
                for step in bmaze_up:
                    string += step
                string += '\n'
                for step in bmaze_down:
                    string += step
            else:
                string_up = ''
                string_down = ''
                for i in range(0, bpos + 1):
                    string_up += bmaze_up[i]
                    string_down += bmaze_down[i]
                for k in range(i + 1, 13):
                    if k in [8, 12]:
                        string_up += '<:door:860432271877210132>'
                        string_down += ':yellow_square:'
                    else:
                        string_up += ':question:'
                        string_down += ':grey_question:'
                string += string_up + '\n' + string_down
            string += '\n__Movement__ :\n'
            for move in moves[1]:
                string += move + ' '
            await string1.edit(embed=discord.Embed(title=ctx.author.name + "'s journey [" + pscore[0] + pscore[1] + pscore[2] + "]",description=string, color=0x7F00FF))
            if pwin == 4 and bwin == 4:
                await ctx.send('Both players escaped the dungeon.')
                break
            elif len(pultsolution) != 0 and pwin == 4:
                await ctx.send('**' + ctx.author.name + '** escaped the dungeon.\n:crown: **' + ctx.author.name + '** won :crown:')
                break
            elif len(pultsolution) != 0 and pmaze_up[ppos] != ':skull_crossbones:' and (ppos == 8 and len(moves[0]) == 4 and pdoor == 12) or (ppos == 12 and len(moves[0]) == 6 and pdoor == 8):
                await ctx.send('**' + ctx.author.name + '**,this door is locked.The other one must be open.')
                pmaze_up[ppos] = ':skull_crossbones:'
            if len(bultsolution) != 0 and bwin == 4:
                await ctx.send('**{}**'.format(arg1.display_name) + ' escaped the dungeon.\n:crown: **{}** won :crown:'.format(arg1.display_name))
                break
            elif len(bultsolution) != 0 and bmaze_up[bpos] != ':skull_crossbones:' and (bpos == 8 and len(moves[1]) == 4 and bdoor == 12) or (bpos == 12 and len(moves[1]) == 6 and bdoor == 8):
                await ctx.send('**{}**,this door is locked.The other one must be open.'.format(arg1.display_name))
                bmaze_up[bpos] = ':skull_crossbones:'
            if (ppos == len(pmaze_up) - 1 and bpos == len(bmaze_up) - 1) or (bmaze_up[bpos] == ':skull_crossbones:' and pmaze_up[ppos] == ':skull_crossbones:') or (pmaze_up[ppos] == ':skull_crossbones:' and bpos == len(bmaze_up) - 1) or (bmaze_up[bpos] == ':skull_crossbones:' and ppos == len(pmaze_up) - 1):
                break
            j = j + 1
        if pwin == 4 or bwin == 4:
            break
    command_usage.remove(ctx.author.id)
    command_usage.remove(arg1._user.id)

@client.command()
async def diedungeon(ctx,arg1: discord.Member = None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    elif arg1 != None and arg1._user.bot == True:
        await ctx.send(ctx.author.mention + ",you can't play with bots!")
        return
    elif arg1 != None and arg1._user.id in command_usage:
        await ctx.send(ctx.author.mention + ',{} is already in a game.'.format(arg1.display_name))
        return
    elif arg1==None:
        await ctx.send(embed=discord.Embed(description='**CORRECT COMMAND USAGE** :\n`teko diedungeon @user`',color=0x7F00FF))
        return
    command_usage.append(ctx.author.id)
    command_usage.append(arg1._user.id)
    decision = t2=0
    await ctx.send("**{}**,do you want to start? [ **y** / **n** ]".format(arg1.display_name))
    try:
        while 1:
            t1=time.time()
            msg = await client.wait_for('message', check=check(arg1._user), timeout=30-t2)
            if msg.content.lower() == "yes" or msg.content.lower() == "y":
                decision = 1
                break
            elif msg.content.lower() == "no" or msg.content.lower() == "n":
                decision = -1
                break
            t2+=int(time.time()-t1)
    except asyncio.TimeoutError:
        await ctx.send("**{}** didn't replied.".format(arg1.display_name))
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    if decision == -1:
        await ctx.send("terminated.")
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    ppos = pscore = bscore = turnmissed = pblock = bblock = 0
    bpos = 48
    maze = []
    phealth = bhealth = 15
    pmax = bmax = 15
    dice_num = ['<:dice1:855341427441139722> (one)', '<:dice2:855341381941329941> (two)','<:dice3:855341405366386698> (three)', '<:dice4:855341364907737098> (four)','<:dice5:855341344728547348> (five)', '<:dice6:855341325721665576> (six)']
    psword = ['<:sword:860809658875772938>', 4]
    bsword = ['<:sword:860809658875772938>', 4]
    ppoison = ['', 0]
    bpoison = ['', 0]
    logs = ''
    for i in range(19):
        maze.append(random.choice(['<:bats:860809874221170688>', '<:demon:860809932207161354>', '<:freezard:860809893250727948>','<:goblin:860809948618817537>', '<:headcrab:860810006005547010>', '<:skeleton:860809590421454849>','<:snake:860809990163660830>']))
        if i < 7:
            maze.append(random.choice(['<:energy_stone:860810158548844564>', '<:energy_stone:860810158548844564>','<:energy_stone:860810158548844564>', '<:energy_stone:860810158548844564>','<:energy_stone:860810158548844564>', '<:energy_stone:860810158548844564>','<:energy_stone:860810158548844564>', '<:energy_stone:860810158548844564>','<:power_stone:860810175195250698>']))
            maze.append(random.choice(['<:white_sword:860809738539237396>', '<:sword:860809658875772938>', '<:sword:860809658875772938>','<:sword:860809658875772938>', '<:sword:860809658875772938>', '<:fire_wand:860809636139106325>','<:fire_wand:860809636139106325>', '<:ice_wand:860809616001990688>', '<:ice_wand:860809616001990688>','<:energy_sword:860809709942734870>']))
            maze.append(random.choice(['<:blue_potion:860809767411515392>', '<:blue_potion:860809767411515392>','<:blue_potion:860809767411515392>', '<:red_potion:860809787021197323>','<:red_potion:860809787021197323>', '<:red_potion:860809787021197323>','<:poison:860809812350074891>', '<:poison:860809812350074891>','<:heavy_potion:860809849930645516>']))
        if i < 5:
            maze.append(random.choice(['<:fake_potion:860809831891861534>', '<:flamethrower:860810196049068043>','<:mystery_chest:860810134506962954>', '<:vampire_sword:860809680410771466>']))
        if i < 2:
            maze.append(random.choice(['<:tentacle_creature:860810024128479233>', '<:spider:860809969263575060>','<:bomb1:860810042508967936>', ':stop_button:', ':twisted_rightwards_arrows:',':arrows_counterclockwise:']))
    random.shuffle(maze)
    maze.append('<:knight1:860809539698950184>')
    maze.reverse()
    maze.append('<:knight2:860809565577543691>')

    def display_maze(maze):
        string = ':yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:'
        for i in range(7):
            string += ':yellow_square:\n:yellow_square:'
            for j in range(7):
                string += maze[i * 7 + j]
        string += ':yellow_square:\n:yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:\n\n'
        return string

    def new_pos(msg, position, dice):
        if msg in ['r', 'right']:
            for i in range(dice):
                if position in [6, 13, 20, 27, 34, 41, 48]:
                    position -= 6
                else:
                    position += 1
        elif msg in ['l', 'left']:
            for i in range(dice):
                if position in [0, 7, 14, 21, 28, 35, 42]:
                    position += 6
                else:
                    position -= 1
        elif msg in ['u', 'up']:
            for i in range(dice):
                if position in [0, 1, 2, 3, 4, 5, 6]:
                    position += 42
                else:
                    position -= 7
        else:
            for i in range(dice):
                if position in [42, 43, 44, 45, 46, 47, 48]:
                    position -= 42
                else:
                    position += 7
        return position

    def new_item():
        chance = random.randint(1, 47)
        if chance <= 2:
            return random.choice(['<:mystery_chest:860810134506962954>', '<:tentacle_creature:860810024128479233>','<:spider:860809969263575060>', ':bomb:', ':stop_button:',':twisted_rightwards_arrows:', ':arrows_counterclockwise:'])
        elif chance <= 6:
            return random.choice(['<:fake_potion:860809831891861534>', '<:flamethrower:860810196049068043>','<:tentacle_creature:860810024128479233>', '<:vampire_sword:860809680410771466>'])
        elif chance <= 15:
            return random.choice([':low_brightness:', ':low_brightness:', ':low_brightness:', ':low_brightness:', ':low_brightness:',':low_brightness:', ':high_brightness:', ':high_brightness:', ':high_brightness:'])
        elif chance <= 20:
            return random.choice(['<:blue_potion:860809767411515392>', '<:blue_potion:860809767411515392>','<:blue_potion:860809767411515392>', '<:red_potion:860809787021197323>','<:red_potion:860809787021197323>', '<:red_potion:860809787021197323>','<:poison:860809812350074891>', '<:poison:860809812350074891>','<:heavy_potion:860809849930645516>'])
        elif chance <= 26:
            return random.choice(['<:white_sword:860809738539237396>', '<:sword:860809658875772938>', '<:sword:860809658875772938>','<:fire_wand:860809636139106325>', '<:fire_wand:860809636139106325>', '<:ice_wand:860809616001990688>','<:ice_wand:860809616001990688>', '<:energy_sword:860809709942734870>'])
        else:
            return random.choice(['<:bats:860809874221170688>', '<:demon:860809932207161354>', '<:freezard:860809893250727948>','<:demon:860809932207161354>', '<:freezard:860809893250727948>', '<:demon:860809932207161354>','<:freezard:860809893250727948>', '<:goblin:860809948618817537>', '<:headcrab:860810006005547010>','<:skeleton:860809590421454849>', '<:snake:860809990163660830>'])

    def flamethrower_goblin(maze, ppos, enemy):
        positions = []
        if ppos in [1, 2, 3, 4, 5]:
            if maze[ppos + 1] in enemy:
                positions.append(ppos + 1)
            if maze[ppos - 1] in enemy:
                positions.append(ppos - 1)
            if maze[ppos + 7] in enemy:
                positions.append(ppos + 7)
        elif ppos == 6:
            if maze[ppos - 1] in enemy:
                positions.append(ppos - 1)
            if maze[ppos + 7] in enemy:
                positions.append(ppos + 7)
        elif ppos in [13, 20, 27, 34, 41]:
            if maze[ppos - 7] in enemy:
                positions.append(ppos - 7)
            if maze[ppos + 7] in enemy:
                positions.append(ppos + 7)
            if maze[ppos - 1] in enemy:
                positions.append(ppos - 1)
        elif ppos in [47, 46, 45, 44, 43]:
            if maze[ppos + 1] in enemy:
                positions.append(ppos + 1)
            if maze[ppos - 1] in enemy:
                positions.append(ppos - 1)
            if maze[ppos - 7] in enemy:
                positions.append(ppos - 7)
        elif ppos == 42:
            if maze[ppos + 1] in enemy:
                positions.append(ppos + 1)
            if maze[ppos - 7] in enemy:
                positions.append(ppos - 7)
        elif ppos in [7, 14, 21, 28, 35]:
            if maze[ppos + 1] in enemy:
                positions.append(ppos + 1)
            if maze[ppos + 7] in enemy:
                positions.append(ppos + 7)
            if maze[ppos - 7] in enemy:
                positions.append(ppos - 7)
        else:
            if maze[ppos - 1] in enemy:
                positions.append(ppos - 1)
            if maze[ppos + 1] in enemy:
                positions.append(ppos + 1)
            if maze[ppos + 7] in enemy:
                positions.append(ppos + 7)
            if maze[ppos - 7] in enemy:
                positions.append(ppos - 7)
        return positions

    def bomb(i):
        row = column = i
        positions = []
        for i in range(6):
            if row in [0, 7, 14, 21, 28, 35, 42]:
                row += 6
            else:
                row -= 1
            if column in [0, 1, 2, 3, 4, 5, 6]:
                column += 42
            else:
                column -= 7
            positions.append(row)
            positions.append(column)
        return positions

    while (pscore + bscore) < 250:
        string = display_maze(maze)
        embed = discord.Embed(title=':skull: DIE DUNGEON :skull:', description=string, color=0x7F00FF)
        string = ":small_blue_diamond: <:game_heart:848505744063332392> : " + str(phealth) + "/" + str(pmax) + ' '
        if ppoison[0] != '':
            string += "," + ppoison[0] + '(' + str(ppoison[1]) + ')'
        if psword[0] != '':
            string += "\n:small_blue_diamond: __Sword__ : " + psword[0] + '[' + str(psword[1]) + ']'
        embed.add_field(name="<:knight1:860809539698950184> **" + ctx.author.name + "'s stats :**",value=string + '\n:small_blue_diamond: __Synergy grant__ : ' + str(pscore) + '<:energy_stone:860810158548844564>', inline=True)
        string = ":small_blue_diamond: <:game_heart:848505744063332392> : " + str(bhealth) + "/" + str(bmax) + ' '
        if bpoison[0] != '':
            string += "," + bpoison[0] + '(' + str(bpoison[1]) + ')'
        if bsword[0] != '':
            string += "\n:small_blue_diamond: __Sword__ : " + bsword[0] + '[' + str(bsword[1]) + ']'
        embed.add_field(name="<:knight2:860809565577543691> **{}'s stats :**".format(arg1.display_name),value=string + '\n:small_blue_diamond: __Synergy grant__ : ' + str(bscore) + '<:energy_stone:860810158548844564>\n\n' + logs, inline=True)
        embed.set_footer(text="'exit' to abort.")
        await ctx.send(embed=embed)
        logs = ''
        if decision % 2 != 0 and pblock == 0:
            string1 = await ctx.send("**" + ctx.author.name + "** turn .. <a:diceroll:855341301993701386>")
            time.sleep(1.5)
            dice = random.randint(1, 6)
            await string1.edit(content="**" + ctx.author.name + "** turn .. " + dice_num[dice - 1] + "\nChoose direction (`u`,`d`,`l`,`r`):")
            t2 = flag = 0
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(ctx.author), timeout=120 - t2)
                    if msg.content.lower() == 'exit':
                        flag = -1
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        break
                    elif msg.content.lower() in ['u', 'd', 'l', 'r', 'up', 'right', 'down', 'left']:
                        prev_pos = ppos
                        ppos = new_pos(msg.content.lower(), ppos, dice)
                        if ppos == 48:
                            await msg.add_reaction('\N{CROSS MARK}')
                            ppos = prev_pos
                        else:
                            turnmissed = 0
                            flag = 1
                            break
                    t2 += int(time.time() - t1)
            except asyncio.TimeoutError:
                turnmissed += 1
                await ctx.send(ctx.author.mention + ' missed their turn.')
            if turnmissed == 2:
                await ctx.send("looks like both player fell asleep,aborted.")
                break
            elif flag == -1:
                break
            if maze[ppos] in ['<:sword:860809658875772938>', '<:white_sword:860809738539237396>','<:fire_wand:860809636139106325>', '<:ice_wand:860809616001990688>','<:energy_sword:860809709942734870>', '<:vampire_sword:860809680410771466>']:
                if psword[0] == maze[ppos]:
                    if psword[0] == '<:sword:860809658875772938>':
                        psword[1] += dice
                    elif psword[0] == '<:white_sword:860809738539237396>':
                        psword[1] += int(2.5 * dice)
                    else:
                        psword[1] += 2 * dice
                else:
                    if maze[ppos] == '<:sword:860809658875772938>':
                        psword[1] = dice
                    elif maze[ppos] == '<:white_sword:860809738539237396>':
                        psword[1] = int(2.5 * dice)
                    else:
                        psword[1] = 2 * dice
                    logs = ">**" + ctx.author.name + "** got " + maze[ppos] + "."
                psword[0] = maze[ppos]
            elif maze[ppos] in ['<:fake_potion:860809831891861534>', '<:poison:860809812350074891>','<:energy_stone:860810158548844564>', '<:power_stone:860810175195250698>','<:blue_potion:860809767411515392>', '<:red_potion:860809787021197323>','<:heavy_potion:860809849930645516>']:
                if maze[ppos] == '<:energy_stone:860810158548844564>':
                    pscore += 4 * dice
                    logs = ">**" + ctx.author.name + "** got " + str(4 * dice) + ' synergy.'
                elif maze[ppos] == '<:power_stone:860810175195250698>':
                    pscore += 5 * dice
                    logs = ">**" + ctx.author.name + "** got " + str(5 * dice) + ' synergy.'
                elif maze[ppos] in '<:poison:860809812350074891>':
                    logs = ">**" + ctx.author.name + "** got poisoned."
                    ppoison[0] = '<:poison:860809812350074891>'
                    ppoison[1] += 1
                elif maze[ppos] in '<:blue_potion:860809767411515392>':
                    phealth += dice
                    logs = ">**" + ctx.author.name + "** got healed."
                elif maze[ppos] in '<:red_potion:860809787021197323>':
                    phealth += dice
                    if len(ppoison[0]) == 0:
                        logs = ">**" + ctx.author.name + "** got healed."
                    else:
                        ppoison = ['', 0]
                        logs = ">**" + ctx.author.name + "** got healed (poison removed)."
                elif maze[ppos] in '<:fake_potion:860809831891861534>':
                    if random.choice(['<:blue_potion:860809767411515392>','<:poison:860809812350074891>']) == '<:poison:860809812350074891>':
                        logs = ">**" + ctx.author.name + "** drank fake potion and got poisoned."
                        ppoison[0] = '<:poison:860809812350074891>'
                        ppoison[1] += 1
                    else:
                        logs = ">**" + ctx.author.name + "** drank fake potion but healed **{}**.".format(arg1.display_name)
                        bhealth += dice
                else:
                    phealth = pmax
                    logs = ">**" + ctx.author.name + "** got healed."
            elif (maze[ppos] in ['<:tentacle_creature:860810024128479233>', '<:bats:860809874221170688>', '<:demon:860809932207161354>', '<:freezard:860809893250727948>','<:goblin:860809948618817537>', '<:headcrab:860810006005547010>','<:skeleton:860809590421454849>', '<:snake:860809990163660830>','<:spider:860809969263575060>']):
                if maze[ppos] in ['<:tentacle_creature:860810024128479233>', '<:bats:860809874221170688>', '<:goblin:860809948618817537>', '<:demon:860809932207161354>','<:headcrab:860810006005547010>', '<:freezard:860809893250727948>','<:skeleton:860809590421454849>']:
                    if (psword[0] == '<:ice_wand:860809616001990688>' and maze[ppos] == '<:demon:860809932207161354>') or (psword[0] == '<:fire_wand:860809636139106325>' and maze[ppos] == '<:freezard:860809893250727948>'):
                        dmg = int(dice / 2)
                    elif maze[ppos] == '<:tentacle_creature:860810024128479233>' or (psword[0] == '<:fire_wand:860809636139106325>' and maze[ppos] == '<:demon:860809932207161354>') or (psword[0] == '<:ice_wand:860809616001990688>' and maze[ppos] == '<:freezard:860809893250727948>'):
                        dmg = dice * 2
                    else:
                        dmg = dice
                    if psword[1] >= dmg:
                        psword[1] -= dmg
                        if psword[0] == '<:vampire_sword:860809680410771466>':
                            phealth += 1
                        if psword[0] != '<:energy_sword:860809709942734870>':
                            dice = int(2 * dice)
                        else:
                            dice = int(2.5 * dice)
                        if maze[ppos] == '<:tentacle_creature:860810024128479233>':
                            dice = 2 * dice
                        pscore += dice
                        logs = ">**" + ctx.author.name + "** killed " + maze[ppos] + " (+" + str(dice) + " synergy)."
                        if psword[1] == 0:
                            psword[0] = ''
                    else:
                        dmg -= psword[1]
                        if psword[0] == '<:vampire_sword:860809680410771466>':
                            phealth += 1
                        if psword[0] == '<:energy_sword:860809709942734870>':
                            dice = int(2.5 * dice)
                        elif psword[0] != '':
                            dice = int(2 * dice)
                        psword = ['', 0]
                        phealth -= dmg
                        if phealth <= 0:
                            logs = ">**" + ctx.author.name + "** got killed by " + maze[ppos] + '.'
                        else:
                            pscore += dice
                            logs = ">**" + ctx.author.name + "** killed " + maze[ppos] + " (+" + str(dice) + " synergy)."
                elif maze[ppos] == '<:snake:860809990163660830>':
                    if psword[0] == '':
                        logs = ">**" + ctx.author.name + "** got poisoned by <:snake:860809990163660830>."
                        ppoison[0] = '<:poison:860809812350074891>'
                        ppoison[1] += 1
                    else:
                        logs = ">**" + ctx.author.name + "** killed <:snake:860809990163660830>."
            elif (maze[ppos] == '<:web:860809911973838848>'):
                logs = ">**" + ctx.author.name + "** got tangled in <:web:860809911973838848> (two turns blocked)."
                pblock = 3
                bblock = 0
            elif maze[ppos] == '<:flamethrower:860810196049068043>':
                enemy = ['<:knight2:860809565577543691>', '<:tentacle_creature:860810024128479233>','<:spider:860809969263575060>', '<:web:860809911973838848>', '<:bats:860809874221170688>','<:demon:860809932207161354>', '<:freezard:860809893250727948>', '<:goblin:860809948618817537>', '<:headcrab:860810006005547010>','<:skeleton:860809590421454849>', '<:snake:860809990163660830>']
                positions = flamethrower_goblin(maze, ppos, enemy)
                if len(positions) != 0:
                    pscore += len(positions) * dice
                    for p in positions:
                        if p not in [0, 48]:
                            maze[p] = new_item()
                    if bpos in positions:
                        bhealth = 0
                    logs = ">**" + ctx.author.name + "** used <:flamethrower:860810196049068043> (+" + str(len(positions) * dice) + " synergy)."
            elif maze[ppos] == ':stop_button:':
                logs = ">**" + ctx.author.name + "** got freezed (two turns blocked)."
                pblock = 3
                bblock = 0
            elif maze[ppos] == ':arrows_counterclockwise:':
                decision += 1
            elif maze[ppos] == ':twisted_rightwards_arrows:':
                for i in range(49):
                    if maze[i] in ['<:knight1:860809539698950184>', '<:knight2:860809565577543691>', maze[ppos],':regional_indicator_o:', ':o2:']:
                        maze[i] = new_item()
                random.shuffle(maze)
                maze[0] = ':regional_indicator_o:'
                maze[48] = ':o2:'
            elif maze[ppos] == '<:mystery_chest:860810134506962954>':
                item = random.choice(['<:web:860809911973838848>', '<:white_sword:860809738539237396>', '<:poison:860809812350074891>','<:energy_stone:860810158548844564>'])
                logs = ">**" + ctx.author.name + "** opened <:mystery_chest:860810134506962954>,"
                if item == '<:white_sword:860809738539237396>':
                    if psword[0] == '<:white_sword:860809738539237396>':
                        psword[1] += int(2.5 * dice)
                    else:
                        psword[1] = int(2.5 * dice)
                    psword[0] = '<:white_sword:860809738539237396>'
                    logs += "got <:white_sword:860809738539237396>."
                elif item == '<:web:860809911973838848>':
                    pblock = 3
                    bblock = 0
                    logs += "got tangled in <:web:860809911973838848> (two turns blocked)."
                elif item == '<:poison:860809812350074891>':
                    ppoison[0] = '<:poison:860809812350074891>'
                    ppoison[1] += 1
                    logs += "got poisoned."
                else:
                    pscore += 4 * dice
                    logs += "got " + str(4 * dice) + ' synergy.'
            elif maze[ppos] in ['<:bomb3:860810082006073355>', '<:bomb2:860810062720532510>','<:bomb1:860810042508967936>']:
                positions = bomb(i)
                for p in positions:
                    if p not in [0, 48]:
                        maze[p] = new_item()
                if bpos in positions:
                    bhealth = 0
                phealth = 0
            if bblock > 0:
                bblock -= 1
            if bblock != 0:
                decision += 1
        elif decision % 2 == 0 and bblock == 0:
            string1 = await ctx.send("**{}** turn .. <a:diceroll:855341301993701386>".format(arg1.display_name))
            time.sleep(1.5)
            dice = random.randint(1, 6)
            await string1.edit(content="**{}** turn .. ".format(arg1.display_name) + dice_num[dice - 1] + "\nChoose direction (`u`,`d`,`l`,`r`):")
            t2 = flag = 0
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(arg1._user), timeout=120 - t2)
                    if msg.content.lower() == 'exit':
                        flag = -1
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        break
                    elif msg.content.lower() in ['u', 'd', 'l', 'r', 'up', 'right', 'down', 'left']:
                        prev_pos = bpos
                        bpos = new_pos(msg.content.lower(), bpos, dice)
                        if bpos == 0:
                            await msg.add_reaction('\N{CROSS MARK}')
                            bpos = prev_pos
                        else:
                            turnmissed = 0
                            flag = 1
                            break
                    t2 += int(time.time() - t1)
            except asyncio.TimeoutError:
                turnmissed += 1
                await ctx.send('{} missed their turn.'.format(arg1.mention))
            if turnmissed == 2:
                await ctx.send("looks like both player fell asleep,aborted.")
                break
            elif flag == -1:
                break
            if maze[bpos] in ['<:sword:860809658875772938>', '<:white_sword:860809738539237396>','<:fire_wand:860809636139106325>', '<:ice_wand:860809616001990688>','<:energy_sword:860809709942734870>', '<:vampire_sword:860809680410771466>']:
                if bsword[0] == maze[bpos]:
                    if bsword[0] == '<:sword:860809658875772938>':
                        bsword[1] += dice
                    elif bsword[0] == '<:white_sword:860809738539237396>':
                        bsword[1] += int(2.5 * dice)
                    else:
                        bsword[1] += 2 * dice
                else:
                    if maze[bpos] == '<:sword:860809658875772938>':
                        bsword[1] = dice
                    elif maze[bpos] == '<:white_sword:860809738539237396>':
                        bsword[1] = int(2.5 * dice)
                    else:
                        bsword[1] = 2 * dice
                    logs = ">**{}** got ".format(arg1.display_name) + maze[bpos] + "."
                bsword[0] = maze[bpos]
            elif maze[bpos] in ['<:fake_potion:860809831891861534>', '<:poison:860809812350074891>','<:energy_stone:860810158548844564>', '<:power_stone:860810175195250698>','<:blue_potion:860809767411515392>', '<:red_potion:860809787021197323>','<:heavy_potion:860809849930645516>']:
                if maze[bpos] == '<:energy_stone:860810158548844564>':
                    bscore += 4 * dice
                    logs = ">**{}** got ".format(arg1.display_name) + str(4 * dice) + ' synergy.'
                elif maze[bpos] == '<:power_stone:860810175195250698>':
                    bscore += 5 * dice
                    logs = ">**{}** got ".format(arg1.display_name) + str(5 * dice) + ' synergy.'
                elif maze[bpos] in '<:poison:860809812350074891>':
                    logs = ">**{}** got poisoned.".format(arg1.display_name)
                    bpoison[0] = '<:poison:860809812350074891>'
                    bpoison[1] += 1
                elif maze[bpos] in '<:blue_potion:860809767411515392>':
                    bhealth += dice
                    logs = ">**{}** got healed.".format(arg1.display_name)
                elif maze[bpos] in '<:red_potion:860809787021197323>':
                    bhealth += dice
                    if len(bpoison[0]) == 0:
                        logs = ">**{}** got healed.".format(arg1.display_name)
                    else:
                        bpoison = ['', 0]
                        logs = ">**{}** got healed (poison removed).".format(arg1.display_name)
                elif maze[bpos] in '<:fake_potion:860809831891861534>':
                    if random.choice(['<:blue_potion:860809767411515392>','<:poison:860809812350074891>']) == '<:poison:860809812350074891>':
                        logs = ">**{}** drank fake potion and got poisoned.".format(arg1.display_name)
                        bpoison[0] = '<:poison:860809812350074891>'
                        bpoison[1] += 1
                    else:
                        logs = ">**{}** drank fake potion but healed.**".format(arg1.display_name) + ctx.author.name + "**. "
                        phealth += dice
                else:
                    bhealth = bmax
                    logs = ">**{}** got healed.".format(arg1.display_name)
            elif (maze[bpos] in ['<:tentacle_creature:860810024128479233>', '<:bats:860809874221170688>','<:demon:860809932207161354>', '<:freezard:860809893250727948>','<:goblin:860809948618817537>', '<:headcrab:860810006005547010>','<:skeleton:860809590421454849>', '<:snake:860809990163660830>','<:spider:860809969263575060>']):
                if maze[bpos] in ['<:tentacle_creature:860810024128479233>', '<:bats:860809874221170688>','<:goblin:860809948618817537>', '<:demon:860809932207161354>', '<:headcrab:860810006005547010>', '<:freezard:860809893250727948>','<:skeleton:860809590421454849>']:
                    if (bsword[0] == '<:ice_wand:860809616001990688>' and maze[bpos] == '<:demon:860809932207161354>') or (bsword[0] == '<:fire_wand:860809636139106325>' and maze[bpos] == '<:freezard:860809893250727948>'):
                        dmg = int(dice / 2)
                    elif maze[bpos] == '<:tentacle_creature:860810024128479233>' or (bsword[0] == '<:fire_wand:860809636139106325>' and maze[bpos] == '<:demon:860809932207161354>') or (bsword[0] == '<:ice_wand:860809616001990688>' and maze[bpos] == '<:freezard:860809893250727948>'):
                        dmg = dice * 2
                    else:
                        dmg = dice
                    if bsword[1] >= dmg:
                        bsword[1] -= dmg
                        if bsword[0] == '<:vampire_sword:860809680410771466>':
                            bhealth += 1
                        if bsword[0] != '<:energy_sword:860809709942734870>':
                            dice = int(2 * dice)
                        else:
                            dice = int(2.5 * dice)
                        if maze[bpos] == '<:tentacle_creature:860810024128479233>':
                            dice = 2 * dice
                        bscore += dice
                        logs = ">**{}** killed ".format(arg1.display_name) + maze[bpos] + " (+" + str(dice) + " synergy)."
                        if bsword[1] == 0:
                            bsword[0] = ''
                    else:
                        dmg -= bsword[1]
                        if bsword[0] == '<:vampire_sword:860809680410771466>':
                            bhealth += 1
                        if bsword[0] == '<:energy_sword:860809709942734870>':
                            dice = int(2.5 * dice)
                        elif bsword[0] != '':
                            dice = int(2 * dice)
                        bsword = ['', 0]
                        bhealth -= dmg
                        if bhealth <= 0:
                            logs = ">**{}** got killed by ".format(arg1.display_name) + maze[bpos] + '.'
                        else:
                            bscore += dice
                            logs = ">**{}** killed ".format(arg1.display_name) + maze[bpos] + " (+" + str(dice) + " synergy)."
                elif maze[bpos] == '<:snake:860809990163660830>':
                    if bsword[0] == '':
                        logs = ">**{}** got poisoned by <:snake:860809990163660830>.".format(arg1.display_name)
                        bpoison[0] = '<:poison:860809812350074891>'
                        bpoison[1] += 1
                    else:
                        logs = ">**{}** killed <:snake:860809990163660830>.".format(arg1.display_name)
            elif (maze[bpos] == '<:web:860809911973838848>'):
                logs = ">**{}** got tangled in <:web:860809911973838848> (two turns blocked).".format(arg1.display_name)
                bblock = 3
                pblock = 0
            elif maze[bpos] == '<:flamethrower:860810196049068043>':
                enemy = ['<:knight1:860809539698950184>', '<:tentacle_creature:860810024128479233>','<:spider:860809969263575060>', '<:web:860809911973838848>', '<:bats:860809874221170688>','<:demon:860809932207161354>', '<:freezard:860809893250727948>','<:goblin:860809948618817537>', '<:headcrab:860810006005547010>','<:skeleton:860809590421454849>', '<:snake:860809990163660830>']
                positions = flamethrower_goblin(maze, bpos, enemy)
                if len(positions) != 0:
                    bscore += len(positions) * dice
                    for p in positions:
                        if p not in [0, 48]:
                            maze[p] = new_item()
                    if ppos in positions:
                        phealth = 0
                    logs = ">**{}** used <:flamethrower:860810196049068043> (+".format(arg1.display_name) + str(
                        len(positions) * dice) + " synergy)."
            elif maze[bpos] == ':stop_button:':
                logs = ">**{}** got freezed (two turns blocked).".format(arg1.display_name)
                bblock = 3
                pblock = 0
            elif maze[bpos] == ':arrows_counterclockwise:':
                decision += 1
            elif maze[bpos] == ':twisted_rightwards_arrows:':
                for i in range(49):
                    if maze[i] in ['<:knight1:860809539698950184>', '<:knight2:860809565577543691>', maze[bpos],':regional_indicator_o:', ':o2:']:
                        maze[i] = new_item()
                random.shuffle(maze)
                maze[0] = ':regional_indicator_o:'
                maze[48] = ':o2:'
            elif maze[bpos] == '<:mystery_chest:860810134506962954>':
                item = random.choice(['<:web:860809911973838848>', '<:white_sword:860809738539237396>', '<:poison:860809812350074891>','<:energy_stone:860810158548844564>'])
                logs = ">**{}** opened <:mystery_chest:860810134506962954>,".format(arg1.display_name)
                if item == '<:white_sword:860809738539237396>':
                    if bsword[0] == '<:white_sword:860809738539237396>':
                        bsword[1] += int(2.5 * dice)
                    else:
                        bsword[1] = int(2.5 * dice)
                    bsword[0] = '<:white_sword:860809738539237396>'
                    logs += "got <:white_sword:860809738539237396>."
                elif item == '<:web:860809911973838848>':
                    bblock = 3
                    pblock = 0
                    logs += "got tangled in <:web:860809911973838848> (two turns blocked)."
                elif item == '<:poison:860809812350074891>':
                    bpoison[0] = '<:poison:860809812350074891>'
                    bpoison[1] += 1
                    logs += "got poisoned."
                else:
                    bscore += 4 * dice
                    logs += "got " + str(4 * dice) + ' synergy.'
            elif maze[bpos] in ['<:bomb3:860810082006073355>', '<:bomb2:860810062720532510>','<:bomb1:860810042508967936>']:
                positions = bomb(i)
                for p in positions:
                    if p not in [0, 48]:
                        maze[p] = new_item()
                if ppos in positions:
                    phealth = 0
                bhealth = 0
            if pblock > 0:
                pblock -= 1
            if pblock != 0:
                decision += 1
        if ppos == bpos:
            if psword[1] > bsword[1]:
                bhealth = 0
                psword = ['', 0]
                pscore += int(random.randint(20, 25) * bscore * 0.01)
            elif bsword[1] > psword[1]:
                phealth = 0
                bsword = ['', 0]
                bscore += int(random.randint(20, 25) * pscore * 0.01)
            elif ((pmax + pscore) > (bmax + bscore)):
                bhealth = 0
                psword = ['', 0]
                pscore += int(random.randint(20, 25) * bscore * 0.01)
            elif ((pmax + pscore) < (bmax + bscore)):
                phealth = 0
                bsword = ['', 0]
                bscore += int(random.randint(20, 25) * pscore * 0.01)
            elif random.choice(['p', 'b']) == 'p':
                bhealth = 0
                psword = ['', 0]
                pscore += int(random.randint(20, 25) * bscore * 0.01)
            else:
                phealth = 0
                bsword = ['', 0]
                bscore += int(random.randint(20, 25) * pscore * 0.01)
        if prev_pos not in [0, 48]:
            maze[prev_pos] = new_item()
        elif prev_pos == 0:
            maze[0] = ':regional_indicator_o:'
        else:
            maze[48] = ':o2:'
        if phealth > pmax:
            phealth = pmax
        if bhealth > bmax:
            bhealth = bmax
        if ppoison[0] != '':
            phealth -= ppoison[1]
        if bpoison[0] != '':
            bhealth -= bpoison[1]
        for i in range(1, 48):
            if maze[i] == '<:goblin:860809948618817537>':
                positions = flamethrower_goblin(maze, i, ['<:energy_stone:860810158548844564>','<:power_stone:860810175195250698>'])
                if positions != 0:
                    for p in positions:
                        maze[p] = new_item()
            elif maze[i] == '<:web:860809911973838848>':
                maze[i] = '<:spider:860809969263575060>'
            elif maze[i] == '<:spider:860809969263575060>':
                maze[i] = '<:web:860809911973838848>'
            elif maze[i] == ':bomb:':
                maze[i] = '<:bomb1:860810042508967936>'
            elif maze[i] == '<:bomb1:860810042508967936>':
                maze[i] = '<:bomb2:860810062720532510>'
            elif maze[i] == '<:bomb2:860810062720532510>':
                maze[i] = '<:bomb3:860810082006073355>'
            elif maze[i] == '<:bomb3:860810082006073355>':
                maze[i] = new_item()
                positions = bomb(i)
                for p in positions:
                    if p not in [0, 48]:
                        maze[p] = new_item()
                if bpos in positions:
                    bhealth = 0
                if ppos in positions:
                    phealth = 0
        for i in range(1, 48):
            if maze[i] == ':high_brightness:':
                maze[i] = '<:power_stone:860810175195250698>'
            elif maze[i] == ':low_brightness:':
                maze[i] = '<:energy_stone:860810158548844564>'
        if phealth <= 0:
            logs += "\n**" + ctx.author.name + "** died."
            if pmax != 6:
                pmax -= 1
            phealth = pmax
            ppoison = ['', 0]
            psword = ['', 0]
            maze[ppos] = new_item()
            ppos = 0
            pscore -= int(random.randint(20, 25) * pscore * 0.01)
        if bhealth <= 0:
            logs += "\n**{}** died.".format(arg1.display_name)
            if bmax != 6:
                bmax -= 1
            bhealth = bmax
            bpoison = ['', 0]
            bsword = ['', 0]
            maze[bpos] = new_item()
            bpos = 48
            bscore -= int(random.randint(20, 25) * bscore * 0.01)
        maze[ppos] = '<:knight1:860809539698950184>'
        maze[bpos] = '<:knight2:860809565577543691>'
        decision += 1
    if pscore + bscore < 250:
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return

    # key holder-----------------------------------------------------
    decision = 1
    ppos = pblock = bblock = 0
    bpos = 48
    boss_health = 1
    boss_pos = 24
    clone_count = 0
    fake_pos = ['', '']

    def display_maze2(maze):
        string = ':purple_square::purple_square::purple_square::lock::lock::lock::purple_square::purple_square:'
        for i in range(7):
            if i == 2:
                string += ':purple_square:\n:lock:'
            elif i in [3, 4]:
                string += ':lock:\n:lock:'
            elif i == 5:
                string += ':lock:\n:purple_square:'
            else:
                string += ':purple_square:\n:purple_square:'
            for j in range(7):
                string += maze[i * 7 + j]
        string += ':purple_square:\n:purple_square::purple_square::purple_square::lock::lock::lock::purple_square::purple_square::purple_square:\n\n'
        return string

    def new_item2(position, clone_count, fake_pos):
        if position in [9, 10, 11, 15, 19, 21, 27, 29, 33, 37, 38, 39]:
            item = ':stop_button:'
        elif position in [1, 2, 3, 4, 5, 6, 7, 13, 35, 41, 42, 43, 44, 45, 46, 47]:
            item = '<:fake_potion:860809831891861534>'
        elif position in [8, 12, 14, 20, 28, 34, 36, 40]:
            item = '<:blue_potion:860809767411515392>'
        elif position == boss_pos:
            item = '<:key_possessor:861563898237681684>'
        elif clone_count >= 5 and position in fake_pos:
            item = '<:key_possessor:861563898237681684>'
        elif position == 0:
            item = ':regional_indicator_o:'
        elif position == 48:
            item = ":o2:"
        else:
            item = '<:red_potion:860809787021197323>'
        return item

    logs = ''
    while 1:
        for i in range(0, 49):
            maze[i] = new_item2(i, clone_count, fake_pos)
        maze[ppos] = '<:knight1:860809539698950184>'
        maze[bpos] = '<:knight2:860809565577543691>'
        string = display_maze2(maze)
        embed = discord.Embed(title=':skull: DIE DUNGEON :skull:', description=string, color=0x7F00FF)
        string = ":small_blue_diamond: <:game_heart:848505744063332392> : " + str(phealth) + "/" + str(pmax) + ' '
        if ppoison[0] != '':
            string += "," + ppoison[0] + '(' + str(ppoison[1]) + ')'
        string += "\n:small_blue_diamond: __Sword__ : <:mace:861577541029330986>[∞]"
        embed.add_field(name="<:knight1:860809539698950184> **" + ctx.author.name + "'s stats :**",value=string + '\n:small_blue_diamond: __Objective__ : kill key possessor.', inline=True)
        string = ":small_blue_diamond: <:game_heart:848505744063332392> : " + str(bhealth) + "/" + str(bmax) + ' '
        if bpoison[0] != '':
            string += "," + bpoison[0] + '(' + str(bpoison[1]) + ')'
        string += "\n:small_blue_diamond: __Sword__ : <:mace:861577541029330986>[∞]"
        embed.add_field(name="<:knight2:860809565577543691> **{}'s stats :**".format(arg1.display_name),value=string + '\n:small_blue_diamond: __Objective__ : kill key possessor.\n\n' + logs,inline=True)
        embed.set_footer(text="'exit' to abort.")
        await ctx.send(embed=embed)
        logs = ''
        if decision % 2 != 0 and pblock == 0:
            string1 = await ctx.send("**" + ctx.author.name + "** turn .. <a:diceroll:855341301993701386>")
            time.sleep(1.5)
            dice = random.randint(1, 6)
            await string1.edit(content="**" + ctx.author.name + "** turn .. " + dice_num[dice - 1] + "\nChoose direction (`u`,`d`,`l`,`r`):")
            t2 = flag = 0
            prev_pos = -1
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(ctx.author), timeout=120 - t2)
                    if msg.content.lower() == 'exit':
                        flag = -1
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        break
                    elif msg.content.lower() in ['u', 'd', 'l', 'r', 'up', 'right', 'down', 'left']:
                        prev_pos = ppos
                        ppos = new_pos(msg.content.lower(), ppos, dice)
                        if ppos == 48:
                            await msg.add_reaction('\N{CROSS MARK}')
                            ppos = prev_pos
                        else:
                            turnmissed = 0
                            flag = 1
                            break
                    t2 += int(time.time() - t1)
            except asyncio.TimeoutError:
                turnmissed += 1
            if turnmissed == 2:
                await ctx.send("looks like both player fell asleep,aborted.")
                break
            elif flag == -1:
                break
            elif prev_pos == -1:
                await ctx.send(ctx.author.mention + ' missed their turn.')
            elif maze[ppos] == ':stop_button:':
                logs = ">**" + ctx.author.name + "** got freezed (two turns blocked)."
                pblock = 3
                bblock = 0
            elif maze[ppos] == '<:blue_potion:860809767411515392>':
                phealth += dice
                logs = ">**" + ctx.author.name + "** got healed."
            elif maze[ppos] in '<:red_potion:860809787021197323>':
                phealth += dice
                if len(ppoison[0]) == 0:
                    logs = ">**" + ctx.author.name + "** got healed."
                else:
                    ppoison = ['', 0]
                    logs = ">**" + ctx.author.name + "** got healed (poison removed)."
            elif maze[ppos] in '<:fake_potion:860809831891861534>':
                if random.choice(['<:blue_potion:860809767411515392>','<:poison:860809812350074891>']) == '<:poison:860809812350074891>':
                    logs = ">**" + ctx.author.name + "** drank fake potion and got poisoned."
                    ppoison[0] = '<:poison:860809812350074891>'
                    ppoison[1] += 1
                else:
                    logs = ">**" + ctx.author.name + "** drank fake potion but healed **{}**.".format(arg1.display_name)
                    bhealth += dice
            elif clone_count >= 5 and ppos in fake_pos:
                logs = ">**" + ctx.author.name + "** killed...oh,it was a clone!"
                fake_pos.remove(fake_pos[-1])
            elif ppos == boss_pos:
                score = random.randint(50, 70)
                logs = ">**" + ctx.author.name + "** killed <:key_possessor:861563898237681684>(+" + str(score) + " synergy)."
                pscore += score
                boss_health = 0
            elif ppos == bpos:
                bhealth = 0
            if bblock > 0:
                bblock -= 1
            if bblock != 0:
                decision += 1
        elif decision % 2 == 0 and bblock == 0:
            string1 = await ctx.send("**{}** turn .. <a:diceroll:855341301993701386>".format(arg1.display_name))
            time.sleep(1.5)
            dice = random.randint(1, 6)
            await string1.edit(content="**{}** turn .. ".format(arg1.display_name) + dice_num[dice - 1] + "\nChoose direction (`u`,`d`,`l`,`r`):")
            t2 = flag = 0
            prev_pos = -1
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(arg1._user), timeout=120 - t2)
                    if msg.content.lower() == 'exit':
                        flag = -1
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        break
                    elif msg.content.lower() in ['u', 'd', 'l', 'r', 'up', 'right', 'down', 'left']:
                        prev_pos = bpos
                        bpos = new_pos(msg.content.lower(), bpos, dice)
                        if bpos == 0:
                            await msg.add_reaction('\N{CROSS MARK}')
                            bpos = prev_pos
                        else:
                            turnmissed = 0
                            flag = 1
                            break
                    t2 += int(time.time() - t1)
            except asyncio.TimeoutError:
                turnmissed += 1
            if turnmissed == 2:
                await ctx.send("looks like both player fell asleep,aborted.")
                break
            elif flag == -1:
                break
            elif prev_pos == -1:
                await ctx.send('{} missed their turn.'.format(arg1.mention))
            elif maze[bpos] == ':stop_button:':
                logs = ">**{}** got freezed (two turns blocked).".format(arg1.display_name)
                bblock = 3
                pblock = 0
            elif maze[bpos] == '<:blue_potion:860809767411515392>':
                bhealth += dice
                logs = ">**{}** got healed.".format(arg1.display_name)
            elif maze[bpos] in '<:red_potion:860809787021197323>':
                bhealth += dice
                if len(bpoison[0]) == 0:
                    logs = ">**{}** got healed.".format(arg1.display_name)
                else:
                    bpoison = ['', 0]
                    logs = ">**{}** got healed (poison removed).".format(arg1.display_name)
            elif maze[bpos] in '<:fake_potion:860809831891861534>':
                if random.choice(['<:blue_potion:860809767411515392>','<:poison:860809812350074891>']) == '<:poison:860809812350074891>':
                    logs = ">**{}** drank fake potion and got poisoned.".format(arg1.display_name)
                    bpoison[0] = '<:poison:860809812350074891>'
                    bpoison[1] += 1
                else:
                    logs = ">**{}** drank fake potion but healed **".format(arg1.display_name) + ctx.author.name + "**."
                    phealth += dice
            elif clone_count >= 5 and bpos in fake_pos:
                logs = ">**{}** killed...oh,it was a clone!".format(arg1.display_name)
                fake_pos.remove(fake_pos[-1])
            elif bpos == boss_pos:
                score = random.randint(50, 70)
                logs = ">**{}** killed <:key_possessor:861563898237681684>(+".format(arg1.display_name) + str(score) + " synergy)."
                bscore += score
                boss_health = 0
            elif bpos == ppos:
                phealth = 0
            if pblock > 0:
                pblock -= 1
            if pblock != 0:
                decision += 1
        if boss_health == 1:
            list = [16, 17, 18, 22, 23, 24, 25, 26, 30, 31, 32]
            if bpos in list:
                list.remove(bpos)
            if ppos in list:
                list.remove(ppos)
            boss_pos = random.choice(list)
        else:
            break
        if prev_pos in [0, 49]:
            maze[prev_pos] = new_item2(prev_pos, clone_count, fake_pos)
        if clone_count <= 6:
            clone_count += 1
            if clone_count in [5, 6]:
                list.remove(boss_pos)
                random.shuffle(list)
                if len(fake_pos) == 2:
                    fake_pos[0] = list[0]
                    fake_pos[1] = list[1]
                else:
                    fake_pos[0] = list[0]
            elif clone_count == 7:
                clone_count = 0
                fake_pos = ['', '']
        if phealth > pmax:
            phealth = pmax
        if bhealth > bmax:
            bhealth = bmax
        if ppoison[0] != '':
            phealth -= ppoison[1]
        if bpoison[0] != '':
            bhealth -= bpoison[1]
        if phealth <= 0:
            logs += "\n**{}** killed **".format(arg1.display_name) + ctx.author.name + "**."
            if pmax != 6:
                pmax -= 1
            phealth = pmax
            ppoison = ['', 0]
            maze[ppos] = new_item2(prev_pos, clone_count, fake_pos)
            ppos = 0
            pscore -= int(random.randint(10, 15) * pscore * 0.01)
            pblock = 0
        if bhealth <= 0:
            logs += "\n**" + ctx.author.name + "** killed **{}**.".format(arg1.display_name)
            if bmax != 6:
                bmax -= 1
            bhealth = bmax
            bpoison = ['', 0]
            maze[bpos] = new_item2(prev_pos, clone_count, fake_pos)
            bpos = 48
            bscore -= int(random.randint(10, 15) * bscore * 0.01)
            bblock = 0
        decision += 1
    if boss_health != 0:
        command_usage.remove(ctx.author.id)
        command_usage.remove(arg1._user.id)
        return
    # find key-----------------------------------------
    ppoison = ['', 0]
    bpoison = ['', 0]
    pobjective = " find <:blue_key:860810213087379476>."
    bobjective = " find <:red_key:860810230702145556>."
    pvertical = [':lock:', ':lock:', ':lock:']
    phorizontal = pvertical.copy()
    bvertical = pvertical.copy()
    bhorizontal = pvertical.copy()
    if abs(pscore - bscore) <= 50:
        max = 6
    elif abs(pscore - bscore) <= 100:
        max = 7
    elif abs(pscore - bscore) <= 150:
        max = 8
    elif abs(pscore - bscore) <= 200:
        max = 9
    elif abs(pscore - bscore) <= 250:
        max = 10
    else:
        max = 11
    pos = []
    key_pos1 = []
    key_pos2 = []
    for i in range(1, 48):
        if i not in [6, 42, 24]:
            pos.append(i)
    random.shuffle(pos)
    for i in range(12):
        if i < max:
            key_pos1.append(pos.pop())
        else:
            key_pos2.append(pos.pop())
    if pscore >= bscore:
        pkey_pos = key_pos1.copy()
        bkey_pos = key_pos2.copy()
    else:
        bkey_pos = key_pos1.copy()
        pkey_pos = key_pos2.copy()
    j = 1
    key_pos1 = -1
    key_pos2 = -1
    poison = []
    potion = []
    for i in pos:
        if j % 2 == 0:
            poison.append(i)
        else:
            potion.append(i)
        j += 1

    def display_maze3(maze, phorizontal, pvertical, bhorizontal, bvertical):
        string = ':brown_square::brown_square::brown_square:' + phorizontal[0] + phorizontal[1] + phorizontal[2] + ':brown_square::brown_square:'
        for i in range(7):
            if i == 2:
                string += ':brown_square:\n' + pvertical[0]
            elif i == 3:
                string += bvertical[0] + '\n' + pvertical[1]
            elif i == 4:
                string += bvertical[1] + '\n' + pvertical[2]
            elif i == 5:
                string += bvertical[2] + '\n:brown_square:'
            else:
                string += ':brown_square:\n:brown_square:'
            for j in range(7):
                string += maze[i * 7 + j]
        string += ':brown_square:\n:brown_square::brown_square::brown_square:' + bhorizontal[0] + bhorizontal[1] +bhorizontal[2] + ':brown_square::brown_square::brown_square:\n\n'
        return string

    def new_item3(position, pkey_pos, bkey_pos, potion):
        if position in pkey_pos:
            return '<:blue_key:860810213087379476>'
        elif position in bkey_pos:
            return '<:red_key:860810230702145556>'
        elif position in potion:
            return '<:red_potion:860809787021197323>'
        elif position == 0:
            return ':regional_indicator_o:'
        elif position == 48:
            return ':o2:'
        elif position in [6, 42]:
            return ':fire:'
        elif position == 24:
            return ':arrows_counterclockwise:'
        else:
            return random.choice(['<:poison:860809812350074891>', '<:snake:860809990163660830>'])

    while 1:
        for i in range(49):
            maze[i] = new_item3(i, pkey_pos, bkey_pos, potion)
        maze[ppos] = '<:knight1:860809539698950184>'
        maze[bpos] = '<:knight2:860809565577543691>'
        string = display_maze3(maze, phorizontal, pvertical, bhorizontal, bvertical)
        embed = discord.Embed(title=':skull: DIE DUNGEON :skull:', description=string, color=0x7F00FF)
        string = ":small_blue_diamond: <:game_heart:848505744063332392> : " + str(phealth) + "/ " + str(pmax) + ' '
        if ppoison[0] != '':
            string += "," + ppoison[0] + '(' + str(ppoison[1]) + ')'
        embed.add_field(name="<:knight1:860809539698950184> **" + ctx.author.name + "'s stats :**",value=string + '\n:small_blue_diamond: __Objective__ : ' + pobjective, inline=True)
        string = ":small_blue_diamond: <:game_heart:848505744063332392> : " + str(bhealth) + "/ " + str(bmax) + ' '
        if bpoison[0] != '':
            string += "," + bpoison[0] + '(' + str(bpoison[1]) + ')'
        embed.add_field(name="<:knight2:860809565577543691> **{}'s stats :**".format(arg1.display_name),value=string + '\n:small_blue_diamond: __Objective__ : ' + bobjective + '\n\n' + logs,inline=True)
        embed.set_footer(text="'exit' to abort.")
        await ctx.send(embed=embed)
        logs = ''
        if decision % 2 != 0:
            string1 = await ctx.send("**" + ctx.author.name + "** turn .. <a:diceroll:855341301993701386>")
            time.sleep(1.5)
            dice = random.randint(1, 6)
            await string1.edit(content="**" + ctx.author.name + "** turn .. " + dice_num[dice - 1] + "\nChoose direction (`u`,`d`,`l`,`r`):")
            t2 = flag = 0
            prev_pos = -1
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(ctx.author), timeout=120 - t2)
                    if msg.content.lower() == 'exit':
                        flag = -1
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        break
                    elif msg.content.lower() in ['u', 'd', 'l', 'r', 'up', 'right', 'down', 'left']:
                        prev_pos = ppos
                        ppos = new_pos(msg.content.lower(), ppos, dice)
                        if ppos == 48 or ppos == bpos:
                            await msg.add_reaction('\N{CROSS MARK}')
                            ppos = prev_pos
                        else:
                            turnmissed = 0
                            flag = 1
                            break
                    t2 += int(time.time() - t1)
            except asyncio.TimeoutError:
                turnmissed += 1
            if turnmissed == 2:
                await ctx.send("looks like both player fell asleep,aborted.")
                break
            elif flag == -1:
                break
            elif prev_pos == -1:
                await ctx.send(ctx.author.mention + ' missed their turn.')
            elif key_pos1 != -1:
                if ppos % 7 in [2, 3, 4]:
                    if (msg.content.lower() in ['u', 'up'] and dice == int(prev_pos / 7) + 1) or (msg.content.lower() in ['d', 'down'] and dice + int(prev_pos / 7) == 7):
                        flag = 2
                        phorizontal[(prev_pos % 7) - 2] = '<:knight1:860809539698950184>'
                if int(ppos / 7) in [2, 3, 4]:
                    if (msg.content.lower() in ['l', 'left'] and dice == (prev_pos % 7) + 1) or (msg.content.lower() in ['r', 'right'] and dice + (prev_pos % 7) == 7):
                        flag = 2
                        pvertical[int(prev_pos / 7) - 2] = '<:knight1:860809539698950184>'
            if maze[ppos] in '<:red_potion:860809787021197323>':
                phealth += dice
                if len(ppoison[0]) == 0:
                    logs = ">**" + ctx.author.name + "** got healed."
                else:
                    ppoison = ['', 0]
                    logs = ">**" + ctx.author.name + "** got healed (poison removed)."
            elif maze[ppos] in ['<:poison:860809812350074891>', '<:snake:860809990163660830>']:
                logs = ">**" + ctx.author.name + "** got poisoned"
                if maze[ppos] == '<:snake:860809990163660830>':
                    logs += ' by <:snake:860809990163660830>'
                logs += '.'
                ppoison[0] = '<:poison:860809812350074891>'
                ppoison[1] += 1
            elif maze[ppos] in ':fire:':
                phealth = 0
            elif maze[ppos] in ':arrows_counterclockwise:':
                decision += 1
            elif ppos in pkey_pos and key_pos1 == -1:
                key_pos1 = ppos
                pkey_pos.remove(ppos)
                phorizontal = [':blue_square:', ':blue_square:', ':blue_square:']
                pvertical = phorizontal.copy()
                pobjective = ' reach :blue_square:.'
        elif decision % 2 == 0:
            string1 = await ctx.send("**{}** turn .. <a:diceroll:855341301993701386>".format(arg1.display_name))
            time.sleep(1.5)
            dice = random.randint(1, 6)
            await string1.edit(content="**{}** turn .. ".format(arg1.display_name) + dice_num[dice - 1] + "\nChoose direction (`u`,`d`,`l`,`r`):")
            t2 = flag = 0
            prev_pos = -1
            try:
                while 1:
                    t1 = time.time()
                    msg = await client.wait_for('message', check=check(arg1._user), timeout=120 - t2)
                    if msg.content.lower() == 'exit':
                        flag = -1
                        await msg.add_reaction('\N{OCTAGONAL SIGN}')
                        break
                    elif msg.content.lower() in ['u', 'd', 'l', 'r', 'up', 'right', 'down', 'left']:
                        prev_pos = bpos
                        bpos = new_pos(msg.content.lower(), bpos, dice)
                        if bpos == 0 or ppos == bpos:
                            await msg.add_reaction('\N{CROSS MARK}')
                            bpos = prev_pos
                        else:
                            turnmissed = 0
                            flag = 1
                            break
                    t2 += int(time.time() - t1)
            except asyncio.TimeoutError:
                turnmissed += 1
            if turnmissed == 2:
                await ctx.send("looks like both player fell asleep,aborted.")
                break
            elif flag == -1:
                break
            elif prev_pos == -1:
                await ctx.send('{} missed their turn.'.format(arg1.display_name))
            elif key_pos2 != -1:
                if bpos % 7 in [2, 3, 4]:
                    if (msg.content.lower() in ['u', 'up'] and dice == int(prev_pos / 7) + 1) or (msg.content.lower() in ['d', 'down'] and dice + int(prev_pos / 7) == 7):
                        flag = 3
                        bhorizontal[(prev_pos % 7) - 2] = '<:knight2:860809565577543691>'
                if int(ppos / 7) in [2, 3, 4]:
                    if (msg.content.lower() in ['l', 'left'] and dice == (prev_pos % 7) + 1) or (msg.content.lower() in ['r', 'right'] and dice + (prev_pos % 7) == 7):
                        flag = 3
                        bvertical[int(prev_pos / 7) - 2] = '<:knight2:860809565577543691>'
            if maze[bpos] in '<:red_potion:860809787021197323>':
                bhealth += dice
                if len(bpoison[0]) == 0:
                    logs = ">**{}** got healed.".format(arg1.display_name)
                else:
                    bpoison = ['', 0]
                    logs = ">**{}** got healed (poison removed).".format(arg1.display_name)
            elif maze[bpos] in ['<:poison:860809812350074891>', '<:snake:860809990163660830>']:
                logs = ">**{}** got poisoned".format(arg1.display_name)
                if maze[bpos] == '<:snake:860809990163660830>':
                    logs += ' by <:snake:860809990163660830>'
                logs += '.'
                bpoison[0] = '<:poison:860809812350074891>'
                bpoison[1] += 1
            elif maze[bpos] in ':fire:':
                bhealth = 0
            elif maze[bpos] in ':arrows_counterclockwise:':
                decision += 1
            elif bpos in bkey_pos and key_pos2 == -1:
                key_pos2 = bpos
                bkey_pos.remove(bpos)
                bhorizontal = [':red_square:', ':red_square:', ':red_square:']
                bvertical = bhorizontal.copy()
                bobjective = ' reach :red_square:.'
        if phealth > pmax:
            phealth = pmax
        if bhealth > bmax:
            bhealth = bmax
        if ppoison[0] != '':
            phealth -= ppoison[1]
        if bpoison[0] != '':
            bhealth -= bpoison[1]
        if phealth <= 0:
            logs += "\n**" + ctx.author.name + "** died"
            if key_pos1 != -1:
                logs += 'and lost the key'
            logs += '.'
            if pmax != 6:
                pmax -= 1
            phealth = pmax
            ppoison = ['', 0]
            pkey_pos.append(key_pos1)
            key_pos1 = -1
            maze[ppos] = new_item3(i, pkey_pos, bkey_pos, potion)
            ppos = 0
            pobjective = " find <:blue_key:860810213087379476>."
            pvertical = [':lock:', ':lock:', ':lock:']
            phorizontal = pvertical.copy()
        if bhealth <= 0:
            logs += "\n**{}** died".format(arg1.display_name)
            if key_pos2 != -1:
                logs += 'and lost the key'
            logs += '.'
            if bmax != 6:
                bmax -= 1
            bhealth = bmax
            bpoison = ['', 0]
            bkey_pos.append(key_pos2)
            key_pos2 = -1
            maze[bpos] = new_item3(i, pkey_pos, bkey_pos, potion)
            bpos = 48
            bobjective = " find <:red_key:860810230702145556>."
            bvertical = [':lock:', ':lock:', ':lock:']
            bhorizontal = bvertical.copy()
        if flag == 2:
            logs = ">**" + ctx.author.name + "** escaped.\n:crown: **" + ctx.author.name + "** won :crown:"
            break
        elif flag == 3:
            logs = ">**{}** escaped.".format(arg1.display_name) + "\n:crown: **{}** won :crown:".format(arg1.display_name)
            break
        decision += 1
    if flag == 2 or flag == 3:
        string = ':brown_square::brown_square::brown_square:' + phorizontal[0] + phorizontal[1] + phorizontal[ 2] + ':brown_square::brown_square:'
        for i in range(7):
            if i == 2:
                string += ':brown_square:\n' + pvertical[0]
            elif i == 3:
                string += bvertical[0] + '\n' + pvertical[1]
            elif i == 4:
                string += bvertical[1] + '\n' + pvertical[2]
            elif i == 5:
                string += bvertical[2] + '\n:brown_square:'
            else:
                string += ':brown_square:\n:brown_square:'
            for j in range(7):
                string += ':fire:'
        string += ':brown_square:\n:brown_square::brown_square::brown_square:' + bhorizontal[0] + bhorizontal[1] + bhorizontal[2] + ':brown_square::brown_square::brown_square:\n\n'
        await ctx.send(embed=discord.Embed(title=':skull: DIE DUNGEON :skull:', description=string + '\n\n' + logs, color=0x7F00FF))
    command_usage.remove(ctx.author.id)
    command_usage.remove(arg1._user.id)

@client.command()
@commands.cooldown(1,3600,commands.BucketType.user)
async def emojiscope(ctx):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    place=['<a:slot_emoji:855461906407358524>','<a:slot_emoji:855461906407358524>','<a:slot_emoji:855461906407358524>']
    emoji=[':grinning:',':rofl:',':face_with_symbols_over_mouth:',':hot_face:',':cold_face:',':skull:',':clap:',':kiss:',':brain:',':person_running:',':ring:',':wilted_rose:',':boom:',':sweat_drops:',':champagne:',':first_place:',':slot_machine:',':train2:',':flying_saucer:',':moyai:',':watch:',':hourglass:',':money_with_wings:',':knife:',':headstone:',':hole:',':mouse_trap:',':tada:',':chart_with_upwards_trend:',':broken_heart:',':cupid:',':no_mobile_phones:',':zzz:',':confounded:',':manual_wheelchair:',':monkey_face:']
    for i in range(4):
        string='<:1bend:855370229806530591><:hstand:855370417963008000><:tup:855370277542166538><:hstand:855370417963008000><:tup:855370277542166538><:hstand:855370417963008000><:2bend:855370326781984809>\n'
        string+='<:vstand:855369922153414666>'+place[0]+'<:vstand:855369922153414666>'+place[1]+'<:vstand:855369922153414666>'+place[2]+'<:vstand:855369922153414666><:handle:855389038084096020>\n'
        string+='<:3bend:855370083916054538><:hstand:855370417963008000><:tdownr:855384917638905857><:hstand:855370417963008000><:tdownl:855384318116495370><:hstand:855370417963008000><:4bend:855370177033273365>\n'
        string+='<:blank:855369446436896778><:blank:855369446436896778><:rstand:855369632718520342>:white_medium_small_square:<:lstand:855369509371379753>\n'
        string+='<:blank:855369446436896778><:blank:855369446436896778><:rstand:855369632718520342>:white_medium_small_square:<:lstand:855369509371379753>'
        embed=discord.Embed(description=string, color=0x7F00FF)
        embed.set_author(name=ctx.author.display_name + "'s emojiscope:", icon_url=ctx.author.avatar_url)
        embed.set_footer(text='command is usable again in 1 hour.')
        if i==0:
            string1=await ctx.send(embed=embed)
        else:
            await string1.edit(embed=embed)
        if i ==  0:
            place[0]=random.choice(emoji)
            time.sleep(2)
        elif i==1:
            place[1]=random.choice(emoji)
            time.sleep(2)
        elif i==2:
            place[2]=random.choice(emoji)
            time.sleep(2)
    await ctx.send(place[0]+','+place[1]+' and '+place[2]+' defines your next hour,**'+ctx.author.name+'**.')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        x = int(error.retry_after)
        if x>60:
            min=int(x/60)
            sec=x-min*60
            await ctx.send(ctx.author.mention + f",you are on cooldown.\nTry again in **" + str(min) + "m " + str(sec) + "s**.")
        else:
            await ctx.send(ctx.author.mention + f",you are on cooldown.\nTry again in **" + str(x) + "s**.")

@client.command()
async def help(ctx,arg0=None,arg1=None):
    if ctx.author.id in command_usage:
        await ctx.send(ctx.author.mention + ',end your current game to use another command.')
        return
    if arg0==None and arg1==None:
        embed=discord.Embed(description="To get info about a specific command , use `teko help [command]`.\nEx: `teko help colorix`,`teko help duel`,etc.\n",color=0x7F00FF)
        embed.set_author(name=ctx.author.display_name + ",here's the command list:", icon_url=ctx.author.avatar_url)
        embed.add_field(name="<:tenth:853876310279847986> __COLORIX__ <:tenth:853876310279847986>",value="`teko colorix`",inline=False)
        embed.add_field(name=":interrobang: __GUESS THE NUMBER__ :interrobang:",value="`teko gtn`",inline=False)
        embed.add_field(name="<:blue0:853560137707683851> __KUROMASU__ <:blue6:853560257744994364>",value="`teko kuromasu`",inline=False)
        embed.add_field(name=":o: __TIC-TAC-TOE__ :x:", value="`teko tictactoe` : play with bot.\n`teko tictactoe @user` : play with friend.", inline=False)
        embed.add_field(name=":chopsticks: __CHOPSTICKS__ :chopsticks:",value="`teko chopsticks` : play with bot.\n`teko chopsticks @user` : play with friend.",inline=False)
        embed.add_field(name=":arrow_up: __HIGHER-LOWER__ :arrow_down:",value="`teko higherlower` : play with bot.\n`teko higherlower @user` : play with friend.",inline=False)
        embed.add_field(name="<:demonic_axe:846721643216371762> __QUICK BATTLE__ <:demonic_axe:846721643216371762>",value="`teko quickbattle` : play with bot.\n`teko quickbattle @user` : play with friend.",inline=False)
        embed.add_field(name=":person_running: __SURVIVORS VS KILLER__ :knife:",value="`teko svk` : play with bot.\n`teko svk @user` : play with friend.",inline=False)
        embed.add_field(name=":chart_with_upwards_trend: __ULTIMATE TIC-TAC-TOE__ :chart_with_upwards_trend:",value="`teko tictactoe2` : play with bot.\n`teko tictactoe2 @user` : play with friend.", inline=False)
        embed.add_field(name="<:map:854786538175856670> __TREASURE HUNT__ <:map:854786538175856670>",value="`teko treasurehunt` : play with bot.\n`teko treasurehunt @user` : play with friend.",inline=False)
        embed.add_field(name=":moneybag: __BANKROB__ :moneybag:",value="`teko bankrob` : play alone.\n`teko bankrob @user` : play with friend.",inline=False)
        embed.add_field(name="<:mole:852848674479931423> __WHACK-A-MOLE__ <:mole:852848674479931423>",value="`teko wam` : play alone.\n`teko wam @user` : play with friend.",inline=False)
        embed.add_field(name=":magic_wand: __SPELLBIND__ :magic_wand:",value="`teko spellbind @user` : play with friend.",inline=False)
        embed.add_field(name=":anchor: __BATTLESHIP__ :anchor:",value="`teko battleship @user` : play with friend.", inline=False)
        embed.add_field(name="<:knight1:860412559445458954> __BLIND RUN__ <:knight2:860410717735747614>", value="`teko blindrun @user` : play with friend.",inline=False)
        embed.add_field(name=":skull: __DIE DUNGEON__ :skull:", value="`teko diedungeon @user` : play with friend.",inline=False)
        embed.add_field(name=":cowboy: __DUEL__ :cowboy:", value="`teko duel @user` : play with friend.",inline=False)
        embed.add_field(name=":sos: __SOS__ :sos:", value="`teko sos @user` : play with friend.", inline=False)
        embed.add_field(name=":lion_face: __ADU HULI__ :lion_face:", value="`teko aduhuli @user` : play with friend.",inline=False)
        embed.add_field(name=":blue_circle: __CONNECT 4__ :red_circle:", value="`teko connect4 @user` : play with friend.",inline=False)
        embed.add_field(name="<:sumo1side:852926755835478078> __SUMO__ <:sumo2side:852936504165531718>", value="`teko sumo @user` : play with friend.",inline=False)
        string=":small_orange_diamond: `teko ques [question]` : ask any question.\n"
        string+=":small_orange_diamond: `teko rps [r/p/s]` : play the rock-paper-scissors with bot.\n"
        string+=":small_orange_diamond: `teko cf [h/t]` : flip a coin.\n"
        string += ":small_orange_diamond: `teko rolldice` : roll dice.\n"
        string += ":small_orange_diamond: `teko emojiscope` : check your hourly emojiscope in slot machine!?\n"
        string+=":small_orange_diamond: `teko cupid [argument/@user]` : check intimacy between you and argument/@user.\n"
        string+=':small_orange_diamond: `teko av` : display avatar.\n'
        embed.add_field(name="__MISCELLANEOUS COMMANDS__", value=string,inline=False)
        await ctx.send(embed=embed)
    elif arg0=='chopsticks' or arg0=='chopstick':
        if arg1==None:
            string='**__Page 1__** : A quick insight into the game.\n**__Page 2__** : Game layout and controls.'
            string+='\n\nTo surf a particular page:\n`teko help chopsticks [page]`'
            await ctx.send(embed=discord.Embed(title='__**CHOPSTICKS GUIDE**__',description=string,color=0x7F00FF))
        elif arg1=='1':
            string=':small_orange_diamond: **Chopsticks** is a hand game in which both players extend their fingers from each hand and transfer ' \
                   'fingers by taking turns to tap one hand against another.\n\n:small_orange_diamond: Each player begins with one finger on each hand.' \
                   "On player's turn,they must either **attack** or **split**.\n\n:small_orange_diamond: To **attack**,a player uses one of their live hands" \
                   " and attacks on opponent's live hand.The number of fingers on opponent's struck hand will increase by number of fingers on the hand " \
                   "used to strike.\nEx: If player attacks with left hand (having 2 fingers) on opponent's right hand (having 1 finger),then resultant " \
                   "fingers on opponent hand will become 2+1=3.\n\n:small_orange_diamond: If any hand reaches five fingers , then that hand gets eliminated." \
                   "If any hand exceeds five fingers,then five fingers gets subtracted from that hand.\nEx: If a 4-finger hand strikes a 3-finger hand,then " \
                   " sum will be 7 (which exceeds 5).Hence the resultant fingers on opponent hand will be 7-5=2.\n\n:small_orange_diamond: With **split**," \
                   "players can re-distribute the number of fingers on their hands in such a way that total sum of fingers before and after splitting remains same.\nEx: If left hand = 2 fingers and right hand = 1 fingers,then player can split" \
                   " in following ways:\ni) left hand = 0 fingers, right hand = 3 fingers\nii) left hand = 1 fingers, right hand = 2 fingers\niii) left hand = 3 fingers, right hand = 0 fingers" \
                   "\n\n:small_orange_diamond: A player can also revive their dead hand using **split** only if other hand has even number of fingers.As " \
                   "such,both hands will have equal fingers.\n:small_orange_diamond: To **win**,the player must eliminate opponent's both hands by raising five fingers on each."
            embed=discord.Embed(title='**__CHOPSTICKS GUIDE__**',description=string,color=0x7F00FF)
            embed.set_footer(text='Page 1/2')
            await ctx.send(embed=embed)
        elif arg1=='2':
            string=":small_orange_diamond: **Game layout** :\n`PLAYER 1\nLH : ↥↥  ,  RH : ↥\nPLAYER 2\nLH : ↥↥↥   ,  RH : ↥↥`\n" \
                   "\nwhere LH and RH represents left hand and right hand respectively and ↥ represents finger.\n\n:small_orange_diamond: **Controls** :" \
                   "\ni) `ll` : tap your left hand on opponent left hand\nii) `lr` : tap your left hand on opponent right hand\niii) `rl` : tap your right hand on opponent left hand" \
                   "\niv) `rr` : tap your right hand on opponent right hand\nv) `split [x] [y]` : split such that there are x and y number of fingers on left hand and right hand respectively" \
                   " (x and y are integers between 0 to 5)\nvi) `split` : revive a dead hand\n\n:small_orange_diamond: **Credits:**  [wikipedia](https://en.m.wikipedia.org/wiki/Chopsticks_(hand_game))"
            embed = discord.Embed(title='**__CHOPSTICKS GUIDE__**', description=string, color=0x7F00FF)
            embed.set_footer(text='Page 2/2')
            await ctx.send(embed=embed)
    elif arg0=='tictactoe':
        string=":small_orange_diamond: **Tic-tac-toe** is a two player game,X and O,who take turns marking their symbol (X or O) in a 3x3 grid.\n\n" \
               ":small_orange_diamond: The player who first places three of their marks diagonally,horizontally or verically wins\n\n:small_orange_diamond: " \
               "**Game layout**:\n  :one: | :two: | :x: |\n  ---------------\n  :four: | :o: | :six: |\n  ---------------\n  :seven: | :o: | :nine: |\n  ---------------\n\n" \
               ":small_orange_diamond: **Controls**: type the corresponding number to mark their.\n\n:small_orange_diamond: **Credits**: [Wikipedia](https://en.m.wikipedia.org/wiki/Tic-tac-toe)"
        embed = discord.Embed(title='**__TIC-TAC-TOE GUIDE__**', description=string, color=0x7F00FF)
        await ctx.send(embed=embed)
    elif arg0 == 'higherlower':
        string=":small_orange_diamond: **Higher-lower** is a two player card game in which a player has to guess whether the next card drawn from the top of the deck will be" \
               " higher or lower in number than the current card number according to the order:\nA<2<3<4<5<6<7<8<9<10<J<Q<K\n\n:small_orange_diamond: If player makes the correct guess,they" \
               " earn a point and play their turn again.\n\n:small_orange_diamond: The game ends when all cards from deck are revealed.The player " \
               "with greater score wins.\n\n:small_orange_diamond: **Game layout**:\n   <:carddeck3:798031475672088606>    <:3red:797796164963401748>" \
               "\nLeft side pile represents the deck of unrevealed cards while right side card represents the current card.\n\n:small_orange_diamond: **Controls: **" \
               "\ni) react :arrow_up: if you think next card number is higher.\nii) react :arrow_down: if you think next card number is lower."
        embed = discord.Embed(title='**__HIGHER-LOWER GUIDE__**', description=string, color=0x7F00FF)
        await ctx.send(embed=embed)
    elif arg0=='quickbattle':
        string=":small_orange_diamond: **QUICK-BATTLE** is a two player turn based game in which both players are given a random gear (sword " \
               "and armor).During their turn, they have to choose whether to **attack**,**block** or **attack while block**.\n\n:small_orange_diamond: " \
               "**Controls:**\ni) react :regional_indicator_a: to attack opponent with sword.\nii) react :regional_indicator_b:" \
               " to block opponent's attack with shield.\niii) react :ab: to attack opponent with sword while blocking their attack with shield." \
               "\n\n:small_orange_diamond: Both players start with 200 HP.In order to win,one must reduce opponent's health to " \
               "0.\n\n:small_orange_diamond: **GEAR INFO:**\n"
        embed = discord.Embed(title='**__QUICK-BATTLE GUIDE__**', description=string, color=0x7F00FF)
        embed.set_image(url='https://i.imgur.com/bnSavnr.png')
        embed.set_footer(text="NOTE:\n• Horned Shield provides some damage (50% AT) while blocking.\n• Cursed Shield provides extra DEF if opponent has Dragon's Axe.\n• Devil's Head provides extra DEF if opponent has Demonic Axe.")
        await ctx.send(embed=embed)
    elif arg0=='duel':
        string=":small_orange_diamond: **Duel** is simply a cowboy standoff in which two cowboys stand face-to-face at a certain distance.\n\n" \
               ":small_orange_diamond: A camera :camera: icon will be shown.As soon as camera flashes :camera_with_flash: ,player has to type `x`" \
               " in order to shoot the opponent.\n\n:small_orange_diamond: First player to type `x` is supposed to pull the trigger and kill the enemy while the other player" \
               " is supposed to miss their shot.\n\n:small_orange_diamond: Both players starts with three health points <:game_heart:848505744063332392> and the first one to shoot two times" \
               " successfully wins."
        embed = discord.Embed(title='**__DUEL GUIDE__**', description=string, color=0x7F00FF)
        await ctx.send(embed=embed)
    elif arg0=='spellbind':
        string=":small_orange_diamond: **Spellbind** is a two player turn based game in which eight cards are displayed on screen.On their turn," \
               " player need to choose two or three cards to caste a spell on opponent.\n\n:small_orange_diamond: There are five types of cards: " \
               "attack cards (<:RED_CARD:792356986410893342>),defense cards (<:BLUE_CARD:792358450155749376>),heal cards (<:GREEN_CARD:792358469500010497>)" \
               ",block cards (<:YELLOW_CARD:792673264266641408>),rare cards (<:RARE_CARD:792661062008700968>).\n>**attack cards** consist of fireball <:fireball:848090622820220938>," \
               "lightning <:lightning:848096066330689567>,ice spear <:ice_spear:848092801639645224>.\n>**Defense cards** consist of stone skin " \
               "<:stoneskin:848099608609816597>,deflect shield <:Deflect_shield:848101470133682186>.\n>**Heal cards** consist of nature call <:nature_call:848110745165758475>,blessing <:blessing:848108213752299550>." \
               "\n>**Block cards** consist of bleeding <:Bleeding:848104514963898388>,deathlock <:deathlock:848122972911829003>.\n>**Rare cards** " \
               "consist of doppelganger <:xoppelganger:848118346154508288>.\n\n:small_orange_diamond: **Controls:** Players have to type the corresponding numbers to pick up cards.\nEx: `23`,`16`,`85`(to pick two cards),`579`(to pick three cards)\n\n" \
               ":small_orange_diamond: **Possible spells:**"
        embed = discord.Embed(title='**__SPELLBIND GUIDE__**', description=string, color=0x7F00FF)
        embed.set_image(url='https://i.imgur.com/uDZQq8c.png')
        embed.set_footer(text="maximum health and defense a player can have is 6 and 3 respectively.")
        await ctx.send(embed=embed)
    elif arg0=='aduhuli':
        if arg1==None:
            string = '**__Page 1__** : A quick insight into the game.\n**__Page 2__** : Game layout and controls.'
            string += '\n\nTo surf a particular page:\n`teko help aduhuli [page]`'
            await ctx.send(embed=discord.Embed(title='__**ADU-HULI GUIDE**__', description=string, color=0x7F00FF))
        elif arg1=='1':
            string=":small_orange_diamond: **Adu Huli Aata/Goats & Tiger/Bagh-Chal** is a two player turn based game in which one player controls tiger and other player controls cattle consisting of" \
                   " 5 animals(cow,pig,monkey,deer and boar).\n\n:small_orange_diamond: The game has two phases: in 1st phase,cattle are put onto board one-by-one" \
                   " on their turn.Then in 2nd phase,cattles are moved.\n\n:small_orange_diamond: Both tiger and cattle are free to move in any adjacent spot (represented by white square " \
                   "in game) on their turn.\n\n:small_orange_diamond: **For tiger to win**,tiger must kill any of the two animals out of five.In order to kill a particular animal," \
                   "tiger must be adjacent to that animal and there should be a vacant spot (near that animal) along the straight line joining tiger and that animal.As such," \
                   "tiger jumps over the animal,lands into the vacant spot and the animal gets eliminated (as shown in fig 1).\n\n:small_orange_diamond: **For cattle to win**" \
                   ",they must surround tiger in such a way that tiger becomes immovable (as shown in fig 2 for example).\n\n:small_orange_diamond: The tiger can only be" \
                   " surrounded by 4 or 5 animals.Hence after two animals dies,it's not possible to surround tiger and hence tiger wins."
            embed=discord.Embed(title="**ADU-HULI GUIDE**",description=string,color=0x7F00FF)
            embed.set_image(url='https://i.imgur.com/I2MDiFh.png')
            embed.set_footer(text="NOTE: The person who starts the game by pinging other person controls tiger while the latter controls cattle.\nPage 1/2")
            await ctx.send(embed=embed)
        elif arg1=='2':
            string=":small_orange_diamond: **Game layout**:\n"
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:' + \
                     ':white_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::no_entry::zero:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::arrow_lower_left::arrow_down::arrow_lower_right::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::no_entry:\n'
            string += ':black_large_square::black_large_square::black_large_square::black_large_square::white_large_square::left_right_arrow::white_large_square::left_right_arrow::white_large_square::black_large_square::black_large_square::black_large_square::black_large_square::no_entry::one::two::three:\n'
            string += ':black_large_square::black_large_square::black_large_square::arrow_lower_left::black_large_square::black_large_square::arrow_down::black_large_square::black_large_square::arrow_lower_right::black_large_square::black_large_square::black_large_square::no_entry:\n'
            string += ':black_large_square::black_large_square::white_large_square::left_right_arrow::left_right_arrow::left_right_arrow::white_large_square::left_right_arrow::left_right_arrow::left_right_arrow::white_large_square::black_large_square::black_large_square::no_entry::four::five::six:\n'
            string += ':black_large_square::arrow_lower_left::black_large_square::black_large_square::black_large_square::black_large_square::arrow_down::black_large_square::black_large_square::black_large_square::black_large_square::arrow_lower_right::black_large_square::no_entry:\n'
            string += ':white_large_square::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::white_large_square::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::left_right_arrow::white_large_square::no_entry::seven::eight::nine:\n'
            embed = discord.Embed(title="**ADU-HULI GUIDE**", description=string, color=0x7F00FF)
            string='all animals movements are limited to white square (number corresponding to each :white_large_square: is shown on right side.)\n' \
                   'For **tiger** to move in an adjacent :white_large_square:,you just need to type the corresponding number.Ex: 2,3,6,etc\nFor **cattle** to ' \
                   'move in an adjacent :white_large_square:,you need to type the first letter of animal(c,m,d,b or p) followed by the corresponding number of :white_large_square:.Ex:\n' \
                   '`c2` - to move **cow** to position **2**\n`b9` - to move **boar** to position **9**,etc.'
            embed.add_field(name=":small_orange_diamond: Controls:",value=string,inline=False)
            embed.set_footer(text="Page 2/2")
            await ctx.send(embed=embed)
    elif arg0=='connect4':
        string=":small_orange_diamond: **Connect 4** is a two player turn based game which is played on a 6x7 grid.One player puts :blue_circle: onto the grid while other puts :red_circle:.\n\n" \
               ":small_orange_diamond: On their turn,a player drops the checker of their color in any one of the seven columns.The checker falls vertically" \
               " downward and fills the grid.\n\n:small_orange_diamond: In order to win,a player must get four checkers of their color in a row either horizontally,vertically or diagonally.\n\n " \
               ":small_orange_diamond: **Controls: **To put your checker in a particular column,you just need to type the number corresponding to that column."
        await ctx.send(embed=discord.Embed(title="**CONNECT FOUR GUIDE**",description=string,color=0x7F00FF))
    elif arg0=='kuromasu':
        string=":small_orange_diamond: **Kuromasu** is a simple puzzle game played on a 4x4 grid with two color dots : :blue_circle: and :red_circle:.\n\n" \
               ":small_orange_diamond: The partially solved puzzle will be displayed and player has to fill remaining spots using :blue_circle: and :red_circle:.\n\n" \
               ":small_orange_diamond: :blue_circle: can see others in their own row and column.They see atleast one.Their number tells how many.:red_circle: " \
               "block their view.Using this logic,player has to fill the whole grid\n\n:small_orange_diamond: **Controls:** Their are total 16 spots on the grid numbered 1 to 16 row-wise." \
               "To put a dot on a particular spot,you need to type the spot number followed by r(for :red_circle:) or b(for :blue_circle:).For eg:\n" \
               "`11b` to insert :blue_circle: on position 11.\n`4r` to insert :red_circle: on position 4."
        await ctx.send(embed=discord.Embed(title="**KUROMASU GUIDE**", description=string, color=0x7F00FF))
    elif arg0=='treasurehunt':
        string=":small_orange_diamond: **Treasure Hunt** is a two player turn based game played on a 7x10 grid.The goal is to find the treasure (<:treasure:855718827220008980>) hidden in a random location on the grid.\n\n" \
               ":small_orange_diamond: One player starts form top-left corner of grid while other player starts from bottom-right corner.Both are free to move upward,downward,leftward or rightward using their pirate ship.\n\n" \
               ":small_orange_diamond: During the journey,you might encounter:\ni)__map piece__ (<:map:854786538175856670>): tells the cardinal points of treasure (through DM) from your position.\nii)__sea dragon__ " \
               "(:dragon:): blocks next two turns.\niii)__cyclone__ (:cyclone:): blocks next three turns.\n\n:small_orange_diamond: First player to find three treasures win.Only one treasure is present on grid at a time.Once it is found,then only " \
               "the next treasure spwans on a random location.Also the positions of <:map:854786538175856670>,:dragon: and :cyclone: will change everytime a player founds treasure.\n\n:small_orange_diamond: **Controls: **\n" \
               "i)react :arrow_up: to move up.\nii)react :arrow_down: to move down.\niii)react :arrow_left: to move left.\niv)react :arrow_right: to move right.\n\n:small_orange_diamond: If both ships comes adjacent to each other,then " \
               "one of them dies randomly and respawn in their starting position."
        await ctx.send(embed=discord.Embed(title="**TREASURE HUNT GUIDE**", description=string, color=0x7F00FF))
    elif arg0=='colorix':
        string=":small_orange_diamond: **Colorix** is a single-player sliding tile puzzle game based on a video game **2048**.It is played on a " \
               "4x4 grid with colored tiles that can be slided in a particular direction(up,down,left or right) by the player.\n\n:small_orange_diamond: The objective of the game is to slide tiles" \
               ",combine them to form higher-ranked coloured tiles until you reach pink.\n\n:small_orange_diamond: The color ranking is\n<:0th:853875973416943617> < <:1st:853876013184319519> < <:2nd:853876034008252456> < <:3rd:853876056737054720> < <:4th:853876087192289340> < <:5th:853876194591113227> < <:6th:853876228121165824> < <:7th:853876250292256810> < <:8th:853876268785598474> < <:9th:853876289483177984> < <:tenth:853876310279847986>" \
               "\nTo form a particular color tile,you need to combine two color tiles of lower rank.Ex:\n<:0th:853875973416943617>+<:0th:853875973416943617>=<:1st:853876013184319519> , <:5th:853876194591113227>+<:5th:853876194591113227>=<:6th:853876228121165824> ,etc.\n\n" \
               ":small_orange_diamond: When a player slides tile in a particular direction,they move as far as possible until they are stopped by another tile or the edge of the grid.\n\n" \
               ":small_orange_diamond: If two tiles of same color comes in contact while sliding,they combine to form a higher ranked color tile.\n\n:small_orange_diamond: " \
               "Every turn,a new tile (either <:0th:853875973416943617>,<:1st:853876013184319519> or <:2nd:853876034008252456>) randomly appears in an empty spot.\n\n:small_orange_diamond: " \
               "A player wins if he/she reaches pink <:tenth:853876310279847986>.If there are no empty spots left,then game ends.\n\n:small_orange_diamond: **Credits**: [Wikipedia](https://en.m.wikipedia.org/wiki/2048_(video_game))"
        await ctx.send(embed=discord.Embed(title="**COLORIX GUIDE**", description=string, color=0x7F00FF))
    elif arg0=='svk':
        string=":small_orange_diamond: **Survivors vs Killer** is a two player turn based game in which one player plays as killer and other player plays from survivors side.\n\n" \
               ":small_orange_diamond: There are six characters :ninja:,:detective:,:vampire:,:mage:,:zombie: and :elf:.The player who plays as killer is informed about their character (through DM).The " \
               "other player has to find out the killer character before before it kills all survivors.\n\n:small_orange_diamond:The game goes through 3 phases/nights:\n" \
               "\n>__PHASE 1__: Each person stands on the corner of hexagon.The killer can kill one of the three people (two on adjacent corner and one on opposite corner).Once killed,the other player has " \
               "to vote out the person they found suspicious.If actual killer gets eliminated,survivors wins else game goes to phase 2.\n>__PHASE 2__: The remaining 4 characters stands on the corners of square.The killer can kill any person." \
               "Once killed,the survivors again vote out suspect.If actual killer gets eliminated,survivors wins else game goes to phase 3.\n>__PHASE 3__: Now there are only 2 characters (one of them being killer).Both players have to make " \
               "a choice (through DM) whether to **run away** :person_running: or **attack** :knife:.\nIf both made the same choice,then survivor wins.\nIf both made opposite choice,then killer wins."
        await ctx.send(embed=discord.Embed(title="**SURVIVORS vs KILLER GUIDE**", description=string, color=0x7F00FF))
    elif arg0=='sos':
        string=":small_orange_diamond: **S-O-S** is a two player turn based game played on a 5x5 grid.\n\n:small_orange_diamond: players take turn to add either" \
               "'**S**' or '**O**' in any empty spot.\n\n:small_orange_diamond: First person to obtain the sequence S-O-S either horizontally,vertically or diagonally wins." \
               "If all spots gets occupied with no S-O-S sequence, then the game is a tie." \
               "\n\n:small_orange_diamond: **Controls:** The rows and columns are sequentially numbered from 1 to 5.To mark at a particular spot,player need to" \
               " type the row number followed by column number followed by either s(to mark '**S**') or o(to mark '**o**').Ex:\n`23s` to mark '**S**' in 2nd row & 3rd column." \
               "\n`51o` to mark '**O**' in 5th row & 1st column.\n\n:small_orange_diamond: **Credits:** [Wikipedia](https://en.m.wikipedia.org/wiki/SOS_(game))"
        await ctx.send(embed=discord.Embed(title="**S-O-S GUIDE**", description=string, color=0x7F00FF))
    elif arg0=='bankrob':
        string=":small_orange_diamond: **Bankrob** is a single/two player game based on a code-breaking game **Mastermind/Bulls And Cows**.Players " \
               "have to guess the pattern lock made up of four coloured dots in order to break into the bank vault and steal the money before police arrives." \
               "\n\n:small_orange_diamond: Both player take turns to guess the code.After each guess,they are informed about number of correct dots" \
               " in right position and the number of correct dots in wrong position.They won't be told exactly which dot is in right position and which " \
               "one is in wrong position.\n\n:small_orange_diamond: Players have to figure out the code before police arrives.First person to figure out the code " \
               "robs the bank and the game goes on to next stage.\n\n:small_orange_diamond: **Controls:** You can make your guess code by reacting in that particular" \
               " order.\nEx: If your guess is :blue_circle::green_circle::yellow_circle::brown_circle:,then you have to react to :blue_circle: first,then " \
               ":green_circle:,then :yellow_circle: and then :brown_circle:.\nThe number of :small_red_triangle: indicates the number of correct dots in right position" \
               " while the number of :small_red_triangle_down: indicates the number of correct dots but in wrong position.There is no indication for wrong dots" \
               " present in the code.\n\n:small_orange_diamond: **Credits:** [Wikipedia](https://en.m.wikipedia.org/wiki/Mastermind_(board_game))"
        embed = discord.Embed(title="**BANKROB GUIDE**", description=string, color=0x7F00FF)
        embed.set_footer(text="NOTE: The amount of money robbed decreases with the increase in number of guesses made.")
        await ctx.send(embed=embed)
    elif arg0 == 'tictactoe2':
        if arg1==None:
            string = '**__Page 1__** : A quick insight into the game.\n**__Page 2__** : Game layout and controls.'
            string += '\n\nTo surf a particular page:\n`teko help tictactoe2 [page]`'
            await ctx.send(embed=discord.Embed(title='__**ULTIMATE TIC-TAC-TOE GUIDE**__', description=string, color=0x7F00FF))
        elif arg1=='1':
            string=':small_orange_diamond: **Ultimat tic-tac-toe** is a two player turn based game composed of nine tic-tac-toe boards (sub-grid)' \
                    'arranged in a 3x3 grid as shown in figure 1 at bottom.\n:small_orange_diamond: Players take turns marking in smaller tic-tac-toe' \
                   ' sub-grids until one of them wins in the larger grid.\n:small_orange_diamond: The sub-grids are numbered 1 to 9 row-wise.The game begins with ' \
                   'first player marking anywhere in the grid.Depending upon the marked location,the second player has' \
                   ' to mark anywhere in the sub-grid corressponding to that location.For ex:\n - If first player marks :x: in 3rd location of 5th sub-grid' \
                   '(as shown in fig. 1),then the second player has to mark in the 3rd subgrid (shown by red square in fig. 1).\nThe game continue to proceed in this manner.' \
                   '\n:small_orange_diamond: If player wins a particular sub-grid,then that player occupies that sub-grid and it is marked big with their symbol(shown in figure 2).' \
                   '\n:small_orange_diamond: If a sub-grid gets completely filled and player is send to that sub-grid,then he/she is free to mark anywhere in the bigger grid.' \
                   '\n:small_orange_diamond: The player who first places three of their marks either horizontally,vertically or diagonally in the bigger grid wins.\n' \
                   ':small_orange_diamond: **Credits:** [Wikipedia](https://en.m.wikipedia.org/wiki/Ultimate_tic-tac-toe)'
            embed = discord.Embed(title="**ULTIMATE TIC-TAC-TOE GUIDE**", description=string, color=0x7F00FF)
            embed.set_image(url='https://i.imgur.com/tO2kMI1.jpg')
            embed.set_footer(text='Page 1/2')
            await ctx.send(embed=embed)
        elif arg1=='2':
            string=":small_orange_diamond: **Game layout:**\n"
            maze=[':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']
            for i in range(3):
                if i != 0:
                    string += ':yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:\n'
                string += maze[0] + maze[1] + maze[2] + ':yellow_square:' + maze[0] + maze[1] + maze[2] + ':yellow_square:' + maze[0] + maze[1] + maze[2] + '\n'
                string += maze[3] + maze[4] + maze[5] + ':yellow_square:' + maze[3] + maze[4] + maze[5] +':yellow_square:' + maze[3] + maze[4] + maze[5] + '\n'
                string += maze[6] + maze[7] + maze[8] + ':yellow_square:' + maze[6] + maze[7] + maze[8] + ':yellow_square:' + maze[6] + maze[7] + maze[8] + '\n'
            string+="\n:small_orange_diamond: **Controls:** Two formats of input are there:\n\n  i) __**2-digit input**__: During the starting of the game,the first player need to " \
                    "type the sub-grid number (1-9) followed by the location (1-9) in that sub-grid where he/she wants to mark .\nFor ex:\n" \
                    "  - `53` : if player wants to mark in 3rd location of 5th sub-grid.\nSimilarly when player is sent to a filled sub-grid,they" \
                    " need to type a new sub-grid number followed by location in it.\n\n  ii) __**1-digit input**__: During the rest of the turns,player don't" \
                    " need to type the sub-grid number as it is dependant on the last turn of other player,they only need to type the location(1-9) where they " \
                    "want to mark.For ex: `7`,`1`,etc."
            embed=discord.Embed(title="**ULTIMATE TIC-TAC-TOE GUIDE**",description=string,color=0x7F00FF)
            embed.set_footer(text="NOTE: Bot will remind you in your turn whether or not you need to mention the sub-grid number.\nPage : 2/2")
            await ctx.send(embed=embed)
    elif arg0=='battleship':
        if arg1==None:
            string = '**__Page 1__** : A quick insight into the game.\n**__Page 2__** : Game layout and controls.'
            string += '\n\nTo surf a particular page:\n`teko help battleship [page]`'
            await ctx.send(embed=discord.Embed(title='__**BATTLESHIP GUIDE**__', description=string, color=0x7F00FF))
        elif arg1=='1':
            string=":small_orange_diamond: **Battleship** is a two player turn-based game played on a 10x10 grid (one for each player.)\n:small_orange_diamond: Both player's" \
                   " ships are hidden randomly in the grid.Players take turns hitting the cells of opponent's grid in order to destroy their fleet.\n:small_orange_diamond: " \
                   "Each fleet consist of :\n  -__One Carrier__ : 5 spaces long\n  -__Two battleships__ : 4 spaces long each\n  -__Three Cruiser__ :" \
                   "3 spaces long each\n  -__Four submarines:__ 1 space long each\nEach ship is arranged either horizontally or vertically.\n\n:small_orange_diamond: If player hits any part of opponent's fleet during their turn," \
                   "they play their turn again until they miss their shot.\n:small_orange_diamond: First player to completely destroy the opponent's fleet wins." \
                   "\n:small_orange_diamond: Both players are given random power-ups at starting " \
                   "of the game which they can use on any turn.\n\n   __**TIER 1 POWER-UPS**__\n\n - __sea mine__ (<:sea_mine:858894878230052884>): four mines" \
                   " are placed in three random cells in player's grid.If opponent hit those cells,it will damage the corressponding cell " \
                   "of their own grid instead.\n - __radar__ (<:radar:858895009569570847>): reveals location of the opponent's ship within the selected 3x3 grid." \
                   "\n - __bomber__ (:airplane_small:): drops three bombs in selected cells on the opponent's grid.\n\n   __**TIER 2 POWER-UPS**__\n\n - __nukeplane__ (:airplane:):" \
                   " drops bomb on every cell of a selected 3x3 area.\n - __torpedo bomber__ (<:torpedo:859668485440405515>): keeps dropping torpedo on every cell of a selected row " \
                   "from right to left until it hits a ship.\n - __air defense system__ (<:defense_system:858895078532317194>): it sets up itself in a random column" \
                   " and protects each cell of that column from any airstrike.If opponent's airforce enters this zone,it will be destroyed.\n\n   __**TIER 3 POWER-UPS**__\n\n" \
                   " - __fractal striker__ (:helicopter:): destroys diagonal cells in a 6x6 area.\n - __ufo__ (:flying_saucer:): destroys cells circularly in " \
                   "a 6x6 area."
            embed = discord.Embed(title="**BATTLESHIP GUIDE**", description=string, color=0x7F00FF)
            embed.set_footer(text="Page : 1/2")
            await ctx.send(embed=embed)
        elif arg1=='2':
            string = ":small_orange_diamond: **Game layout:**\n:black_large_square::one::two::three::four::five::six::seven::eight::nine::keycap_ten:"
            positions = [':regional_indicator_a:', ':regional_indicator_b:', ':regional_indicator_c:',':regional_indicator_d:', ':regional_indicator_e:', ':regional_indicator_f:',':regional_indicator_g:', ':regional_indicator_h:', ':regional_indicator_i:',':regional_indicator_j:']
            for i in range(10):
                string += '\n' + positions[i]
                for j in range(10):
                    if 10*i+j in (2,9,23,76,55):
                        string+=':x:'
                    elif 10*i+j in (5,61,30,44,89,92):
                        string+=':boom:'
                    elif 10*i+j in (27,37,47,57):
                        string+=':fire:'
                    else:
                        string +=":blue_square:"
            embed = discord.Embed(title="**BATTLESHIP GUIDE**", description=string+"\n:x: - miss , :boom: - hit, :fire: - completely destroyed.", color=0x7F00FF)
            string="rows are numbered A-J while" \
                    " columns are numbered 1-10.To hit a particular cell,player need to type the row number followed by the column number.Ex:\n" \
                   " - `g3` : to drop bomb on cell located at row **G** and column **3**.\n\n__**Power-ups Usage:**__\n\n<:radar:858895009569570847> : `radar [cell]`\n to" \
                   " use radar on a 3x3 area with [cell] being center of that area.\n\n:airplane_small: : `bomber [cell1] [cell2] [cell3]`\n to drop bombs on cells with locations" \
                   " [cell1],[cell2] and [cell3].\n\n:airplane: : `nukeplane [cell]`\n to drop bombs in a 3x3 area with [cell] being center of that area." \
                   "\n\n<:torpedo:859668485440405515> : `torpedo [A-J]`\n to lauch torpedo bomber in a particular row (A-J).\n\n:helicopter: : `striker`\n to drop bombs in" \
                   " a 6x6 area (no need to type cell location).\n\n:flying_saucer: : `ufo`\n to drop bombs in a 6x6 area (no need to type cell location)."
            embed.add_field(name=":small_orange_diamond: **Controls:**",value=string,inline=False)
            embed.set_footer(text="Page : 2/2")
            await ctx.send(embed=embed)
    elif arg0=='blindrun':
        string=":small_orange_diamond: **Blind Run** is a two player turn-based memory game in which players has to escape the dungeon by collecting" \
               " three coloured gems (required to open the exit door).\n\n:small_orange_diamond: The game consist of four levels.First three levels " \
               "are for each coloured gems and the last one is for finding correct exit door.\n\n:small_orange_diamond: For first three levels, players " \
               "will be given a glimpse of their path for a short time duration.After which players have a form a correct combination of moves using `up`," \
               "`right` and `down` to reach their destination.Ex :\n`left right right up` or `l r r u`.\nEach is move is used to tackle a certain obstacle:\n - `right` to kill enemy (<:skeleton:860809590421454849>)" \
               "\n - `up` to jump over cliff (:yellow_square::black_large_square::yellow_square:)\n - `down` to slide under spike (<:spike:860432293919195146>)\n\n" \
               ":small_orange_diamond: In last level,there will be two exit doors (one of them being a trap).Players have to figure out the path themselves as" \
               " they won't be given hint this time.Also,there will be only spikes and cliffs as obstacle in last level. "
        embed = discord.Embed(title="**BLIND RUN GUIDE**", description=string, color=0x7F00FF)
        await ctx.send(embed=embed)
    elif arg0=='diedungeon':
        if arg1==None:
            string = '**__Page 1__** : A quick insight into the game.\n**__Page 2__** : Power-ups explanation.'
            string += '\n\nTo surf a particular page:\n`teko help diedungeon [page]`'
            await ctx.send(embed=discord.Embed(title='__**DIE DUNGEON GUIDE**__', description=string, color=0x7F00FF))
        elif arg1=='1':
            string=":small_orange_diamond: **Die Dungeon** is a two player turn-based game played on a 7x7 grid along with a :game_die:.Both players are stuck inside the dungeon" \
                   " and they have to escape before it completely burns down.\n\n:small_orange_diamond: Players will roll dice upon their turn and depending " \
                   "on the number (1-6),they move their character by that much step(s) either up,down,left or right.\n 1st player (blue) : <:knight1:860809539698950184>  ,  2nd player (red) : " \
                   "<:knight2:860809565577543691>\n\n:small_orange_diamond: Game goes through three phases:\n\n - **__PHASE 1__** :\n" \
                   "Players need to collect synergy points from energy stones,by killing enemies or by killing opponent without much dying.\n\n - **__PHASE 2__** :\n" \
                   "When combined synergy reaches a certain value,the key possessor summons.In phase 2,players need to kill the key possessor.\n\n- **__PHASE 3__** :\n" \
                   "After key possessor is killed, the keys to the exit door appears in grid (<:blue_key:860810213087379476> for player 1 and <:red_key:860810230702145556>" \
                   "for player 2).The number of a keys spawned depends that player's synergy points.After finding keys,the exit appears." \
                   "First one to escape wins.\n\n:small_orange_diamond: Game consist of several power-ups explained in next page."
            embed = discord.Embed(title="**DIE DUNGEON GUIDE**", description=string, color=0x7F00FF)
            embed.set_footer(text="NOTE:\n• Every time a player dies,their maximum HP reduces by 1 (minimum to 6).\n• The grid is toroidally connected,means players can move across the edges.\nPage : 1/2")
            await ctx.send(embed=embed)
        elif arg1=='2':
            string=":small_orange_diamond: **SWORD**: all swords have attack value equal to twice the number on :game_die: except normie sword." \
                   "\n\n - __normie sword__(<:sword:860809658875772938>): attack value equal to the number on :game_die:\n - __white sword__(<:white_sword:860809738539237396>): provides extra attack value than other swords" \
                   "\n - __energy sword__(<:energy_sword:860809709942734870>): provides extra synergy when killing enemies\n - __fire wand__(<:fire_wand:860809636139106325>): takes half damage when killing <:freezard:860809893250727948>" \
                   " but double damage when killing <:demon:860809932207161354>\n - __ice wand__(<:ice_wand:860809616001990688>): takes half damage when killing <:demon:860809932207161354> but double damage when killing " \
                   "<:freezard:860809893250727948>\n - __vampire sword__(<:vampire_sword:860809680410771466>): heals player when killing an enemy"
            embed = discord.Embed(title="**DIE DUNGEON GUIDE (power-ups)**", description=string, color=0x7F00FF)
            string=" - __poison__(<:poison:860809812350074891>): adds poison to player,consuming 1HP per turn\n - __blue potion__(<:blue_potion:860809767411515392>): heals player by amount equal to the number on :game_die:\n" \
                   " - __red potion__(<:red_potion:860809787021197323>): heals player,removes poison effect\n - __heavy potion__(<:heavy_potion:860809849930645516>): heals by maximum amount\n - __fake potion__(<:fake_potion:860809831891861534>):" \
                   " can either heal opponent or add poison effect to player"
            embed.add_field(name=":small_orange_diamond: **POTION:**", value=string, inline=False)
            string=" - __energy stone__ (<:energy_stone:860810158548844564>): provides synergy equal to 4x the number on :game_die:\n - __power stone__" \
                   " (<:power_stone:860810175195250698>): provides synergy equal to 5x the number on :game_die:"
            embed.add_field(name=":small_orange_diamond: **SYNERGY:**", value=string, inline=False)
            string ="- __common enemies__ : includes bats <:bats:860809874221170688>, demon <:demon:860809932207161354>, freezard <:freezard:860809893250727948>, headcrab <:headcrab:860810006005547010>, skeleton <:skeleton:860809590421454849>\n" \
                    " - __goblin__(<:goblin:860809948618817537>): steals energy stone from adjacent cells\n - __spider__(<:spider:860809969263575060>) : alternates itself between <:spider:860809969263575060> and " \
                    "<:web:860809911973838848>.When stepped on it during web phase,players next two turns will get blocked\n - __snake__(<:snake:860809990163660830>): adds poison effect if killed bare hands.Also they don't provide any " \
                    "synergy when killed\n - tentacle creature(<:tentacle_creature:860810024128479233>): provides extra damage\n - __key possessor__(<:key_possessor:861563898237681684>):" \
                    " teleports to random cells every turn , also capable of forming clones of itself"
            embed.add_field(name=":small_orange_diamond: **ENEMY:** (provides damage equal to number on :game_die: which can be counterattack using sword)", value=string, inline=False)
            string = " - __flamethrower__ (<:flamethrower:860810196049068043>): destroys enemies and/or opponent in adjacent cells\n - __block zone__(:stop_button:): blocks next two turns\n" \
                     " - __replay__(:arrows_counterclockwise:): play your turn again\n - __shuffle__(:twisted_rightwards_arrows:): shuffles the contents of grid." \
                     "\n - __mystery chest__(<:mystery_chest:860810134506962954>): contains a random power-up\n - __bomb__(<:bomb3:860810082006073355>): explodes after three turns " \
                     ",destroying everything(even players) in it's row and column.If a player directly steps over bomb, it will explode"
            embed.add_field(name=":small_orange_diamond: **OTHER:**", value=string, inline=False)
            embed.set_footer(text="NOTE: If a player steps over other player, the one with lower attack value will die.Also,both will lose their sword.If they are bare hands,then the one with lesser synergy will die.\nPage : 2/2")
            await ctx.send(embed=embed)

@client.event
async def on_message(message):
    message.content = message.content.lower()
    await client.process_commands(message)

client.run('NzYxNDU1NjEwNjA3ODI5MDAy.X3a2zA.Q9aSWbk6o98RZB3Jt77qEUFKSYo')
