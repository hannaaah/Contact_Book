import pickle
import sys
import os

CONTACT_DETAILS = 'contactdetails.pkl'

class Contact:
    
    def add_contact(self):
        self.name = input('\tContact name: ')
        self.ph = input('\tContact no. : ')
        self.addr = input('\tContact address: ')
        self.email = input('\tEmail id: ')
     
    def display_contact(self):
        print('\n\t ',self.name,'  - ',self.ph)
        print('\t Address: ',self.addr,'\n\t Email id: ',self.email)

    def get_name(self):
        return self.name
    
    def get_ph(self):
        return self.ph

def menu():
    print('\n\n\t\t\t    WELCOME TO TINKER.PY CONTACT BOOK')
    print('\t\t\t    *********************************\n')
    ch = int(input('\t\t\t\t1.Search for a contact\n\t\t\t\t2.Display all contacts\n\t\t\t\t3.Add a new contact\n\t\t\t\t4.Edit a Contact\n\t\t\t\t5.Delete a contact\n\t\t\t\t6.Exit\n\n\n\t\t\t  Enter your choice: '))
    return ch

def search():
    val = int(input('\n\n\t\t\t\tPress\n\n\t\t\t\t1.To search by Name\n\t\t\t\t2.To search by Phone number\n\n\n\t\t\t   Enter you choice:'))
    if val == 1:
      if searchByName() == 0:
        print('\n       Sorry,No Matches Found!')
    elif val == 2:
      if searchByPhoneno() == 0:
        print('\n       Sorry,No Matches Found!')
    else:
        print('\n\n\n\t\tNot a proper choice !')


def searchByName():
  found = 0
  contact = Contact()
  with open(CONTACT_DETAILS,'rb') as contactdetails:
      name = input("\n\n\t\t\tEnter the Name:")
      os.system('clear')
      print('\n\t    SEARCH RESULTS')
      print('\t    **************\n')
      try:
        while 1:
          contact = pickle.load(contactdetails) 
          if (contact.get_name().lower()).find(name.lower()) != -1: 
            contact.display_contact()
            found = 1
      except EOFError:
        pass
  return found

def searchByPhoneno():
  found = 0
  contact = Contact()
  with open(CONTACT_DETAILS,'rb') as contactdetails:
      ph = input("\n\n\t\t\tEnter the Phone No.:")
      os.system('clear')
      print('\n\t    SEARCH RESULTS')
      print('\t    **************\n')
      try:
        while 1:
          contact = pickle.load(contactdetails) 
          if contact.get_ph().find(ph) != -1: 
            contact.display_contact()
            found = 1
      except EOFError:
        pass
  return found


def editContact():
  found = 0
  name = input('\n\nEnter name of contact you want to edit: ')
  f = open("NewContactDetails.pkl","wb")
  f.close()
  with open(CONTACT_DETAILS,'rb') as contactdetails:
    try:
      with open("NewContactDetails.pkl","ab") as newfile:
        while 1:
          contact = pickle.load(contactdetails)
          if contact.get_name().lower() == name.lower():
              found = 1
              print('\n\tEnter new contact details:\n')
              contact.add_contact()
              print('\n\n\t   Contact Edited !')
          pickle.dump(contact,newfile)
    except EOFError:
      pass
  if found == 0:
        print(f"\n\n\t  No Contact found with name '{name}'!")   
  os.remove(CONTACT_DETAILS)
  os.rename("NewContactDetails.pkl",CONTACT_DETAILS)


def delContact():
  name = input('\n\nEnter name of the contact to delete: ')
  found = 0
  f = open("NewContactDetails.pkl","wb")
  f.close()
  with open(CONTACT_DETAILS,'rb') as contactdetails:
    try:
        with open("NewContactDetails.pkl","ab") as newfile:
          while 1:
            contact = pickle.load(contactdetails)
            if contact.get_name().lower() == name.lower():
              found = 1
              ans = input(f"\n\n\n\tAre you sure that you want to delete contact '{name}'(Y/N) ? ")
              if ans == 'Y':
                  print('\n\n\t   Contact Deleted !')
              else:
                  pickle.dump(contact,newfile)
            else:
              pickle.dump(contact,newfile)     
    except EOFError:
      pass

  if found == 0:
    print(f"\n\n\t  No Contact found with name '{name}' !")
  os.remove(CONTACT_DETAILS)
  os.rename("NewContactDetails.pkl",CONTACT_DETAILS)


while 1:
    os.system('clear')
    choice = menu()
    contact = Contact()
    os.system('clear')
    if choice==1:
      search()

    elif choice==2:
      with open(CONTACT_DETAILS,'rb') as contactdetails: 
        print('\n\t      ALL CONTACTS\n\t      ************\n')
        try:
          while 1:
            contact = pickle.load(contactdetails)
            contact.display_contact()
        except EOFError:
          pass
         
    elif choice==3:
      print('\n\tEnter the following details:\n')
      contact.add_contact()
      with open(CONTACT_DETAILS,'ab') as contactdetails:
        pickle.dump(contact,contactdetails)

    elif choice == 4:
      editContact()

    elif choice==5:
      delContact()

    elif choice==6:
      print('\n\n\n\n\n\t\t\t\t\tTHANK YOU :)\n\n\n\n\n\n\n\n\n')
      sys.exit()

    else:
      print('\n\n\n\t\tEnter a valid choice please.')
    
    any = input('\n\n\n      Press any key to go back...')
