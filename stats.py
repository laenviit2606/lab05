# Return the total of a list of prices
def total(prices):
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