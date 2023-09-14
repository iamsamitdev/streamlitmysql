import pymysql

# สร้างฟังก์ชันสำหรับการเชื่อมต่อฐานข้อมูล
def connectdb():
    # connection = pymysql.connect(
    #     host='localhost',
    #     user='root',
    #     password='12345678',
    #     db='pythondb',
    #     port=3306,
    #     cursorclass=pymysql.cursors.DictCursor
    # )
    connection = pymysql.connect(
        host='bsxlwlo7mm54jimf3oid-mysql.services.clever-cloud.com',
        user='utkrhrvd3nsx8fn6',
        password='1OQu9GrOWtr5sw1DOO4l',
        db='bsxlwlo7mm54jimf3oid',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# ทดสอบเรียกใช้งานฟังก์ชัน
# print(connectdb())