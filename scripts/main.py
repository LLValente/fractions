import os
import datetime

import aspose.pdf as ap

import sql_manipulation as sqlm
import my_fractions as frac
import periodical_decimal as perd
import operations as op
import questions as qst


SUBJECT = "Fractions"

TODAY = str(datetime.date.today())
NOW = str(datetime.datetime.now())[11:19].replace(":", "-")
FILE_NAME = f"Avaliação de {SUBJECT} (Data {TODAY} # Hora {NOW}).tex"

ABS_PATH = os.path.dirname(os.path.dirname(__file__))
FILE_PATH = os.path.join(ABS_PATH, "exams", FILE_NAME)

def main():

    consult = sqlm.Consultation(SUBJECT, data_type="subject")

    begin_document()

    with open(FILE_PATH, "a+", encoding="UTF-8") as latex_file:

        for data in consult.infos:

            quest = qst.Question(data)

            question_to_be_writted = quest.write_question_in_latex()

            latex_file.write(question_to_be_writted)

    end_document()

    print("Concluído!!!")


def begin_document():
    
    file = open(FILE_PATH, "w", encoding="UTF-8")

    document_beggining = "\\documentclass{article}\n\n\\usepackage{graphicx}\n\\usepackage[brazilian]{babel}\n\n\\title{Avaliação}\n\\author{Lucas L. Valente}\
        \n\\date{%s}\n\n\\begin{document}\n\maketitle\n\\newpage\n\n\\begin{enumerate}\n" % (str(datetime.date.today()))

    file.write(document_beggining)

    file.close()


def end_document():
    
    file = open(FILE_PATH, "a+", encoding="UTF-8")

    document_ending = "\\end{enumerate}\n\\end{document}"

    file.write(document_ending)

    file.close()


main()

