class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to", self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Rachan"
customer1.lastName = "Chira"
customer2 = Customer()
customer2.name = "Piya"
customer2.lastName = "Wongthai"
customer3 = Customer()
customer3.name = "Ekachai"
customer3.lastName = "Sresunan"
customer4 = Customer()
customer4.name = "Pichet"
customer4.lastName = "Eaimwong"
customer5 = Customer()
customer5.name = "Chetha"
customer5.lastName = "Wiroj"
customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()
customer5.addCart()
