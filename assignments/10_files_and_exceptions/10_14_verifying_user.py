from pathlib import Path
import json
def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
       contents = path.read_text()
       username = input("What is your name? ")
       age = input("What is your age? ")
       city = input("What city do you live in? ")
       return username, age, city
    print(username)
   
    
    

    
