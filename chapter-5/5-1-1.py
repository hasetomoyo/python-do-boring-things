birthdays = {'はせとも': '7/2'}

while True:
    print('名前を入力してください：(終了するにはEnterを押してください)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + 'の誕生日は' + birthdays[name])
    else:
        print(name + 'の誕生日は未登録です')
        print('誕生日を入力してください：')
        bday = input()
        birthdays[name] = bday
        print('誕生日データベースを更新しました')