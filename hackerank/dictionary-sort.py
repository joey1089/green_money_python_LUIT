#!/usr/bin/python3.10
if __name__ == '__main__':
    dict_item = {}
    for i in range(int(input())):
        name = input()
        score = float(input())
        dict_item[name] = score
        
    new_alpha = dict_item.items()
    print(new_alpha)    
    new_val = sorted(new_alpha)
    
    print(new_val)