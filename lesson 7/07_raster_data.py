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
#                                  LESSON 7
# Expected learning outcomes:
#  - Read geospatial raster files into in-memory xarray data structures
#  - Extract values of raster at a geospatial location
#  - Reclassify raster values
#  - Perform mathematical operations (raster calculator)
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 19.05.2026
#
################################################################################

import yaml
import cmd
import argparse
import abc
from shapely import Point, LineString, distance, wkt
import xarray as xr
import xrspatial
import rioxarray
import random
import sys

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

    def __init__(self, name, location):
        """ Initialises the Mine using a name and the location

        Parameters
        ----------
        name : str
            The name of the mine.
        location : Point
            Shapely Point of the mine's location.
        """

        self.name = name
        self.location = location

    def purchase_salt(self, amount):
        """Method to buy salt

        This method allows to buy a certain amount of salt from a mine.

        Parameters
        ----------
        amount : float
            The amount of salt that should be bought (in kilogram).

        Returns
        -------
        float
            The cost of the salt that was purchased.
        """

        cost = amount * config["trading"]["costs"]["buy_cost"]
        return cost

    def get_location(self):
        """ Returns the location as Shapely Point.

        Returns
        -------
        Point
            The Shapely Point of the location.
        """
        return self.location


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

    def __init__(self, name, location):
        """ Initialises the Market using a name and the location.

        Parameters
        ----------
        name : str
            The name of the market.
        location : Point
            Shapely Point of the market's location.
        """

        self.name = name
        self.location = location

    def sell_salt(self, amount):
        """Method to sell salt

        This method allows to sell a certain amount of salt to a market.

        Parameters
        ----------
        amount : float
            The amount of salt that should be sold (in kilogram).

        Returns
        -------
        float
            The revenue from the salt that was sold.
        """

        revenue = amount * config["trading"]["revenue"]["price"]
        return revenue

    def get_location(self):
        """ Returns the location as Shapely Point.

        Returns
        -------
        Point
            The Shapely Point of the location.
        """
        return self.location


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

    def __init__(self, gold, salt, location):
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
        self.MAX_STOCK = config["trading"]["stock"]["max"]
        self.location = location

    def get_salt(self):
        """Returns the amount of salt in stock in kilogram.

        Returns
        -------
        float
            The the amount of salt currently in the stock (in kg).
        """

        return self.salt

    def get_gold(self):
        """Returns the amount of gold in stock.

        Returns
        -------
        float
            The the amount of gold currently in the stock.
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

    def get_location(self):
        """ Returns the location as Shapely Point.

        Returns
        -------
        Point
            The Shapely Point of the location.
        """
        return self.location


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
        Returns the name of the merchant.
    """

    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    def get_name(self):
        """Returns the name of the merchant

        Returns
        -------
        str
            The name of the merchant."""
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

    def __init__(self):
        self.shipping_cost = config["trading"]["costs"]["shipping_cost"]

    def print_name(self):
        """ Prints the name of the route """
        print(self.name)

    def get_name(self):
        """ Returns the name of the route

        Returns
        -------
        str
            The name of the route."""
        return self.name

    def get_merchant_name(self):
        """ Returns the name of the merchant currently employed on this route

        Returns
        -------
        str
            The name of the merchant for this route.
        """
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

    def get_length(self):
        """Returns the length of the route. The length is calculated using the
        shortest distance between the start and end point (linear distance).

        Returns
        -------
        float
            The length of the route in the unit of the CRS.
        """

        return self.route.length


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

    def __init__(self, name, mine, stock):
        super().__init__()
        self.name = name
        self.mine = mine
        self.stock = stock
        self.route = LineString([mine.get_location(), stock.get_location()])

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

    def __init__(self, name, market, stock):
        super().__init__()
        self.name = name
        self.market = market
        self.stock = stock
        self.route = LineString([market.get_location(), stock.get_location()])

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


class Topography():
    """
    Class for spatial calculations and deriving information for the mines and
    the markets. Basic information for topography (based on a digital elevation
    model) and weather (precipitation including snow and rain) is provided.

    Attributes
    ----------
    dem : xarray Dataset
        xarray raster Dataset containing altitude values in meter. To be loaded
        from a dem raster file.
    snow_depth : xarray Dataset
        xarray raster Dataset containing the snow depth in cm.
    precipitation : xarray Dataset
        xarray raster Dataset containing the precipitation values. To be loaded
        from a simulated raster file using a random choice from one of tree
        files.
    SN_COND_MSG: dict
        Dictionary with text messages for the snow conditions.
    PR_COND_MSG: dict
        Dictionary with text messages for the precipitation conditions.

    Methods
    ----------
    get_altitude(point)
        Returns the altitude of a given location passed as a Shapely Point.
    get_snow_depth(point)
        Returns the altitude of a given location passed as a Shapely Point.
    print_weather_report(point)
        Returns the weather report of a given location passed as a Shapely
        Point.
    """

    def __init__(self, base_dir):

        self._base_data_dir = base_dir + '/'

        try:
            self.dem = (
                rioxarray.open_rasterio(self._base_data_dir + 'salt_traders_dem.tif', lock = False)
                .load()
                .sel(band = 1)
            )
            self.snow_depth = xr.zeros_like(self.dem)
            self._weather_update()
        except Exception as e:
            print(e)
            sys.exit()

        self.SN_COND_MSG = {
            0: "We are below the snow line, precipitation is rain",
            1: "We are above the snow line, precipitation is snow"
        }

        self.PR_COND_MSG = {
            0: "It is dry as the overcooked steak we had for lunch. Btw, we should get a new cook",
            1: "Expect some light precipitation. It will be likely not enough to interrupt our business",
            2: "Precipitation will be coming",
            3: "We expect heavy precipitation. Brace yourself",
            4: "We have a serious problem, and this time it's not the cook"
        }

    def _weather_update(self):
        """ Updates the weather information. This includes selecting randomly a
            file for the precipitation, updating the snowline and the snow
            depth.
        """

        #
        # Reading one of three precipitation raster files. The precipitation
        # values have been simulated.
        #
        try:
            pr_file = self._base_data_dir + "precipitation_scenario_" + str(random.randint(1,3)) + ".tif"
            self.precipitation = (
                rioxarray.open_rasterio(pr_file, lock = False)
                .load()
                .sel(band = 1)
            )
        except Exception as e:
            print(e)
            sys.exit()

        #
        # Define a random snow line altitude. Above this altitude, the
        # precipitation will be snow, below this altitude it will be rain.
        #
        snowline_altitude = random.randint(100, 1000)

        #
        # Set all values in the raster cell to 0 if they are below the snow line
        # and to 1 if they are above.
        #
        self.snowline = xr.where(self.dem > snowline_altitude, 1, 0).astype("uint8")

        #
        # Calculating the snow depth by adding to the existing one 10% of the
        # precipitation if the precipitation is above the snowline.
        #
        self.snow_depth = self.snow_depth + (self.snowline * self.precipitation / 10)

        #
        # Reclassify the precipitation values into code ranging from 0 to 4:
        #   0 - No precipitation
        #   1 - light precipitation
        #   2 - medium precipitation
        #   3 - heavy precipitation
        #   4 - very heavy precipitation
        #
        self.precipitation = xrspatial.reclassify(
            self.precipitation,
            bins=[0, 20, 50, 75, 100],
            new_values=[0, 1, 2, 3, 4])

    def _get_value(self, dataset, point):
        """ Returns the value of a certain location. The location needs to be
        passed as Shapely point.

        Parameters
        ----------
        point : Point
            The location as Shapely point.

        Returns
        -------
        object
            Raster value of the point location. Type depends on the
            raster data type (e.g. str, int, list).
        """
        return dataset.sel(x=point.y, y=point.x, method="nearest").values

    def get_altitude(self, point):
        """ Returns the altitude at a certain location. The location needs to
        be passed as Shapely point.

        Parameters
        ----------
        point : Point
            The location as Shapely point.

        Returns
        -------
        object
            Raster value of the point location. Type depends on the
            raster data type (e.g. str, int, list).
        """
        return self._get_value(self.dem, point)

    def get_snow_depth(self, point):
        """ Returns the snow depth at a certain location. The location needs to
        be passed as Shapely point.

        Parameters
        ----------
        point : Point
            The location as Shapely point.

        Returns
        -------
        object
            Raster value of the point location. Type depends on the
            raster data type (e.g. str, int, list).
        """
        return self._get_value(self.snow_depth, point)

    def print_weather_report(self, point):
        """ Prints the weather report of a certain location to the screen. The
        location needs to be passed a Shapely point.

        Parameters
        ----------
        point : Point
            The location as Shapely point.
        """
        self._weather_update()

        snow_condition = self._get_value(self.snowline, point)
        rain_condition = self._get_value(self.precipitation, point)

        print(
            f"The location is on {self.get_altitude(point):.2f}m above sea level. " +
            self.SN_COND_MSG.get(int(snow_condition)) + ". " +
            f"There is {self.get_snow_depth(point):.2f} cm of snow. " +
            self.PR_COND_MSG.get(int(rain_condition)) + ". "
        )


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
        'add_market Burghausen POINT(48.16925 12.83139)'. Get the weather report
        by typing 'weather <name>' where <name> is any market or mine.
        """
        prompt = "The Salt Traders> "

        stock_location = Point(
            config["trading"]["stock"]["latitude"],
            config["trading"]["stock"]["longitude"])
        my_stock = Stock(
            gold = args.gold,
            salt = args.salt,
            location = stock_location)
        mines = {}
        markets = {}
        trade_routes = {}
        merchants = []

        def __init__(self):
            super().__init__()
            for mine in config["mines"]:
                name = mine["name"]
                lat = mine["latitude"]
                lon = mine["longitude"]
                self.mines[name] = Mine(name, Point(lat, lon))

            for market in config["markets"]:
                name = market["name"]
                lat = market["latitude"]
                lon = market["longitude"]
                self.markets[name] = Market(name, Point(lat, lon))

            self.merchants.append(Merchant("Karl", 0.1, 1))
            self.merchants.append(Merchant("Freya", 0.2, 3))
            self.merchants.append(Merchant("Ulrich", 0.1, 2))

            self.dem = Topography('../data')

        def do_list_stock(self, _):
            "List your stock"
            print(f"You have {self.my_stock.get_salt()}kg of salt and {self.my_stock.get_gold()} gold")

        def do_add_route(self, line):
            "Add a new trading route"
            type, name, target = line.split()
            if type == "purchase":
                self.trade_routes[name] = PurchaseRoute(name, self.mines[target], self.my_stock)
            if type == "sell":
                self.trade_routes[name] = SellRoute(name, self.markets[target], self.my_stock)
            print(f"Added new route {self.trade_routes[name].get_name()}.")

        def do_list_routes(self, _):
            "List your trading routes"
            print(f"You have {len(self.trade_routes)} routes:")
            for route in self.trade_routes.values():
                route.print_name()

        def do_trade(self, line):
            "Purchase salt from a mine"
            amount, route = line.split()
            amount = int(amount)

            try:
                self.trade_routes[route].trade(amount)
            except Exception as e:
                print(e)

        def do_hire_merchant(self, line):
            "Hire a new merchant for the route"
            merchant_name, route_name = line.split()
            for merchant in self.merchants:
                if merchant.get_name() == merchant_name:
                    self.trade_routes[route_name].hire_merchant(merchant)
                    print(f"You hired merchant {merchant_name} for route {self.trade_routes[route_name].get_name()}")

        def do_fire_merchant(self, line):
            "Fire a merchant from a route"
            merchant_name = line
            for route in self.trade_routes.values():
                if route.get_merchant_name() == merchant_name:
                    route.fire_merchant()
                    print(f"You fired merchant {merchant_name} from route {route.get_name()}")

        def do_explore_route(self, line):
            "Explores a route and reports the distance and shipping costs"
            destination = line

            stock_location = self.my_stock.get_location()

            if destination in self.mines:
                target_location = self.mines[destination].get_location()
            elif destination in self.markets:
                target_location = self.markets[destination].get_location()
            else:
                print(f"Could not find route to destination {destination}!")
                return

            distance = stock_location.distance(target_location)
            shipping_cost = distance * config["trading"]["costs"]["shipping_cost"]
            print(f"The distance between your stock and the target {destination} is {distance}! " +
                    f"The shipping costs are {shipping_cost} gold per kg of salt.")

        def do_add_market(self, line):
            "Adding a new market using a name and the WKT geometry"
            name, wkt_geometry = line.split(' ', 1)
            self.markets[name] = Market(name, wkt.loads(wkt_geometry))
            print(f"Added market {name} at {wkt_geometry}.")

        def do_weather(self, line):
            "Prints the weather report"
            location = line
            if location in self.mines:
                target_location = self.mines[location].get_location()
                self.dem.print_weather_report(target_location)
            elif location in self.markets:
                target_location = self.markets[location].get_location()
                self.dem.print_weather_report(target_location)
            else:
                print(f"Could not find weather for location {location}!")
                return

        def do_exit(self, _):
            "Exit the game"
            return True

    TheSaltTraders().cmdloop()


# Options to improve on your own:
#
# - The snow is accumulating, it does not melt. Update the raster calculator
#   formula to allow melting of 10% of the snow if it is under the snow line.
# - Use the weather data to influence the cost of the salt trade. If there is
#   snow, the shipping cost will increase.

# Next week:
#
# - Coordinate transformations and handling geometries with different coordinate
#   reference systems.