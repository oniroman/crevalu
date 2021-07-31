import sys, time
from evalu import Evalu


evalus = []


def startmenu():
    print()
    stars = '*' * 50
    print(stars)
    print('******************** CREVALU *********************')
    print(stars)
    print('''
    1. LIST of evalu
    2. ADD new evalu
    3. LOAD/EDIT evalu
    4. REMOVE an evalu
    X. QUIT
    ''')
    print(stars)
    choice = input('1/2/3/4/X ? ')
    if choice == '1':
        listmenu()
    elif choice == '2':
        add()
        startmenu()
    elif choice == '3':
        pass
    elif choice == '4':
        remove()
        startmenu()
    elif choice == 'X':
        quit()
    else:
        print('Invalid choice... Restarting ...')
        time.sleep(3)
        startmenu()

def listmenu():
    print('******************** CREVALU *********************')
    print('''
List of evalu:
            
    ''')
    if len(evalus) == 0:
        print('Aucune evalu!')
        time.sleep(3)
        startmenu()
    for i, l in enumerate(evalus):
        print(str(i) + ' - ' + l.title)
        time.sleep(1)


def add():
    title = input('Titre ? ')
    eval_type = input('Type d\'évaluation? ')
    klas = input('Classe(s) ? ')
    ev = Evalu(title, eval_type, klas)
    print(len(evalus))
    evalus.append(ev)

def remove():
    pass

def quit():
    print('Quitting...')
    time.sleep(5)
    sys.exit()


startmenu()


