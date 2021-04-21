import json
import random

class PreProcess:
    def __init__(self):
        self.File_list = []
        self.final_list = []
        pass

    def filter_txt(self, path, db_name, start_idx, jump_idx):
        self.load_txt_2_list(path)
        idx = start_idx
        sz = len(self.File_list)
        while idx < sz:
            self.final_list.append(self.File_list[idx].lower())
            # print(self.File_list[idx].lower())
            idx += jump_idx
        self.safe_json_DB(db_name)

    def load_txt_2_list(self, path):
        with open(path, "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                self.File_list.append(stripped_line)
                # print(stripped_line)

    def safe_json_DB(self, db_name):
        with open('JsonDB/'+db_name + '.json', 'w') as f:
            json.dump(self.final_list, f)

    def get_list(self):
        return self.final_list

