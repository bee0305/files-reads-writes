import pickle

# read file content 1:1 without any uitwerken
# mostely for reading objects from a file / or saving objects to a file


try:
    with open('src.bin', 'rb') as fh:
        # zal niet lukken: fh.write(obj)
        # args(object, destination=where to write via file handle
        obj = pickle.load(fh)
        obj_2 = pickle.load(fh)
        print('object read from a binary is:', obj)
        print('object read from a binary is:', obj_2)
except FileNotFoundError:
    print('Can not find file or read it.')
