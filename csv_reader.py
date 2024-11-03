import csv
import json
import re

class CSV_Reader(object):
    reader = None
    def __init__(self):
        self.reader = csv.reader

    def create_indexes_file(self, file_path):
        with open(file_path, 'rb') as file:
            offset = 0
            indexes = dict()
            prev_price = None

            # Loop through each line, if the credit not exist in the indexes dict, add it to the dict
            # Store offset as an array, first element is min_offset, second element is max_offset
            for line in file: 
                decode_text = line.decode('utf-8')
                credit = decode_text.split(',')[2]

                if prev_price != credit and prev_price != None:
                    indexes[prev_price].append(offset)
                if indexes.get(credit) is None: 
                    indexes[credit] = [offset]
                prev_price = credit
                offset += len(line)

        indexes[prev_price].append(offset)
        indexes['max_offset'] = offset # offset of the last line in the csv file

        with open('index.json', 'w') as file: 
            json.dump(indexes, file, separators=(',', ':'))

    def filter_transaction_with_message(self, file_path, target_message, page, min_offset, max_offset):
        result = []
        skip = -10 * (page - 1) # Split the result into each page, each page has 10 transactions

        with open(file_path, 'rb') as file: 
            # Jump to position of first transaction match by credit
            file.seek(min_offset) 
            current_offset = file.tell()
            # If current_offset > max_offset, 
            # it means all transactions match by credit have been checked, stop now (don't need to read to the end of the file)
            while current_offset < max_offset: 
                line = file.readline()
                current_offset += len(line)
                line = line.rstrip()
                line = line.decode('utf-8')
                line = line.split(',')
                message = line[4]

                if skip >= 10:
                    return result 
                # Check if detail of transaction match with the message
                if re.search(target_message, message, re.IGNORECASE) is not None:
                    # Only add transaction to the result if skip enough
                    if skip >= 0:
                        transaction = {
                            "date": line[0],
                            'transaction_id': line[1],
                            "credit": line[2],
                            'debit': line[3], 
                            'detail': line[4]
                        }
                        result.append(transaction)
                    skip += 1
        return result