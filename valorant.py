import random

class Valorant:
    list = []

    def __init__(self, name, role):
        self.name = name
        self.role = role
        Valorant.list.append(self)        

    @staticmethod
    def read():
        try:
            file = open('files/valorant.txt')
            name = ''
            role = ''
            for line in file:
                name, role = line.split(', ')
                role = role.split('\n')[0]
                Valorant(name, role)
        except:
            print('Error reading files')

    @staticmethod
    def search_random_agent(role = 'none', count = 1):
        # return empty string if count is less than 1
        if count < 1:
            return []

        # continue if count is more than 0
        agents = []
        for x in range(count):
            again = True
            while again:
                if role == 'none':
                    random_agent = random.choice(Valorant.list)
                else:
                    agents_with_role = []
                    for agent in Valorant.list:
                        if agent.role == role:
                            agents_with_role.append(agent)
                    random_agent = random.choice(agents_with_role)
                if len(agents) > 0:
                    for agent in agents:
                        if random_agent != agent:
                            again = False
                            agents.append(random_agent)
                else:
                    again = False
                    agents.append(random_agent)
        return agents

    @staticmethod
    def search_five_men(number_of_duelist = 1, number_of_initiator = 1, number_of_controller = 2, number_of_sentinel = 1):
        agents = []
        for agent in Valorant.search_random_agent('Duelist', number_of_duelist):
            agents.append(agent)
        for agent in Valorant.search_random_agent('Initiator', number_of_initiator):
            agents.append(agent)
        for agent in Valorant.search_random_agent('Controller', number_of_controller):
            agents.append(agent)
        for agent in Valorant.search_random_agent('Sentinel', number_of_sentinel):
            agents.append(agent)
        return agents
    
    @staticmethod
    def number_in_role(role):
        counter = 0
        for agent in Valorant.list:
            if agent.role == role:
                counter += 1
        return counter