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

            for line in file: 

                decode_text = line.decode('utf-8')
                price = decode_text.split(',')[2]
                if prev_price != price and prev_price != None:
                    indexes[prev_price].append(offset)
                if indexes.get(price) is None: 
                    indexes[price] = [offset]
                prev_price = price
                offset += len(line)

        indexes[prev_price].append(offset)
        indexes['max_offset'] = offset

        with open('index.json', 'w') as file: 
            json.dump(indexes, file, separators=(',', ':'))

    def filter_transaction_with_message(self, file_path, target_message, page, min_offset, max_offset):
        result = []
        skip = -10 * (page - 1)
        with open(file_path, 'rb') as file: 
            file.seek(min_offset)
            current_offset = file.tell()
            while current_offset < max_offset: 
                line = file.readline()
                current_offset += len(line)
                line = line.rstrip()
                line = line.decode('utf-8')
                line = line.split(',')
                message = line[4]

                if skip >= 10:
                    return result 
                if re.search(target_message, message, re.IGNORECASE) is not None:
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