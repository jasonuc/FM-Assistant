import csv

fifa_data = open('fifa19.csv')
fifa = csv.DictReader(fifa_data)

print("WELCOME TO FIFA MANAGER ASSISTANT")
print("Note that this software uses Fifa 19 dataset.")

manager = str(input("WHAT IS YOUR NAME? ")).upper()

print("\nWelcome to the player window search".upper())
p_position = str(input("What position are you looking for:")).upper()
p_age = int(input("What is the highest age you're looking for: "))
p_overall = int(input("What is the least rating you would like: "))
p_potential = int(input("What is the least potential you would like: "))


lst_of_players = []
for player in fifa:
    if player['Position'] == p_position:
        if int(player['Age']) <= p_age:
            if int(player['Overall']) >= p_overall:
                if int(player['Potential']) >= p_potential:
                    lst_of_players.append({"Name":player["Name"], 
                    "Age":str(player['Age']), 
                    "Overall":str(player["Overall"]),
                    "Potential": str(player["Potential"]),
                    "Position":player['Position'],
                    "Wage":str(player['Wage']),
                    "Value":str(player['Value']),
                    "Club":player['Club']
                    })


for player in lst_of_players:
        name = player["Name"]
        age = player['Age']
        potential = player["Potential"]
        overall = player["Overall"]
        value = player['Value']
        wage = player['Wage']
        pos = player['Position']
        club = player['Club']
        player_bio = open('player_bio_file.txt', 'a')
        player_bio.write('\n'+"-"*50+f"\nThis is from Manager {manager} in search of {p_position}")
        player_bio.write(f"""\nPLAYER BIO:
This player's name is {name} and he is {age} years old.
His current rating is {overall} and he's potential is {potential}
His value is {value} and his wage is {wage}. His current position is {pos}.
Also he currently plays for {club}
""")
        player_bio.close()
