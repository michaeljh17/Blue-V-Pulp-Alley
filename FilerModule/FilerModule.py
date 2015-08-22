__author__ = 'sef0097'
from FilerModule.FilerExeption import FilerException
import pickle

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
        Print("Hello!")