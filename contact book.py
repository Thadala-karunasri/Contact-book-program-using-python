contacts = []

def add_contact():
  """Prompts user for contact information and adds it to the list"""
  name = input("Enter contact name: ")
  number = input("Enter phone number: ")
  contacts.append({"name": name, "number": number})
  print(f"Contact {name} added successfully!")

def view_contacts():
  """Prints all contacts in the list"""
  if not contacts:
    print("There are no contacts in the book.")
    return
  print("-" * 30)
  for i, contact in enumerate(contacts):
    print(f"{i+1}. {contact['name']} - {contact['number']}")
  print("-" * 30)

def search_contact():
  """Searches for a contact by name"""
  name = input("Enter contact name to search: ")
  found = False
  for contact in contacts:
    if contact["name"].lower() == name.lower():
      print(f"Contact found: {contact['name']} - {contact['number']}")
      found = True
      break
  if not found:
    print(f"Contact '{name}' not found.")

def delete_contact():
  """Deletes a contact by index"""
  view_contacts()  # Show list for reference
  if not contacts:
    return
  index = int(input("Enter the index of the contact to delete: ")) - 1
  if index >= 0 and index < len(contacts):
    del contacts[index]
    print("Contact deleted successfully!")
  else:
    print("Invalid index entered.")

def main():
  """Main program loop"""
  while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      add_contact()
    elif choice == '2':
      view_contacts()
    elif choice == '3':
      search_contact()
    elif choice == '4':
      delete_contact()
    elif choice == '5':
      print("Exiting Contact Book...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
