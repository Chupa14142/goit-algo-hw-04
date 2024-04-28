"""Module 4/ Task 3"""

def parse_input(user_input):
    """Parse user input like command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def unpack_name_and_phone(user_data: list):
    """Unpack name and phone from user_data"""
    try:
        name, phone = user_data
    except ValueError:
        return f"Incorrect user_data: {user_data}. Should have name and phone"
    return (name, phone)


def add_contact(user_data: list, contacts: dict):
    """Add contact to the list"""
    name, phone = unpack_name_and_phone(user_data)
    contacts[name] = phone
    return "Contact added."


def change_contact(user_data: list, contacts: dict):
    """Change user phone if it's already exist"""
    name, phone = unpack_name_and_phone(user_data)
    contacts[name] = phone
    return "Contact changed."


def show_phone(user_name, contacts: dict):
    """Show phone number by username"""
    username = user_name[0]
    if not username in contacts:
        return f"User not found error. User not in the list {contacts}"    
    return contacts[username]


def main():
    """Run bot"""
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "phone":
                print(show_phone(args, contacts))
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "all":
                print(contacts)
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
