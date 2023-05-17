import pymysql

class MSSQL(object):
    instance = None
    def __init__(self, host: str = '127.0.0.1', port: int = 3306, user: str = 'root',
                 pwd: str = '123456', database: str = 'facesorce_app', charset: str = 'utf8') -> None:
        self._conn = pymysql.connect(host=host, port=port, user=user, passwd=pwd, db=database, charset=charset)
        self._cur = self._conn.cursor()

    def get_instance(cls):
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

    def store_notice_data(self,data):
        sql = "INSERT INTO notice_data(author,notice) VALUES " \
                  "(%s,%s)"
        self._cur.execute(sql, data)
        self._conn.commit()

    def get_work_data_info(self):
        sql = "select * from client_info"  # 将数据从数据库中拿出来
        self._cur.execute(sql)
        total = self._cur.fetchall()
        return total

    def delete(self,numb):
        sql = 'DELETE FROM client_info WHERE acount=%s'
        self._cur.execute(sql, numb)
        self._conn.commit()

    def add(self,n):
        sql_insert = 'INSERT INTO client_info (acount, password, telephone, email) VALUE (%s,%s,%s,%s) '
        self._cur.execute(sql_insert,n)
        self._conn.commit()

