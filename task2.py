import collections


def sort(filename):
    ip_sort = collections.Counter()
    with open(filename) as f:
        for line in f:
            string = line.split(" ")
            if len(string) > 0:
                ip = string[0]
            else:
                ip = 'Undefined'
            ip_sort[ip] += 1

    with open('sort.txt', 'w') as f:
        for key, val in ip_sort.items():
            f.write('{}:{}\n'.format(key, val))
