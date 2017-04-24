import os.path

# dictioanry to store all contacts
contacts_dict = {}

# counters
added_contacts_count = 0
deleted_contacts_count = 0
total_contacts_count = 0

# user action
action = ''

# contacts file
contacts_file = "contacts.dat"

### text file structure
# name1, 347, a@b.com
# name2, 456, b@c.com

### dictionary structure
# {name1 : [347, a@b.com], name2 : [456, b@c.com]}

# load contacts from a file into the dictionary
def load_contacts_from_disk():
    # check if contacts file exists
    if os.path.isfile(contacts_file):
        global total_contacts_count
        with open(contacts_file) as contacts:
            for contact in contacts:
                # handle empty lines
                if ',' in contact:
                    attributes = contact.split(', ')
                    # handle \n while reading from file
                    if "\n" in attributes[2]:
                        attributes[2] = attributes[2].strip("\n")
                    contacts_dict[attributes[0]] = [attributes[1], attributes[2]]
        contacts.close()
        total_contacts_count = len(contacts_dict)

    # Create new contacts file
    else:
        open(contacts_file, 'w').close()

# print contacts
def print_contacts():
    for key in contacts_dict:
        #values = ', '.join(contacts_dict[key])
        print("%s : %s" % (key, contacts_dict[key]))

    ## optional : to print in sorted order by name
    '''
    for key in sorted(contacts_dict):
        print("%s : %s" % (key, contacts_dict[key]))
    '''
    return

# search contacts
def search_contacts():
    query = str(input("Enter the search query : "))
    found = False

    # performing search over name
    for key in contacts_dict:
        if query in key:
            found = True
            value = contacts_dict[key]
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

# add a contact
def add_contact():
    name = ","
    while "," in name:
        name = input("Enter name (without commas) : ")

    # check if the entered name already exists. If yes, call edit function
    if name in contacts_dict:
        print("Contact already exists! Select edit option to edit the contact.")

    else:
        global added_contacts_count
        global total_contacts_count

        # handle commas to maintain integrity of the file (and program) (else program will faile while reading file)
        phone = ","
        while "," in phone:
            phone = input("Enter phone number (without commas) : ")

        email = ","
        while "," in email:
            email = input("Enter email address (without commas) : ")

        contacts_dict[name] = [phone, email]
        total_contacts_count = total_contacts_count + 1
        added_contacts_count = added_contacts_count + 1

    return

# edit a contact. flag denotes whether to ask user for the name
def edit_contact():
    key = str(input("Enter the name whose contact you want to edit : "))

    if key in contacts_dict:
        value = contacts_dict[key]

        update_phone = input("Enter y if you want to edit phone, else press n : ")
        if update_phone == "y":
            value[0] = ","
            while "," in value[0]:
                value[0] = input("Enter phone number (without commas) : ")

        update_email = input("Enter y if you want to edit email, else press n : ")
        if update_email == "y":
            value[1] = ","
            while "," in value[1]:
               value[1] = input("Enter email address (without commas) : ")

        contacts_dict[key] = [value[0], value[1]]
        print("Contact Updated!")
    else:
        print("Contact Not Found.. returning...")

    return

# delete a contact
def delete_contact():
    name = str(input("Enter the name of the contact to be deleted : "))
    if name in contacts_dict:
        global deleted_contacts_count
        global total_contacts_count
        del contacts_dict[name]
        total_contacts_count = total_contacts_count - 1
        deleted_contacts_count = deleted_contacts_count + 1
        print("Contact deleted!")
    else:
        print("Contact not found!")
    return

# export the contacts to a file
def saves_contacts_to_disk():
    global added_contacts_count
    global total_contacts_count
    global deleted_contacts_count

    print("\nSaving contacts to the file " + contacts_file)

    with open(contacts_file, 'w') as contacts:
        for key, value in contacts_dict.items():
            contacts.write(str(key) + ", ")
            contacts.write(str(value[0]) + ", ")
            contacts.write(str(value[1]))
            contacts.write("\n")
        contacts.close

    print("=================================")
    print(str(added_contacts_count) + " contacts added in current session")
    print(str(deleted_contacts_count) + " contacts deleted in current session")
    print(str(total_contacts_count) + " contacts in the contacts file")
    print("=================================")
    return

# help menu with all options
def help_menu():
    print("=================================")
    print("The following acions are supported:")
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
load_contacts_from_disk()
help_menu()

# ask user for commands
while action != 'q':
    action = input("\nWhich action do you want to do? [press 'h' for help] : ")
    if action == 'p':
        print_contacts()
    elif action == 's':
        search_contacts()
    elif action == 'a':
        add_contact()
    elif action == 'd':
        delete_contact()
    elif action == 'e':
        edit_contact()
    elif action == 'h':
        help_menu()
    elif action == 'q':
        saves_contacts_to_disk()
    else:
        print("Invalid command. Enter h for help!")
