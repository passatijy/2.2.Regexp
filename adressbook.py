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
		else:
			res_contacts.append(elem)
	return res_contacts

def glue_two_elems(elem1,elem2):
	'''return only one element with maximum info'''
	one = elem1.copy()
	two = elem2.copy()
	i = 0
	while i < len(elem1):
#		if one[i] and two[i] is not '':
		if one[i] is not '':
			if two[i] is not '':
				if one[i] != two[i]:
					one[i] = one[i] + '/' + two[i]
		else:
			if two[i] is not '':
				one[i] = two[i]
		i = i + 1
	return one


def my_uniq(mylist):
	'''uniq bu ID = lastname '''
	templist = mylist.copy()
	res_contacts=[]
	i = 0
	while i < len(templist):
		res_elem = templist[i]
		#print('Перебираем, элемент номер:',i,'является:',templist[i])
		k = i + 1
		while k < len(templist):
			#print(' ищем совпадения, рез. элемент:', res_elem,'элемент k:', templist[k])
			if res_elem[0] == templist[k][0]:
				#print(' совпадение найдено')
				res_elem = glue_two_elems(res_elem,templist[k])
				templist.remove(templist[k])
				#print('    результирующий элемент для добавления:',res_elem)
			#else:
				#print(' совпадение не найдено')
			k = k + 1
		res_contacts.append(res_elem)
		i = i + 1
	return res_contacts

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def filewriter(outputlist):
	with open("phonebook.csv", "w", encoding="utf-8") as f:
		datawriter = csv.writer(f, delimiter=',')
		# Вместо contacts_list подставьте свой список
		datawriter.writerows(outputlist)


if __name__ == '__main__':
	for k in contacts_list:
		print('Initial list:', k)
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
	#print(rename2)
	print('========================')
	result = my_uniq(rename2)
	for k in result:
		print('Result list:', k)
	filewriter(result)
