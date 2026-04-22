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
#                               PART 3
# Expected learing outcomes:
#  - Passing arguments to the program
#  - Command-line interfaces
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 22.04.2026
#
################################################################################

import sys
import yaml
import cmd
import argparse

################################################################################
#
# Variables and constants
#
################################################################################

#
# Initial state of the stock
#
gold = 1500.0
salt = 0

#
# Configuration
#
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config.yml')
args = parser.parse_args()

with open(args.config, 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)

################################################################################
#
# Function definitions
#
################################################################################

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

################################################################################
#
# Start of the program.
# This is the heart of the mechanism.
#
################################################################################

if __name__ == "__main__":

    class Game(cmd.Cmd):
        intro = """
        Welcome to the world of salt, merchant!

        You can see your stock by typing 'list_stock'. Type 'purchase <amount> <mine>'
        to purchase salt from a mine. For example: 'purchase 100 Dürrnberg' to
        purchase 100kg from the Dürrnberg mine. Type 'sell <amount> <market>'
        to sell salt to a market. For example: 'sell 100 Passau' to sell 100kg
        of salt to Passau.
        """
        prompt = "The Salt Traders> "

        def do_list_stock(self, name):
            """ List your stock """
            print(f"You have {salt}kg of salt and {gold} gold")

        def do_purchase(self, args):
            """Purchase salt from a mine"""
            amount, mine = args.split()
            amount = int(amount)

            global salt
            global gold

            try:

                cost = buy_salt(amount, mine)
                salt = salt + amount
                gold = gold - cost
            except Exception as e:
                print(e)

            if is_bankrupt(gold):
                print("You are bankrupt")
                sys.exit()

        def do_sell(self, args):
            """Sell salt to a market in a city"""

            amount, market = args.split()
            amount = int(amount)

            global salt
            global gold

            try:
                revenue = sell_salt(amount, market)
                gold = gold + revenue
                salt = salt - amount
            except Exception as e:
                print(e)

        def do_exit(self, _):
            "Exit the game"
            return True

    Game().cmdloop()

# Options to improve on your own:
#
# - Add a function that lists available markets and mines.
# - Add checks that only existing mines and markets can be used.
# - If you have programmed random events and the bank from the previous
#   exercise, add the command-line interfaces to it.

# Next week:
#
# - Using an object-oriented programming style to extend the program more
#   easily.