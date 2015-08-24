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
        """
        This method will read data from a file
        :param filename: filepath of the file to be read
        :return: The data obtained from the file
        """
        data = []
        file_content = open(filename, "r")
        for line in file_content:
            if line != "\n":
                self.get_line_data(line, data)
        file_content.close()
        return data

    @staticmethod
    def get_line_data(line, data):
        """
        This method will obtain comma-separated values from a string.
        :param line: a string
        :param data: a list
        :return: Although there are no values which are returned, the method
        will append the strings obtained from each line to the list which is
        passed into this method.
        """
        csv_strings = []
        for attr in line.split(','):
            attr = attr.strip(string.punctuation + string.whitespace)
            csv_strings.append(attr)
        data.append(csv_strings)
