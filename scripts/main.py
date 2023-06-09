import os
import datetime
import sql_manipulation as sqlm
import my_fractions as frac
import periodical_decimal as perd
import operations as op
import questions as qst
import aspose.pdf as ap

SUBJECT = "Fractions"

def main():

    data_path = os.path.join(os.getcwd(), "data")

    file_path = os.path.join(data_path, "temp.tex")

    consult = sqlm.Consultation(SUBJECT, data_type="subject")

    begin_document()

    for data in consult.infos:

        quest = qst.Question(data)

        quest.write_question_in_latex()

    end_document()

    print("Concluído!!!")


def begin_document():

    data_path = os.path.join(os.getcwd(), "exams")

    file_path = os.path.join(data_path, f"Avaliação - {SUBJECT} - [{str(datetime.date.today())}].tex")

    file = open(file_path, "w", encoding="UTF-8")

    document_beggining = "\\documentclass{article}\n\n\\usepackage{graphicx}\n\\usepackage[brazilian]{babel}\n\n\\title{Avaliação}\n\\author{Lucas L. Valente}\
        \n\\date{%s}\n\n\\begin{document}\n\maketitle\n\\newpage\n\n\\begin{enumerate}\n" % (str(datetime.date.today()))

    file.write(document_beggining)

    file.close()


def end_document():

    data_path = os.path.join(os.getcwd(), "exams")

    file_path = os.path.join(data_path, f"Avaliação - {SUBJECT} - [{str(datetime.date.today())}].tex")
    
    file = open(file_path, "a+", encoding="UTF-8")

    document_ending = "\\end{enumerate}\n\\end{document}"

    file.write(document_ending)

    file.close()


main()

