# Rubrica:

# Descrizione: Crea un'applicazione che permetta all'utente di salvare, visualizzare, modificare e cancellare contatti in una rubrica.
# Caratteristiche: Salvataggio dei contatti in un file (ad esempio, un file CSV o un file JSON), ricerca per nome o numero, 
#  e interfaccia a linea di comando per navigare tra le opzioni.
# Obiettivo: Lavorare con file, liste e dizionari, e creare un sistema CRUD (Create, Read, Update, Delete).
import os
import csv

# File path
ADDRESS_BOOK_PATH = "Rubrica/Address_book.csv"

# User menu function
def user_menu():
    print("------ Address Book ------")
    print("1. Save new contact")
    print("2. Show all contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Exit")


# Save contact function
def save_contact(first_name, last_name, phone_number):
    # contact to save
    contact = {"First Name": first_name, "Last Name": last_name, "Phone Number": phone_number}
    # columns name
    field_names = ["First Name", "Last Name", "Phone Number"]

    # Ensure the directory exists
    os.makedirs("Rubrica", exist_ok= True)

    # Checks if the contact already exists
    if contact_exists(first_name, last_name):
        print(f">>> Contact '{first_name} {last_name}' already exists.")
        return 
        

    # Check if the file already exists
    file_exists = os.path.isfile(ADDRESS_BOOK_PATH)
    
    # Opening file in adding mode 'a'
    with open(ADDRESS_BOOK_PATH, 'a', newline='') as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames= field_names)

        # Write the header only if the file does not exist or is empty
        if not file_exists:
            writer.writeheader() # Write header only if file not exists
        # Adding dictionary row
        writer.writerow(contact)
    
    print(">>> New contact saved.")

# Function to check if a contact already exists
def contact_exists(first_name, last_name):
    if not os.path.isfile(ADDRESS_BOOK_PATH):
        return False
    try:
        with open(ADDRESS_BOOK_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["First Name"].strip().lower() == first_name.strip().lower() and row["Last Name"].strip().lower() == last_name.strip().lower():
                    return True
        #return False
    except Exception as e:
        print(f"Error reading the file: {e}")
        return False
    
    return False


# Show all contacts function
def show_contact():
    if not os.path.isfile(ADDRESS_BOOK_PATH):
        print(">>> No contacts found.")
        return

    with open(ADDRESS_BOOK_PATH, 'r') as file:
        reader = csv.DictReader(file)
        print("\n>>> Contact List:")
        print(f"{'First Name':<15} {'Last Name':<15} {'Phone Number':<15}")
        print("-" * 45)
        for row in reader:
            print(f"{row['First Name']:<15} {row['Last Name']:<15} {row['Phone Number']:<15}")
    print()


# Update contact function
def update_contact(first_name, last_name, new_first_name, new_last_name, new_phone_number):
    if not contact_exists(first_name, last_name):
        print(f">>> Contact '{first_name} {last_name}' not found.")
        return

    # Read all file lines
    with open(ADDRESS_BOOK_PATH, 'r') as file:
        reader = csv.DictReader(file)
        contacts = list(reader)

        # Update contact
        for contact in contacts:
            if contact['First Name'] == first_name and contact['Last Name'] == last_name:
                contact["First Name"] = new_first_name
                contact["Last Name"] = new_last_name
                contact['Phone Number'] = new_phone_number
  
    # Update contact
    # SISTEMARE QUESTA FUNZIONE
    with open(ADDRESS_BOOK_PATH, 'w', newline='') as file:
        fieldnames = ["First Name", "Last Name", "Phone Number"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

    print(">>> Contact updated successfully")


# Delete contact function
def delete_contact(first_name, last_name):
    if not contact_exists(first_name, last_name):
        print(f">>> Contact '{first_name} {last_name}' not found.")
        return
    
    # Read all file lines
    with open(ADDRESS_BOOK_PATH, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)

    # Write again only the lines that not contain the words to the credential
    with open(ADDRESS_BOOK_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        for line in lines:
            if line[0] == first_name and line[1] == last_name:
                continue
            writer.writerow(line)
    print(">>> Contact removed successfully.")


# Validate phone number function
def validate_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) >= 7 # de min length


# Validate new phone number function
def validate_phone_number(new_phone_number):
    return new_phone_number.isdigit() and len(new_phone_number) >= 7 # de min length

# Main function
def main():
    while True:
        try:
            user_menu()
            user_choice = input("Enter your choice (1 to 5): ")

            if user_choice not in ['1', '2', '3', '4', '5']:
                print("Error! Enter a valid value.")
                print()
                continue
            
            if user_choice == '5':
                print("Exit from program.")
                break

            if user_choice == '1': # Save a contact
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                phone_number = input("Enter phone number: ")

                if not phone_number.isdigit():
                    print(">>> Error! Phone number should contain digits.")
                    continue
                
                save_contact(first_name, last_name, phone_number)
                print()

            elif user_choice == '2': # Show contacts
                show_contact()

            elif user_choice == '3': # Update a contact
                print("Enter credential of contact to update")
                first_name = input("First name: ")
                last_name = input("Last name: ")
                print()
                
                print("Enter new credentials")
                new_first_name = input("New first name: ")
                new_last_name = input("New last name: ")
                new_number = input("New number: ")

                if not new_number.isdigit():
                    print(">>> Error! Phone number should contain digits.")
                    continue
                
                update_contact(first_name, last_name, new_first_name, new_last_name, new_number)
                print()

            
            elif user_choice == '4': # Delete a contact
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                delete_contact(first_name, last_name)
                print()
            
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()