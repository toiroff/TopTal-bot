import sqlite3
Xudoberdi = sqlite3.connect('main.db')

def bot_stat():
    odam = Xudoberdi.execute('''SELECT id FROM languages''')
    return odam.fetchall()


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_userss(self):
        sql = """
        CREATE TABLE users (
        id INTEGER NOT NULL UNIQUE,
        ism	TEXT NOT NULL,
        fam TEXT,
        tg_id INTEGER NOT NULL UNIQUE,
        PRIMARY KEY(id AUTOINCREMENT)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

#--------------------------------

    def create_table_royxat(self):
        sql = """
        CREATE TABLE royxat (
        id INTEGER NOT NULL UNIQUE,
        number INTEGER,
        nick_name TEXT,
        PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)


    def royxat_qoshish(self,id:int=None,number:int=None,nick_name:str=None,ball:int=None,daraja:str=None,username:str=None):
        # SQL_EXAMPLE ="INSERT INTO myfiles_teacher(id,name,email)VALUES(1,"john","john@hgmail.com")"

        sql="""
        INSERT INTO royxat ( id,number, nick_name , ball,daraja,username) VALUES(?, ?, ?,?,?,?)
        """
        self.execute(sql, parameters=(id,number,nick_name,ball,daraja,username), commit=True)

    def select_royxat(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM royxat WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_all_royxat(self):
        sql = """
        SELECT * FROM royxat
        """
        return self.execute(sql, fetchone=True)



    def create_table_zakaz(self):
        sql = """
        CREATE TABLE zakaz (
        id INTEGER NOT NULL UNIQUE,
        zakaz TEXT,
        tg_id INTEGER,
        PRIMARY KEY(id AUTOINCREMENT)
            );
"""
        self.execute(sql, commit=True)

    def zakaz_qoshish(self,nomi:str=None,tarifi:str=None,narxi:int=None,kategoriya:str=None,user_id:int=None, username:int=None,daraja:str=None):
        # SQL_EXAMPLE ="INSERT INTO myfiles_teacher(id,name,email)VALUES(1,"john","john@hgmail.com")"

        sql="""
        INSERT INTO zakaz (nomi,narxi,tarifi,kategoriya,user_id,username,daraja) VALUES(?, ?, ?, ?, ?,?,?)
        """
        self.execute(sql, parameters=(nomi,narxi,tarifi,kategoriya,user_id,username,daraja), commit=True)

    def select_zakaz(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM zakaz WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_zakaz(self):
        sql = """
        SELECT * FROM zakaz
          """
        return self.execute(sql, fetchall=True)



    def select_zakaz_random(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM zakaz ORDER BY random() LIMIT 5 "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)





    def select_taklif1(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM zakaz WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def create_table_taklif(self):
        sql = """
        CREATE TABLE taklif (
        id INTEGER NOT NULL UNIQUE,
        Tid INTEGER,
        zakaz TEXT,
        tg_id INTEGER,
        PRIMARY KEY (id AUTOINCREMENT)
            );
"""
        self.execute(sql, commit=True)

    def taklif_qoshish(self, Fid: str= None, zakaz: str = None, tg_id: str = None, holat: str = None,buyurtma_id: int=None,taklif:str=None,data:str=None,deletedata:str=None):
        # SQL_EXAMPLE ="INSERT INTO myfiles_teacher(id,name,email)VALUES(1,"john","john@hgmail.com")"

        sql = """
         INSERT INTO taklif ( Fid, zakaz, tg_id,holat,buyurtma_id,taklif,data,deletedata) VALUES(?,?, ?, ?,?,?,?,?)
         """
        self.execute(sql, parameters=(Fid, zakaz, tg_id,holat,buyurtma_id,taklif,data,deletedata), commit=True)

    def select_taklifs(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM taklif WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_bal(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM royxat WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)


    def update_kategoriya(self, kategoriya, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE royxat
         SET kategoriya=? WHERE id=?
        """
        return self.execute(sql, parameters=(kategoriya, id), commit=True)

    def update_ball(self, ball, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE royxat
         SET ball=? WHERE id=?
        """
        return self.execute(sql, parameters=(ball, id), commit=True)

    def update_daraja(self, daraja, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE royxat
         SET daraja=? WHERE id=?
        """
        return self.execute(sql, parameters=(daraja, id), commit=True)

    def add_ball(self, ball, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
         UPDATE royxat SET ball = ball + ? WHERE id = ?
         """
        return self.execute(sql, parameters=(ball, id), commit=True)

    def delete_ball(self, ball, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
         UPDATE royxat SET ball = ball - ? WHERE id = ?
         """
        return self.execute(sql, parameters=(ball, id), commit=True)
# About me ------------------------------------------------------------------------------
    def select_daraja(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM royxat WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def buyurtma_raqami(self):
        return self.execute("SELECT COUNT(*) FROM zakaz;", fetchone=True)

    def filter(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM taklif WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def filterall(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM taklif WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def filterr(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM royxat WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def filter_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM royxat WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def filter_zakaz(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM zakaz WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def zakaz_filter(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM zakaz WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def delete(self):
        self.execute("DELETE FROM zakaz WHERE TRUE", commit=True)

    def update_nomer(self, number, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE royxat
         SET number=? WHERE id=?
        """
        return self.execute(sql, parameters=(number, id), commit=True)

    def update_name(self, name,id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE royxat
         SET nick_name=? WHERE id=?
        """
        return self.execute(sql, parameters=(name,id), commit=True)


    def update_taklif(self, holat,buyurtma_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
        sql = f"""
        UPDATE taklif
         SET holat=? WHERE buyurtma_id=?
        """
        return self.execute(sql, parameters=(holat,buyurtma_id), commit=True)
    def select_taklif(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM taklif WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def delete_zakaz(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " DELETE FROM zakaz WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def delete_taklif(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " DELETE FROM taklif WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def buyurtma_bekor(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " DELETE FROM taklif WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def filter_royhat(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM zakaz ORDER BY random() LIMIT 5 WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)


    def count_zakaz(self):
        return self.execute("SELECT COUNT(*) FROM zakaz;", fetchone=True)
def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")