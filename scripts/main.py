import sql_manipulation as sqlm
import my_fractions as frac
import periodical_decimal as perd
import operations as op
import questions as qst
import aspose.pdf as ap
import os

def main():

    data_path = os.path.join(os.getcwd(), "data")

    file_path = os.path.join(data_path, "temp.tex")

    subject = "Fractions"

    consult = sqlm.Consultation(subject, data_type="subject")

    qst.begin_document()

    for data in consult.infos:

        quest = qst.Question(data)

        quest.write_question_in_latex()

    qst.end_document()

    options = ap.TeXLoadOptions()

    document = ap.Document(file_path , options)

    document.save("temp.pdf")

    print("Concluído!!!")

main()