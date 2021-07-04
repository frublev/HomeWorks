import hashlib


def output_hash(file_name):
    with open(file_name) as read_file:
        for line in read_file:
            yield hashlib.md5(line.encode()).digest()


if __name__ == '__main__':
    for line_h in output_hash("country-link.txt"):
        print(line_h)
