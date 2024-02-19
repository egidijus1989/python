class DataBase:
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance__ == None:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Jungiames prie DB: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('atsijungiame')

db1 = DataBase('Admin', '1234', 8080)
print(id(db1))
db1 = 5
db2 = DataBase("NoAdmin", "12345", 80)

print(id(db1), id(db2))