import mysql.connector

mydb = mysql.connector.connect(
    host="rm-bp13na1cho4m4n4vcto.mysql.rds.aliyuncs.com",  # 数据库主机地址
    user="nikang",  # 数据库用户名
    passwd="nikang@123456"  # 数据库密码
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE hangzhoutest")
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)