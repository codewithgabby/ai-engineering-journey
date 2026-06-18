""" class Database:

    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Closed")


with Database() as db:
    print("Running Query") """

########################################################

""" class FileManager:

    def __enter__(self):
        print("File Opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("File Closed")


with FileManager() as file:
    print("Reading File")
    print("Processing File")

print("Program Finished") """

###########################################################

""" with database_session() as db:
    save_user()
    raise Exception("Payment Failed")
    create_order()

return {"message": "success"} """