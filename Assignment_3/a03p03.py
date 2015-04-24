l_i_s_t = [1, 2, 3, 4, 'Rohan', 'Guitar', 'All of me', {'movie': [
    'FF6', 'FF7'], 'actors': ['Paul', 'Vin', 'Ludacris']}, [777, 'ios', 'android']]

for each_item in l_i_s_t:
    if type(each_item) == dict:
        print(each_item.keys())
        print(each_item.values())
