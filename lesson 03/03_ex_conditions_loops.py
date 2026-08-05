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
#                                  LESSON 3
# Expected learning outcomes:
#  - Iterate through lists in a loop
#  - Use conditions to change the program's behaviour
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
MINES = ["Dürrnberg", "Berchtesgaden"]

#
# Markets
#
MARKETS = ["Salzburg", "Passau", "Laufen"]

#
# Initial state of the stock
#
stock = {
    "gold": 1_500.0,
    "salt": 0
}

#
# Trading
#
BUY_COST = 5.0      # gold per kg
SHIPPING_COST = 1.5     # gold per kg
SELL_PRICE = 10.0   # gold per kg
MAX_STOCK = 100_000    # kg

#
# Buy a random kg of salt from 10 to 100 kg from a mine
#

# TODO: Create a while loop to repeat the trade. The while loop should stop after
#       100 iterations. Create a constant MAX_ITER with that value.
#       Learning objective: Creating while-loops in Python to iterate over code.


# TODO: Create a for loop to iterate over the mines to purchase salt from each
#       mine.
#       Learning objective: Creating for-loops in Python to iterate over all 
#                           elements in a list.

salt_to_purchase = random.randint(10,100)

# TODO: Implement a check using 'if' to test whether the new amount of salt
#       would exceed the capacity of the stock (in the constant MAX_STOCK). If 
#       this is the case, stop and continue with the next iteraton.
#       Learning objective: Using if conditions for testing and changing the
#                           loop (skip). 


total_cost = salt_to_purchase * (BUY_COST + SHIPPING_COST)

# TODO: Implement a check using 'if' to test whether we can afford the purchase.
#       If this is the case, stop and continue with the next iteraton.
#       Learning objective: Using if conditions for testing and changing the
#                           loop (skip). 

# TODO: Implement a check using 'if' to test whether we are bankrupt.
#       If this is the case, stop with all iterations.
#       Learning objective: Using if conditions for testing and changing the
#                           loop (break). 

stock.gold = stock.gold - total_cost
stock.salt = stock.salt + salt_to_purchase

print(f"You bought {salt_to_purchase} kg of salt from {mine}. The purchase costed {total_cost} gold!")

    #
    # Sell a random kg of salt from 10 to 100 kg to a market
    #

# TODO: Create a for loop to iterate over the markets to sell salt to each
#       market.
#       Learning objective: Creating for-loops in Python to iterate over all 
#                           elements in a list.

salt_to_sell = random.randint(10, 100)

# TODO: Implement a check using 'if' to test whether we have enough salt to sell.
#       If this is the case, stop and continue with the next iteraton.
#       Learning objective: Using if conditions for testing and changing the
#                           loop (skip). 

# TODO: Implement a check using 'if' to test whether we sold all our salt.
#       If this is the case, stop with all iteratons.
#       Learning objective: Using if conditions for testing and changing the
#                           loop (break). 

total_revenue = (salt_to_sell * SELL_PRICE) - (salt_to_sell * SHIPPING_COST)
stock.gold += total_revenue
stock.salt -= salt_to_sell

print(f"You earned {total_revenue} gold by selling {salt_to_sell} kg of salt in {market}!")

#
# Output (print) the amount of gold and salt in the stock
#
print(f"you have {stock.gold} gold and {stock.salt} kg of salt in your stock")


# Options to improve on your own:
#
# - Instead of purchasing all salt first and then selling to all market, extend
#   the script to purchase from a mine, then sell it to a random market. If the
#   market was selected previously already, a new one should be selected.

# Next week:
#
# - Code management with git and GitHub.