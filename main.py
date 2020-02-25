
from libs.math_lib import MathLib 


def main_method():

    ml = MathLib()

    my_values = {
        "value1": 7,
        "value2": 4,
        "value3": 5,
        "value4": 3
    }

    user_values = {}
    try:
        user_values = input("\n\n Enter some values:  ")
    except Exception as exec_error:
        print(exec_error)
        exit(0)
    else:
        # print(type(user_values), '\n Value: ', user_values)
        user_values = user_values.strip().split(',')
        print(user_values)

    result = ml.sum_dict(my_values)
    print(result)



if __name__=='__main__':
    main_method()


