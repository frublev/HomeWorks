from pprint import pprint


def cookbook_load(cookbook_name):
    cook_dict = {}
    with open(cookbook_name, encoding="utf-8") as f_cook_book:
        for line in f_cook_book:
            dishes = line.strip()
            cook_dict[dishes] = list()
            ingr_num = int(f_cook_book.readline())
            for i in range(0, ingr_num):
                ingredients_dict = {}
                ingredient = f_cook_book.readline().split(" | ")
                ingredients_dict['ingredient_name'] = ingredient[0]
                ingredients_dict['quantity'] = int(ingredient[1])
                ingredients_dict['measure'] = ingredient[2].strip()
                cook_dict[dishes].append(ingredients_dict)
            f_cook_book.readline()
    return cook_dict


pprint(cookbook_load("recipes.txt"))


def get_shop_list_by_dishes(dishes, person_count):
    cook_dict = cookbook_load("recipes.txt")
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_dict[dish]:
            if ingredient["ingredient_name"] in shop_list.keys():
                shop_list[ingredient["ingredient_name"]]["quantity"] += ingredient["quantity"] * person_count
            else:
                shop_list[ingredient["ingredient_name"]] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity'] * person_count}
    pprint(shop_list)


get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)