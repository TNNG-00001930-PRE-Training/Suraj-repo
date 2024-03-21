a = "python is a programming lanuguage"
list_a = list(a.split(' '))
for i in list_a:
    length = len(i)
    if (length % 2 == 0):
        print(i)