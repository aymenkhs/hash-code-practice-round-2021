

def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def separate_first_line(content):
    # find the index of the first '\n'
    index = content.find('\n')
    first_line = content[:index]
    content = content[index+1:]
    return first_line, content

def separate_content(nb_line):
    lines = content.split("\n")
    return lines[:-1] # we remove the last line which is ''


def first_line_content(first_line):
    values = first_line.split(' ')
    nb_pizza = int(values[0])
    teams2 = int(values[1])
    teams3 = int(values[2])
    teams4 = int(values[3])
    return nb_pizza, teams2, teams3, teams4

def line_content(line):
    values = line.split(' ')
    nb_ingredients = int(values[0])
    ingrediants = values[1:]
    return nb_ingredients, ingrediants
