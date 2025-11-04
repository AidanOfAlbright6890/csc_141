from pathlib import Path
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path ('C:/Users/aidan/OneDrive/Documents/CSC 141/assignments/10_files_and_exceptions/programming.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)