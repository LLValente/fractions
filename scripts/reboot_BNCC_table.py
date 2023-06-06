import os
import json
import datetime
import pyodbc


def main():

    directory_path = os.path.dirname(os.path.dirname(__file__))

    json_files = ['BNCC_EF_backup_data.json', 'BNCC_EM_backup_data.json']

    connection_info =    ("Driver={SQL Server};"
                        "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                        "Database=SQL_Exams_DB;")

    connection = pyodbc.connect(connection_info)

    cursor = connection.cursor()

    command = f"""ALTER TABLE Questions DROP CONSTRAINT fk_id_competence;
    ALTER TABLE Exams DROP CONSTRAINT fk_id_question;
    ALTER TABLE Exams DROP CONSTRAINT fk_id_competence2;"""

    cursor.execute(command)

    command = f"""DELETE FROM BNCC;""" 

    cursor.execute(command)

    for json_file in json_files:

        absolute_path = os.path.join(directory_path, 'data', json_file)

        with open(absolute_path, "r", encoding="utf8") as file:

            data = json.load(file)

            for dict_ in data['data']:

                if json_file == "BNCC_EF_backup_data.json":

                    id_competence = dict_['HABILIDADES'][1:9]
                    school_year = 'EF0' + dict_['ANO/FAIXA'][0]
                    theme = dict_['UNIDADES TEMÁTICAS']
                    competence_description = dict_['HABILIDADES'][11:]
                    register_date = str(datetime.datetime.now())[:-7]
                    register_user = os.getlogin()

                elif json_file == "BNCC_EM_backup_data.json":

                    id_competence = dict_['Cód. Hab']
                    school_year = 'EF0F'
                    theme = 'None'
                    competence_description = dict_['HABILIDADES']
                    register_date = str(datetime.datetime.now())[:-7]
                    register_user = os.getlogin()
                
                command = f"""INSERT INTO BNCC (id_competence, school_year, theme, competence_description, register_date, register_user)
                VALUES ('{id_competence}', '{school_year}', '{theme}', '{competence_description}', '{register_date}', '{register_user}')"""
                    
                cursor.execute(command)
                cursor.commit()

    command =   f"""ALTER TABLE Questions ADD CONSTRAINT fk_id_competence FOREIGN KEY (id_competence) REFERENCES BNCC (id_competence);
                ALTER TABLE Exams ADD CONSTRAINT fk_id_question FOREIGN KEY (id_question) REFERENCES Questions (id_question);
                ALTER TABLE Exams ADD CONSTRAINT fk_id_competence2 FOREIGN KEY (id_competence) REFERENCES BNCC (id_competence)"""

    cursor.execute(command)
    cursor.commit()



    connection.close()

main()