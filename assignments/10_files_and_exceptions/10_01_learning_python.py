from pathlib import Path
path = Path('C:/Users/aidan/OneDrive/Documents/CSC 141/assignments/10_files_and_exceptions/pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

    
