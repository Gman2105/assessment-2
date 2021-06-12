from video import Video
from customer import Customer
import csv
import os

class Inventory():
    
    # for Mode 1.
    # A method to view the inventory of movies.
    def view_inventory(self):
        for video in self.videos:
            print(video)
            
   
    # for Mode 2.        
    # Method to view to see customers is renting a movie or not.
    def view_customers_videos(self):
        customer_id = input(f'\nEnter your customer id:\t')
        for customer in self.customers:
            if customer['id'] == customer_id and customer['current_video_rentals'] != '':
                return(print(f"\n{customer['first_name']} {customer['last_name']} are currently renting: {customer['current_video_rentals']}\n"))
            elif customer['id'] == customer_id and customer['current_video_rentals'] == '':
                return(print(f"\n{customer['first_name']} {customer['last_name']} are not currently renting a movie.\n"))
        print(f'\nCustomer id not found\n')
        
    
    # for Mode 3.
    # Method for renting videos, and saving it to the inventory and customer list. 
    def rent_video(self):
        customer_id = input(f'\nEnter customer id: ')
        video_title = input(f'\nEnter video title: ')
        customer_vid = False
        available_vid = False 
        
        #checking for any copies that may or may not be available.
        for video in self.videos:
            if video['title'] == video_title and int(video['copies_available']) >= 0:
                available_vid = True
                break
            elif video['title'] == video_title and int(video['copies_available']) == 0:
                print(f"\nNo available copies of {video['title']}.\n")
                return
        
        # check if the movie title is in the inventory.    
        if available_vid == False:
            print(f'\n{video_title} is not in our inventory.\n')
            return
        
        # check if the customer has reached their rental limit.
        for customer in self.customers:
            if customer['id'] == customer_id and len(customer['current_video_rentals'].split('/')) < 3:
                customer_vid = True
                break
            elif customer['id'] == customer_id and len(customer['current_video_rentals'].split('/')) == 3:
                print(f'\n{customer["first_name"]} {customer["last_name"]} is currently renting 3 movies, return one or more to check another movie.')
                return
            
        if customer_vid == False:
            print(f'\nCustomer id is not found!\n')
            return
        
        # Taking movies count from the inventory to the customer when they rent it. Than reflects on the customer's profile what movie they are renting.
        if customer['current_video_rentals'] == '':
            customer['current_video_rentals'] = video['title']
        else:
            customer['current_video_rentals'] += f"/{video['title']}"
        video['copies_available'] = str(int(video['copies_available']) - 1)
        Inventory.new_save('inventory',['id','title','rating','copies_available'],self.videos)
        Inventory.new_save('customers',['id','first_name','last_name','current_video_rentals'],self.customers)

   
    #for Mode 4.
    # Method for returning videos.
    def return_video(self):
        customer_id = input(f'\nEnter customer id: ')
        video_title = input(f'\nEnter video title: ')
        video_vid = False
        customer_vid = False 
        last_vid = False
        
        for customer in self.customers:
            if customer['id'] == customer_id:
                customer_vid = True
                break
        if customer_vid == False:
            print(f'\nCustomer id was not found\n')
            return
        
        for video in self.videos:
            if video['title'] == video_title:
                video_vid = True
                break
        if video_vid == False:
            print(f'\n{video_title} was not found.\n')
            return
        
        customer_movie_list = customer['current_video_rentals'].split('/')
        new_movie_list = []
        for x in customer_movie_list:
            if x == video_title:
                last_vid = True
                continue
            else:
                new_movie_list.append(x)
        if last_vid == False:
            print(f'\n{video_title} was not checked out to you.\n')

        video['copies_available'] = str(int(video['copies_available']) + 1)
        customer['current_video_rentals'] = ('' if new_movie_list==[] else '/'.join(new_movie_list))
        Inventory.new_save('inventory',['id','title','rating','copies_available'],self.videos)
        Inventory.new_save('customers',['id','first_name','last_name','current_video_rentals'],self.customers)

   
    # for Mode 5.
    # Method to add new customer to customer list.
    def add_customer(self, add_customer_id):
        first_name = input(f'\nEnter first name: ')
        last_name = input(f'\nEnter last name: ')
        self.customers.append({
            'id': add_customer_id + 1,
            'first_name' : first_name,
            'last_name' : last_name,
            'current_video_rentals' : ''
        })
        Inventory.new_save('customers',['id','first_name','last_name','current_video_rentals'],self.customers)
        

    # Used to read the list.
    @classmethod
    def objects(cls, save_data):
        data = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/{save_data}.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data, int(row['id'])
        
        
    # Used to write and save data to list.
    @classmethod
    def new_save(cls, save_data, headers_list, data):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/{save_data}.csv")
        new_list = []
        for i in data:
            new_list.append(list(i.values()))
        with open(path, 'w') as csvfile:
            data_csv = csv.writer(csvfile, delimiter=',')
            data_csv.writerow(headers_list)
            data_csv.writerows(new_list)