# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, sep = ","):
    group1 = group1.split(sep)
    group2 = group2.split(sep)

    intersect_sets = list(set(group2).intersection(set(group1)))
    intersect_sets.sort()

    return intersect_sets
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,"|"))