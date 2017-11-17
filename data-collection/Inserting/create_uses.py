import sets


def main():
    made_by_file = open("made_by.csv", 'r').read().splitlines()
    contains_file = open("contains.csv", 'r').read().splitlines()
    uses_file = open("uses.csv", 'w')

    brand_makes = {}

    for line in made_by_file:
        line_sep = line.split(",")
        if line_sep[1] not in brand_makes:
            brand_makes[line_sep[1]] = [line_sep[0]]
        else:
            brand_makes[line_sep[1]].append(line_sep[0])

    product_contains = {}

    for line in contains_file:
        line_sep = line.split(",")
        if line_sep[0] not in product_contains:
            product_contains[line_sep[0]] = [line_sep[1]]
        else:
            product_contains[line_sep[0]].append(line_sep[1])

    brand_uses = {}

    for brand in brand_makes:
        l = brand_makes[brand]
        brand_uses[brand] = []
        print brand
        for p in l:
            brand_uses[brand] = brand_uses[brand] + product_contains[p]
        brand_uses[brand] = list(set(brand_uses[brand]))

    for brand in brand_uses:
        use = brand_uses[brand]
        for ing in use:
            uses_file.write(str(brand) + "," + str(ing) + "\n")

    uses_file.close()

if __name__ == "__main__":
    main()