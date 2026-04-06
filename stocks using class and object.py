class Product:
    def set_datailes(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock =  stock
    def update_price(self,change):
        self.price=self. price+change
    def update_stock(self,quantity):
        self.stock = self.stock+quantity
    def display(self):
        print("Product name:",self.name)
        print("Price:",self.price)
        print("stock:",self.stock) 
        print("stock cost is:",self.stock*self.price)  
p = Product()
p.set_datailes("laptop",50000,10) 
p.update_price(5000)
p.update_price(10)
p.display()            
            