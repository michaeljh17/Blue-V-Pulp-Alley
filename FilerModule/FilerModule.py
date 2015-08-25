# __author__ = 'sef0097'
from FilerModule.FilerExeption import FilerException
# from league_model import LeagueModel
import pickle
import string
import os


class FilerModule(object):

    def export_league_binary_to_fs(self, input_object, directory='',
                                   file_name='data.pickles'):
        '''
        #Function to make a deep copy of an object then pickle it
        #Written by Sean
        #:param input_object:
        object to be pickled, should be a league object
        #:param directory:
        #path to file excluding filename
        #:param file_name:
        #filename to be used
        #:return:
        #void
        '''
        if not os.path.exists(directory) and directory != '':
            os.makedirs(directory)
            file_path = directory + "/" + file_name
        elif os.path.exists(directory) and directory != '':
            file_path = directory + "/" + file_name
        else:
            file_path = file_name

        with open(file_path, 'wb') as f:
            pickle.dump(input_object, f)

    def import_binary_league(self, directory='', file_name='data.pickles'):
        '''
        #Function to bring back a league from a binary pickle file
        #written by Sean
        '''

        if directory != '':
            file_path = directory + "/" + file_name
        else:
            file_path = file_name

        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                output = pickle.load(f)
            return output

        return None

    # File reading functions:

    def read_file(self, filename):
        """
        Written by MH
        This method will read data from a file
        :param filename: filepath of the file to be read
        :return: The data obtained from the file
        """
        data = []
        try:
            with open(filename, 'r') as file_content:
                for line in file_content:
                    if line != "\n":
                        self.get_line_data(line, data, ',', False)
            return data
        except FileNotFoundError as e:
            print("Error loading a file: " + filename)
            return None

    @staticmethod
    def get_line_data(line, data, separator, get_punct_ws_bool):
        """
        Written by MH
        This method will obtain delimiter-separated values from a string.
        :param line: a string
        :param data: a list
        :param separator: the delimiter to use when obtaining strings from
        the line
        :param get_punct_ws_bool: A boolean value which will indicate whether
        to include punctuation and whitespace in the strings which are obtained
        :return: Although there are no values which are returned, the method
        will append the strings obtained from each line to the list which is
        passed into this method.
        """
        strings_obtained = []
        for attr in line.split(separator):
            if not get_punct_ws_bool:
                attr = attr.strip(string.punctuation + string.whitespace)
            strings_obtained.append(attr)
        data.append(strings_obtained)
