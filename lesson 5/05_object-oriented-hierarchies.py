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

    Methods
    ----------
    purchase_salt(amount)
        Buys salt from the mine.
    """

    name = None

    def __init__(self, name):
        """ Initialises the Mine using a name and the shipping cost.

        Parameters
        ----------
        name : str
            The name of the mine.
        """

        self.name = name

    def purchase_salt(self, amount):
        """Method to buy salt

        This method allows to buy a certain amount of salt from a mine.

        Parameters
        ----------
        amount : float
            The amount of salt that should be bought (in kilogram).
        """

        cost = amount * config["trading"]["costs"]["buy_cost"]
        return cost


class Market():
    """
    A Market allows to sell salt.

    Attributes
    ----------
    name : str
        The name of the market

    Methods
    ----------
    sell_salt(amount)
        Sells salt from the mine (in kilogram).
    """

    name = None
    shipping_cost = 0

    def __init__(self, name):
        """ Initialises the Market using a name and the shipping cost.

        Parameters
        ----------
        name : str
            The name of the market.
        """

        self.name = name

    def sell_salt(self, amount):
        """Method to sell salt

        This method allows to sell a certain amount of salt to a market.

        Parameters
        ----------
        amount : float
            The amount of salt that should be sold (in kilogram).
        """

        revenue = amount * config["trading"]["revenue"]["price"]
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


class Merchant():
    """
    A Merchant can be employed for a route.

    Attributes
    ----------
    name : str
        The experience of a merchant

    experience : int
        The experience of a merchant

    salary : float
        The salary of a merchant (% commission of a trade)

    Methods
    ----------
    get_name()
        Returns the name of the Merchant.
    """

    experience = 1 # 1 to 5 stars
    salary = 0.1 # in percent
    name = None

    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    def get_name(self):
        """Returns the name of the merchant"""
        return self.name


class TradeRoute(abc.ABC):
    """
    Abstract base class for trading routes

    Attributes
    ----------
    name : str
        The name of the route.

    merchant : Merchant
        The Merchant for the route (or None).

    shipping_cost : float
        The shipping cost for the route.

    Methods
    ----------
    get_name()
        Returns the name of the route.

    get_merchant_name()
        Returns the name of the merchant for the route.

    hire_merchant()
        Hires a Merchant for the route.

    fire_merchant()
        Fires the Merchant of the route
    """

    name = None
    merchant = None
    shipping_cost = 1.5

    def print_name(self):
        """ Prints the name of the route """
        print(self.name)

    def get_name(self):
        """ Returns the name of the route """
        return self.name
    
    def get_merchant_name(self):
        """ Returns the name of the merchant """
        return self.merchant.get_name()
    
    def hire_merchant(self, merchant):
        """ Hires a merchant for the route.

        Parameters
        ----------
        merchant : Merchant
            The merchant that will be employed in the route.
        """

        if (self.merchant != None):
            raise Exception("There is aleady a merchant on this route!")
        self.merchant = merchant
        print(f"Merchant {self.merchant.get_name()} was hired")

    def fire_merchant(self):
        """ Fires the merchant from  the route. """

        if (self.merchant == None):
            raise Exception("There is no merchant on this route")
        
        print(f"Fire merchant {self.merchant.get_name()}")
        self.merchant = None


class PurchaseRoute(TradeRoute):
    """
    Subclass of the TradeRoute to instantiate a route from the mine to our
    stock.

    Attributes
    ----------
    name : str
        The name of the route.

    mine : Mine
        The Mine for purchasing the salt.

    stock : Stock
        Our Stock.

    Methods
    ----------
    trade(amount)
        Buys the amount of salt from the mine and deposits it in our stock.
    """

    name = None
    mine = None
    stock = None

    def __init__(self, name, mine, stock):
        self.name = name
        self.mine = mine
        self.stock = stock

    def trade(self, amount):
        """ Buys the amount of salt from the mine and deposits it in our stock.

        Parameters
        ----------
        amount : float
            The amount of salt to buy.
        """

        cost = self.mine.purchase_salt(amount) + self.shipping_cost
        self.stock.remove_gold(cost)
        self.stock.add_salt(amount)
        print(f"Purchased {amount}kg of salt for {cost} gold.")


class SellRoute(TradeRoute):
    """
    Subclass of the TradeRoute to instantiate a route from the our stock to
    a market.

    Attributes
    ----------
    name : str
        The name of the route.

    market : Market
        The Market for selling the salt.

    stock : Stock
        Our Stock.

    Methods
    ----------
    trade(amount)
        Sells the amount of salt at the market.
    """

    name = None
    Market = None
    stock = None

    def __init__(self, name, market, stock):
        self.name = name
        self.market = market
        self.stock = stock

    def trade(self, amount):
        """ Sells the amount of salt at the market.

        Parameters
        ----------
        amount : float
            The amount of salt to sell.
        """

        revenue = self.market.sell_salt(amount) - self.shipping_cost
        self.stock.add_gold(revenue)
        self.stock.remove_salt(amount)
        print(f"Sold {amount}kg of salt for {revenue} gold.")


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

        def do_add_route(self, args):
            "Add a new trading route"
            type, name, target = args.split()
            if type == "purchase":
                self.trade_routes[name] = PurchaseRoute(name, self.mines[target], self.my_stock)
            if type == "sell":
                self.trade_routes[name] = SellRoute(name, self.markets[target], self.my_stock)
            print(f"Added new route {self.trade_routes[name].get_name()}.")

        def do_list_routes(self, args):
            "List your trading routes"
            print(f"You have {len(self.trade_routes)} routes:")
            for route in self.trade_routes.values():
                route.print_name() 

        def do_trade(self, args):
            "Purchase salt from a mine"
            amount, route = args.split()
            amount = int(amount)

            try:
                self.trade_routes[route].trade(amount)
            except Exception as e:
                print(e)

        def do_hire_merchant(self, args):
            "Hire a new merchant for the route"
            merchant_name, route_name = args.split()
            for merchant in self.merchants:
                if merchant.get_name() == merchant_name:
                    self.trade_routes[route_name].hire_merchant(merchant)
                    print(f"You hired merchant {merchant_name} for route {self.trade_routes[route_name].get_name()}")

        def do_fire_merchant(self, args):
            "Fire a merchant from a route"
            merchant_name = args
            for route in self.trade_routes.values():
                if route.get_merchant_name() == merchant_name:
                    route.fire_merchant()
                    print(f"You fired merchant {merchant_name} from route {route.get_name()}")

        def do_exit(self, _):
            "Exit the game"
            return True

    Game().cmdloop()

# Options to improve on your own:
#
# - Use the salary and experience of the merchant to influence the price.
# - Add more merchants and add a check that a merchant can only be hired
#   if they are free. Then, implement a CLI-method to list the available 
#   merchants.
# - Add a class StockClerk that can be employed in the stock to increase the 
#   maximum capacity. Hint: You may use a class employees and use.
#   inheritance or composition for the merchants and the stock clerk.
# - Change the shipping cost to a cost per unit and not per overall shipment.
# - Split the classes into individual files for a organisation of the source
#   code.

# Next week:
#
# - Use geospatial vector data to position mines and markets and calculate
#   addition geometric and topological attributes (e.g. distances).