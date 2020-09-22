from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):pass

    @abstractmethod
    def disconnect(self):pass

class Oracle(DBInterface):
    def connect(self):
        print("Connected to Oracle")
    def disconnect(self):
        print("Disconnected from Oracle")

class SqlServer(DBInterface):
    def connect(self):
        print("Connected to SqlServer")
    def disconnect(self):
        print("Disconnected from SqlServer")


db = input("Enter database name: ")
obj = globals()[db]()
obj.connect()
obj.disconnect()

