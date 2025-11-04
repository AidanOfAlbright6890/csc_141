from pathlib import Path
import json
username = input("What is your name? ")
age = input("What is your age? ")
city = input("What city do you live in? ")
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")
print(f"I figured you where {age} years old!")
print(f"{city} is a great place to live!")



from pathlib import Path
import json
def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
   