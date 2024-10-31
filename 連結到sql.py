# 
import pymysql

# 基本設定
db_settings = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"90409991",
    "db":"my_db",
    "charset":"utf8"

}

# 建立cursor
try:
    conn = pymysql.connect(**db_settings)
    print("成功")

except Exception as ex:
    print(ex)


# with陳述式區塊中，撰寫與執行SQL語法
with conn.cursor() as cursor:
    # 查詢資料庫資料: 使用SQL語法
    command = "SELECT * FROM students"

    cursor.execute(command)

    result = cursor.fetchall()

    print(result)
    print(type(result))





    