def create_dictionary(sheet_1, sheet_2):
    dictionary = {}
    if len(sheet_1) > len(sheet_2):
        for i in range(len(sheet_1) - len(sheet_2)):
            sheet_2.append(None)

    for i in range(len(sheet_1)):
            dictionary[sheet_1[i]] = sheet_2[i]
    return dictionary

