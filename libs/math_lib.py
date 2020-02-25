""" I AM BANCH: master """

class MathLib(object):

    def sum_dict(self, dict_values):
        total_sum = 0
        if dict_values:
            for key in dict_values.keys():
                total_sum += dict_values[key]
        else:
            print("\n\n INVALID DICTIONARY")
    
        return total_sum


    def sum_list(self, list_values):
        total_sum = 0
        for value in list_values:
            total_sum += value

        return total_sum

