import MySQLdb
import json
import argparse
import itertools
import sets


def flatten(lst):
    flat = []
    for l in lst:
        for tup in l:
            flat.append(tup[0] + " " + tup[1])
    return list(set(flat))


def get_combinations(s):
    print s

    ss = s.split(" ")

    pieces = []

    count = s.count("/")

    for i in range(0, len(ss)):
        if "/" in ss[i]:
            pieces.append(ss[i].split("/"))
        else:
            pieces.append([ss[i]])

    if count > 0:
        combos = pieces[0]
        for i in range(1, len(pieces)):
            if len(combos) < len(pieces[i]):
                combos = flatten([zip(combos, x) for x in itertools.permutations(pieces[i], len(combos))])
            else:
                combos = flatten([zip(x, pieces[i]) for x in itertools.permutations(combos, len(pieces[i]))])

    if count == 1:
        combos = combos + s.split("/")

    print combos

    return combos


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ingred", type=str, help="The file containing the ingredient information")

    args = parser.parse_args()

    ingredient_data = json.load(open(args.ingred))

    output = open("ingredient.csv", "w")

    num_items = len(ingredient_data['ingredients'])

    id = 1

    for i in range(0, num_items):
        item = ingredient_data['ingredients'][i]
        name = str(item["name"]).lower()
        if "," in name:
            print str(i + 1) + name
        rating = str(item["rating"]).lower()
        if "/" in name:
            names = get_combinations(name)
            for item in names:
                output.write(str(id) + "," + item + "," + rating + "\n")
                print str(id) + "," + item + "," + rating + "\n"
                id = id + 1
        else:
            if i == len(num_items):
                output.write(str(id) + "," + name + "," + rating + "\n")
            else:
                output.write(str(id) + "," + name + "," + rating + "\n")
            id = id + 1

    output.close()


if __name__ == "__main__":
    main()