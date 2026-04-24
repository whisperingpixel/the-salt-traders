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
#                                    PART 1
# Expected learning outcomes:
#  - Creating and using functions in Python.
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 22.04.2026
#
################################################################################

import random
import sys

###############################################################################
#
# Variables and constants
#
###############################################################################

#
# Cities and mines
#
MINES = ["Dürrnberg", "Berchtesgaden"]
MARKETS = ["Salzburg", "Laufen", "Passau"]

#
# Trading
#
BUY_COST = 5.0      # gold per kg
SHIP_COST = 1.5     # gold per transaction
SELL_PRICE = 10.0   # gold per kg
MAX_STOCK = 100_000    # kg

#
# Initial state of the stock
#
gold = 1500.0
salt = 0

#
# Simulation / game parameters
#
MAX_ITER = 100

###############################################################################
#
# Function definitions
#
###############################################################################

# TODO: Add a function to buy salt

# TODO: Add a function to sell salt

# TODO: Add a function that checks whether you are bankrupt

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

        for mine in MINES:
            pass
            # TODO: buy salt. Use your function defined above and additional calculations!
            # NOTE: Remove the 'pass' keyword

        for market in MARKETS:
            pass
            # TODO: sell salt. Use your function defined above and additional calculations!
            # NOTE: Remove the 'pass' keyword

        # TODO: Check whether you are bankrupt

        iteration = iteration + 1
        input()

# Options to improve on your own:
#
# - add more cities
# - add capacities for mines
# - add market saturation for cities
# - add different shipping costs for mines and cities (we will do that later based
#   on their location!)
# - adjust purchasing and selling based on the limits we have

# Next week:
#
# - better error handing: The program should not crash when something goes wrong!
# - separation of configuration and program execution
# - better documentation of the code!