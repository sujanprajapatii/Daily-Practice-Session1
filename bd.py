if __name__ == '__main__':

    birthdays = {
        'Sujan': '03/14/1879',
        'Sudharsan': '01/17/1706',
        'Kripa': '12/10/1815',
        'Bidhi': '06/14/1946',
        'Radha': '01/6/1955'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)#This shows the user which names are available in the dictionary.

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is on {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))