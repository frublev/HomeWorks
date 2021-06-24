import re
import csv

contacts_list =[]
correct_list = []

with open("phonebook_raw.csv", encoding='utf8') as f:
  rows = csv.reader(f, delimiter=",")
  for row in rows:
      contacts_list.append(','.join(row))

patterns = [
    ['^(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)', r'\1,\3,\5,\7'],
    ['(\+7|8)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})', r'+7(\3)\4-\5-\6'],
    ['\(?доб\.\s(\d{4})\)*', r'доб.\1']
    ]

for contact in contacts_list:
    for pattern in patterns:
        find = re.findall(pattern[0], contact)
        contact = re.sub(pattern[0], pattern[1], contact)
    # print(contact)
    correct_list.append(contact.split(','))

fname_sname = []
for contact in correct_list:
    fname_sname.append(contact[0] + contact[1])

del_cont = []
for i in range(1, len(correct_list) - 1):
    for m in range(i + 1, len(correct_list)):
        if correct_list[i][0] == correct_list[m][0]:
            for k in range(7):
                if correct_list[i][k] == '':
                    correct_list[i][k] = correct_list[m][k]
            del_cont.append(correct_list[m])

for d in del_cont:
    correct_list.remove(d)

with open("phonebook.csv", "w", encoding='utf8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(correct_list)