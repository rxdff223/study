from pymysql import Connect

conn = Connect(
    host='localhost',   # 主机地址
    port=3306, # 端口号
    user='root', # 用户名
    password="123456", # 密码
    autocommit=True # 自动提交事务
)

print(conn.get_host_info()) # 获取主机信息

cursor = conn.cursor() # 获取游标对象

conn.select_db('world') # 选择数据库

cursor.execute("insert into student values(1,'张三',18)")

conn.close() # 关闭连接
