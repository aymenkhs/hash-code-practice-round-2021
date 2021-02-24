import input

class Pizza:

    def __init__(self, pizza_num, nb_ingrediants, list_ingrediants):
        self.pizza_num = pizza_num
        self.nb_ingrediants = nb_ingrediants
        self.list_ingrediants = list_ingrediants

    def __str__(self):
        return "num:{}\nnb_ingrediants:{}\ningrediants{}\n".format(self.pizza_num,
            self.nb_ingrediants, self.list_ingrediants)

    def __repr__(self):
        return str(self)

    def __contains__(self, ingrediant):
        if ingrediant in self.list_ingrediants:
            return True
        else:
            return False

    def __getitem__(self, index):
        return self.list_ingrediants[index]

    def __iter__(self):
        return iter(self.list_ingrediants)

    def __next__(self):
        return next(self.list_ingrediants)


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
    for i in range(nb_pizza):
        nb_ingredients, ingrediants = input.line_content(lines[i])
        pizzas.append(Pizza(i, nb_ingredients, ingrediants))


if __name__ == '__main__':
    main()
