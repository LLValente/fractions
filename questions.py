import fractions as frac
import pyodbc
import datetime
import os


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


def sign_in_question(dict):

    conection_info = (
        "Driver={SQL Server};"
        "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
        "Database=SQL_Exams_DB;"    
    )

    conection = pyodbc.connect(conection_info)

    cursor = conection.cursor()

    command = f"""INSERT INTO Questions (id_question, question_subject, question_type, question_difficulty, question_header, pontuation, double_items, items_number, question_ending, id_competence, register_date, register_user)
    VALUES ('{dict['id_question']}', '{dict['question_subject']}', '{dict['question_type']}', '{dict['question_difficulty']}', '{dict['question_header']}', '{dict['pontuation']}', '{dict['double_items']}', '{dict['items_number']}', '{dict['question_ending']}', '{dict['id_competence']}', '{dict['register_date']}', '{dict['register_user']}')"""

    cursor.execute(command)
    cursor.commit()