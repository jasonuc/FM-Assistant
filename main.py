import pandas as pd

#Load in Fifa 19 CSV
fifa = pd.read_csv('fifa19.csv')
# print(fifa.head())

#Start
print("WELCOME TO FIFA MANAGER ASSISTANT")
print("Note that this software uses Fifa 19 dataset.")

# manager = str(input("WHAT IS YOUR NAME? ")).upper()
manager = 'JCU'

print("\nWelcome to the player window search".upper())
# p_position = str(input(
# """
# What position are you looking for:
# Postions: CAM, CB, CDM, CF, CB, GK, LB, LCM, LCB LAM, LF, LM, LW, LWB, RB, RCM, RCB RAM, RF, RM, RW, RWB, ST
# """
# )).upper()
# p_age = int(input("What is the highest age you're looking for: "))
# p_overall = int(input("What is the least rating you would like(0-100): "))
# p_potential = int(input("What is the least potential you would like(0-100): "))

p_position = 'CB'
p_age = 23
p_overall = 75
p_potential = 85

players = fifa[(fifa.Age <= p_age) & (fifa.Position == p_position) & (fifa.Overall >= p_overall) & (fifa.Potential >= p_potential)]
# names = list(players['Name'])

for index, row in players.iterrows():
    name = row["Name"]
    age = row['Age']
    potential = row["Potential"]
    overall = row["Overall"]
    value = row['Value']
    wage = row['Wage']
    pos = row['Position']
    club = row['Club']
    player_bio = open('player_bio_file.txt', 'a')
    player_bio.write('\n'+"-"*50+f"\nThis is from Manager {manager} in search of a {p_position}")
    player_bio.write(f"""\nPLAYER BIO:
This player's name is {name} and he is {age} years old.
His current rating is {overall} and he's potential is {potential}
His value is {value} and his wage is {wage}. His current position is {pos}.
Also he currently plays for {club}
""")
    player_bio.close()


print("Player data has been written into player_bio_file.txt. Check it out!!!")



