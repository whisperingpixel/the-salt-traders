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
#                                  LESSON 6
# Expected learning outcomes:
#  - Instantiate Shapely geometries (Point, Linestring)
#  - Use Well-Known Text (WKT) to instantiate Shapely geometries
#  - Calculate geometric properties of Shapely geometries
#  - Calculate geometric relationships between Shapely geometries
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 06.05.2026
#
################################################################################

import yaml
import cmd
import argparse
import abc
from shapely import Point, LineString, distance, wkt

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
try:
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("No read access")
except OSError as e:
    print(f"OS error: {e}")

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
    location : Point
        Shapely Point of the mine's location.

    Methods
    ----------
    purchase_salt(amount)
        Buys salt from the mine.
    get_location()
        Returns the Shapely Point of the mine's location.
    """

    name = None
    # TODO: Add a location variable that holds the location as Shapely
    # coordinates.

    def __init__(self, name):
        """ Initialises the Mine using a name and the location

        Parameters
        ----------
        name : str
            The name of the mine.
        location : Point
            Shapely Point of the mine's location.
        """

        self.name = name
        # TODO: Initialise the location variable passed in this constructor as 
        #       a variable.

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

    # TODO: Implement a function that returns the location variable.

class Market():
    """
    A Market allows to sell salt.

    Attributes
    ----------
    name : str
        The name of the market
    location : Point
        Shapely Point of the market's location.

    Methods
    ----------
    sell_salt(amount)
        Sells salt at the market (in kilogram).
    get_location()
        Returns the Shapely Point of the markets's location.
    """

    name = None
    # TODO: Add a location variable that holds the location as Shapely
    # coordinates.

    def __init__(self, name):
        """ Initialises the Market using a name and the location.

        Parameters
        ----------
        name : str
            The name of the market.
        location : Point
            Shapely Point of the market's location.
        """

        self.name = name
        # TODO: Initialise the location variable passed in this constructor as 
        #       a variable.

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

    # TODO: Implement a function that returns the location variable.

class Stock():
    """
    The Stock manages your salt and gold

    Attributes
    ----------
    gold : float
        The amount of gold in the stock in kilogram.
    salt : float
        the amount of salt in the stock in kilogram.
    location : Point
        Shapely Point of the stock's location.
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
    get_location()
        Returns the location of the stock as Shapely Point.
    """

    gold = 0
    salt = 0
    MAX_STOCK = config["trading"]["stock"]["max"]

    # TODO: Add a location variable that holds the location as Shapely
    # coordinates.

    def __init__(self, gold, salt):
        """ Initialises the Stock using a default gold and salt.

        Parameters
        ----------
        gold : float
            The initial amount of gold in the stock.
        salt : float
            The initial amount of salt in the stock (usually 0).
        location : Point
            Shapely Point of the stock's location.
        """

        self.gold = gold
        self.salt = salt
        # TODO: Initialise the location variable.

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

    # TODO: Implement a function that returns the location variable


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
    route : LineString
        A shapely geometry of the route
    merchant : Merchant
        The Merchant for the route (or None).
    shipping_cost : float
        The shipping cost for 1kg of salt per 1 travel unit.

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
    get_length()
        Returns the length of the route
    """

    name = None
    merchant = None
    shipping_cost = config["trading"]["costs"]["shipping_cost"]

    # TODO: Add a variable called 'route' that will hold the LineString as 
    #       Shapely geometry.

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

    # TODO: Implement a function called 'get_length()' that returns the length
    #       of the route using the LineString variable
    #       Learning objective: Accessing geometric properties from Shapely
    #       geometries. Additionally: Using inheritance as object-oriented
    #       programming concept.


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
    get_length()
        Returns the length of the route
    """

    name = None
    mine = None
    stock = None

    def __init__(self, name, mine, stock):
        self.name = name
        self.mine = mine
        self.stock = stock
        # TODO: Add the route as LineString using the mine and stock location
        #       Use the previously implemented get_location() method.
        #       Learning objective: Instantiating Shapely geometries.

    def trade(self, amount):
        """ Buys the amount of salt from the mine and deposits it in our stock.

        Parameters
        ----------
        amount : float
            The amount of salt to buy.
        """

        cost = self.mine.purchase_salt(amount) + (amount * self.get_length() * self.shipping_cost)
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
    get_length()
        Returns the length of the route
    """

    name = None
    Market = None
    stock = None

    def __init__(self, name, market, stock):
        self.name = name
        self.market = market
        self.stock = stock
        # TODO: Add the route as LineString using the market and stock location
        #       Use the previously implemented get_location() method.
        #       Learning objective: Instantiating Shapely geometries.

    def trade(self, amount):
        """ Sells the amount of salt at the market.

        Parameters
        ----------
        amount : float
            The amount of salt to sell.
        """

        revenue = self.market.sell_salt(amount) - (amount * self.get_length() * self.shipping_cost)
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

    class TheSaltTraders(cmd.Cmd):
        intro = """
        Welcome to the world of salt, merchant!

        You can see your stock by typing 'list_stock'. Explore a trading route
        by tying 'explore_route <name>' and while name is the name of the mine
        or market. Add a trading route by typing 'add_route purchase <name> <mine>'
        for purchasing salt at a mine and 'add_route sell <name> <market>' for
        selling salt at a market. Type 'trade <amount> <name>' to trade on a
        route, while <amount> is the kg of salt and name is the <name> of the
        route. You can hire a merchant by typing 'hire_merchant <merchant_name> <route_name>'
        and fire a merchant by typing 'fire_merchant <merchant_name>'. Add a new
        market by typing 'add_market <name> POINT(<latitude> <longitude>)', e.g.
        'add_market Burghausen POINT(48.16925 12.83139)'.
        """
        prompt = "The Salt Traders> "

        # TODO: Use the latitude and longitude in the config file to define the
        #       location of our stock using a Shapely Point. Don't forget to
        #       pass it to the Stock's constructor!
        #       Learning objective: Instantiating Shapely geometries.

        my_stock = Stock(
            gold = args.gold,
            salt = args.salt)
        mines = {}
        markets = {}
        trade_routes = {}
        merchants = []

        def __init__(self):
            super().__init__()
            for mine in config["mines"]:
                name = mine["name"]
                # TODO: Use the latitude and longitude in the config file to
                #       define the location of the mine using a Shapely Point.
                #       Don't forget to pass it to the Mine's constructor!
                #       Learning objective: Instantiating Shapely geometries.
                self.mines[name] = Mine(name)

            for market in config["markets"]:
                name = market["name"]
                # TODO: Use the latitude and longitude in the config file to
                #       define the location of the mine using a Shapely Point.
                #       Don't forget to pass it to the Mine's constructor!
                #       Learning objective: Instantiating Shapely geometries.
                self.markets[name] = Market(name)

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

        # TODO: Complete the function that calculates the distance between our 
        #       stock and a destination (mine or market) defined by the user
        #       input.
        #       Learning objective: Calculating geometric relationships between
        #       two Shapely geometries.
        def do_explore_route(self, args):
            "Explores a route and reports the distance and shipping costs"
            destination = args
            distance = None
            shipping_cost = distance * config["trading"]["costs"]["shipping_cost"]
            print(f"The distance between your stock and the target {destination} is {distance}! " +
                    f"The shipping costs are {shipping_cost} gold per kg of salt.")

        # TODO: Complete the function that adds a new market using a latitude
        #       and longitude coordinate tuple as user input. Translate them
        #       into a WKT format for input.
        #       Learning objective: Using WKT to instantiate Shapely geometries.
        def do_add_market(self, args):
            "Adding a new market using a name and the WKT geometry"
            name, wkt_geometry = args.split()
            print(f"Added market {name} at {wkt_geometry}.")

        def do_exit(self, _):
            "Exit the game"
            return True

    TheSaltTraders().cmdloop()


# Options to improve on your own:
#
# - Use the event class you created as the assignment of lesson 4 and extend it
#   with polygon geometries. For each event occurrence, check whether the
#   polygon of the event intersects with the trading route.
# - Calculate the travel time by using a reasonable distance per day ratio
#   (consider medieval boat shipping!).

# Next week:
#
# - Use geospatial raster data for additional calculations (e.g. using a digital
#   elevation model).