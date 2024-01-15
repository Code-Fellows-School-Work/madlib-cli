import re
from pathlib import Path

welcome = """
Welcome to Madlibs!\n
Please answer the following prompts and in return you'll receive a fun madlib story!\n
"""
print(welcome)

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
