#python code for DnD character generation

#need to find best way to store character information

#define a function that takes raw input from the user and appends it to a dictionary wih associated keys

#add conditionals to change stats based on class and race modifiers

#write separate script for dice rolls? 

#_______________________________________________________________________________________
# Step 1 Choose a race
	#Dwarf
		#Hill Dwarf
		#Mountain Dwarf
	#Elf
		#High Elf
		#Wood Elf
	#Halfling
	#Human
	
	#Racial traits
	   #Ability score increase
	   #Age
	   #Alignment
	   #Size
	   #Speed
	   #Languages


			

	


#Step 2 Choose a class
    #Cleric
    #Fighter
    #Rogue
    #Wizard

    #Add modifiers based on class	
	

#class CharGen():
    #empty_dic = {} this will contain whole character sheet
#class will take no args but will initiate the data capture process then save user input to txt or pdf...csv wouldnt be a bad option here
    
    #def race_and_class(self):
    #def stat_add(self, strength,charisma, dexterity, intelligence, wisdom constitution) takes original values as arguments 

menu = {}
menu['1'] = "Choose race"
menu['2'] = "Choose class"
menu['3'] = "Exit"

	
data_store = {"Race"  :  "", "Class":  ""}
	

while True:	
	
	options = menu.keys()
	options.sort()
	
	for entry in options:
		print entry, menu[entry]
		
	selection = raw_input("Please select")
	
	if selection == '1':
		print "Race selector"
	
		race = raw_input("Please pick one of the following races: Dwarf, Elf, Halfling, Human ")

		if race == "Dwarf":
			choice_race = raw_input("Press 1) for Mountain Dwarf or press 2) for Hill Dwarf ")
			if choice_race == "1":
				race = "Mountain Dwarf"
				data_store["Race"] = race
			elif choice_race == "2":
				race = "Hill Dwarf"
				data_store["Race"] = race
		
			
			
		elif race == "Elf":
		  choice_race = raw_input("Press 1) for High Elf or press 2) for Wood Elf ")
		  if choice_race == "1":
		      race = "High Elf"
		      data_store["Race"] = race
		  elif choice_race == "2":
		      race = "Wood Elf"
		      data_store["Race"] = race
		
		elif race == "Halfling":
			data_store["Race"] = race
	
		elif race == "Human":
			data_store["Race"] = race
		
		else:
			print "Unknown race selected"
	
	elif selection == '2':
		
		print "Class selector"
		profession = raw_input("Please pick one of the following classes: Cleric, Fighter, Rogue, Wizard ")
		
		if profession == "Cleric":
			data_store["Class"] = profession
		
		elif profession == "Fighter":
			data_store["Class"] = "Fighter"
		elif profession == "Rogue":
			data_store["Class"] = "Rogue"
		elif profession == "Wizard":
			data_store["Class"] = "Wizard"
		else:
			print "Unknown class selected"
	
	elif selection == '3':
		break
	else:
		print "Unknown option selected"

print data_store

	





#Dictionary to hold stats i.e {examples_stat: stat_value}
#Function for each stat?
#This could be a class for a real game for stat changes



#Step 3 Determine ability scores

#Strength
#Dexterity
#Constitution
#Intelligence
#Wisdom
#Charisma

#Base + modifiers
#Take into account Racial modifiers
# Use conditional for that


#Step 4 Character
#Name
#Sex
#Height and Weight
#Other
#Alignment
#Languages

#use raw input and store in dictionary 



