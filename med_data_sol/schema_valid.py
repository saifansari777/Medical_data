med_record_validator = {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "pateint_name", "docter_name" ,"diagnoses","comment",],
         "properties": {
            "pateint_name": {
               "bsonType": "string",
               "maxlength":100,
               "description": "must be a string and is required"
            },
            "doctor_name":{
               "bsonType": "string",
                "maxLength":100,
               "description": "must be a string and is required"
            },
            "diagnoses":{
                "bsonType": "string",
                 "maxLength":100,
               "description": "must be a string and is required"
            },
            
            "registration_date":{
              "bsonType":"date",
              "description": "must be a date and is required"
            },
            "last_checkup_date":{
              "bsonType":"date",
              "description": "must be a date and is required"
            },
            "comment":{
              "bsonType": "string",
              "maxLength":5000,
               "description": "must be a string and is required"

            },
            }
         }
      }

user_validator = {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "username", "email", "password", "user_group" ],
         "properties": {
            "username": {
               "bsonType": "string",
               "uniqueItems": "true",
               "maxLength":24,
               "description": "must be a string and is required"
            },
            "email":{
               "bsonType": "string",
              "uniqueItems": "true",
              "pattern" : "^.+@.+$",
               "description": "must be a string and is required"
            },
            "password":{
               "bsonType": "string",
               "minLength":8,
               "maxLength":32,
               "description": "must be a string and is required and shoul be between 8 to 32 characters"

            },
            "user_group" :{
              "enum":["Admin", "Docter", "Patient"],
              "description":"have to choose one from these"

            }
            
            }
         }
      }

