data_structure = [[1, 2, 3],  {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):
    summa=0

    # print(data_structure)
    # print(type(12data_structure))
    # a=isinstance(data_structure, int)
    # print (a)
    # print("summ=", summa)
    # print()


    if isinstance(data_structure,(int, float)):
        summa+=data_structure
    elif isinstance(data_structure,str):
        summa+=len(data_structure)

    elif isinstance(data_structure,(list, tuple, set)):
        for i in data_structure:
            # calculate_structure_sum(i)
            # print(calculate_structure_sum(i))
            summa+=calculate_structure_sum(i)

    # elif isinstance(data_structure,tuple):
    #     for i in data_structure:
    #         # calculate_structure_sum(i)
    #         # print(calculate_structure_sum(i))
    #         summa += calculate_structure_sum(i)
    #
    #
    # elif isinstance(data_structure,set):
    #     for i in data_structure:
    #         calculate_structure_sum(i)
    #         summa += calculate_structure_sum(i)

    elif isinstance(data_structure,dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)

    # print("SUMMA=",summa, data_structure, type(data_structure))
    return summa




result = calculate_structure_sum(data_structure)
print(result)

