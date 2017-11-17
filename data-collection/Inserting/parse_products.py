import json
import argparse
import difflib

exception = "1, 2-hexanediol"


def get_last_brand_info():
    brands = open("brand.csv", 'r').read().splitlines()

    b = []
    bs = []
    bd = {}

    for line in brands:
        line_sep = line.split(",")
        b.append(line_sep[1])
        bs.append((int(line_sep[0]), line_sep[1]))

    bid = 0
    if len(brands) != 0:
        bid = bs[-1][0]

    return bid + 1, b, bs



def get_prod_num():
    products = open("product.txt", 'r').read().splitlines()
    if len(products) == 0:
        return 1
    else:
        last = products[-1].split(",/,")
        return int(last[0]) + 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("products", type=str, help="The file containing the product information")

    args = parser.parse_args()

    product_json = json.load(open(args.products))

    ingredients = open("ingredient.csv", "r").read().splitlines()

    ingredients_data = [(1, "1, 2-hexanediol")]

    ingredients_list = ["1, 2-hexanediol"]

    for i in range(1, len(ingredients)):
        sep = ingredients[i].split(",")
        ingredients_data.append((int(sep[0]), sep[1]))
        ingredients_list.append(sep[1])

    pid = get_prod_num()

    product_file = open("product.txt", 'a+')
    brand_file = open("brand.csv", 'a+')
    made_by_file = open("made_by.csv", 'a+')
    contains_file = open("contains.csv", 'a+')

    bid, brands, brand_data = get_last_brand_info()

    brand_dict = {}

    print bid
    print brands

    "hello"

    "hello"

    products = []

    for item in product_json:
        if "ingredients" in item:
            brand = item["brand"][0].encode('utf-8')
            price = float(item["price"][1:].encode('utf-8'))
            title = item["title"][0].encode('utf-8')
            if " - " in title:
                sep = title.split(" - ")
                title = sep[0]
            ingredients = item["ingredients"].encode('utf-8')
            ingredients = [x.strip().lower() for x in ingredients.split(",")]
            if "." in ingredients[-1]:
                sep = ingredients[-1].split(".")
                ingredients[-1] = sep[0]
            products.append((pid, title, price, brand, ingredients))
            product_file.write(str(pid) + ",/," + title + ",/," + str(price) + "\n")
            if brand not in brands:
                brand_data.append((bid, brand))
                brands.append(brand)
                brand_file.write(str(bid) + "," + brand + "\n")
                bid = bid + 1
            cbid = brand_data[brands.index(brand)][0]
            if cbid in brand_dict:
                brand_dict[cbid].append(pid)
            else:
                brand_dict[cbid] = [pid]
            pid = pid + 1

    print brand_dict

    for key in brand_dict:
        l = brand_dict[key]
        for p in l:
            made_by_file.write(str(p) + "," + str(key) + "\n")


    contains_dict = {}

    for item in products:
        p = item[0]
        ingred = item[4]
        contains_dict[p] = []
        print "\n"
        print item
        for ing in ingred:
            try:
                match = difflib.get_close_matches(ing, ingredients_list)[0]
                match_ind = ingredients_list.index(match)
                print match
                contains_dict[p].append(ingredients_data[match_ind][0])
            except:
                continue

    print contains_dict

    for key in contains_dict:
        l = contains_dict[key]
        for iid in l:
            contains_file.write(str(key) + "," + str(iid) + "\n")

    product_file.close()
    brand_file.close()
    made_by_file.close()


if __name__ == "__main__":
    main()