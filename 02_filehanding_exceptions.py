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
#                               PART 2
# Expected learing outcomes:
#  - File handling
#  - YAML
#  - Handling errors and exceptions
#  - Documentation
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 22.04.2026
#
################################################################################

import random
import sys
import yaml

###############################################################################
#
# Variables and constants
#
###############################################################################

#
# Initial state of the stock
#
gold = 1500.0
salt = 0

#
# Simulation parameters
#
MAX_ITER = 100

#
# Configuration
#
with open('config.yml', 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)

###############################################################################
#
# Function definitions
#
###############################################################################

def buy_salt(amount, mine):
    """Function to buy salt

    This function allows to buy a certain amount of salt from a mine.

    Parameters
    ----------
    amount : int
        The amount of salt that should be bought.
    mine : str
        The name of the mine.
    """

    if (salt + amount) > config["trading"]["stock"]["max"]:
        raise Exception("Can not buy salt, not enough room in the stock")

    cost_per_kg = config["trading"]["costs"]["buy_cost"] + config["trading"]["costs"]["ship_cost"]
    total_cost = cost_per_kg * amount
    if total_cost > gold:
        raise Exception("Can not afford salt, not enough gold")

    print(f"Bought {amount}kg from {mine} for {total_cost}g")
    return total_cost


def sell_salt(amount, market):
    """Function to sell salt

    This function allows to sell a certain amount of salt to a market.

    Parameters
    ----------
    amount : int
        The amount of salt that should be sold.
    market : str
        The name of the market of a city.
    """

    if(amount > salt):
        raise Exception(f"You can not sell more than you have!")

    revenue = (config["trading"]["revenue"]["price"] - config["trading"]["costs"]["ship_cost"]) * amount
    print(f"Sold {amount}kg of salt at the {market} market and earned {gold} gold")
    return revenue


def is_bankrupt(gold):
    """Checks whether you are bankrupt or not.

    By definition, you are bankrupt if your gold is less than or equal to 0.

    Parameters
    ----------
    gold : int
        The amount of gold in your stock.
    """

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

        for mine in config["mines"]:
            try:
                salt_to_purcase = random.randint(50,150)
                cost = buy_salt(salt_to_purcase, mine)
                salt = salt + salt_to_purcase
                gold = gold - cost
            except Exception as e:
                print(e)

        for market in config["markets"]:
            try:
                salt_to_sell = random.randint(30, 70)
                revenue = sell_salt(salt_to_sell, market)
                gold = gold + revenue
                salt = salt - salt_to_sell
            except Exception as e:
                print(e)

        if is_bankrupt(gold):
            print("You are bankrupt")
            sys.exit()

        iteration = iteration + 1
        input()

# Assignment for next week:
#
# - Add random events in an interation, which could be an attack of outlaws that
#   steal the shipment or a broken boat, which means that the salt gets lost.

# Options to improve on your own (no assignment):
#
# - Add a random disaster (e.g. flooding, mine or bridge accident) that prevents
#   salt from being purchased or sold. This event can happen at a random chance
#   during an event. Money might be necessary to fix it.
# - Add a bank that can give a credit to buy salt or recover from the disaster,
#   but the money needs to be paid back.
# - Add randomly an option for war outbreak that increases the shipping cost
#   until the war is over. Peace may be also randomly, but only if there is
#   a war.

# Next week:
#
# - Create an interactive program with a command-line interface!