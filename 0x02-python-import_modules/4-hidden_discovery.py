#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    total_func = dir()
    for i in range(0, len(total_func)):
        if total_func[i][:2] != "__":
            print("{:s}".format(total_func[i]))
