class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Database connection established"
            print("Creating new database connection")
        return cls._instance

    def query(self, sql):
        return f"Executing: {sql}"


def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(f"db1 ID: {id(db1)}")
    print(f"db2 ID: {id(db2)}")
    print(f"Are they the same instance? {db1 is db2}")

    print(db1.query("SELECT * FROM users"))
    print(db2.query("SELECT * FROM products"))
    print()