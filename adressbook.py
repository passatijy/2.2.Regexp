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
#print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

def my_replace(srch_pattrn, rpl_pattrn, mylist):
	res_contacts = []
	for elem in mylist:
		if elem[0] != 'lastname':
			k = ','.join(elem)
			k = re.sub(srch_pattrn, rpl_pattrn, k)
			elem = k.split(',')
			res_contacts.append(elem)
	return res_contacts

def my_uniq(mylist):
	res_contacts = []
	for elem in mylist:
		for 
		pass
	return res_contacts

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)


if __name__ == '__main__':
	print(contacts_list)
	# first call r"(^([А-Яа-я])*)(\s)([А-Яа-я])", r"\1,\4", k
	rename = my_replace(
		r"(^([А-Яа-я])*)(\s)([А-Яа-я])"
		, r"\1,\4"
		, contacts_list)
	# second call r",([А-Яа-я]*)( )([А-Яа-я]*)(,)", r",\1,\3", k
	rename1 = my_replace(
		r",([А-Яа-я]*)( )([А-Яа-я]*)(,)"
		, r",\1,\3"
		, rename)
	#print(rename1)
	# last call r"(\+)*(\d)(\s)*(\(*)(\d\d\d)(\)*)(\s*)(\-*)(\d\d\d)(\-*)(\d\d)(\-*)(\d\d)(\s*)(\(*)(доб\.)*(\s*)(\d*)(\))*", r"+\2(\5)\9-\11-\13 \16\18", k
	rename2 = my_replace(
		r"(\+)*(\d)(\s)*(\(*)(\d\d\d)(\)*)(\s*)(\-*)(\d\d\d)(\-*)(\d\d)(\-*)(\d\d)(\s*)(\(*)(доб\.)*(\s*)(\d*)(\))*"
		, r"+\2(\5)\9-\11-\13 \16\18"
		, rename1)
	print(rename2)
