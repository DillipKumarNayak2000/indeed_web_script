import pymongo
from scrap_data import scrape_indeed_jobs

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/labDB")

# Database Name
dataBase = client["labDB"]

# Collection  Name
collection = dataBase['Products']

def insert_data_to_mongodb(data):
    collection.insert_many(data)

# Scrape job listings
jobs_data = scrape_indeed_jobs('keyword')

# Store job listings in MongoDB
#insert_data_to_mongodb(jobs_data)
# Store job listings in MongoDB
if jobs_data:  # Check if the list is not empty
    insert_data_to_mongodb(jobs_data)
else:
    print("No job data to insert.")

