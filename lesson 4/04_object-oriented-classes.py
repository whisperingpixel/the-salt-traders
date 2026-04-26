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

class Mine():
    """
    A Mine allows to purchase salt.

    Attributes
    ----------
    name : str
        The name of the mine
    shipping_cost : float
        the amount of gold required to bring the salt from the mine to your
        stock.

    Methods
    ----------
    purchase_salt(amount)
        Buys salt from the mine.
    """

    name = None
    shipping_cost = 0

    def __init__(self, name, shipping_cost):
        """ Initialises the Mine using a name and the shipping cost.

        Parameters
        ----------
        name : str
            The name of the mine.
        shipping_cost : float
            The amount of gold required to bring the salt from the mine to your
            stock.
        """

        self.name = name
        self.shipping_cost = shipping_cost

    def purchase_salt(self, amount):
        """Method to buy salt

        This method allows to buy a certain amount of salt from a mine.

        Parameters
        ----------
        amount : float
            The amount of salt that should be bought (in kilogram).
        """

        cost = amount * (config["trading"]["costs"]["buy_cost"] + config["trading"]["costs"]["shipping_cost"])
        return cost


class Market():
    """
    A Market allows to sell salt.

    Attributes
    ----------
    name : str
        The name of the market
    shipping_cost : float
        the amount of gold required to bring the salt from the market to your
        stock.

    Methods
    ----------
    sell_salt(amount)
        Sells salt from the mine (in kilogram).
    """

    name = None
    shipping_cost = 0

    def __init__(self, name, shipping_cost):
        """ Initialises the Market using a name and the shipping cost.

        Parameters
        ----------
        name : str
            The name of the market.
        shipping_cost : float
            The amount of gold required to bring the salt from your stock to the
            market.
        """

        self.name = name
        self.shipping_cost = self.shipping_cost

    def sell_salt(self, amount):
        """Method to sell salt

        This method allows to sell a certain amount of salt to a market.

        Parameters
        ----------
        amount : float
            The amount of salt that should be sold (in kilogram).
        """

        revenue = amount * (config["trading"]["revenue"]["price"] - config["trading"]["costs"]["shipping_cost"])
        return revenue


class Stock():
    """
    The Stock manages your salt and gold

    Attributes
    ----------
    gold : float
        The amount of gold in the stock in kilogram.
    salt : float
        the amount of salt in the stock in kilogram.
    MAX_STOCK : float
        the maximum amount of salt in the stock in kilogram.

    Methods
    ----------
    get_salt()
        Returns the amount of salt in kilogram.
    
    get_gold()
        Returns the amount of gold in stock.

    add_salt(amount)
        Adds salt to the stock (in kilogram).
    
    remove_salt(amount)
        Removes salt from the stock (in kilogram).
    
    add_gold(amont)
        adds gold to the stock.
    
    remove_gold(amount)
        removes gold from the stock.
    """

    gold = 0
    salt = 0
    MAX_STOCK = config["trading"]["stock"]["max"]

    def __init__(self, gold, salt):
        """ Initialises the Stock using a default gold and salt.

        Parameters
        ----------
        gold : float
            The initial amount of gold in the stock.
        salt : float
            The initial amount of salt in the stock (usually 0).
        """

        self.gold = gold
        self.salt = salt

    def get_salt(self):
        """Returns the amount of salt in stock in kilogram.
        """

        return self.salt

    def get_gold(self):
        """Returns the amount of gold in stock.
        """

        return self.gold

    def add_salt(self, amount):
        """Method to add salt to the stock.

        This method adds salt to the stock if there is still enough space. If
        the amount exceeds the MAX_STOCK parameter, the salt will be rejected.

        Parameters
        ----------
        amount : float
            The amount of salt that should be added.
        """

        if (self.salt + amount) > self.MAX_STOCK:
            raise Exception(f"You are full! You have {self.salt}kg of salt and can not add another {amount}kg")

        self.salt = self.salt + amount

    def remove_salt(self, amount):
        """Method to remove salt from the stock.

        This method removes salt from the stock if it is in there. If the amount
        exceeds the current amount of salt in stock, an exception will be
        thrown.

        Parameters
        ----------
        amount : float
            The amount of salt that should be removed.
        """

        if amount > self.salt:
            raise Exception(f"You can't remove {amount}kg of salt from your stock, you only have {self.salt}kg")

        self.salt = self.salt - amount

    def add_gold(self, amount):
        """Method to add gold to the stock

        Parameters
        ----------
        amount : float
            The amount of gold that should be added.
        """

        self.gold = self.gold + amount

    def remove_gold(self, amount):
        """Method to remove gold from the stock

        Parameters
        ----------
        amount : float
            The amount of gold that should be removed.
        """

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
        intro = """
        Welcome to the world of salt, merchant!

        You can see your stock by typing 'list_stock'. Type 'purchase <amount> <mine>'
        to purchase salt from a mine. For example: 'purchase 100 Dürrnberg' to
        purchase 100kg from the Dürrnberg mine. Type 'sell <amount> <market>'
        to sell salt to a market. For example: 'sell 100 Passau' to sell 100kg
        of salt to Passau.
        """
        prompt = "The Salt Traders> "

        my_stock = Stock(gold = args.gold, salt = args.salt)
        mines = {}
        markets = {}

        def __init__(self):
            super().__init__()
            for mine in config["mines"]:
                self.mines[mine] = Mine(mine, shipping_cost = config["trading"]["costs"]["shipping_cost"])

            for market in config["markets"]:
                self.markets[market] = Market(market, shipping_cost = config["trading"]["costs"]["shipping_cost"])

        def do_list_stock(self, args):
            "List your stock"
            print(f"You have {self.my_stock.get_salt()}kg of salt and {self.my_stock.get_gold()} gold")

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


# Assignment for next week:
#
# - Add a class for events (as in the assignment in lesson 2) that can block
#   buying or selling salt. Instantiate the classes with probabilities for an
#   outbreak. Add a method that checks whether or not an outbreak happened when 
#   a do_sell or do_purchase command is executed.

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
# - Create trading routes for selling and purchasing (class hierarchy)
# - Add a merchant that can influence the price (composition).