class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def Add_NewContacts(self, name, PNumbers):
        self.contacts [name] = PNumbers
        print(f"Contact: ({name}) has been added to the contact list")

    def Search_ForContacts(self, name):
        return self.contacts.get(name,"Contact does not exist")


    def delete_Contacts(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact has been deleted")
        else:
            print("Contact does not exist")

PB = PhoneBook()
PB.Add_NewContacts("Tayon", "516-223-1905")
PB.Add_NewContacts("Ange", "347-875-8542")
PB.Add_NewContacts("Josh", "855-321-4567")
PB.Add_NewContacts("Caroline", "137-098-6751")

print(PB.Search_ForContacts("Tayon"))
print(PB.delete_Contacts("Tayon"))
print(PB.Search_ForContacts("Tayon"))
print(PB.Search_ForContacts("Ange"))
print(PB.delete_Contacts("Ange"))
print(PB.Search_ForContacts("Ange"))
print(PB.Search_ForContacts("Josh"))
print(PB.delete_Contacts("Josh"))
print(PB.Search_ForContacts("Josh"))
print(PB.Search_ForContacts("Caroline"))
print(PB.delete_Contacts("Caroline"))
print(PB.Search_ForContacts("Caroline"))





