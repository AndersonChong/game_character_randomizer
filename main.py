import discord
import random
import system
import valorant

system.init()
client = discord.Client()
TOKEN = 'ODA4OTIyMDU5MDE0Mjc1MTEz.YCNlXw.ztTnjdsa4_fZZmjJ-RLgB7X1_0Q'

# Method to call when the bot is online

@client.event
async def on_ready():
    print('{0.user} logged in'.format(client))

# Method to call after receiving an incoming message

@client.event
async def on_message(message):
    # check if bot is reading its own message

    if message.author == client.user:
        return

    # check message conditions
    if message.content.startswith('ply'):
        command = message.content.split(' ')

        # greet message
        if len(command) == 1:
            await message.channel.send(open('files/greet.txt').read())

        # user manual
        elif len(command) == 2 and command[1] == 'help':
            await message.channel.send(open('files/user_manual.txt').read())

        # valorant all random
        elif len(command) == 2 and command[1] == 'valorant':
            agent = valorant.Valorant.search_random_agent()[0]
            await message.channel.send(agent.name)

        # valorant random based on roles
        elif len(command) == 3 and command[1] == 'valorant' and (command[2] == 'duelist' or command[2] == 'd'):
            searched_agent = valorant.Valorant.search_random_agent('Duelist')[0]
            await message.channel.send(searched_agent.name)
        elif len(command) == 3 and command[1] == 'valorant' and (command[2] == 'initiator' or command[2] == 'i'):
            searched_agent = valorant.Valorant.search_random_agent('Initiator')[0]
            await message.channel.send(searched_agent.name)
        elif len(command) == 3 and command[1] == 'valorant' and (command[2] == 'controller' or command[2] == 'c'):
            searched_agent = valorant.Valorant.search_random_agent('Controller')[0]
            await message.channel.send(searched_agent.name)
        elif len(command) == 3 and command[1] == 'valorant' and (command[2] == 'sentinel' or command[2] == 's'):
            searched_agent = valorant.Valorant.search_random_agent('Sentinel')[0]
            await message.channel.send(searched_agent.name)

        # valorant random 5 men
        elif len(command) == 3 and command[1] == 'valorant' and command[2] == '5men':
            searched_agents = valorant.Valorant.search_five_men()
            for agent in searched_agents:
                await message.channel.send(agent.name)
        elif len(command) == 4 and command[1] == 'valorant' and command[2] == '5men':
            if len(command[3]) != 4:
                await message.channel.send('Please enter the numbers of 4 roles only\nEnter \'ply help\' for more info')
                return
            try:
                number_of_duelist = int(command[3][:1])
                number_of_initiator = int(command[3][1:2])
                number_of_controller = int(command[3][2:3])
                number_of_sentinel = int(command[3][3:])
            except:
                await message.channel.send('Please enter integers only for number of roles\nEnter \'ply help\' for more info')
                return
            if number_of_duelist + number_of_initiator + number_of_controller + number_of_sentinel != 5:
                await message.channel.send('Please enter numbers that sums up to 5 players only\nEnter \'ply help\' for more info')
                return
            if number_of_duelist > valorant.Valorant.number_in_role('Duelist') or number_of_initiator > valorant.Valorant.number_in_role('Initiator') or number_of_controller > valorant.Valorant.number_in_role('Controller') or number_of_sentinel > valorant.Valorant.number_in_role('Sentinel'):
                await message.channel.send('Exceed to total amount of characters in a role\nEnter \'ply help\' for more info')
                return
            searched_agents = valorant.Valorant.search_five_men(number_of_duelist, number_of_initiator, number_of_controller, number_of_sentinel)
            for agent in searched_agents:
                await message.channel.send(agent.name)
            
        
client.run(TOKEN)