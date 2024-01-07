def create_new_contact(file_name):
    information = []
    current_id = count_contact(file_name)
    information.append(str(current_id))
    information.append(input("Enter contact name: "))
    information.append(input("Enter contact phone number: "))
    information.append(input("Enter contact group: "))
    with open(file_name, "a") as file:
        file.write(';'.join(information) + "\n")
def delete_contact(contacts):
    show_contacts(contacts)
    id_to_del=int(input("Enter id to delete"))
    if contacts.get(id_to_del):
        del contacts[str(id_to_del)]
        show_contacts(contacts)
    else:
        print('Id not  found')
def convert_file_to_dict(file_name):
    contacts = {}

    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(';')
            contacts[parts[0]] = parts[1:]

    return contacts


def count_contact(file_name):
    lines = 0
    with open(file_name, 'r') as file:
        for line in file:
            lines += 1
    return lines


def find_contact(contacts):
    print("If you want to find a contact by ID, enter 1.")
    print("If you want to find a contact by name, enter 2.")
    user_choice = int(input())

    if user_choice == 1:
        contact_id = input("Enter ID: ")
        if contacts.get(contact_id):
            print(f"Contact ID: {contact_id}, Information: {contacts[contact_id]}")
        else:
            print("ID not found")
    elif user_choice == 2:
        contact_name = input("Enter name: ")
        found = False
        for key, value in contacts.items():
            if contact_name == item:
                print(f"Contact ID: {key}, Information: {value}")
                found = True
        if not found:
            print("Contact not found by name")


def show_contacts(contacts):
    for value in contacts:
        print(f" Id contact {value}  inforamtion: {contacts[value]}")


def change_contact_information(file_name):
    pass
