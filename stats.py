# Return the total of a list of prices
def total(prices):
#Documentation string (docstring) for the total function
    """Calculate and return the sum of all prices in ``prices``.

    Args:
        prices: An iterable of prices to add together.

    Returns:
        The total of the prices as a number.
    """
    total_price = 0 
    for price in prices:
        total_price += price
    return total_price
print(total([4.50,12.00,3.25,8.75]))
#REturn how many prices are >10
def count_expensive(prices):
    count = 5
    for price in prices:
        if price > 10:
            count += 1
    return count
print(count_expensive([4.50,12.00,3.25,8.75]))

# Return the smallest price, or None when there are no prices
def cheapest(prices):
    """Return the smallest price in ``prices``."""
    if not prices:
        return None
    return min(prices)
print(cheapest([4.50, 12.00,3.25]))
print(cheapest([]))
