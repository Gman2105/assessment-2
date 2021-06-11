from customers  import Customers
from inventory  import Inventory
from rent   import Rent
from return_    import Return 

import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
customers_path = os.path.join(my_path, "customers.csv")
inventory_path = os.path.join(my_path, "inventory.csv")


class Interface:

    def __init__(self):
      pass

    def run(self):
    
        mode = input(self.menu())
    
        #to view video inventory    
        if mode == '1':
            self.view_movies()
        
        #to view customer's rented vidoes    
        elif mode == '2':
            self.view_customers()
            pass
           
            
        #to rent video
        elif mode == '3':
            self.rent_movies()
            
            pass
            
        #to return video
        elif mode == '4':
            self.return_movies()
            pass
            
        
        #to add new customer
        elif mode == '5':
            self.add_customer()
            
            pass
            
        #to exit program    
        elif mode == '6':
            break
            
    #for the start-up menu.
    def menu(self):
        return "\nWhat would you like to do?\nOptions:\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n6. Quit\n"
        
    # Looks into cvs file to view the movie list (MODE 1)
    def view_movies(self):
        for movie in self.all_movies:
            print(movie) 
     
            
    # Customers renting movies MODE 3.
    def rent_movies(self):
        if self.customer_id and self.movie_count() > 3:
            print ("You've reached the maximium amount of rentals. Please return rentals to rent more.")
        else:
             print("** Enter the Title of Movie you want to Rent today. **")
             
        if self.copies_available in self.inventory > 0:
            print ("Enjoy Your Movie.")
            self.copies_available.remove()
           
            
    
    # Customers returning movie MODE 4.        
    def return_movies(self):
        
         self.copies_available.append()
            
    
    # Control the amount how many movies a customer can check out.
    def movie_count(self):
        num_movie = 0
        for movie in self.all_movies:
            if movie.id == self.customer_id:
                num_movie += 1
        return num_movie
            
            
    # Add new customer (MODE 5).
    def add_customer(self):
        print("** Enter New Customers Information Below **")
        first_name = input('Enter customers first name: ')
        last_name = input('Enter customers last name: ')
        all_customers = Interface.get_all_customers()
        all_customers.append(id,first_name, last_name)
        print("""New Customer Created!""")
        self.save_customers(all_customers)
        self.save_customers()
        
        
    #save new customer to the list.
    def save_customers(self, all_customers):
        with open(my_path, 'w') as csvfile:
             customer_csv = csv.writer(csvfile, delimiter=',')
             customer_csv.writerow(['first name', 'last name' 'current_video_rentals'])
             for customer in all_customers:
                customer_csv.writerow([customer.first_name, customer.last_name, customer.current_video_rentals])
    
    
    
    # Looks into cvs file to view the movie list.
    @classmethod
    def get_all_movies(cls):
        with open(my_path, 'r') as movies_file:
            movies = csv.DictReader(movies_file)
            movies_list = []
        for movie in movies:
            movies = (movie['title'], movie['rating'], movie['copies_available'])
        return movies_list
