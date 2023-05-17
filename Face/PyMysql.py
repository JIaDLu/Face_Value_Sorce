# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host="127.0.0.1", user="root", password="123456",
# 	 db="studentsdb", port=3306, charset='utf8')
#
# # 使用cursor()方法获取操作游标
# cur = db.cursor()
import pymysql

class MSSQL(object):
    instance = None
    def __init__(self, host: str = '127.0.0.1', port: int = 3306, user: str = 'root',
                 pwd: str = '123456', database: str = 'facesorce_app', charset: str = 'utf8') -> None:
        """
        database operation class
        :param host: the database server host name
        :param port: the database server port number
        :param user: the database server user name
        :param pwd: the database server key
        :param database: the database name
        :param charset: the encode of the database server
        """
        self._conn = pymysql.connect(host=host, port=port, user=user, passwd=pwd, db=database, charset=charset)
        self._cur = self._conn.cursor()

    @classmethod

    def get_instance(cls):
        """
        get a class instance just only one.
        :return:the class instance
        """
        if cls.instance:
            return cls.instance
        else:
            cls.instance = MSSQL()
            return cls.instance

    def insert_user_2_db(self, data):
        sql = "INSERT INTO client_info(acount,password, telephone, email) VALUES " \
                  "(%s, %s, %s, %s)"
        self._cur.execute(sql, data)
        self._conn.commit()

    def query_super(self, table_name,args,usr_name,usr_pwd):
        sql = "select * from {} where {} = '{}' and {}='{}'".format(table_name, args[0], usr_name, args[1], usr_pwd)
        count = self._cur.execute(sql)
        ret = self._cur.fetchall()
        return count

    def insert_mark_data(self,data):
        sql= 'UPDATE mark_data SET mark = %s WHERE id = 1'
        self._cur.execute(sql, data)
        self._conn.commit()

    def get_notice_data(self):
        sql = "select * from notice_data"  # 将数据从数据库中拿出来
        self._cur.execute(sql)
        total = self._cur.fetchall()
        return total

    def get_mark_data(self):
        #print('1122')
        sql = "select * from mark_data"  # 将数据从数据库中拿出来
        self._cur.execute(sql)
        total = self._cur.fetchall()
        #print('dsad',total)
        return total
