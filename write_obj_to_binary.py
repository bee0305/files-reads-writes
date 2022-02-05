import pickle

# read file content 1:1 without any uitwerken
# mostely for reading objects from a file / or saving objects to a file

obj = {'apple': 'green', 'id': 12}
obj2 = {'zoo': 123}
try:
    with open('src.bin', 'wb') as fh:
        # zal niet lukken: fh.write(obj)
        # args(object, where to write via file handle
        pickle.dump(obj, fh)
        pickle.dump(obj2, fh)
except FileNotFoundError:
    print('Can not find file or read it.')
