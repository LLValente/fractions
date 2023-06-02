import fractions as frac
import pyodbc
import datetime
import os


def main():

    main_path = "C:\\Users\\lucas\\VSCodeProjects\\TCC_Estácio_git"

    file_path = os.path.join(main_path, 'data\\backup')

    def read_dicts():

        with open(os.path.join(file_path,'original_question_dicts.txt'), mode="r", encoding="utf-8") as file:

            content = ''

            rows = file.readlines()

            for row in rows:

                content = content + row

        return content


    Drawing=    {'id_question': 'fracdraw01',
	            'question_subject': 'Fractions',         #varchar(20) NOT NULL,
	            'question_type': 'Drawing',            #varchar(15) NOT NULL,
	            'question_difficulty': 1,      #int NOT NULL,
	            'question_header': 'Escreva por extenso o nome de cada fração abaixo.',          #varchar(500) NOT NULL,
	            'pontuation': 1.0,               #float NOT NULL,
	            'double_items': 0,             #int NOT NULL,
	            'items_number': 4,             #int NOT NULL,
	            'question_ending': '',          #varchar(8) NOT NULL,
	            'id_competence': 'EF06MA07',            #varchar(10) NOT NULL,
	            'register_date': str(datetime.datetime.now())[:-7],            #datetime NOT NULL,
	            'register_user': os.getlogin()}            #varchar(15) NOT NULL
	
    Reading=    {'id_question': 'fracread01',
	            'question_subject': 'Fractions',         #varchar(20) NOT NULL,
	            'question_type': 'Reading',            #varchar(15) NOT NULL,
	            'question_difficulty': 1,      #int NOT NULL,
	            'question_header': 'Para cada fração a seguir, faça uma representação geométrica.',          #varchar(500) NOT NULL,
        	    'pontuation': 1.0,               #float NOT NULL,
	            'double_items': 0,             #int NOT NULL,
	            'items_number': 6,             #int NOT NULL,
	            'question_ending': '',          #varchar(8) NOT NULL,
	            'id_competence': 'EF06MA07',            #varchar(10) NOT NULL,
	            'register_date': str(datetime.datetime.now())[:-7],            #datetime NOT NULL,
	            'register_user': os.getlogin()}            #varchar(15) NOT NULL
	
    Comparing=  {'id_question': 'fraccomp01',
	            'question_subject': 'Fractions',         #varchar(20) NOT NULL,
	            'question_type': 'Comparing',            #varchar(15) NOT NULL,
	            'question_difficulty': 1,      #int NOT NULL,
	            'question_header': 'Observe as frações em cada item abaixo e assinale $<$, $>$ ou $=$.',          #varchar(500) NOT NULL,
	            'pontuation': 1.5,               #float NOT NULL,
	            'double_items': 1,             #int NOT NULL,
	            'items_number': 6,             #int NOT NULL,
	            'question_ending': '',          #varchar(8) NOT NULL,
	            'id_competence': 'EF06MA07',            #varchar(10) NOT NULL,
	            'register_date': str(datetime.datetime.now())[:-7],            #datetime NOT NULL,
        	    'register_user': os.getlogin()}            #varchar(15) NOT NULL
	
    Conversion= {'id_question': 'fracconv01',
	            'question_subject': 'Fractions',         #varchar(20) NOT NULL,
	            'question_type': 'Conversion',            #varchar(15) NOT NULL,
	            'question_difficulty': 1,      #int NOT NULL,
	            'question_header': 'Encontre a fração geratriz para cada dízima periódica abaixo.',          #varchar(500) NOT NULL,
	            'pontuation': 2.0,               #float NOT NULL,
	            'double_items': 0,             #int NOT NULL,
	            'items_number': 4,             #int NOT NULL,
        	    'question_ending': '',          #varchar(8) NOT NULL,
	            'id_competence': 'EF08MA05',            #varchar(10) NOT NULL,
	            'register_date': str(datetime.datetime.now())[:-7],            #datetime NOT NULL
	            'register_user': os.getlogin()}            #varchar(15) NOT NULL
	
    dicts = [Drawing, Reading, Comparing, Conversion]

    connection_info =   ("Driver={SQL Server};"
                        "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                        "Database=SQL_Exams_DB;")

    connection = pyodbc.connect(connection_info)

    cursor = connection.cursor()

    command = f"""DELETE FROM Questions"""

    cursor.execute(command)

    for dict in dicts:

        command = f"""INSERT INTO Questions(id_question, question_subject, question_type, question_difficulty, question_header, pontuation, double_items, items_number, question_ending, id_competence, register_date, register_user)
        VALUES ('{dict['id_question']}', '{dict['question_subject']}', '{dict['question_type']}', '{dict['question_difficulty']}', '{dict['question_header']}', '{dict['pontuation']}', '{dict['double_items']}', '{dict['items_number']}', '{dict['question_ending']}', '{dict['id_competence']}', '{dict['register_date']}', '{dict['register_user']}')"""

        cursor.execute(command)
        cursor.commit()

    connection.close()


main()