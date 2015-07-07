# create a program that takes a list of skyrim races/genders/skills and returns a randomized character

import random

#create lists
races = ['Altmer', 'Argonian', 'Bosmer', 'Breton', 'Dunmer', 'Imperial', 'Khajiit', 'Nord', 'Orc', 'Redguard']
genders = ['Male', 'Female']
magic_skills = ['Alteration', 'Conjuration', 'Destruction', 'Illusion', 'Restoration']
combat_skills = ['Archery', 'Block', 'Heavy Armor', 'One-handed', 'Two Handed']
stealth_skills = ['Light Armor', 'Lockpicking', 'Pickpocket', 'Sneak', 'Speech']
crafting_skills = ['Enchanting', 'Smithing', 'Alchemy']
crafting_enabled = False
player_character = []
final_skills = []

#define function to give random race
def random_race():
	player_character.append(random.choice(races))

#define function to give random gender
def random_gender():
	player_character.append(random.choice(genders))

#define function to return three magic skills, after removing two at random
#this function also checks for crafting, generating 2 skills instead of 3.
#all list functions run the same
def random_magic():
	while len(magic_skills) > 3:
		magic_skills.remove(random.choice(magic_skills))
	if crafting_enabled:
		magic_skills.remove(random.choice(magic_skills))

def random_combat():
	while len(combat_skills) > 3:
		combat_skills.remove(random.choice(combat_skills))
	if crafting_enabled:
		combat_skills.remove(random.choice(combat_skills))

def random_stealth():
	while len(stealth_skills) > 3:
		stealth_skills.remove(random.choice(stealth_skills))
	if crafting_enabled:
		stealth_skills.remove(random.choice(stealth_skills))

#define function that creates a final skill list
def create_skills(): 
	final_skills.extend(magic_skills)
	final_skills.extend(combat_skills)
	final_skills.extend(stealth_skills)
	if crafting_enabled:
		final_skills.extend(crafting_skills)

#create a function that creates the player character
def create_player():
	foo = random.choice(final_skills)
	while len(final_skills) > 3:
		player_character.append(foo)
		final_skills.remove(foo)
		foo = random.choice(final_skills)

#create a function that formats the final output
def format():
	s = "Your character is a {0} {1}. Their primary skills are {2}, {3}, {4}, {5}, {6}, and {7}."
	x = player_character
	return(s.format(*x))

while len(player_character) < 8:
	yn = input("Would you like to roll for crafting skills? Y/N:  ") #ask to modify crafting_enabled

	#run, debug input
	if yn == 'Y':
		crafting_enabled = True
		print("Okay, your character may have crafting skills.")
	elif yn == 'N':
		print("Okay, your character will not have crafting skills.")
	else:
		print("I'm sorry, I did not understand your answer.")
		yn = input("Would you like to roll for crafting skills? Please enter Y or N:  ")

	random_gender()
	random_race()
	random_magic()
	random_combat()
	random_stealth()
	create_skills()
	create_player()
	say = format()
	print(say)
	
