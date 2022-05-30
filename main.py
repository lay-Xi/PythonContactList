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
    pass


def search_for_contact(contacts):
    pass


def delete_contact(contacts):
    pass


def list_contacts(contacts):
    pass


def main(contacts_path):
    print("Welcome to your contact list!")
    print("The following is a list of useable commands:")
    print('"add": Adds a contact.')
    print('"delete": Deletes a contact.')
    print('"list": Lists all contacts.')
    print('"search": Searches for a contact by name.')
    print('"q": Quits the program and saves the contact list.')
    print()

    contacts = read_contacts(contacts_path)
    command = input("Type a command: ")

    if (command == "add"):
        pass
    elif (command == "delete"):
        pass
    elif (command == "list"):
        pass
    elif (command == "search"):
        pass
    elif (command == "q"):
        write_contacts(contacts_path, contacts)
        print("Contacts were saved successfully.")


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
