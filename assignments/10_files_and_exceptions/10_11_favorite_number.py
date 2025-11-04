from pathlib import Path
import json
number = input("What is your favorite number?  ")
path=Path('number.json')
contents=json.dumps(number)
path.write_text(contents)
print(f"I know your favorite number! It's {number}")
