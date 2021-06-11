from customers  import Customer
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
inventory_path = os.path.join(my_path, "inventory.csv")
customers_path = os.path.join(my_path, "../data/customers.csv")

class Inventory:
    all_movies = []

    def __init__(self, id, title, rating, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available
        
    
    
    @classmethod
    def get_all_movies(cls):
        with open(my_path, 'r') as movies_file:
            movies = csv.DictReader(movies_file)
            movies_list = []
        for movie in movies:
            movies = (movie['title'], movie['rating'], movie['copies_available'])
            
        return movies_list