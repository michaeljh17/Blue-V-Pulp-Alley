__author__ = 'sef0097'
from FilerModule.FilerExeption import FilerException
#from league_model import LeagueModel
import pickle
import string
import os

class FilerModule(object):

    def export_league_binary_to_fs(self, input_object, directory='', file_name='data.pickles'):
        '''
        #Function to make a deep copy of an object then pickle it
        #Written by Sean
        #:param input_object:
        object to be pickled, should be a league object
        #:param file_path:
        #path to file including filename
        #:return:
        #void
        '''
        if not os.path.exists(directory) and directory != '':
            os.makedirs(directory)
            file_path = directory + "/" + file_name
        else:
            file_path = file_name

        print(input_object)
        print(input_object._my_league)
        print(dir(input_object))
        print(input_object.__dict__)
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
