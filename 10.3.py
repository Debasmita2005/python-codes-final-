#Accept contact details from the user and create a vcard that we can directly store in our mobile.

name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")

card = f"""
-----------------------
     CONTACT CARD     
-----------------------
Name  : {name}
Phone : {phone}
Email : {email}
-----------------------
"""

with open("contact_card.txt", "w") as file:
    file.write(card)

print("Contact card saved in 'contact_card.txt'")
