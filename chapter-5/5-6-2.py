def display_inventory(inventory):
    print('持ち物リスト：')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print('アイテム総数：' + str(item_total))

def add_to_inventory(inventory, added_items):
    for k in added_items:
        inventory.setdefault(k, 0)
        inventory[k] = inventory[k] + 1
        print(inventory)
    return inventory

inv = {'金貨':42, 'ロープ':1}

dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']

print(inv)

inv = add_to_inventory(inv, dragon_loot)

print(inv)

display_inventory(inv)