class Dish:
    def __init__(self , name , price , ratings):
       self.name = name
       self.price = price
       self.ratings = ratings
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.name ,"|",self.price)
        print(self.ratings)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
class Menu:
    def __init__(self , title , num_of_dishes , dishes):
       self.title = title     
       self.num_of_dishes = num_of_dishes     
       self.dishes = dishes    
    def show(self):
        print("#######################")
        print(self.title ,"|",self.num_of_dishes)
        print("#######################")
        for idx in range(len(self.dishes)):
             self.dishes[idx].show()
class Restaurant:
     def __init__(self , name , address , phone , ratings , menu):
       self.name = name
       self.address = address
       self.phone = phone
       self.ratings = ratings
       self.menu = menu            
     def show(self):
        print("+++++++++++++++++++++++")
        print(self.name ,"|",self.address)
        print(self.phone,"|",self.ratings)
        print("+++++++++++++++++++++++")
        self.menu.show()
     def main():
       dish1 = Dish("Dal Makhani", 350, 4.5)    
       dish2 = Dish("Paneer do pyaza", 450, 4.8)    
       dish3 = Dish("Noodles", 250, 4.3)    
       dish4 = Dish("Burger", 150, 4.0)    
       dish5 = Dish("Fries", 100, 3.8)
       dishes= [dish1 , dish2 , dish3 , dish4 , dish5]
       menu =Menu(title="Indian Delight", num_of_dishes=len(dishes) , dishes=dishes )
       restaurant= Restaurant("Maharaja", "Redwood Shores", "+91 99991-22331" , 4.5 , menu = menu)
       restaurant.show()
     if __name__=="__main__":
        main()
