import datetime

class Evalu:

    def __init__(self, title='Titre', eval_type='CE', group='5 Handel'):
        self.created = datetime.datetime.now()
        self.title = title
        self.eval_type = eval_type
        self.group = group
        self.questions = []
        self.deleted_questions = []

    def print_questions(self):
        print(self.get_title() + ': ')
        for i, q in enumerate(self.questions):
            print(str(i) + ". " + q)
        print('#' * 50)

    def get_title(self):
        return self.title

    def get_question(self, idx):
        return self.questions[idx]

    def add_question(self):
        q = input('Question à ajouter: ')
        self.questions.append(q)

    def add_question_at_index(self):
        q = input('Question à ajouter: ')
        idx = int(input('Ajoute la question à l\'index #: '))
        self.questions.insert(idx, q)

    def edit_title(self):
        temp = self.get_title()
        print('Change titre: ' + temp)
        temp2 = input('Nouveau titre: ')
        self.title = temp2

    def edit_question(self, idx):
        temp = self.get_question(idx)
        print('Modifie cette question: ' + temp)
        temp2 = input('Modifie en: ')
        self.questions[idx] = temp2

    def remove_question(self):
        self.print_questions()
        i = int(input('Efface question #: '))
        self.deleted_questions.append(self.questions.pop(i))


eval = Evalu()

eval.add_question_number_from_df()
eval.print_questions()
