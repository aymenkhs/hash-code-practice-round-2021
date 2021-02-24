import input



def main():
    # read the file
    content = input.read_file(input.path_files["a"])
    # separate the first line
    first_line, content = input.separate_first_line(content)
    # extract content from the first line
    nb_pizza, nb_teams2, nb_teams3, nb_teams4 = input.first_line_content(first_line)
    # separate the folowing lines
    lines = input.separate_content(content)
    # extract the content from each line
    pizzas = [] 

if __name__ == '__main__':
    main()
