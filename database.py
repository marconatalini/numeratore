import sqlite3
import os
from datetime import datetime

class DB:
    '''Definizione del data base'''
    cn : sqlite3.Connection = None
    cr : sqlite3.Cursor = None

    def __init__(self) -> None:
        self.cn = sqlite3.connect('db_numeri.db')
        self.cn.isolation_level = None
        self.cr = self.cn.cursor()
        
        try:
            self.cr.execute("SELECT * FROM tb_numeri")
        except sqlite3.OperationalError:
            self.cr.execute("CREATE TABLE tb_numeri (numero INTEGER PRIMARY KEY, utente TEXT, pc TEXT, data TEXT)")
            self.cr.execute("INSERT INTO tb_numeri (numero) VALUES (500001)")
            self.cr.execute("INSERT INTO tb_numeri (numero) VALUES (800001)")
            self.cn.commit()

    def close(self) -> None:        
        self.cn.close()
    
    def get_next_numero_alluminio(self) -> int:
        self.cr.execute("SELECT MAX(numero) FROM tb_numeri WHERE numero > 800000")
        n = self.cr.fetchone()[0]
        return n + 1

        
    def get_next_numero_persiane(self) -> int:
        self.cr.execute("SELECT MAX(numero) FROM tb_numeri WHERE numero > 500000")
        n = self.cr.fetchone()[0]
        return n + 1

    def save_numero(self, numero) -> None:
        parm = (numero, os.environ.get("USERNAME"), os.environ.get("COMPUTERNAME"), datetime.now())
        self.cr.execute("INSERT INTO tb_numeri (numero, utente, pc, data) VALUES (?,?,?,?)", parm)
        self.cn.commit()

    def get_lasts(self, limit: int = 10) -> list:
        self.cr.execute("SELECT * FROM tb_numeri ORDER BY data DESC LIMIT ?", (limit ,))
        return self.cr.fetchall()

        
if __name__ == '__main__':
    db = DB()
    print(db.get_next_numero_alluminio())



    