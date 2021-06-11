import csv
import os

class Customer:

    def __init__(self, customer_id, first_name, last_name, current_video_rentals):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        
    def __str__(self):
        return f'\n{self.first_name.upper + " " + self.last_name.upper()}\n---------------\nage: {self.current_video_rentals}\nid: {self.customer_id}\n'
        
    

    @classmethod
    def get_all_customers(cls):
        customer_list = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(dict(row))
                customer_list.append(Customer(**dict(row)))
                
        return customer_list
        