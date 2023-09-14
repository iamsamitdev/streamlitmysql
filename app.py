import pymysql
import streamlit as st
import connectmysql as conn

st.title('MySQL Person CRUD App')

# Create Connection and Cursor
connection = conn.connectdb()
cursor = connection.cursor()

# Function อ่านข้อมูลจากตาราง persons ใน MySQL Database
def read_persons():
    cursor.execute("SELECT * FROM person")
    persons = cursor.fetchall()
    return persons

# Function สำหรับเพิ่มข้อมูลเข้าตาราง person
def create_person(fullname, email, age):
    try:
        cursor.execute(
            "INSERT INTO person (fullname, email, age) VALUES (%s, %s, %s)", (fullname, email, age)
        )
        connection.commit()
        st.success('เพิ่มข้อมูลเรียบร้อยแล้ว')
        
        st.markdown("""
            <a href="?menu=Read" target="_self">Click here</a> to view the list of persons.
        """, unsafe_allow_html=True)

    except pymysql.Error:
        connection.rollback()
        st.error(f'Error create person: {pymysql.Error}')


# Funtion สำหรับอัพเดทข้อมูลในตาราง person
def update_person(id, fullname="", email="", age=""):
    try:
        cursor.execute(
            "UPDATE person SET fullname=%s, email=%s, age=%s WHERE id=%s", (fullname, email, age, id)
        )
        connection.commit()
        st.success('อัพเดทข้อมูลเรียบร้อยแล้ว')
        st.markdown("""
            <a href="?menu=Read" target="_self">Click here</a> to view the list of persons.
        """, unsafe_allow_html=True)
    except pymysql.Error:
        connection.rollback()
        st.error(f'Error update person: {pymysql.Error}')


# Function สำหรับลบข้อมูลในตาราง person
def delete_person(id):
    try:
        cursor.execute("DELETE FROM person WHERE id=%s", (id))
        connection.commit()
        st.success('ลบข้อมูลเรียบร้อยแล้ว')
        st.markdown("""
            <a href="?menu=Read" target="_self">Click here</a> to view the list of persons.
        """, unsafe_allow_html=True)
    except pymysql.Error:
        connection.rollback()
        st.error(f'Error delete person: {pymysql.Error}')

# Main Menu
menu = st.sidebar.selectbox("Menu", ["Read", "Create", "Update", "Delete"])

# Menu: Read
if menu == "Read":
    st.subheader("Read Persons")
    persons = read_persons()

    # check persons is not empty
    if persons:
        # Create table to show persons
        table_data = [["ID", "Full Name", "Email", "Age", "Edit", "Delete"]]
        for person in persons:
            edit_link = f"[Edit {person['id']}]"
            delete_link = f"[Delete {person['id']}]"
            row = [person['id'], person['fullname'], person['email'], person['age'], edit_link, delete_link]
            table_data.append(row)
        st.table(table_data)
    else:
        st.info('ไม่มีข้อมูลในฐานข้อมูล')

# Menu: Create
elif menu == "Create":
    st.subheader("Create Person")
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", 0, 100, 1)

    # button create
    if st.button("Create"):
        # check fullname, email, age is not empty
        if fullname and email and age:
            create_person(fullname, email, age)
        else:
            st.warning("กรุณาป้อนข้อมูลให้ครบถ้วน")

# Menu: Update
elif menu == "Update":
    st.subheader("Update Person")
    id = st.number_input("ID", min_value=1)
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1, max_value=100)

    if st.button("Update"):
        update_person(id, fullname, email, age)

# Menu: Delete
elif menu == "Delete":
    st.subheader("Delete Person")
    id = st.number_input("ID", min_value=1)

    if st.button("Delete"):
        delete_person(id)