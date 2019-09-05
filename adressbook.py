# Tasks:
'''
1. поместить Фамилию, Имя и Отчество человека в поля lastname, 
firstname и surname соответственно. В записной книжке 
изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
2. привести все телефоны в формат +7(999)999-99-99. 
Если есть добавочный номер, формат будет такой: 
+7(999)999-99-99 доб.9999;
3. объединить все дублирующиеся записи о человеке в одну.
'''
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
res_contacts = []
for elem in contacts_list:
	lastn_patt = re.compile('(^([А-Яа-я])*)(\s)([А-Яа-я])')
	if elem[0] != 'lastname':
		k = ','.join(elem)
		k = re.sub(r"(^([А-Яа-я])*)(\s)([А-Яа-я])", r"\1,\4", k)
		#print('k: ', k)
		elem = k.split(',')
		#print('elem: ', elem)
		res_contacts.append(elem)
#print('=============================')
#pprint(res_contacts)

contacts_list = res_contacts.copy()
res_contacts = []

for elem in contacts_list:
	if elem[0] != 'lastname':
		k = ','.join(elem)
		k = re.sub(r",([А-Яа-я]*)( )([А-Яа-я]*)(,)", r",\1,\3", k)
		#print('k: ', k)
		elem = k.split(',')
		#print('elem: ', elem)
		res_contacts.append(elem)
#print('=============================')
#pprint(res_contacts)

# pattern for phone '\+(\d)(\s*)(\(*)(\d*)(\)*)(\s*)(\d*)(\-*)(\d*)(\-*)(\d*)(\s*)(\(*)((доб.)*)(\s*)(\d*)'

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
