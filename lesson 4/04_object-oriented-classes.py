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
#                               PART 4
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
# Cities and mines
#
###############################################################################

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config.yml')
args = parser.parse_args()

with open(args.config, 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)


class Mine():
    name = None
    shipping_cost = 0

    def __init__(self, name, shipping_cost):
        self.name = name
        self.shipping_cost = shipping_cost

    def purchase_salt(self, amount):
        cost = amount * (config["trading"]["costs"]["buy_cost"] + config["trading"]["costs"]["ship_cost"])
        return cost


class Market():
    name = None
    shipping_cost = 0

    def __init__(self, name, shipping_cost):
        self.name = name
        self.shipping_cost = self.shipping_cost

    def sell_salt(self, amount):
        revenue = amount * (config["trading"]["revenue"]["price"] - config["trading"]["costs"]["ship_cost"])
        return revenue


class Stock():
    gold = 0
    stock = 0
    MAX_STOCK = config["trading"]["stock"]["max"]

    def __init__(self, gold, stock):
        self.gold = gold
        self.stock = stock

    def get_stock(self):
        return self.stock

    def get_gold(self):
        return self.gold

    def add_salt(self, amount):
        if (self.stock + amount) > self.MAX_STOCK:
            raise Exception(f"You are full! You have {self.stock}kg of salt and can not add another {amount}kg")

        self.stock = self.stock + amount

    def remove_salt(self, amount):
        if amount > self.stock:
            raise Exception(f"You can't remove {amount}kg of salt from your stock, you only have {self.stock}kg")

        self.stock = self.stock - amount

    def add_gold(self, amount):
        self.gold = self.gold + amount

    def remove_gold(self, amount):
        if amount > self.gold:
            raise Exception(f"Can not remove more gold than you currently have. You have {self.gold} gold")
        self.gold = self.gold - amount

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

        my_stock = Stock(gold = 1500.0, stock = 0.0)
        mines = {}
        markets = {}

        def __init__(self):
            for mine in config["mines"]:
                self.mines[mine] = Mine(mine, shipping_cost = config["trading"]["costs"]["ship_cost"])

            for market in config["markets"]:
                self.markets[market] = Market(market, shipping_cost = config["trading"]["costs"]["ship_cost"])

        def do_list_stock(self):
            "List your stock"
            print(f"You have {self.my_stock.get_stock()}kg of salt and {self.my_stock.get_gold()} gold")

        def do_purchase(self, args):
            "Purchase salt from a mine"
            amount, mine = args.split()
            amount = int(amount)

            try:
                cost = self.mines[mine].purchase_salt(amount)
                self.my_stock.remove_gold(cost)
                self.my_stock.add_salt(amount)
                print(f"Purchased {amount}kg of salt for {cost} gold.")
            except Exception as e:
                print(e)

        def do_sell(self, args):
            "Sell salt to a market in a city"
            amount, market = args.split()
            amount = int(amount)

            try:
                revenue = self.markets[market].sell_salt(amount)
                self.my_stock.remove_salt(amount)
                self.my_stock.add_gold(revenue)
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