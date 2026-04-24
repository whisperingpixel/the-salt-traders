################################################################################
#
# The Salt Traders · A merchant simulation game of the medieval salt trade
#
################################################################################
#
# This program is part of the exercise "Basics of Software Development Practice"
# at the Department of Geoinformatics (University of Salzburg) in Summer 2026.
# It consists of several parts that build upon each other.
#
# Background: The medieval salt trade was the foundation of Salzburg's wealth
# and power. Salt was often referred to as "white gold" and heavily influenced
# the region's art, particularly under the rule of the prince-archbishops.
# Significant amounts of salt were mined, especially in Dürrnberg, but also
# partly in Berchtesgaden. The salt was transported along the Salzach River to
# downstream cities, including Salzburg, Laufen, and Passau.
#
# Step into the footsteps of a medieval merchant and build your salt trading
# business.
#
# Note: The salt trade represented here is largely simplified. It will become
#       more complex in the next parts but will remain simplified for teaching
#       purposes.
#
#                                    PART 1
# Expected learning outcomes:
#  - Creating and using functions in Python.
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 22.04.2026
#
################################################################################

import random
import sys

###############################################################################
#
# Variables and constants
#
###############################################################################

#
# Cities and mines
#
MINES = ["Dürrnberg", "Berchtesgaden"]
MARKETS = ["Salzburg", "Laufen", "Passau"]

#
# Trading
#
BUY_COST = 5.0      # gold per kg
SHIP_COST = 1.5     # gold per transaction
SELL_PRICE = 10.0   # gold per kg
MAX_STOCK = 100_000    # kg

#
# Initial state of the stock
#
gold = 1500.0
salt = 0

#
# Simulation / game parameters
#
MAX_ITER = 100

###############################################################################
#
# Function definitions
#
###############################################################################

def buy_salt(amount, mine):

    if (salt + amount) > MAX_STOCK:
        print("Can not buy salt, not enough room in the stock")
        return

    cost_per_kg = BUY_COST + SHIP_COST
    total_cost = cost_per_kg * amount
    if total_cost > gold:
        print("Can not afford salt, not enough gold")
        return

    print(f"Bought {amount}kg from {mine} for {total_cost}g")
    return total_cost


def sell_salt(amount, market):

    if(amount > salt):
        print(f"You can not sell more than you have!")
        return

    revenue = (SELL_PRICE - SHIP_COST) * amount
    print(f"Sold {amount}kg of salt at the {market} market and earned {gold} gold")
    return revenue


def is_bankrupt(gold):
    return gold <= 0

###############################################################################
#
# Start of the program.
# This is the heart of the mechanism.
#
###############################################################################

if __name__ == "__main__":
    #
    # Running the game
    #
    iteration = 0

    while iteration < MAX_ITER:

        print(f"Next iteration: {iteration}/{MAX_ITER}")
        print(f"You have {salt}kg of salt and {gold} gold")

        for mine in MINES:
            salt_to_purcase = random.randint(50,150)
            cost = buy_salt(salt_to_purcase, mine)
            salt = salt + salt_to_purcase
            gold = gold - cost

        for market in MARKETS:
            salt_to_sell = random.randint(30, 70)
            revenue = sell_salt(salt_to_sell, market)
            gold = gold + revenue
            salt = salt - salt_to_sell

        if is_bankrupt(gold):
            print("You are bankrupt")
            sys.exit()

        iteration = iteration + 1
        input()

# Options to improve on your own:
#
# - add more cities
# - add capacities for mines
# - add market saturation for cities
# - add different shipping costs for mines and cities (we will do that later based
#   on their location!)
# - adjust purchasing and selling based on the limits we have

# Next week:
#
# - better error handing: The program should not crash when something goes wrong!
# - separation of configuration and program execution
# - better documentation of the code!