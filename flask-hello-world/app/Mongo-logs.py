from pymongo import MongoClient

# Replace with your MongoDB connection string
MONGO_URI = "mongodb+srv://amrupendse:XXX@cluster-monitoring.udx2ebr.mongodb.net/"  # or use your cloud URI

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Choose your database and collection
db = client["Log_Monitoring"]  # Replace with your database name
collection = db["logs"]  # Replace with your collection name

# Fetch all documents in the collection
documents = collection.find()

# Print documents
for doc in documents:
    print(doc)

# Optional: close the client connection
client.close()
