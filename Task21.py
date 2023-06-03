# Задача №21. Напишите программу для печати всех уникальных значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005"}, {"V":" S009 "}, {"VIII":" S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'} 
# Примечание: Список словарей задан изначально. Пользователь его не вводит 

list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
result = []

for i in range(len(list_dict)):
    for value in list_dict[i]:
        result.append(list_dict[i][value].strip())

print (set(result))