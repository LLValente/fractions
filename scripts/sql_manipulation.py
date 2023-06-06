import pyodbc

CONNECTION_INFO =   ("Driver={SQL Server};"
                    "Server=DESKTOP-EKI2AGF\SQLEXPRESS;"
                    "Database=SQL_Exams_DB;")

CONNECTION = pyodbc.connect(CONNECTION_INFO)

CURSOR = CONNECTION.cursor()


class Consultation:

    def __init__(self, data_info, data_type = 'id'):

        self.data_info = data_info
        self.infos = self.read_data()
        self.columns = self.get_columns()

        if data_type == 'id':
           
            self.id_question = self.infos[0][0]
            self.question_subject = self.infos[0][1]
            self.question_type = self.infos[0][2]
            self.question_difficulty = self.infos[0][3]
            self.question_header = self.infos[0][4]
            self.pontuation = self.infos[0][5]
            self.double_items = self.infos[0][6]
            self.items_number = self.infos[0][7]
            self.question_ending = self.infos[0][8]
            self.id_competence = self.infos[0][9]
            self.register_date = self.infos[0][10]
            self.register_user = self.infos[0][11]


    def get_columns(self):

        command = f"""SELECT * FROM sys.columns WHERE object_id = OBJECT_ID('dbo.Questions')"""

        CURSOR.execute(command)

        rows = CURSOR.fetchall()

        columns = []

        for row in rows:

            columns.append(row[1])
        
        return columns


    def read_data(self):

        command = f"""SELECT * FROM Questions"""

        CURSOR.execute(command)

        rows = CURSOR.fetchall()

        data_list = []

        for row in rows:

            if self.data_info in row:

                data_list.append(row)

        return data_list


    def print_id_info(self):

        data_list = self.read_data()

        columns_name = self.columns

        for i in range(0, len(data_list)):

            for k in range(0, len(columns_name)):

                print(f"{columns_name[k]}:      {data_list[i][k]}")

            print("\n*********************************************\n")

