import pickle
import sys
import os

CONTACT_DETAILS = 'contactdetails.pkl'

class Contact:
    def add_contact(self):
        print('Enter the following details:\n')
        self.name = input('Contact name:')
        self.ph = input('Contact no. :')
        self.addr = input('Contact address:')
        self.email = input('Email id:')
     
    def display_contact(self):
        print('\n ',self.name,'  - ',self.ph)
        print(' Address: ',self.addr,'\n Email id: ',self.email)

    def get_name(self):
        return self.name
    
    def get_ph(self):
        return self.ph

def menu():
    print('\n\n\t\t\t    WELCOME TO TINKER.PY CONTACT BOOK')
    print('\t\t\t    *********************************\n')
    ch = int(input('\t\t\t\t1.Search for a contact\n\t\t\t\t2.Display all contacts\n\t\t\t\t3.Add a new contact\n\t\t\t\t4.Delete a contact\n\t\t\t\t5.Exit\n\n\n\t\t\t  Enter your choice:'))
    return ch

def search(s):
    found = 0
    with open(CONTACT_DETAILS,'rb') as contactdetails:
      if s==1:
        name = input("\n\n\t\t\tEnter the Name:")
        os.system('clear')
        print('\n  *SEARCH RESULTS*\n')
      
        try:
          while 1:
            newContact = pickle.load(contactdetails) 
            if (newContact.get_name().lower()).find(name) != -1: 
              newContact.display_contact()
              found = 1
        except EOFError:
          print("")
            
      else:
        ph = input("\n\n\t\t\tEnter the Phone No.:")
        os.system('clear')
        print('\n  *SEARCH RESULTS*\n')
        try:
          while 1:
            newContact = pickle.load(contactdetails) 
            if newContact.get_ph().find(ph) != -1: 
              newContact.display_contact()
              found = 1   
        except EOFError:
          print("")

    if found==0:
      print('\n  Sorry,No Matches Found!')


while 1:
    os.system('clear')
    choice = menu()
    newContact = Contact()
    os.system('clear')
    if choice==1:
      s = int(input('\n\n\t\t\t\tPress\n\n\t\t\t\t1.To search by Name\n\t\t\t\t2.To search by Phone number\n\n\n\t\t\t   Enter you choice:'))
      search(s)

    elif choice==2:
      with open(CONTACT_DETAILS,'rb') as contactdetails: 
        print('\n  **ALL CONTACTS**\n')
 
        try:
          while 1:
            newContact = pickle.load(contactdetails)
            newContact.display_contact()
        except EOFError:
          print("")
         

    elif choice==3:
      newContact.add_contact()
      with open(CONTACT_DETAILS,'ab') as contactdetails:
        pickle.dump(newContact,contactdetails)

    elif choice==5:
      print('\n\n\n\n\n\t\t\t\t\tTHANK YOU :)\n\n\n\n\n')
      sys.exit()
    
    any = input('\n\n\nPress any key to go back...')
