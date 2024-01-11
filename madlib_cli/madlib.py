import re

# welcome = """
# Welcome to Madlibs!\n
# Please answer the following prompts and in return you'll receive a fun madlib story!\n
# If prompted with an adjective, input an adjective\n
# If prompted with a first name, input a first name\n
# """
# print(welcome)

def read_template(file):
    with open(file, 'r') as reader:
        content = reader.read()
        print(content)
        # used ChatGPT and determined I need to include return content
        return content

# Used ChatGPT to figure out I can use regex to find the {}
# Used ChatGPT to figure out re.findall and re.sub method
def parse_template(file):
    # takes all instances of {} and converts to tuple
    template = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", file))
    # replaces the extracted {Adjective} and {Noun} with {}
    stripped_template = re.sub(r"\{([A-Za-z0-9 '_]+)\}", '{}', file)
    return stripped_template, template

# Used ChatGPT to figure out for loop and .replace method
def merge(template, tuple):
    for words in tuple:
        template = template.replace('{}', str(words), 1)
    return template