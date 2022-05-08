with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for txt in file.read().split('\n\n'):
        name, _, *args = txt.split('\n')
        tmp = []
        for arg in args:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
            tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[name] = tmp


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      new_shop_list_item = dict(ingredient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingredient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

