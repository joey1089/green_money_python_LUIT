#!/usr/bin/python3.10
if __name__ == '__main__':
    dict_item = {}
    
    for i in range(int(input())):
        name = input()
        score = float(input())
        dict_item[name] = score
        
    new_alpha = dict_item.items()
    newdict_list = dict(new_alpha) # Convert tuple to dictionary
    print("Prints the Tuple list : ",new_alpha)    
    new_val = sorted(new_alpha) # sort the tuple list
    sortedValues = sorted(newdict_list.items())
    print(f"Sorted values : {sortedValues}")
    #sortvalue = dict(sorted(newdict_list) for k,v in newdict_list)
    
    print(new_val)
  