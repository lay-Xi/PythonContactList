import json


CONTACT_FILE_PATH = "contacts.json"


def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)['contacts']
    except FileNotFoundError:
        contacts = []

    return contacts


def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def add_contact(contacts):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    mobile = input("Mobile Phone Number: ")
    home = input("Home Phone Number: ")
    email = input("Email Address: ")
    address = input("Address: ")

    while True:
        already_exists = False
        for contact in contacts:
            if (first_name.lower() == contact["first_name"] and last_name.lower() == contact["last_name"]):
                print("A contact with this name already exists.")
                already_exists = True    
                break
            
        if (already_exists):
            break

        if (len(mobile) > 0):
            if (not mobile.replace('-', '').isdigit()):
                print("Invalid mobile phone number.")
                break
            else:
                if (len(mobile.replace('-', '')) != 10):
                    print("Invalid mobile phone number.")
                    break

        if (len(home) > 0 and not home.replace('-', '').isdigit()):
            print("Invalid home phone number.")
            break

        if (len(email) > 0 and not verify_email_address(email)):
            print("Invalid email address.")
            break

        contacts.append({"first_name": first_name.lower(), "last_name": last_name.lower(),
                     "mobile": mobile, "home": home, "email": email, "address": address})
        
        print("Contact Added!")
        return contacts

    print("You entered invalid information, this contact was not added.")


def search_for_contact(contacts):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    filtered_contacts = []

    for contact in contacts:
        if (first_name.lower() in contact["first_name"] and last_name.lower() in contact["last_name"]):
            filtered_contacts.append(contact)

    print(f"Found {len(filtered_contacts)} matching contacts.")
    for id, contact in enumerate(filtered_contacts):
        _print_contact(id, contact)


def delete_contact(contacts):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    selected_idx = -1

    for idx, contact in enumerate(contacts):
        if (first_name.lower() == contact["first_name"] and last_name.lower() == contact["last_name"]):
            selected_idx = idx
            break
    
    if (selected_idx == -1):
        print("No contact with this name exists.")
    else:
        confirm = input("Are you sure you would like to delete this contact (y/n)? ")
        
        if (confirm == "y"):
            del contacts[selected_idx]
            print("Contact deleted!")

    return contacts


def _print_contact(id, contact):
    print(f"{id + 1}. {contact['first_name'].capitalize()} {contact['last_name'].capitalize()}")
    if len(contact["mobile"]) > 0:
        print(f"       Mobile: {contact['mobile']}") 
    
    if len(contact["home"]) > 0:
        print(f"       Home: {contact['home']}") 
    
    if len(contact["email"]) > 0:
        print(f"       Email: {contact['email']}") 
    
    if len(contact["address"]) > 0:
        print(f"       Address: {contact['address']}") 


def list_contacts(contacts):
    contacts.sort(key=lambda contact: contact["first_name"])

    for id, contact in enumerate(contacts):
        _print_contact(id, contact)


def main(contacts_path):
    print("Welcome to your contact list!")
    print()
    print()
    print("The following is a list of useable commands:")
    print('"add": Adds a contact.')
    print('"delete": Deletes a contact.')
    print('"list": Lists all contacts.')
    print('"search": Searches for a contact by name.')
    print('"q": Quits the program and saves the contact list.')
    print()

    contacts = read_contacts(contacts_path)
    while True:
        command = input("Type a command: ")

        if (command == "add"):
            contacts = add_contact(contacts)
        elif (command == "delete"):
            contacts = delete_contact(contacts)
        elif (command == "list"):
            list_contacts(contacts)
        elif (command == "search"):
            search_for_contact(contacts)
        elif (command == "q"):
            write_contacts(contacts_path, contacts)
            print("Contacts were saved successfully.")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
