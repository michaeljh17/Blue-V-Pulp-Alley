__author__ = 'sef0097'
from FilerModule.FilerExeption import FilerException
import pickle
import string

class FilerModule(object):

    def export_league_binary_to_fs(self, input_object, file_path="data.pickles"):
        '''
        Function to make a deep copy of an object then pickle it
        Written by Sean
        :param input_object:

        :param file_path:

        :return:
        '''
        with open(file_path, 'wb') as f:
            pickle.dump(lm, f)

    def export_league_text_file(self, input_2d_array):
        '''

        :param input_2d_array:
        :return:
        '''
        print("Hello!")

    # File handling and reading functions:

    def read_file(self, filename):
        data = []
        file_content = open(filename, "r")
        for line in file_content:
            if line != "\n":
                self.get_line_data(line, data)
        file_content.close()
        return data

    @staticmethod
    def get_line_data(line, data):
        # line = line.replace('/', ' ')
        ability_details = []
        for attr in line.split(','):
            # attr = attr.lower() ?
            attr = attr.strip(string.punctuation + string.whitespace)
            ability_details.append(attr)
        data.append(ability_details)
