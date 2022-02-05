# read file
try:
    with open('src.txt', 'a+', encoding='utf-8') as fh:
        # each char == 2 bytes; widows 1250 = 1 byte
        fh.seek(0)
        print(fh.tell())
        result = fh.read()
        print('result is',result)
        fh.write('вмсиср')
        print(fh.tell())

except FileNotFoundError:
    print('File does not exist or can not be open')
finally:
    print(fh.closed)
