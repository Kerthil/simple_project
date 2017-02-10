class Product:
    def __init__(self, pid, disc, price = 0.0):
        self.price = price
        self.id = pid
        self.disc = disc

    def print_product(self):
        print "Product_%d:%s:$%.2f" % (self.pid, self.desc, self.price)

class Inventory:
    def __init__(self, name):
        self.name = name
        self.p = Product(0,"error")
        self.total_inventory = []

    def insert(self, product):
        self.total_inventory.append(product)
        print "added " + str(product.disc) + " to inventory."

    def report(self):
        for i in total_inventory:
            print total_inventory.index[i]

store_a = Inventory("Caitlin's Store")
eggs = Product(1,"eggs",3.49)
milk = Product(2,"Milk",5.99)
store_a.insert(eggs)
store_a.insert(milk)
store_a.report


