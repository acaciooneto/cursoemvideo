c = ('\033[m',      #0 sem cores
'\033[0;31m',       #1 vermelho
'\033[0;32m',       #2 verde
'\033[0;33m',       #3 amarelo
'\033[0;34m',       #4 ciano
'\033[0;35m',       #5 roxo
'\033[0;36m')       #6 azul escuro

def archive():
    while True:
        arquivo = open('namesandages.txt', 'r')
        all_people = arquivo.readlines()
        print('-'*50)
        print(f"{'MAIN MENU':^50}")
        print('-'*50)
        print(f"""{c[3]}1 - {c[6]}See indexed people{c[0]}
{c[3]}2 - {c[6]}Register a new person{c[0]}
{c[3]}3 - {c[6]}Exit the system{c[0]}""")
        try:
            option = int(input(f'{c[2]}Tell me your choice: {c[0]}'))
        except:
                print(f'{c[1]}ERROr! Invalid option.{c[0]}')     
        else:
            if option < 1 or option > 3:
                print(f'{c[1]}ERROr! Invalid option, pick your choice again.{c[0]}')   
            if option == 3:
                print('-'*50)
                print(f'{c[5]}Exiting the system... See you soon!{c[0]}')
                print('-'*50)
                break
            elif option == 2:
                print('-'*50)
                print(f'{"NEW REGISTER":^50}')
                print('-'*50)
                name = str(input('Say me the name of the person: ')).title()
                while True:
                    try:
                        age = int(input('Now the age of that person: '))
                    except:
                        print(f'{c[1]}ERROR! This is not a correct number for age.{c[0]}')
                    else:
                        break
                print(f'{name} was successfully added.')
                arquivo = open('namesandages.txt', 'w', encoding="utf8")
                all_people.append(f'{name:<35}')
                all_people.append(f'{age} years old')
                all_people.append('\n')
                arquivo.writelines(all_people)
            elif option == 1:
                print('-'*50)
                print(f'{"INDEXED PEOPLE":^50}')
                print('-'*50)
                f = open('namesandages.txt', 'r')
                for line in f:
                    print(f'{line}', end='')
