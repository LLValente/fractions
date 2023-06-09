import os
import json
import datetime
import pyodbc

def main():

	connection_info =    ("Driver={SQL Server};"
                        "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                        "Database=SQL_Exams_DB;")

	connection = pyodbc.connect(connection_info)

	cursor = connection.cursor()

	command = f"""DELETE FROM Questions;""" 

	cursor.execute(command)

	directory_path = os.path.dirname(os.path.dirname(__file__))

	json_file = 'questions_backup_data.json' 

	absolute_path = os.path.join(directory_path, 'data', json_file)

	with open(absolute_path, "r", encoding="utf8") as file:

		data = json.load(file)

		for dict_ in data['data']:

			id_question = dict_['id_question']
			question_subject = dict_['question_subject']
			question_type = dict_['question_type']
			question_difficulty = dict_['question_difficulty']
			question_header = dict_['question_header']
			pontuation = dict_['pontuation']
			double_items = dict_['double_items']
			items_number = dict_['items_number']
			question_ending = dict_['question_ending']
			id_competence = dict_['id_competence']
			register_date = str(datetime.datetime.now())[:-7]
			register_user = os.getlogin()

			command = 	f"""INSERT INTO Questions (id_question, question_subject, question_type, question_difficulty, question_header, pontuation, double_items, items_number, question_ending, id_competence, register_date, register_user)
						VALUES ('{id_question}', '{question_subject}', '{question_type}', {question_difficulty}, '{question_header}', {pontuation}, {double_items}, {items_number}, '{question_ending}', '{id_competence}', '{register_date}', '{register_user}')"""
                    
			cursor.execute(command)
			cursor.commit()

			print(f"Question {id_question} inserted!!")


main()