import json
import random
import os

monsters = []
original_list = []

with open("monsters.json") as file:
	data = json.load(file)

for item in data:
	nimi = str(item['nimi'])
	kuvaus = str(item['monologi'])

	monster = f"========{nimi.upper()}========\n\n{kuvaus}"
	
	monsters.append(monster)


while True:
	while True:
	    
		if len(monsters) == 0:
			print("Sekoitetaan pakkaa...")
			print("")
			for item in data:
				nimi = str(item['nimi'])
				kuvaus = str(item['monologi'])

				monster = f"========{nimi.upper()}========\n\n{kuvaus}"
				
				monsters.append(monster)
		chosen = random.choice(monsters)
		print(chosen)
		monsters.remove(chosen)
		input()
		os.system('clear')
