def sort_dict_by_value(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))


my_map= {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
sorted_map = sort_dict_by_value(my_map)
print(sorted_map)
