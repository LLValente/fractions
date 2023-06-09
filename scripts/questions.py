import os
import sys
import random as rd
import datetime

import pyodbc

import sql_manipulation as sm
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

        fractions = self.items

        latex_question_header = "\t\\item %s \\textbf{(%.1f pnts)}\n\n" % (self.header, self.pontuation)
        latex_items_block = "\t\t\\begin{enumerate}\n"
        latex_items = ''

        if self.double_items == 0:

            for fraction in fractions:

                latex_item = "\t\t\t" "\\item " + f"${fraction.latex_line}$\n"
                latex_items = latex_items + latex_item

        elif self.double_items == 1:

            if self.id_question == "fraccomp01":

                for i in range(0, int(len(fractions)/2)):

                    latex_item = "\t\t\t" + f"\\item ${fractions[i].latex_line} e {fractions[i + 1].latex_line}$\n"

                    latex_items = latex_items + latex_item

            elif self.id_question == "fracarit01":

                operators = ["+", "-", ".", ":", "^"]

                for i in range(0, int(len(fractions)/2)):

                    if operators[i] != "^":

                        latex_item = "\t\t\t" + f"\\item ${fractions[i].latex_line} {operators[i]} {fractions[i + 1].latex_line}$\n"

                        latex_items = latex_items + latex_item

                        continue
                    
                    latex_item = "\t\t\t" + f"\\item $\\left({fractions[i].latex_line}\\right) {operators[i]} {rd.randint(2, 3)}$\n"

                    latex_items = latex_items + latex_item

        latex_question_ending = "\t\t" + "\\end{enumerate}\n\n"

        question_in_latex = latex_question_header + latex_items_block + latex_items + latex_question_ending

        return question_in_latex
