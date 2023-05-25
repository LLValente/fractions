import fractions as frac

Questions_dict = {'Drawing': {'question_header': '\\item Para cada fração a seguir, faça uma representação geométrica.',
                            'pontuation': '\\textbf\{(1,0 pnts)\}',
                            'items_number': 5,
                            'double_items': False,
                            'item_type': False,
                            'level': 'easy',
                            'question_ending': ''},

                'Reading':  {'question_header': '\\item Escreva por extenso o nome de cada fração abaixo.',
                            'pontuation': '\\textbf\{(1 pnts)\}',
                            'items_number': 6,
                            'double_items': False,
                            'item_type': 'mixed',
                            'level': 'easy',
                            'question_ending': ''},

                'Comparing':{'question_header': '\\item Observe as frações em cada item abaixo e assinale <, > ou =.',
                            'pontuation': '\\textbf\{(1,5 pnts)\}',
                            'items_number': 6,
                            'double_items': True,
                            'item_type': 'mixed',
                            'level': 'easy',
                            'question_ending': ''},

                'Conversion':{'question_header': '.',
                            'pontuation': '\\textbf\{(1,5 pnts)\}',
                            'items_number': 6,
                            'double_items': True,
                            'item_type': 'mixed',
                            'level': 'easy',
                            'question_ending': ''},

                '':         {}}


class Question:

    def __init__(self, question_type):

        #self.start = QUESTIONS_START[self.type]
        #self.end = QUESTIONS_START[self.type]
        self.type = question_type
        self.items = self.items(Questions_dict[self.type][items_number])
        self.answears = ''



    def items(self, items_numbers):
    # Cria as fraçãoes a serem utilizadas em uma questão (em alguns tipos de questões, deverá construir o dobro do esperado)

        fractions = []

        i = 1

        while i <= items_numbers:

            fraction = frac.Fraction()
            fractions.append(fraction)

            i += 1

        return fractions

    
    def write(self):
    # Deverá escrever a questão em LaTeX

        pass
