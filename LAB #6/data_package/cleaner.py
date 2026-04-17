def remove_duplicates(data_list):
    newList = []
    for item in data_list:
        if item not in newList:
            newList.append(item)
    return newList

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]
