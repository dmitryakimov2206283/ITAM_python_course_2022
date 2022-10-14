def key_difference(dict1:dict, dict2:dict) -> dict:
    result_dict = {}
    
    for key, value in dict1.items():
        if key in dict2:
            if value == dict2[key]:
                result_dict[key] = "equal"
            else:
                result_dict[key] = "changed"
        else:
            result_dict[key] = "deleted"

    for key in dict2:
        if key not in result_dict:
            result_dict[key] = "added"

    return result_dict

dict1 = {"a":"b", "b":"a"}
dict2 = {"a":"b", "b":"a", "c": "a"}
print(key_difference(dict1, dict2))

dict1 = {"a":"b", "b":"a",  "c": "a"}
dict2 = {"a":"b", "b":"a", "d":"a"}
print(key_difference(dict1, dict2))
