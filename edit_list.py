def show_questions_in_db():
    file = open('questions1.txt', 'r', encoding='utf8')
    temp_list = [q for q in file]
    for i, q in enumerate(temp_list):
        print(str(i) + '. ' + q.rstrip())
        file.close()

def get_questions_in_db():
    file = open('questions1.txt', 'r', encoding='utf8')
    temp_list = [q for q in file]
    file.close()
    return temp_list

def add_to_db():
    q = input('Introduis une nouvelle question: ') + '\n'
    with open('questions1.txt', 'a', encoding='utf8') as f:
        f.write(q)
        f.close()
        show_questions_in_db()


add_to_db()
