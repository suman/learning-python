# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

user_decision = "yes"

all_bids = {}
while user_decision == "yes":
    name = input("What is your name ")
    bid_price = int(input("What is your bid price!"))
    all_bids[name] = bid_price
    is_bid_again = input("Does other user wants to bid again 'yes' or 'no'")

    if is_bid_again == "yes":
        print("\n" * 30)

    else:
        max = 0
        winner = ""
        for key in all_bids:
            if all_bids[key] > max:
                max = all_bids[key]
                winner = key

        user_decision = "no"
        print(f"The bid winner is {winner} with bid price {max}")
