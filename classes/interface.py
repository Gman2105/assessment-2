from inventory import Inventory

class Interface():
    def __init__(self):
        self.videos, self.vid_id = Inventory.objects('inventory')
        self.customers, self.add_customer_id = Inventory.objects('customers')
       

    def run(self):

        print(f'\nWelcome to Gman Videos!')

        while True:
            mode = input(self.main_menu())

            if mode == '1':
                Inventory.view_inventory(self)
            
            elif mode == '2':
                Inventory.view_customers_videos(self)

            elif mode == '3':
                Inventory.rent_video(self)

            elif mode == '4':
                Inventory.return_video(self)

            elif mode == '5':
                Inventory.add_customer(self, self.add_customer_id)
                self.add_customer_id += 1

            elif mode == '6':
                break

           
    def main_menu(self):
        return ('''
        What would you like to do?
        
        1. View video inventory 
        2. View customer's rented videos
        3. Rent video
        4. Return video
        5. Add new customer
        6. Exit
    ''')
    
    