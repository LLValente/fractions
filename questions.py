import fractions as frac
import pyodbc
import datetime
import os


class Question:
    # Verificar se existe a id na base de dados
    # Coletar dados existentes
    # Alterar dados existentes
    # Registrar dados inexistentes


    def __init__(self, id_question='', question_type=''):

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

                latex_item = "\t\t\t" + r"\item $\frac{" + str(fraction.numerator) + "}{" + str(fraction.denominator) + "}$" + "\n" # ou r"\item \frac{}{} e \frac{}{}***"

                latex_items = latex_items + latex_item

        elif self.double_items == 1:

            for i in range(0, int(len(fractions)/2)):

                latex_item = "\t\t\t" + r"\item $\frac{" + str(fractions[i].numerator) + "}{" + str(fractions[i].denominator) + "}$" + " e " + r"$\frac{" + str(fractions[i + 1].numerator) + "}{" + str(fractions[i + 1].denominator) + "}$" + "\n"

                latex_items = latex_items + latex_item

        if self.ending == '':

            latex_ending = "\t\t" + r"\end{enumerate}"
        
        elif self.ending == r'\n':

            latex_ending = "\t\t" + r"\end{enumerate}" + "\n"

        else:

            pass

        print(latex_header + latex_items_block +  latex_items + latex_ending)

