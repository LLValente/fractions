import fractions as frac
import pyodbc
import datetime
import os


class Question:
    # Verificar se existe a id na base de dados
    # Coletar dados existentes
    # Alterar dados existentes
    # Registrar dados inexistentes


    def __init__(self, id_question, question_type=''):

        conection_info =    ("Driver={SQL Server};"
                            "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                            "Database=SQL_Exams_DB;")

        global conection

        conection = pyodbc.connect(conection_info)

        cursor = conection.cursor()

        cursor.execute("SELECT * FROM Questions")

        while True:

            row = cursor.fetchone()

            if id_question in row:

                break

        self.id, self.subject, self.type, self.difficulty, self.header, self.pontuation, self.double_items, self.items_number, self.ending, self.id_competence = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]
        
        self.info = f"""id:   {self.id}\nsubject:    {self.subject}\ntype:   {self.type}\ndifficulty: {self.difficulty}\nheader: {self.header}\npontuation: {self.pontuation}\ndouble items:   {self.double_items}\nitems number:   {self.items_number}\nending: {self.ending}\ncompetence: {self.id_competence}"""

        print(self.info)


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

        if self.double_items == 0:

            for fraction in fractions:

                latex_item = "\t\t\t" + r"\item $\frac{" + str(fraction.numerator) + "}{" + str(fraction.denominator) + "}$\n"

                latex_items = latex_items + latex_item

        elif self.double_items == 1:

            for i in range(0, int(len(fractions)/2)):

                latex_item = "\t\t\t" + r"\item $\frac{" + str(fractions[i].numerator) + "}{" + str(fractions[i].denominator) + "}$" + " e " + r"$\frac{" + str(fractions[i + 1].numerator) + "}{" + str(fractions[i + 1].denominator) + "}$" + "\n"

                latex_items = latex_items + latex_item

        if self.ending != '' and self.ending != r'\n':

            latex_ending = "\t" + self.ending + "\n\t\t" + r"\end{enumerate}"
        
        elif self.ending == r'\n':

            latex_ending = "\t\t" + r"\end{enumerate}" + "\n"

        else:

            pass

        print(latex_header + latex_items_block +  latex_items + latex_ending)


def register_question():

    cursor = conection.cursor()

    command =   f"""ALTER TABLE Questions DROP CONSTRAINT fk_id_competence;
                ALTER TABLE Exams DROP CONSTRAINT fk_id_question;
                ALTER TABLE Exams DROP CONSTRAINT fk_id_competence2;

                INSERT INTO Questions(id_question, question_subject, question_type, question_difficulty, question_header, pontuation, double_items, items_number, question_ending, id_competence, register_date, register_user)
                VALUES ('{dict['id_question']}', '{dict['question_subject']}', '{dict['question_type']}', '{dict['question_difficulty']}', '{dict['question_header']}', '{dict['pontuation']}', '{dict['double_items']}', '{dict['items_number']}', '{dict['question_ending']}', '{dict['id_competence']}', '{dict['register_date']}', '{dict['register_user']}')

                ALTER TABLE Questions ADD CONSTRAINT fk_id_competence FOREIGN KEY (id_competence) REFERENCES BNCC (id_competence)
                ALTER TABLE Exams ADD CONSTRAINT fk_id_question FOREIGN KEY (id_question) REFERENCES Questions (id_question)
                ALTER TABLE Exams ADD CONSTRAINT fk_id_competence2 FOREIGN KEY (id_competence) REFERENCES BNCC (id_competence)"""

    cursor.execute(command)

    pass