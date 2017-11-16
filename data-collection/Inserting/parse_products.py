import json
import argparse

exception = "1, 2-hexanediol"

def get_last_prod_num():
    products = open("product.txt", 'r').readlines()
    last = products[-1].split("/")
    return int(last[0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("products", type=str, help="The file containing the product information")

    args = parser.parse_args()

    product_json = json.load(open(args.products))

    ingredients = open("ingredient.csv", "r").readlines()

    ingredients[0] = (1, "1, 2-hexanediol")

    for i in range(1, len(ingredients)):
        sep = ingredients[i].split(",")
        ingredients[i] = (int(sep[0]), sep[1])

    id = get_last_prod_num() + 1

    print id

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
            products.append((id, title, price, brand, ingredients))
            id = id + 1

    for stuff in products:
        print "\n\n"
        print stuff

    # print products[0]


if __name__ == "__main__":
    main()