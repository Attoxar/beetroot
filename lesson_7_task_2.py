def stock_prices(stock_, prices_):
    return sum(stock_[item] * prices_[item] for item in stock if item in prices)


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


total_price = stock_prices(stock, prices)
print("Total stock price: ", total_price)
