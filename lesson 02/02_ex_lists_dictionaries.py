################################################################################
#
# The Salt Traders · A merchant simulation game of the medieval salt trade
#
################################################################################
#
# This program is part of the exercise "Basics of Software Development Practice"
# at the Department of Geoinformatics (University of Salzburg).
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
#                                  LESSON 2
# Expected learning outcomes:
#  - Creating and using lists and dictionaries in Python
#  - Accessing values from lists and dictionaries
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 05.08.2026
#
################################################################################

import random

###############################################################################
#
# Variables and constants
#
###############################################################################

#
# Mines
#

# TODO: Create a list that contains the names of the two mines 'Dürrnberg' and
#       'Berchtesgaden'
#       Learning objective: Creating lists in Python.
mines = ...

#
# Markets
#

# TODO: Create a list that contains the names of the three markets 'Salzburg',
#       'Passau', and 'Laufen'.
#       Learning objective: Creating lists in Python.
markets = ...

#
# Initial state of the stock
#

# TODO: Instead of storing the two variables 'salt' and 'gold' separately,
#       create a dictionary 'stock' with two attributes.
#       Learning objective: Creating dictionaries in Python.
stock = ...

#
# Trading
#
BUYING_COST = 5.0      # gold per kg
SHIPPING_COST = 1.5     # gold per kg
SELLING_PRICE = 10.0   # gold per kg
MAX_STOCK = 100_000    # kg

#
# Buy a random kg of salt from 10 to 100 kg from a mine
#

# TODO: Access the first element of the mines list to get the name of the mine
#       Learning objective: Accessing values in lists.
mine = ...

salt_to_purchase = random.randint(10,100)

total_cost = salt_to_purchase * (BUYING_COST + SHIPPING_COST)

# TODO: Update the gold and salt attributes in the stock dictionary.
#       Learning objective: Accessing and updating values in dictionaries.

print(f"You bought {salt_to_purchase} kg of salt from {mine}. The purchase costed {total_cost} gold!")

#
# Sell a random kg of salt from 10 to 100 kg to a market
#

# TODO: Access the a random element of the markets list to get the name of the
#       market.
#       Learning objective: Accessing values in dictionaries.

market = ...
salt_to_sell = random.randint(10, 100)

total_revenue = (salt_to_sell * SELLING_PRICE) - (salt_to_sell * SHIPPING_COST)

# TODO: Update the gold and salt attributes in the stock dictionary.
#       Learning objective: Accessing and updating values in dictionaries.

print(f"You earned {total_revenue} gold by selling {salt_to_sell} kg of salt in {market}!")

#
# Output (print) the amount of gold and salt in the stock
#
print(f"you have {stock.gold} gold and {stock.salt} kg of salt in your stock")

# Options to improve on your own:
#
# - Add more mines.
# - add more markets.
# - Test different indexes to access the list object, including indexes that are
#   out of range and negative ones.

# Next week:
#
# - Using conditions and loops to repeat code (iteration)