'''
   Flatten an arbitrary nested array
   [[1,2,[3]],4] -> [1,2,3,4]
'''

def flat(array):
    '''flatten a nested array '''

    if not array:
        return
    flattened_list = []

    for element in array:
        if isinstance(element, (tuple, list)):
            if not element:
                continue
            flattened_list.extend(flat(element))
        else:
            flattened_list.append(element)

    return flattened_list
