import random
import pandas as pd
import matplotlib.pyplot as plt



print("Special Blackjack!")
# create arrays for player and dealer so that I can compare the value later.
dealer = []
player = []
dealer_win = []
player_win =[]
# to keep the record of less,more, or equal
less_more_equal_array = []
game_end = 0
# dealer's hidden card array
hidden_dealer_card = []
more_win_counter = 0
more_all_counter = 0
less_win_counter = 0
less_all_counter = 0
equal_win_counter = 0
equal_all_counter = 0
result = []
bet_tracker = []
# Ace will just be a value of "1"
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'J', 'Q', 'K']
betting = ['less', 'more', 'equal']





# function to calculate card value.
def sum(value):
    total_value = 0
    for i in range(2):
        # A = 1 in this simulation
        if value[0] == 'A':
            total_value = total_value + 1
        # special cases
        elif value[0] == 'J' or value[0] == 'K' or value[0] == 'Q':
            total_value = total_value + 10
        else:
            total_value = total_value + value[0]
    return total_value

def getRandomBet():
    betting_list = ["more", "less", "equal"]
    return random.choice(betting_list)

# returns two random numbers list for each time two card's drawn
def getRandom():
    two_cards = []
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    two_cards_value = random.choice(cards)
    two_cards.append(cards[two_cards_value])

    two_cards_value = random.choice(cards)
    two_cards.append(cards[two_cards_value])
    return two_cards

game_end = int(input("Enter the number of times you want the simulator to run: "))

for i in range(game_end):
    two_cards = getRandom()  # get the random numbers
    dealer.append(two_cards)
    print("Dealer's Card: ", end="")
    print(str(two_cards[0]) + "," + "?")
    two_cards = getRandom()
    # append the values to lists for storing
    player.append(two_cards)
    print("Your Card: ", end="")
    print(str(two_cards[0]) + "," + str(two_cards[1]))
    bet_choice = getRandomBet()
    # print("Your bet: " + getRandomBet())
    less_more_equal_array.append(bet_choice)
    print("Dealer's hidden card: " + str(dealer[-1][1]))
    hidden_dealer_card.append(str(dealer[-1][1]))
    dealer_sum = sum(dealer[-1])
    player_sum = sum(player[-1])
    print("Dealer's total point: " + str(dealer_sum))
    print("Player's total point: " + str(player_sum))
    print(bet_choice)
    # increment win conditions on types of betting.
    if dealer_sum < player_sum and bet_choice == "more":  # compare conditions and print the result
        # print("You won your bet!")
        result.append("Win")
        bet_tracker.append("more")
        player_win.append('1')
        dealer_win.append('0')
        more_win_counter = more_win_counter + 1
        more_all_counter = more_all_counter + 1
    elif dealer_sum > player_sum and bet_choice == "more":
        #print("You lost your bet!")
        result.append("Lose")
        bet_tracker.append("more")
        player_win.append('0')
        dealer_win.append('1')
        more_all_counter = more_all_counter + 1
    elif dealer_sum < player_sum and bet_choice == "less":
        # print("You lost your bet!")
        result.append("Lose")
        bet_tracker.append("less")
        player_win.append('0')
        dealer_win.append('1')
        less_all_counter = less_all_counter + 1
    elif dealer_sum > player_sum and bet_choice == "less":
        # print("You won your bet!")
        result.append("Win")
        bet_tracker.append("less")
        player_win.append('1')
        dealer_win.append('0')
        less_win_counter = less_win_counter + 1
        less_all_counter = less_all_counter + 1
    elif dealer_sum == player_sum and bet_choice == "equal":
        # print("You won your bet!")

        result.append("Win")
        bet_tracker.append("equal")
        player_win.append('1')
        dealer_win.append('0')
        equal_win_counter = equal_win_counter + 1
        equal_all_counter = equal_all_counter + 1
    else:
        # print("You lost your bet!")
        result.append("Lose")
        bet_tracker.append("equal")
        player_win.append('0')
        dealer_win.append('1')
        equal_all_counter = equal_all_counter + 1

    '''
    elif dealer_sum != player_sum and bet_choice == "equal":
        print("You lost your bet!")
        result.append("Lose")
        equal_all_counter = equal_all_counter + 1
    '''
    # ch = input("Play again? y/n:")
    ch = 1
    if ch == 1:  # continue loop if ch is y
        game_end = game_end + 1
        continue
    else:
        break


# result creator
print("******************************************************************************************")
print("#Dealer# \t\t#Player# \t\t#Less/More/Equal# \t\t#Hidden card# \t\t#Win/Lose#")
for i in range(len(dealer)):  # print the data of all games
    print(str(dealer[i][0]) + "," + str(dealer[i][1]) + "     ", end=" ")
    print("\t\t" + str(player[i][0]) + "," + str(player[i][1]), end=" ")
    print("\t\t\t\t" + less_more_equal_array[i], end=" ")
    print("\t\t\t\t\t" + str(hidden_dealer_card[i]), end=" ")
    print("\t\t\t\t\t" + result[i])
print("******************************************************************************************")
# making a 2D format
df = pd.DataFrame()
data = {'dealer_card':[0:dealer[i]}
df['dealer_card'] = dealer
df['player_card'] = player



for i in range(len(dealer)):



if more_all_counter > 0:
    morewinrate = (more_win_counter / more_all_counter) * 100
else:
    morewinrate = 0
if less_all_counter > 0:
    lesswinrate = (less_win_counter/less_all_counter) * 100
else:
    lesswinrate = 0
if equal_all_counter > 0:
    equalwinrate = (equal_win_counter/equal_all_counter) * 100
else:
    equalwinrate = 0

print("Winrate for when you bet on for 'more': " +str(morewinrate) + "%")
print("Winrate for when you bet on for 'less': " +str(lesswinrate) + "%")
print("Winrate for when you bet on for 'equal': " +str(equalwinrate) + "%")



