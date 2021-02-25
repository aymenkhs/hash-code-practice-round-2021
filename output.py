import os

outputs_files = {
    "a": os.path.join("outputs", "a_example"),
    "b": os.path.join("outputs", "b_little_bit_of_everything.in"),
    "c": os.path.join("outputs", "c_many_ingredients.in"),
    "d": os.path.join("outputs", "d_many_pizzas.in"),
    "e": os.path.join("outputs", "e_many_teams.in"),
}

def write_file(file_path, deliveries):
    string = ""
    string += str(len(deliveries))
    string += "\n"
    for delivery in deliveries:
        string += str(delivery.nb)
        string += " "
        pizzas = " ".join(delivery.index_pizzas)
        string += pizzas
        string += "\n"

    with open(file_path, "w") as file:
        content = file.write(string)
