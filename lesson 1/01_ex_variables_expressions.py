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
#                                  LESSON 1
# Expected learning outcomes:
#  - Creating and using variables in Python (definition and initialisation)
#  - Using expressions in Python
#  - using external libraries
#
# Author: Martin Sudmanns (martin.sudmanns@plus.ac.at)
# Date: 17.07.2026
#
################################################################################

# TODO: Check new imports
import random

###############################################################################
#
# Variables and constants
#
###############################################################################

#
# Initial state of the stock
#

# TODO: Define and initialize variables (i.e. assign values to them). The
#       variables are 'gold' with a value of '1500' and 'salt' with a value of '0'.
#       Learning objective: Learn how to define and initialize variables.

#
# Trading
#

# TODO: Define and initialize constants (i.e. assign values to them). The
#       variables are 'BUY_COST' (value: 5.0), 'SHIPPING_COST' (value: 1.5),
#       'SELL_PRICE (value: 10.0) and 'MAX_STOCK' (value 100000).
#       Learning objective: Learn how to define and initialize constants.

#
# Buy a random kg of salt from 10 to 100 kg from a mine
#

# TODO: Define a variable and initialize it with a random value between 10 and 100.
#       Learning objective: Learn how to define and initialize a variable using
#       a random value.

salt_to_purchase = ...

# TODO: Calculate the total cost of the purchase based on the amount of salt,
#       BUY_COST and SHIPPING_COST. Store it in a new variable.
#       Learning objective: Use expressions to calculate values and store them
#       in a variable.

total_cost = ...

# TODO: Update the values of the stock (gold, salt) with the new values after
#       the purchase.
#       Learning objective: Use expressions to calculate values and store them
#       in a variable.

# TODO: Create a print statement that the purchase was completed and inform
#       the user about the costs.
#       Learning objective: Use print statement to output a result.

#
# Sell a random kg of salt from 10 to 100 kg to a market
#

# TODO: Define a variable and initialize it with a random value between 10 and 100.
#       Learning objective: Learn how to define and initialize a variable using
#       a random value.
salt_to_sell = ...

# TODO: Calculate the total revenue of the sold salt based on the amount of salt,
#       SELL_PRICE and SHIPPING_COST. Store it in a new variable.
#       Learning objective: Use expressions to calculate values and store them
#       in a variable.

total_revenue = ...

# TODO: Update the values of the stock (gold, salt) with the new values after
#       the purchase.
#       Learning objective: Use expressions to calculate values and store them
#       in a variable.

# TODO: Create a print statement that the salt was sold and inform the user
#       about the revenue.
#       Learning objective: Use print statement to output a result.

#
# Output (print) the amount of gold and salt in the stock
#
# TODO: Create a print statement to inform the user about the current values in
#       the stock .
#       Learning objective: Use print statement to output a result.


# Options to improve on your own:
#
# - 

# Next week:
#
# - Using lists and dictionaries for more complex variables