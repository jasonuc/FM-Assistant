import csv

fifa_data = open('fifa19.csv')
fifa = csv.DictReader(fifa_data)

print("WELCOME TO FIFA MANAGER ASSISTANT")
print("Note that this software uses Fifa 19 dataset.")

# manager = str(input("WHAT IS YOUR NAME? ")).upper()
manager = "JASON UMAHI"

print("\nWelcome to the player window search".upper())
# p_position = str(input("What position are you looking for:")).upper()
# p_age = int(input("What is the highest age you're looking for: "))
# p_overall = int(input("What is the least rating you would like: "))
# p_potential = int(input("What is the least potential you would like: "))
p_position = "ST"
p_age = int(25)
p_overall = int(70)
p_potential = int(85)


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

