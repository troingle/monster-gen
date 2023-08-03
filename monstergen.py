import json
import random
import os

monsters = []
bonuses = []

p1 = []
p2 = []
p3 = []
p4 = []

with open("monsters.json") as file:
	data = json.load(file)

with open("bonuses.json") as file:
	bonus_data = json.load(file)

for item in data:
	nimi = str(item['nimi'])
	kuvaus = str(item['monologi'])

	monster = f"========{nimi.upper()}========\n\n{kuvaus}"
	
	monsters.append(monster)

for item in bonus_data:
	nimi = str(item['nimi'])
	kuvaus = str(item['kuvaus'])

	bonus = f"========BONUS: {nimi.upper()}========\n\n{kuvaus}"
	
	bonuses.append(bonus)


while True:
	os.system('clear')
	print("""                                                              _ _        _                _        
                                                             | | |      | |              | |       
 _ __ ___  _   _ _ __ ___  _ __ ___  _   _ _ __   __   ____ _| | |_ __ _| | ___   _ _ __ | |_ __ _ 
| '_ ` _ \| | | | '_ ` _ \| '_ ` _ \| | | | '_ \  \ \ / / _` | | __/ _` | |/ / | | | '_ \| __/ _` |
| | | | | | |_| | | | | | | | | | | | |_| | | | |  \ V / (_| | | || (_| |   <| |_| | | | | || (_| |
|_| |_| |_|\__,_|_| |_| |_|_| |_| |_|\__,_|_| |_|   \_/ \__,_|_|\__\__,_|_|\_\\__,_|_| |_|\__\__,_|""")
	print("\nh: hirviö")
	print("b: bonus")
	print("p: poista bonus")
	print("numero 1-3: katso pelaajan bonukset")
	a = input("\n~ ")
	os.system('clear')
	if a == "h":
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
		input("\n~ ")
	elif a == "b":
		try:
			pelaaja = int(input("Mille pelaajalle bonus annetaan? (1-3) "))
			if pelaaja > 0 and pelaaja < 4:
				os.system('clear')
				chosen_bonus = random.choice(bonuses) + f" [{random.randint(1, 1000)}]"
				print(chosen_bonus)
				if pelaaja == 1:
					p1.append(chosen_bonus)
				elif pelaaja == 2:
					p2.append(chosen_bonus)
				elif pelaaja == 3:
					p3.append(chosen_bonus)
				elif pelaaja == 4:
					p4.apppend(chosen_bonus)
			else:
				print(int("stupid fix"))
		except:
			os.system('clear')
			print("Virheellinen syöte. Bonuksia ei lisätty.")
		input("\n~ ")
	elif a == "p":
		os.system('clear')
		num = input("Syötä bonuksen koodinumero: ")
		for i in p1:
			if num in i:
				p1.remove(i)
		for i in p2:
			if num in i:
				p2.remove(i)
		for i in p3:
			if num in i:
				p3.remove(i)
		os.system('clear')
		print(f"Kaikki koodinumerolla {num} varustetut bonukset poistettu.")
		input("\n~ ")
	elif a == "1":
		os.system('clear')
		print("======PELAAJA 1======\n")
		for i in p1:
			print(f"{i}\n")
		input("\n~ ")
	elif a == "2":
		os.system('clear')
		print("======PELAAJA 2======\n")
		for i in p2:
			print(f"{i}\n")
		input("\n~ ")
	elif a == "3":
		os.system('clear')
		print("======PELAAJA 3======\n")
		for i in p3:
			print(f"{i}\n")
		input("\n~ ")
	else:
		os.system('clear')
		print("Virheellinen syöte.")
		input("\n~ ")

		


