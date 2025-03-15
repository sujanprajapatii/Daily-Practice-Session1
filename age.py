if __name__ == '__main__':

    Age ={
        'Sujan': '18',
       'Sudharsan': '19',
        'Kripa': '18',
        'Bidhi': '19',
        'Radha': '20',
        'Prashant':'26'
        }

    print('Welcome to the Age dictionary.')
    for name in Age:
        print(name)

    print('Who\'s Age do you want to look up?')
    name = input()
    if name in Age:
        print('{}\'s age is {}.'.format(name, Age[name]))
    else:
        print('Sadly, we don\'t have {}\'s Age.'.format(name))