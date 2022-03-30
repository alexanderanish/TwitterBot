def get_database():
    from pymongo import MongoClient
    import pymongo
    from credential import connection_string
    

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = connection_string

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['Polls']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()

    #print(dbname)

    StockData= dbname["StockData"]

    item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
    "category" : "kitchen appliance"
    }

    StockData.insert_one(item_1)

    print(StockData)