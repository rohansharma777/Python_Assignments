l1 = [x for x in range(1, 11)]
l2 = [x for x in range(10, 101, 10)]
l3 = ['Django', 'Flask', 'Python', 'string', 'function', 'classes']
l1 = [x for x in range(1, 11)]
l1 = [l1 * 2]
l5 = l1
main_list = []
main_list.append(l1 + l2 + l3 + l5)
print(main_list)
