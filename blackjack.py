from random import shuffle, choice


cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K',
         '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K',
         '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K',
         '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']


def shuffle_deck(cards):
        deck = cards
        shuffle(deck)
        return deck

def check_card(card, hand_sum):
        try:
                return int(card)
        except:
                if card == "A":
                        if hand_sum < 11:
                                return 11
                        else:
                                return 1
                else:
                        return 10


def draw_card(card, hand_sum):
        _hand_sum = hand_sum
        _hand_sum += check_card(card, hand_sum)
        return _hand_sum


def blackjack(hand_sum):
        return True if hand_sum == 21 else False


def answer():
        answers = ["yes", "no"]
        return choice(answers)


def get_bet():
        file = open("money.txt", "r")
        get_bet.bet = input(f"You have {file.read()} money. Enter how much do you want to bet (default is 0): ")
        file.close()
        get_bet.money = 0
        if get_bet.bet == '':
                get_bet.money = 0
        else:
                get_bet.money = int(get_bet.bet)


def game():
        deck = shuffle_deck(cards)
        player_hand_sum = 0
        dealer_hand_sum = 0
        num_card = 0
        running = True
        decision = answer()
        f = open("money.txt", "r+")
        money = int(f.read().strip())
        f.seek(0)
        f.truncate()


        while running:
                for i in range(2):
                        player_hand_sum = draw_card(deck[num_card], player_hand_sum)
                        num_card += 1
                for i in range(2):
                        dealer_hand_sum = draw_card(deck[num_card], dealer_hand_sum)
                        num_card += 1

                print(f"Your hand sum is {player_hand_sum}")
                print(f"Dealer's hand sum is {dealer_hand_sum}")

                if blackjack(player_hand_sum) == True and blackjack(dealer_hand_sum) == False:
                        print("You win!")
                        money += get_bet.money
                        break
                elif blackjack(player_hand_sum) == False and blackjack(dealer_hand_sum) == True:
                        print("Dealer wins!")
                        money -= get_bet.money
                        break
                elif blackjack(player_hand_sum) == True and blackjack(dealer_hand_sum) == True:
                        print("Tie!")
                        break

                ask = input("Hit | Stand\n> ")

                while ask != "win" or ask != "lose":
                        if ask.lower() == "hit":
                                player_hand_sum = draw_card(deck[num_card], player_hand_sum)
                                num_card += 1
                                print(f"Your hand sum is {player_hand_sum}")
                                print(f"Dealer's hand sum is {dealer_hand_sum}")
                                if blackjack(player_hand_sum) == True:
                                        ask = "win"
                                        break
                                elif player_hand_sum > 21:
                                        ask = "lose"
                                        break
                                else:
                                        ask = input("Hit | Stand\n> ")
                        elif ask.lower() == "stand":
                                print(f"Your hand sum is {player_hand_sum}")
                                print(f"Dealer's hand sum is {dealer_hand_sum}")
                                break
                        else:
                                print(f"Your hand sum is {player_hand_sum}")
                                print(f"Dealer's hand sum is {dealer_hand_sum}")
                                ask = input("Hit | Stand\n> ")

                if ask == "win":
                        print("You win!")
                        money += get_bet.money
                        break
                elif ask == "lose":
                        print("Dealer wins!")
                        money -= get_bet.money
                        break

                while dealer_hand_sum <= 11:
                        dealer_hand_sum = draw_card(deck[num_card], dealer_hand_sum)
                        num_card += 1
                        print(f"Your hand sum is {player_hand_sum}")
                        print(f"Dealer's hand sum is {dealer_hand_sum}")

                if blackjack(dealer_hand_sum):
                        print("Dealer wins!")
                        money -= get_bet.money
                        break
                elif dealer_hand_sum > 21:
                        print("You win!")
                        break

                while decision != "win" or decision != "lose" or decision != "tie":
                        if decision == "yes":
                                dealer_hand_sum = draw_card(deck[num_card], dealer_hand_sum)
                                num_card += 1
                                print(f"Your hand sum is {player_hand_sum}")
                                print(f"Dealer's hand sum is {dealer_hand_sum}")
                                if blackjack(dealer_hand_sum) == True:
                                        decision = "win"
                                        break
                                elif dealer_hand_sum > 21:
                                        decision = "lose"
                                        break
                                else:
                                        decision = answer()
                        elif decision == "no":
                                if dealer_hand_sum > player_hand_sum and dealer_hand_sum <= 21:
                                        decision = "win"
                                        break
                                elif dealer_hand_sum == player_hand_sum:
                                        decision = "tie"
                                        break
                                elif dealer_hand_sum < player_hand_sum:
                                        decision = "lose"
                                        break

                if decision == "win":
                        print("Dealer wins!")
                        money -= get_bet.money
                        break
                elif decision == "lose":
                        print("You win!")
                        money += get_bet.money
                        break
                elif decision == "tie":
                        print("Tie!")
                        break

        f.write(str(money))
        f.close()
        play_again = input("Do you want to play again (y/n)? ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                main()
        else:
                raise SystemExit


def main():
        get_bet()
        game()


if __name__ == '__main__':
        main()
