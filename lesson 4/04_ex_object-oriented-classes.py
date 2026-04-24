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
#                                    PART 4
# Expected learing outcomes:
#  - Creating and instantiating classes
#  - Using class methods
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 22.04.2026
#
################################################################################

import yaml
import cmd
import argparse

###############################################################################
#
# Configuration
#
###############################################################################

#
# Command-line input
#
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config.yml')
parser.add_argument('--gold', type=float, default=1500)
parser.add_argument('--salt', type=float, default=0)
args = parser.parse_args()

#
# Configuration
#
with open(args.config, 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)

###############################################################################
#
# Classes
#
###############################################################################

# TODO: Create a class 'Mine' that allows purchasing salt

# TODO: Create a class 'Market' that allows selling salt

# TODO: Create a class 'Stock' that manages your gold and salt

###############################################################################
#
# Start of the program.
# This is the heart of the mechanism.
#
###############################################################################

if __name__ == "__main__":

    class Game(cmd.Cmd):
        intro = "Welcome"
        prompt = "Anno> "

        # TODO: Initialise your stock
        mines = {}
        markets = {}

        def __init__(self):
            for mine in config["mines"]:
                pass
                # TODO: Initialise the mine.
                # NOTE: Remove the 'pass' keyword!

            for market in config["markets"]:
                pass
                # TODO: Initialise the market.
                # NOTE: Remove the 'pass' keyword!

        def do_list_stock(self):
            "List your stock"
            print(f"You have {self.my_stock.get_salt()}kg of salt and {self.my_stock.get_gold()} gold")

        def do_purchase(self, args):
            "Purchase salt from a mine"
            amount, mine = args.split()
            amount = int(amount)

            try:
                # TODO: Purchase the salt from the mine, add the salt to your
                #       stock and reduce the money.
                print(f"Purchased {amount}kg of salt for {cost} gold.")
            except Exception as e:
                print(e)

        def do_sell(self, args):
            "Sell salt to a market in a city"
            amount, market = args.split()
            amount = int(amount)

            try:
                # TODO: Sell the salt at the market, reduce the salt in your
                #       stock and add the money.
                print(f"Sold {amount}kg of salt for {revenue} gold")
            except Exception as e:
                print(e)

        def do_exit(self, _):
            "Exit the game"
            return True

    Game().cmdloop()

# Options to improve on your own:
# - Add more markets.
# - Add a class bank that can give a credit to buy salt,
#   but the money needs to be paid back.
# - Add a individual deposit per mine that fills per iteration with a certain
#   amount (capacity). You can only buy what's in the deposit for each
#   iteration.
# - Add custom shipping costs per mine.
# - Add a market saturation.

# Next week:
#
# - Create trading routes
# - Add a merchant that can influence the price.
# - Add random disaster events