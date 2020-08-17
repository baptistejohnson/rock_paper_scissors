import random

player_name = input("Enter your name: ")
print("Hello, " + player_name)

# reading player score
player_score = 0
scores_dict = {}
scores = open('rating.txt', 'r')
for line in scores:
    player, score = line.split()
    score = int(score.replace("\n", ""))
    scores_dict[player] = score

if player_name in scores_dict:
    player_score = scores_dict[player_name]

# defining custom options and win lists for all options
cust_options_list = []
cust_options = input("What options do you want to play with?")
if cust_options == "":
    cust_options_list = ["rock", "paper", "scissors"]
else:
    cust_options_list = cust_options.split(",")

cust_wins = {}
for item in cust_options_list:
    item_win_list = []
    counter = 1
    while counter <= int((len(cust_options_list) - 1) / 2):
        item_win_list.append(cust_options_list[cust_options_list.index(item) - counter])
        counter += 1
    cust_wins[item] = item_win_list

print("Okay, let's start")

p_option = input()

while p_option != "!exit":
    c_option = random.choice(cust_options_list)
    if p_option in cust_options_list:
        if p_option == c_option:
            print("There is a draw ({})".format(p_option))
            player_score += 50
        elif c_option in cust_wins[p_option]:
            print("Well done. The computer chose {} and failed".format(c_option))
            player_score += 100
        else:
            print("Sorry, but the computer chose {}".format(c_option))
    elif p_option == "!rating":
        print("Your rating: " + str(player_score))
    else:
        print("Invalid input")
    p_option = input()
print("Bye!")

