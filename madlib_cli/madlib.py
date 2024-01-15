import re
from pathlib import Path

# welcome = """
# Welcome to Madlibs!\n
# Please answer the following prompts and in return you'll receive a fun madlib story!\n
# """
# # print(welcome)

# file_path = Path("./assets/dark_and_stormy_night_template.txt")
# # Uncomment for debugging to checking if the path exists
# # if file_path.exists():
# #     content = file_path.read_text()
# #     print(content)
# # else:
# #     print("File does not exist.")

# def madlib_template(file_path):
#     """Reads and prints a txt file from the argument file_path"""
#     with open(file_path, 'r') as reader:
#         content = reader.read()
#         print(content)

# madlib = madlib_template(file_path)


# # can't figure out what this error is
# def parse_template(madlib):
#     """Parses through txt file and removes instances of {}."""
#     # takes all instances of {} and converts to tuple
#     template = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", madlib))
#     print(template)

# parse_template(madlib)



# Tests

def read_template(file):
    """Reads and prints a txt file from the argument file_path"""
    with open(file, 'r') as reader:
        content = reader.read()
        print(content)
        # used ChatGPT and determined I need to include return content
        return content

# Used ChatGPT to figure out I can use regex to find each {}
# Used ChatGPT to figure out re.findall and re.sub method
def parse_template(file):
    """Parses through txt file and removes strings within {} and stores in a tuple. Returns original string with {} as place holders and returns a tuple"""
    # takes all instances of {} and converts to tuple
    template = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", file))
    # replaces the extracted {Adjective} and {Noun} with {}
    stripped_template = re.sub(r"\{([A-Za-z0-9 '_]+)\}", '{}', file)
    return stripped_template, template

# Used ChatGPT to figure out for loop and .replace method
def merge(template, tuple):
    """Loops through a template and replaces {} with the elements in a tuple. Returns string"""
    for words in tuple:
        template = template.replace('{}', str(words), 1)
    return template

# From class review, this will also pass the third test
def merge(stripped_template, parts):
    return stripped_template.format(*parts)