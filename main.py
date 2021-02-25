import input

class Pizza:
    PIZZAS = []
    SORTED_PIZZAS = []

    def __init__(self, pizza_num, nb_ingrediants, list_ingrediants):
        self.pizza_num = pizza_num
        self.nb_ingrediants = nb_ingrediants
        self.list_ingrediants = list_ingrediants
        self.delivered = False

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

class Team:
    def __init__(self, nb, pizzas):
        self.nb = nb
        self.pizzas = pizzas
        self.index_pizzas = [pizza.pizza_num for pizza in pizzas]


def create_delivery(team_nb):
    # we choose the pizza with the most ingrediants
    selected_pizzas = [Pizza.PIZZAS[0]]
    Pizza.PIZZAS[0].delivered = True
    del(Pizza.PIZZAS[0])
    # then we'll choose the pizza that add the max different igrediants
    for _ in range(1,team_nb):
        max_diff = 0
        max_pizza = None
        for pizza in Pizza.PIZZAS:
            if pizza.delivered:
                continue
            diff = 0
            for ingrediant in pizza:
                present = False # if the ingrediant is already present in our selected pizzas
                for pizza_i in selected_pizzas:
                    if ingrediant in pizza_i:
                        present = True # if we find the ingrediant we make the value to true
                if not present:
                    # we increment the number of different ingredients if it's not present in the other pizzas
                    diff += 1

            if diff > max_diff:
                max_diff = diff
                max_pizza = pizza
            elif (diff == max_diff) and (max_pizza == None):
                max_diff = diff
                max_pizza = pizza
            elif (diff == max_diff) and (max_pizza.nb_ingrediants > pizza.nb_ingrediants):
                print(pizza, diff, pizza.nb_ingrediants)
                print(max_pizza, max_diff, max_pizza.nb_ingrediants)
                max_diff = diff
                max_pizza = pizza

        selected_pizzas.append(max_pizza)
        max_pizza.delivered = True
        del Pizza.PIZZAS[Pizza.PIZZAS.index(max_pizza)]

    return Team(team_nb, selected_pizzas)


def build_solution(nb_pizza, nb_teams2, nb_teams3, nb_teams4):

    deliveries = []

    # sort our list
    Pizza.PIZZAS.sort(key=lambda pizza: pizza.nb_ingrediants, reverse=True)

    remaining_pizzas = nb_pizza

    # we begin to fill the 4 members teams deliveries
    for _ in range(nb_teams4):
        if remaining_pizzas < 4:
            break;
        deliveries.append(create_delivery(4))
        remaining_pizzas-=4

    # then we fill the 3 members teams deliveries
    for _ in range(nb_teams3):
        if remaining_pizzas < 3:
            break;
        deliveries.append(create_delivery(3))
        remaining_pizzas-=3

    # finally the 2 members teams deliveries
    for _ in range(nb_teams2):
        if remaining_pizzas < 2:
            break;
        deliveries.append(create_delivery(2))
        remaining_pizzas-=2

    return deliveries


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
    for i in range(nb_pizza):
        nb_ingredients, ingrediants = input.line_content(lines[i])
        Pizza.PIZZAS.append(Pizza(i, nb_ingredients, ingrediants))

    print(build_solution(nb_pizza, nb_teams2, nb_teams3, nb_teams4))


if __name__ == '__main__':
    main()
