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
#  - Creating hierachies of classes
#  - Using class composition
#  - Using polymorphism to reduce the code.
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 26.04.2026
#
################################################################################

import yaml
import cmd
import argparse
import abc

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

    # TODO: remove shipping_cost from the Mine and add it to the route.

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

    # TODO: remove shipping_cost from the Mine and add it to the route.

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


# TODO: Add class Merchant (remove pass)
#       Learning objective: Learn how to use class composition for organising
#       classes.
class Merchant():
    pass

# TODO: Add abstract class TradeRoute
#       Learning objective: Learn how to use object hierarchies for organising
#       classes.
class TradeRoute():
    pass

# TODO: Add class PurchaseRoute
#       Learning objective: Learn how to use object hierarchies for organising
#       classes.
class PurchaseRoute():
    pass

# TODO: Add class SellRoute
#       Learning objective: Learn how to use object hierarchies for organising
#       classes.
class SellRoute():
    pass

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

        You can see your stock by typing 'list_stock'. Add a trading route by
        typing 'add_route purchase <name> <mine>' for purchasing salt at a mine
        and 'add_route sell <name> <market>' for selling salt at a market. Type
        'trade <amount> <name>' to trade on a route, while <amount> is the kg of
        salt and name is the <name> of the route. You can hire a merchant by 
        typing 'hire_merchant <merchant_name> <route_name>' and fire a merchant
        by typing 'fire_merchant <merchant_name>'.
        """
        prompt = "The Salt Traders> "

        my_stock = Stock(gold = args.gold, salt = args.salt)
        mines = {}
        markets = {}
        trade_routes = {}
        merchants = []

        def __init__(self):
            super().__init__()
            for mine in config["mines"]:
                self.mines[mine] = Mine(mine)
                
            for market in config["markets"]:
                self.markets[market] = Market(market)

            self.merchants.append(Merchant("Karl", 0.1, 1))
            self.merchants.append(Merchant("Freya", 0.2, 3))
            self.merchants.append(Merchant("Ulrich", 0.1, 2))

        def do_list_stock(self, args):
            "List your stock"
            print(f"You have {self.my_stock.get_salt()}kg of salt and {self.my_stock.get_gold()} gold")

        # TODO: Add a method to add a trading route (for purchasing or selling)
        #       and a method to list the routes.
        #       Learning objective: Learn how to use object hierarchies for
        #       organising classes.

        # TODO: Remove do_purchase and do_sell and replace with a single
        #       method do_trading that takes the amount and trading route.
        #       Learning objective: Learn how to use polymorphism in object-
        #       oriented programming.
    
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

        # TODO: Add a method to hire a merchant and one to fire them.

        def do_exit(self, _):
            "Exit the game"
            return True

    Game().cmdloop()

# Options to improve on your own:
#
# - Use the salary and experience of the merchant to influence the price.
# - Add more merchants and add a check that a merchant can only be hired
#   if they are free.
# - Add a class StockClerk that can be employed in the stock to increase the 
#   maximum capacity. Hint: You may use a class employees and use
#   inheritance or composition for the merchants and the stock clerk.
# - Change the shipping cost to a cost per unit and not per overall shipment.

# Next week:
#
# - Use geospatial vector data to position mines and markets and calculate
#   addition geometric and topological attributes (e.g. distances).