import fractions as frac
import pyodbc
import datetime
import os


class Question:
    # Alterar questões existentes


    def __init__(self, id_question='', question_type=''):

        def verify_id(id_question):

            conection_info =    ("Driver={SQL Server};"
                                "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                                "Database=SQL_Exams_DB;")

            conection = pyodbc.connect(conection_info)

            cursor = conection.cursor()

            cursor.execute("SELECT * FROM Questions;")

            rows = cursor.fetchall()

            for row in rows:

                if id_question in row:

                    self.id = row[0]
                    self.subject = row[1]
                    self.type = row[2]
                    self.difficulty = row[3]
                    self.header = row[4]
                    self.pontuation = row[5]
                    self.double_items = row[6]
                    self.items_number = row[7]
                    self.ending = row[8]
                    self.id_competence = row[9]

                    return True

            return False


        def register_question(self, question_type=''):

            if question_type == '':

                question_type = input('Qual o tipo da questão?')

            self.id = 'frac' + question_type.lower()[-1:-4]
            self.subject = 'Fractions'
            self.type = question_type
            self.difficulty = input('Qual o nível de dificuldade da questão? (1, 2 ou 3):')
            self.header = input('Qual o cabeçalho da questão? (Em string):')
            self.pontuation = input('Quanto vale a questão? (Em decimais):')
            self.double_items = input('Duplicar items? (0 ou 1):')
            self.items_number = input('Qual a quantidade de items na questão? (Em int):')
            self.ending = input('Qual o final da questão? (Em string):')
            self.id_competence = input('Qual a competência da BNCC? (Em string):')

            conection_info =    ("Driver={SQL Server};"
                                "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                                "Database=SQL_Exams_DB;")

            conection = pyodbc.connect(conection_info)

            cursor = conection.cursor()

            command = f"""INSERT INTO Questions (id_question, question_subject, question_type, question_difficulty, question_header, pontuation, double_items, items_number, question_ending, id_competence, register_date, register_user)
            VALUES ('{self.id}', '{self.subject}', '{self.type}', {self.difficulty}, '{self.header}', {self.pontuation}, {self.double_items}, {self.items_number}, '{self.ending}', '{self.id_competence}', '{str(datetime.datetime.now())[:-7]}', '{os.getlogin()}')"""

            cursor.execute(command)
            cursor.commit()


        if not verify_id(id_question):

            register_question(question_type)


    def items(self):

        if self.double_items == 1:

            items_number = 2 * self.items_number

        elif self.double_items == 0:

            items_number = self.items_number

        fractions = []

        i = 1

        while i <= items_number:

            fraction = frac.Fraction()
            fractions.append(fraction)

            i += 1

        return fractions

    
    def write_question_in_latex(self):

        fractions = self.items()

        latex_header = "\t" + r"\item " + self.header + r" \textbf{(" + str(self.pontuation) + r" pontos)}" + "\n"
        latex_items_block = "\t\t" + r"\begin{enumerate}" + "\n"
        latex_items = ''

        for fraction in fractions:

            latex_item = "\t\t\t" + r"\item $\frac{" + str(fraction.numerator) + "}{" + str(fraction.denominator) + "}$" + "\n" # ou r"\item \frac{}{} e \frac{}{}***"

            latex_items = latex_items + latex_item

        if self.ending == '':

            latex_ending = "\t\t" + r"\end{enumerate}"
        
        else:

            latex_ending = "\t" + self.ending + "\n\t\t" + r"\end{enumerate}"

        print(latex_header + latex_items_block +  latex_items + latex_ending)

