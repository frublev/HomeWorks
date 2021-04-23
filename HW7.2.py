file_names = ['1.txt', '2.txt', '3.txt']
file_sum = 'Sum.txt'


def file_analyse(file_name):
    with open(file_name, encoding="utf-8") as work_files:
        text = work_files.readlines()
        str_count = len(text)
        return [file_name, str_count, text]


def file_list_sort(file_name):
    file_count_text = []
    for file in file_name:
        file_count_text.append(file_analyse(file))
    file_count_text.sort(key=lambda count: count[1])
    for file in file_count_text:
        file[0] += '\n'
        file[1] = str(file[1]) + '\n'
        file[2] = ''.join(file[2]) + '\n'
    return file_count_text


def file_writer(file_name, sum_file):
    with open(sum_file, 'w', encoding="utf-8") as work_file:
        for_write = file_list_sort(file_name)
        for content in for_write:
            for x in content:
                work_file.write(x)


file_writer(file_names, file_sum)
# with open('Sum.txt', 'w', encoding="utf-8") as work_file:
#     print(file_analyse('3.txt'))
#     pass
