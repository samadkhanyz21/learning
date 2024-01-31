class Store:

    def __init__(self, name):
        """You'll need 'name' as an argument to this
        method. Then, initialise 'self.name' to be
        the argument, and 'self.items' to be an
        empty list."""
        self.name = name
        self.items = []

    def add_item(self, name, price):

        """Create a dictionary with keys name and price,
        and append that to self.items"""
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):

        """Add together all item prices in self.items
        and return the total"""
        return sum([item['price'] for item in self.items])


# Create a Store instance with a name
store = Store("My Store")

# Add items to the store using the add_item method
store.add_item("ketchup", 2.45)

# Get the stock price of the store
total_price = store.stock_price()
print(total_price)