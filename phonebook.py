import os.path
import pickle
import Contact

class PhoneBook:

     # counters
    added_contacts_count = 0
    deleted_contacts_count = 0
    total_contacts_count = 0

    def __init__(self, filename): # called a 'constructor'
        
        self.contacts = set()
        
        self.filename = filename # file where the data for this phonebook is stored (and will be written to by __del__())
        
        contact_file = 'contacts.pickle'

        # try to read contacts file (if it exists)
        try:
            contact_file = open(filename, 'r')
        except FileNotFoundError:
            pass # "do nothing"
        
        # read contacts into dict
        
        if contact_file is not None: # or: "if contact_file"
            
            for line in contact_file.readlines():
                
                new_contact = line.rstrip().split(',')
                new_name = new_contact[0]
                new_phone = new_contact[1]
                new_email = new_contact[2]
                self.add_contact(new_name, new_phone, new_email)
                # creates a dictionary such as {'john': ['917-544-4444','j@stern.nyu.edu'] }
                
            contact_file.close()
        return

    def save_to_disk(self):
        self.contacts = {}

        global added_contacts_count
        global total_contacts_count
        global deleted_contacts_count

        # Store data (serialize)
        with open('contacts.pickle', 'wb') as handle:
            pickle.dump(self.contacts, handle, protocol=pickle.HIGHEST_PROTOCOL)

            print("=================================")
            print(str(added_contacts_count) + " contacts added in current session")
            print(str(deleted_contacts_count) + " contacts deleted in current session")
            print(str(total_contacts_count) + " contacts in the contacts file")
            print("=================================")
            return

        # Load data (deserialize)
    def load_from_disk(self):

        with open('contacts.pickle', 'rb') as handle:
            unserialized_data = pickle.load(handle)

        print(self.contacts == unserialized_data)

    def add_contact(self, name, phone, email): # all info already provided as arguments
        
        self.contacts[name] = [phone, email]
        return
    
    def print_all_contacts(self):
        
        for name in self.contacts.keys():
            print('Name: %s\nPhone: %s\nEmail: %s\n' % (name, self.contacts[name][0], self.contacts[name][1]))
        return 

    def get_all_contacts(self): # returns a copy of the contacts stored in our PhoneBook object (external code could also directly access the .contacts attribute of the PhoneBook object, but that is typically poor practice because it invites external code to modify internal attributes of our objects)
        
     return self.contacts.copy()

     def search_contacts(self):
         query = str(input("Enter the search query : "))
         found = False

         # performing search over name
         for key in self.contacts:
             if query in key:
                 found = True
                 value = self.contacts[key]
                 print("Name = " + key + " Phone = " + value[0] + " Email = " + value[1])

         if found == False:
             print("Contact not found!")

         ## optional (search over values)
         '''
         for key, value in contacts_dict.items():
             if query in key:
                 found = True
                 value = contacts_dict[key]
                 print("Name = " + key + " Phone = " + value[0] + " Email = " + value[1])
             else:
                 for entry in value
                     if query in entry:
                         found = True
                         value = contacts_dict[key]
                         print("Name = " + key + " Phone = " + value[0] + " Email = " + value[1])
                         break

         if found == False:
             print("Contact not found!")
         '''
         return

    def del_contact(self, name): # returns True if contact was found+deleted, False otherwise

        try:
            del self.contacts[name] # alternatively: self.contacts.remove(name)
            success = True
        except KeyError:
            success = False
            
        return success

    # help menu with all options
def help_menu():
    print("=================================")
    print("The following actions are supported:")
    print("Print all contacts: p")
    print("Search contacts: s")
    print("Add a contact: a")
    print("Delete a contact: d")
    print("Edit a contact: e")
    print("Help Menu: h")
    print("Quit: q")
    print("=================================")
    return

# once program starts, load contacts from file to dictionary
    load_from_disk()
    help_menu()

# ask user for commands
    while action != 'q':
        action = input("\nWhich action do you want to do? [press 'h' for help] : ")
        if action == 'p':
            print_all_contacts()
        elif action == 's':
            search_contacts()
        elif action == 'a':
         add_contact()
        elif action == 'd':
            del_contact()
        elif action == 'e':
            edit_contact()
        elif action == 'h':
            help_menu()
        elif action == 'q':
            saves_contacts_to_disk()
    else:
        print("Invalid command. Enter h for help!")

