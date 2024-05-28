def add_contact():
     nm = input("Enter name of person: ")
     ph = input("Enter the phone number: ")
     em = input("Enter the email: ")
     ad = input("Enter the address: ")

     # query = f"INSERT INTO TABLE "
     # cur.
     query = f'INSERT INTO Contacts (name,phone,email,address) Values ("{nm}","{ph}","{em}","{ad}");'
     print(query)
     try:
          mycur.execute(query)
          mydb.commit()
          print("query fail")
     except:
          mydb.rollback()


def del_contact():
     pass
def update_contact():
     pass
def search_contact():
     pass
def disp_contact():
     pass

import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="krypton"
)
mycur = mydb.cursor()
qu1 = "CREATE DATABASE IF NOT EXISTS ContactBook;"
qu2 = "USE ContactBook;"
qu3 = """CREATE TABLE IF NOT EXISTS Contacts (id int AUTO_INCREMENT PRIMARY KEY,
      name varchar(50) NOT NULL,
      phone varchar(10) NOT NULL,
      email varchar(25),
      address varchar(100));"""

try:
     mycur.execute(qu1)
     mycur.execute(qu2)
     mycur.execute(qu3)
     mydb.commit()
except Exception as e:
      mydb.rollback()
      print(e)

# Contact Information: Store name, phone number, email, and address for each contact. 
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers. 
# Search Contact: Implement a search function to find contacts by name or phone number. 
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

print("Welcome!\n")
resp="y"
while (resp.lower()=="y" or resp=="1"):
    print("Please type the number of your choice!")
    out_choice = int(input("1. Display all contacts\n2. Add a contact\n3. Delete a contact\n4.Search for a contact\n5.Update/Change a contact\n6. Exit\nYour choice:"))

    match out_choice:
        case 1: 
               #print contacts here
               disp_contact()
               ch = int(input("Enter the serial number of contact to view it, or 0 to go back: "))
                

        case 2:
               inc = 1
               while (inc == 1):
                    add_contact()
                    inc = int(input("Do you wish to add more? (Yes-1, No-0)"))

        case 3:
               inc = 1
               while (inc == 1):
                    del_contact()
                    inc = int(input("Do you wish to del more? (Yes-1, No-0)"))

        case 4:
               inc = 1
               while (inc == 1):
                    search_contact()
                    inc = int(input("Do you wish to search more? (Yes-1, No-0)"))

        case 5:
               inc = 1
               while (inc == 1):
                    update_contact()
                    inc = int(input("Do you wish to update more? (Yes-1, No-0)"))
        case 6:
               print("Exiting the program...\n")
               break

        case _: 
               print("Invalid choice option!\n")
               # out_choice = int(input("1. Display all contacts\n2. Add a contact\n3. Delete a contact\n4.Search for a contact\n5. Exit\nYour choice:"))
               resp="y"
               continue
mydb.commit()
mydb.close()