import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="krypton"
)

#for printing contacts in a pretty way
def formatted_disp(iter):
          print(" ---------------------------------------------------------------------------------------------------------------------- ")
          print("| No. |  Name               |  Phone     |  Email                   |  Address                                          |")
          print(" ---------------------------------------------------------------------------------------------------------------------- ")
          count = 1
          for i in iter:
               #calculations for whitespace padding to ensure proper display
               nm = i[1]; ph=i[2]; em=i[3]; ad=i[4]
               lnm = 20 - len(nm); lph = 10 - len(ph); lem = 25 - len(em); lad = 50 - len(ad)
               name = nm+(" "*lnm); phone = ph+(" "*lph); email = em+(" "*lem); address = ad+(" "*lad)
               lnum = 3-len(str(count)); num = str(count)+(" "*lnum)
               print(f"| {num} | {name}| {phone} | {email}| {address}|")
               count+=1
          print(" ---------------------------------------------------------------------------------------------------------------------- \n")
          return iter

#adding a contact 
def add_contact():
     in_resp="y"
     while (in_resp.lower()=="y" or in_resp=="1"):
          #taking input of contact information
          nm = input("Enter name of person: ")
          ph = input("Enter the phone number: ")
          em = input("Enter the email: ")
          ad = input("Enter the address: ")
          #query for inserting
          insert_query = f'INSERT INTO Contacts (name,phone,email,address) Values ("{nm}","{ph}","{em}","{ad}");'
          try:
               mycur.execute(insert_query)
               mydb.commit()
          except:
               mydb.rollback()
          in_resp=input("Do you wish to add more? (Yes-1, No-0): ")

#deleting a contact
def del_contact():
     in_resp="y"
     while (in_resp.lower()=="y" or in_resp=="1"):
          contacts = disp_contact()
          try:
               ch = int(input("Enter the serial number of contact to delete or enter 0 to go back: "))
          except:
               print("\nWrong input!Try again\n")
               in_resp="y"
               continue
     
          if (ch==0):  break  #user chose to go back
          else:
               del_id = contacts[ch-1][0]    #getting id of contact to be deleted
               select_query = f"SELECT name,email,phone,address FROM contacts WHERE id={del_id};"
               mycur.execute(select_query)
               rec = mycur.fetchone()        #getting the record for confirmation
               usr_resp = input(f"\nThe following record will be deleted- Name:{rec[0]}, Phone No.:{rec[1]}, Email:{rec[2]}, Address:{rec[3]}\nType 1 to continue, or 0 to go back\n")   #confirmation message
               if usr_resp=="1":   #user confirms choice
                     delete_query = f"DELETE FROM Contacts WHERE id={del_id};"
                     try:
                         mycur.execute(delete_query)
                         mydb.commit()
                     except:
                           mydb.rollback()
                           print("\nSome error occured, please try again\n")
                           continue
               else:          #aborts the deletion
                    continue
          in_resp = input("Do you wish to delete more? (Yes-1, No-0): ")

#updating a contact
def update_contact():
     in_resp="y"
     while (in_resp.lower()=="y" or in_resp=="1"):
          contacts = disp_contact()
          try:
               ch = int(input("Enter the serial number of contact to update or enter 0 to go back: "))
          except:
               print("\nWrong input!Try again\n")
               in_resp="y"
               continue
     
          if (ch==0):
                break
          else:
               upd_id = contacts[ch-1][0]
               query = f"SELECT name,email,phone,address FROM contacts WHERE id={upd_id};"
               mycur.execute(query)
               rec = mycur.fetchone()
               usr_resp = input(f"\nThe following record will be changed- Name:{rec[0]}, Phone No.:{rec[1]}, Email:{rec[2]}, Address:{rec[3]}\nType 1 to continue, or 0 to go back\n")
               if usr_resp=="1":
                    ch = int(input("Choose what you wish to change\n1. Name\n2. Number\n3. Email\n4. Address\n5. Back\n"))
                    match ch:
                         case 1:
                              nm = input("Enter the new name: ")
                              qu = f'UPDATE Contacts SET name="{nm}" WHERE id={upd_id};'   
                         case 2:
                              ph = input("Enter the phone new number: ")
                              qu = f'UPDATE Contacts SET phone="{ph}" WHERE id={upd_id};'   
                    
                         case 3:
                              em = input("Enter the new email: ")
                              qu = f'UPDATE Contacts SET email="{em}" WHERE id={upd_id};'   
                    
                         case 4:
                              ad = input("Enter the new address: ")
                              qu = f'UPDATE Contacts SET address="{ad}" WHERE id={upd_id};'   
                         
                         case 5:
                              break
                         case _:
                              print("Wrong choice!\n")
                              in_resp="y"

                    try:
                         mycur.execute(qu)
                         mydb.commit()
                    except:
                         mydb.rollback()
                         print("\nSome error occured, please try again\n")
                         continue
                     
          in_resp = input("Do you wish to update more? (Yes-1, No-0): ")
     
#searching for a contact
def search_contact():
     in_resp="y"
     while (in_resp.lower()=="y" or in_resp=="1"):
          ch = int(input("\nChoose how you wish to search\n1. Search by name\n2. Search by number\n3. Search by Email\n4. Search by address\n5. Back\n"))
          match ch:
               case 1:
                    nm = input("Enter the name: ")
                    query = f"SELECT id,name,phone,email,address FROM Contacts WHERE name LIKE '%{nm}%';"   
               case 2:
                    ph = input("Enter the phone number: ")
                    query = f"SELECT id,name,phone,email,address FROM Contacts WHERE phone LIKE '%{ph}%';"   
          
               case 3:
                    em = input("Enter the email: ")
                    query = f"SELECT id,name,phone,email,address FROM Contacts WHERE email LIKE '%{em}%';"   
          
               case 4:
                    ad = input("Enter the address: ")
                    query = f"SELECT id,name,phone,email,address FROM Contacts WHERE address LIKE '%{ad}%';"   
               
               case 5:
                    break
               case _:
                    print("\nWrong choice!PLease try again")
                    in_resp="y"
                    continue

          mycur.execute(query)
          matched_contacts = mycur.fetchall()

          if matched_contacts:
               formatted_disp(matched_contacts)
          
          else:
               print("No contacts matching the search criteria found!\n")

          in_resp = input("Do you wish to do more? (Yes-1, Back-0): ")

#displaying all contacts
def disp_contact():
     query = "SELECT id,name,phone,email,address FROM Contacts ORDER BY name ASC;"
     mycur.execute(query)
     contacts = mycur.fetchall()

     if contacts:
          iter = formatted_disp(contacts)
     else:
          print("No contacts added yet!\n")

     return iter

#main block

mycur = mydb.cursor()    #database cursor
#initialization queries
qu1 = "CREATE DATABASE IF NOT EXISTS ContactBook;"
qu2 = "USE ContactBook;"
qu3 = """CREATE TABLE IF NOT EXISTS Contacts (id int AUTO_INCREMENT PRIMARY KEY,
      name varchar(50) NOT NULL,
      phone varchar(10) NOT NULL,
      email varchar(25),
      address varchar(100));"""
#executing the queries for creating database and table
try:
     mycur.execute(qu1)
     mycur.execute(qu2)
     mycur.execute(qu3)
     mydb.commit()
except: 
      mydb.rollback()

print("\n\nWelcome!\n")
resp="y"
while (resp.lower()=="y" or resp=="1"):
    print("\nPlease type the number of your choice!")
    #taking user choice
    out_choice = int(input("1. Display all contacts\n2. Add a contact\n3. Delete a contact\n4. Search for a contact\n5. Update/Change a contact\n6. Exit\nYour choice: "))
     #matching user choice
    match out_choice:
        case 1: disp_contact()     #displaying all contacts

        case 2: add_contact()      #add a contact

        case 3: del_contact()      #delete a particualr contact

        case 4: search_contact()   #search contacts for a contact based on name, phone, email or address

        case 5: update_contact()   #update a contact (name, email, phone, address)

        case 6: break              #exit program

        case _:                    #wrong choice
               print("Invalid choice option!\n")
               resp="y"
               continue
#end of program         
print("Exiting the program...\n")
mydb.commit()
mydb.close()