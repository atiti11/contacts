import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='mysql-engeto.alwaysdata.net ',
            database='engeto_contacts',
            user='engeto',
            password=']$4?Z6B^g_VNcm@'
        )
        if connection.is_connected():
            print("Connected to db")
            return connection
    except Error as e:
        print(f"Chyba při připojování k databázi: {e}")
        raise ConnectionAbortedError(f"Connection was not successful")

def find_contact(name: str, surname: str) -> list[dict]:
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT id, name, surname, phone, mail, address, note FROM contacts
    WHERE (name='{name}' and surname='{surname}');
    """)
    contacts = cursor.fetchall()
    contacts_dict = []
    if contacts:
        for contact in contacts:
            c_dict = {
                "id": contact[0],
                "name": contact[1],
                "surname": contact[2],
                "phone": contact[3],
                "mail": contact[4],
                "address": contact[5],
                "note": contact[6]
            }
            contacts_dict.append(c_dict)
    
    return contacts_dict

print(find_contact("Anna", "Nováková"))