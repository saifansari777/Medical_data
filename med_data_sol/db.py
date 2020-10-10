from pymongo import MongoClient
import json
from .schema_valid import med_record_validator, user_validator


def init_db():
  
  client = MongoClient("mongodb+srv://saif:brick@cluster0.j6jw7.mongodb.net/<dbname>?retryWrites=true&w=majority")

  db = client.med_data_sol


  if db.med_record:
    pass
  else:
    db.create_collection("med_record", validator=med_record_validator)

  if db.users:
    pass
  else:
    db.create_collection("user", validator=user_validator)

 
  return db