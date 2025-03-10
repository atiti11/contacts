import mysql.connector
from mysql.connector import Error
from uuid import UUID
from datetime import datetime

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='mysql-engeto.alwaysdata.net ',
            database='engeto_contacts',
            user='engeto',
            password=']$4?Z6B^g_VNcm@'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Chyba při připojování k databázi: {e}")
        raise ConnectionAbortedError(f"Connection was not successful")

def find_contact(name: str, surname: str) -> list[dict]:
    connection =connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT id, name, surname, phone, mail, address, note, created_at FROM contacts
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
                "note": contact[6],
                "created_at": contact[7]
            }
            contacts_dict.append(c_dict)
    
    connection.close()
    return contacts_dict

def delete_contact(id: UUID):
    connection =connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM contacts WHERE id = %s;
    """, (id,))
    ukol = cursor.fetchone()

    if not ukol:
        print(f"Contact with this id ({id}) does not exist")
        raise NameError(f"Contact with this id ({id}) does not exist")

    cursor.execute("""
    DELETE FROM contacts WHERE id = %s;
    """, (id,))
    connection.commit()
    connection.close()

def create_contact(name, surname, phone, email , address, note):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"""
    INSERT INTO contacts (name, surname, phone, mail, address, note)
    VALUES ('{name}', '{surname}', '{phone}', '{email}', '{address}', '{note}');
    """)
    connection.commit()

    contacts = sorted(find_contact(name, surname), key=lambda x: x["created_at"], reverse=True)
    connection.close()
    return contacts[0]["id"]
