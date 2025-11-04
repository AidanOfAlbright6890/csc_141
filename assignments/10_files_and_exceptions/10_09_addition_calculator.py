from pathlib import Path
def count_cats(filename):
    """Count the approximate number of cats in a file"""
    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file:
        cats = contents.split()
        num_cats = len(cats)
        print(f"Please come meet my {num_cats} cats, {filename}.")
    filename = Path('C:/Users/aidan/OneDrive/Documents/CSC 141/assignments/10_files_and_exceptions/cats.txt')
filenames = ['cats.txt']
for filename in filenames:
    path = Path(filename)
    count_cats(path)





from pathlib import Path
def count_dogs(filename):
    """Count the approximate number of cats in a file"""
    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file:
        dogs = contents.split()
        num_dogs = len(dogs)
        print(f"Please come meet my {num_dogs} dogs, {filename}.")
    filename = Path('C:/Users/aidan/OneDrive/Documents/CSC 141/assignments/10_files_and_exceptions/dogs.txt')
filenames = ['dogs.txt']
for filename in filenames:
    path = Path(filename)
    count_dogs(path)