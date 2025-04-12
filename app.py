from flexidb import get_database
# Connect to MongoDB
# Note: Make sure MongoDB is running on localhost:27017
db = get_database("mongodb", uri="mongodb://localhost:27017", database="flexidb_test")

# Create a document
user_id = db.create("users", {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
})
print(f"Created user with ID: {user_id}")

# Select a document
user = db.select("users", {"name": "John Doe"})
print(f"Found user: {user}")

# Update a document
updated = db.update("users", {"name": "John Doe"}, {"age": 31})
print(f"Updated {updated} user(s)")

# Select again to verify update
user = db.select("users", {"name": "John Doe"})
print(f"Updated user: {user}")

# Delete a document
deleted = db.delete("users", {"name": "John Doe"})
print(f"Deleted {deleted} user(s)")

# Clean up
db.disconnect()