class Dish:
    def __init__(self , name="" , price=0 , ratings=4.0 ):
        self.name = name
        self.price = price
        self.ratings = ratings
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("Name:",self.name)
        print("Price:",self.price)
        print("Rating:",self.ratings)
        print("~~~~~~~~~~~~~~~~~~~~~`")
dish1 = Dish("Noodles" , 300 , 4.5)
dish2 = Dish("Burger" , 100 , 4.3)
dish3 = Dish("fries" , 75 , 3.5)
          
dish1.show()
dish2.show()
dish3.show()

         