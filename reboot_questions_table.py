import fractions as frac
import pyodbc
import datetime
import os


def main():

    def read_dicts():

        with open('original_question_dicts.txt', mode="r", encoding="utf-8") as file:

            content = ''

            rows = file.readlines()

            for row in rows:

                content = content + row

        return content


    exec(read_dicts())


    for dict in dicts:

        command = f"""INSERT INTO Questions (id_question, question_subject, question_type, question_difficulty, question_header, pontuation, double_items, items_number, question_ending, id_competence, register_date, register_user)
        VALUES ('{dict['id_question']}', '{dict['question_subject']}', '{dict['question_type']}', '{dict['question_difficulty']}', '{dict['question_header']}', '{dict['pontuation']}', '{dict['double_items']}', '{dict['items_number']}', '{dict['question_ending']}', '{dict['id_competence']}', '{dict['register_date']}', '{dict['register_user']}')"""

        cursor.execute(command)
        cursor.commit()

        sign_in_question(dict)

main()