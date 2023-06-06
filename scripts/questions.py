import pyodbc
import datetime
import os
import sys

main_path = os.getcwd()

sql_path = os.path.join(main_path, 'modules\\sql')
frac_path = os.path.join(main_path, 'modules\\math')

sys.path.append(sql_path)
import sql_manipulation as sm

sys.path.append(frac_path)
import my_fractions as frac


class Question:

    def __init__(self, question_data):

        self.id_question = question_data[0]
        self.subject = question_data[1]
        self.type = question_data[2]
        self.difficulty = question_data[3]
        self.header = question_data[4]
        self.pontuation = question_data[5]
        self.double_items = question_data[6]
        self.items_number = question_data[7]
        self.ending = question_data[8]
        self.id_competence = question_data[9]
        self.register_date = str(question_data[10])
        self.register_user = question_data[11]

        self.items = self.items()


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

    
    def print_question_in_latex(self):

        fractions = self.items

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

        print(latex_header + latex_items_block +  latex_items + "\t\t" +  r"\end{enumerate}", end='\n')


    def write_question_in_latex(self):

        data_path = os.path.join(os.getcwd(), "data")

        file_path = os.path.join(data_path, "temp.tex")

        fractions = self.items

        latex_question_header = "\t" + r"\item " + self.header + r" \textbf{(" + str(self.pontuation) + r" pontos)}" + "\n"
        latex_items_block = "\t\t" + r"\begin{enumerate}" + "\n"
        latex_items = ''

        if self.double_items == 0:

            for fraction in fractions:

                latex_item = "\t\t\t" + r"\item $\frac{" + str(fraction.numerator) + "}{" + str(fraction.denominator) + "}$\n"

                latex_items = latex_items + latex_item

        elif self.double_items == 1:

            if self.id_question == "fraccomp01":

                for i in range(0, int(len(fractions)/2)):

                    latex_item = "\t\t\t" + r"\item $\frac{" + str(fractions[i].numerator) + "}{" + str(fractions[i].denominator) + "}$" + \
                    " e " + r"$\frac{" + str(fractions[i + 1].numerator) + "}{" + str(fractions[i + 1].denominator) + "}$" + "\n"

                    latex_items = latex_items + latex_item

            else:

                operators = ["+", "-", ".", ":"]

                for i in range(0, int(len(fractions)/2)):

                    latex_item = "\t\t\t" + r"\item $\frac{" + str(fractions[i].numerator) + "}{" + str(fractions[i].denominator) + "}$" + \
                    f" {operators[i]} " + r"$\frac{" + str(fractions[i + 1].numerator) + "}{" + str(fractions[i + 1].denominator) + "}$" + "\n"

                    latex_items = latex_items + latex_item

        latex_question_ending = "\t\t" + r"\end{enumerate}" + "\n"

        with open(file_path, "a+") as ltx_file:

            ltx_file.write(latex_question_header + latex_items_block + latex_items + latex_question_ending)


def begin_document():

    data_path = os.path.join(os.getcwd(), "data")

    file_path = os.path.join(data_path, "temp.tex")

    file = open(file_path, "w")

    document_beggining = r"\documentclass{article}" + "\n" + r"\usepackage{graphicx}" + "\n" + r"\usepackage[brazilian]{babel}" + "\n" + r"\title{Avaliação}" \
    + "\n" + r"\author{Lucas L. Valente}" + "\n" + r"\date{" + str(datetime.date.today()) + "}" + "\n\n" + r"\begin{document}" + "\n\n" + r"\maketitle" + "\n\n" + r"\newpage" + "\n\n" + \
    r"\begin{enumerate}" + "\n"

    file.write(document_beggining)

    file.close()


def end_document():

    data_path = os.path.join(os.getcwd(), "data")

    file_path = os.path.join(data_path, "temp.tex")
    
    file = open(file_path, "a+")

    document_ending = r"\end{enumerate}" + "\n\n" + r"\end{document}"

    file.write(document_ending)

    file.close()

