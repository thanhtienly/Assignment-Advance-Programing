import pandas as pd
from csv_reader import CSV_Reader


def create_sorted_file(file_path, file_name):
    data = pd.read_csv(file_path)
    data = data.sort_values(by=["credit"])
    
    data.to_csv(file_name, encoding='utf-8', index = False, header= False)

def create_index_file(file_path):
    csv_reader = CSV_Reader()

    csv_reader.create_indexes_file(file_path)


def migrate():
    create_sorted_file('./chuyen_khoan.csv', 'sorted_transactions.csv')
    create_index_file('./sorted_transactions.csv')
    

migrate()