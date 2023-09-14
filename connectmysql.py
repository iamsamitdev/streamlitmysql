import pymysql

# สร้างฟังก์ชันสำหรับการเชื่อมต่อฐานข้อมูล
def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        db='pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# ทดสอบเรียกใช้งานฟังก์ชัน
# print(connectdb())