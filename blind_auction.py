from os import system

auction_dict = {}
waiting_bidders = True


while waiting_bidders:
    user_name = input("What is your name?\n")
    bid = float(input("How much would you like to bid?\n$"))
    auction_dict[user_name] = bid

    another_bidder = input("Are there more bidders?(y/n)")
    system('cls')

    if another_bidder == "n":
        waiting_bidders = False
        max_bid = 0
        winner = "the house"
        for person in auction_dict:
            if max_bid < auction_dict[person]:
                max_bid = auction_dict[person]
                winner = person

        print(f"The Auction has concluded the winner is {winner} with a bid of $" + "{:.2f}".format(max_bid))
