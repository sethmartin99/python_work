from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

def get_winning_ticket(possibilities):
	winning_ticket=[]
	while len(winning_ticket)<4:
		pulled_item=choice(possibilities)
		winning_ticket.append(pulled_item)
	return winning_ticket

def check_ticket(played_ticket, winning_ticket):
	for element in played_ticket:
		if element not in winning_ticket:
			return False

	return True

def make_random_ticket(possibilities):
	ticket=[]
	while len(ticket)<4:
		pulled_item=choice(possibilities)
		ticket.append(pulled_item)

	return ticket 









