
from libs.math_lib import MathLib 


def main_method():

    ml = MathLib()

    my_values = {
        "value1": 7,
        "value2": 4,
        "value3": 5,
        "value4": 3
    }

    user_values = ()
    print("\n\n Enter some values separeted by commer\n")
    try:
        user_values = input("\n\n Enter some values:  ")
    except Exception as exec_error:
        print(exec_error)
        exit(0)
    else:
        # print(type(user_values), '\n Value: ', user_values)
        user_values = user_values.strip().split(',')

    result = ml.sum_dict(my_values)
    print("\n\n MY VALUES: {}".format(result))

    user_values_help = list(user_values)
    user_values.clear()
    for value in user_values_help:
        user_values.append(int(value))   
    
    result = ml.sum_list(user_values)
    print("\n\n USER VALUES: {}".format(result))

    print("\n\n\n")


if __name__=='__main__':
    main_method()
