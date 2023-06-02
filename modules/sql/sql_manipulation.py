import pyodbc

CONNECTION_INFO =   ("Driver={SQL Server};"
                    "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                    "Database=SQL_Exams_DB;")

CONNECTION = pyodbc.connect(CONNECTION_INFO)

CURSOR = CONNECTION.cursor()


class Table:

    def __init__(self, table_name):
    # OK

        self.table_name = table_name
        self.table_data = self.get_table_data()
        self.columns = self.get_columns()

        pass


    def get_columns(self):
        
        command = f"""SELECT * FROM sys.columns WHERE object_id = OBJECT_ID('{self.table_name}')"""

        CURSOR.execute(command)

        rows = CURSOR.fetchall()

        columns = []

        for row in rows:

            columns.append(row[1])

        return columns
    # OK


    def get_table_data(self):


        command = f"""SELECT * FROM {self.table_name}"""

        CURSOR.execute(command)

        rows = CURSOR.fetchall()

        return rows
    # OK


    def print_table(self):
    # Imprimi tabelas com dados
    # TODO: Consertar

        max_iter = len(self.columns) - 1

        for c in range(0, max_iter):

            if c != max_iter:

                print(self.columns[c], end="\t")

                next


            else:

                print(self.columns[c])

        rows = self.table_data

        for row in rows:

            for c in range(0, max_iter):

                if c != max_iter:

                    print(row[c], end="\t")

                    next


                else:

                    print(row[c])

    
class Consultation:

    def __init__(self, id_question):

        self.id = id_question
        self.in_db = self.verify_id()

        if self.in_db:

            self.infos = self.read_question_data()

            self.id_question = self.infos[0]
            self.question_subject = self.infos[1]
            self.question_type = self.infos[2]
            self.question_difficulty = self.infos[3]
            self.question_header = self.infos[4]
            self.pontuation = self.infos[5]
            self.double_items = self.infos[6]
            self.items_number = self.infos[7]
            self.question_ending = self.infos[8]
            self.id_competence = self.infos[9]
            self.register_date = self.infos[10]
            self.register_user = self.infos[11]

        else:

            

            self.infos = None

        if not verify_id():

            action = input('Cadastrar questão? (s ou n):')

            if action == 'y':

                self.sign_in_id()


    def verify_id(self):
    # Verificar existência de uma id no banco de dados

        command = f"""SELECT * FROM Questions"""

        CURSOR.execute(command)

        rows = CURSOR.fetchall()

        for row in rows:

            if self.id in row:

                return True

        return False

    
    def read_question_data(self):
    # Resgatar dados já existentes

        command = f"""SELECT * FROM Questions"""

        CURSOR.execute(command)

        rows = CURSOR.fetchall()

        while True:

            row = CURSOR.fetchone()

            if self.id in row:

                return row


    def sign_in_id(self):
    # Registrar dados não cadastrados

        command = f"""INSERT INTO Questions (id_question, question_subject, question_type, question_difficulty, question_header, pontuation, double_items, items_number, question_ending, id_competence, register_date, register_user)
        VALUES ()"""

        CURSOR.execute(command)


    def print_id_info(self):
    # Imprimi dados da id

        row = self.read_question_data()

        columns_name = get_columns_names("Questions")

        for column in columns_name:

            print(column, end='\t')

        for info in row:

            print(info, end='\t')

