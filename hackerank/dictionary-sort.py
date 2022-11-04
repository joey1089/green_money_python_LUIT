#!/usr/bin/python3.10
# Find the second lowest score of the students
if __name__ == '__main__':    
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Zeb', 42.0]]
    student_score = [37.21, 37.21, 37.2, 42.0]
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name,score])        
    # student_score.append(score)
    print(students)
    student_score = sorted(set(student_score))[1] # finds the 2nd sorted item

    name =[ i[0] for i in students if student_score == i[1] ]   
    print("Students with second Lowest scores : ","\n".join(sorted(name)))


    # dict_item = {}    
    # # for i in range(int(input())):
    # #     name = input()
    # #     score = float(input())
    # #     dict_item[name] = score
    # dict_item = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti':41, 'Harsh':39}
        
    # new_dictlist = dict(dict_item.items()) # Convert tuple to dictionary
    # # print(new_dictlist)
    # sorteditems = sorted((value,key) for (key,value) in new_dictlist.items()) # creates tuples
    # for i in sorteditems:
    #     if sorteditems[i] < sorteditems[i+1]:
    #         print(sorteditems[i])
    #     else:
    #         pass

    # print(sorteditems)
    # secondlowest = sorteditems[len(new_dictlist.items())-4]
    # secondlowest_1 = sorteditems[len(new_dictlist.items())-3]
    # secondlowest = sorteditems[1] # works here not in hackerank
    # secondlowest_1 = sorteditems[2]
    # print(list(secondlowest)[1])
    # print(list(secondlowest_1)[1])
    # works only when values are unique in dictionary, dictionary doesn't allow duplicates
    # sorteditems = dict(sorted((value,key) for (key,value) in new_dictlist.items()))
    # print(sorteditems.values())
    # list_values = list(sorteditems.values())
    # print(list_values[1])
    # print(list_values[2])


   # print("Prints the Tuple list : ",new_alpha)    
    # new_val = sorted(new_alpha) # sort the tuple list
    # sortedValues = sorted(newdict_list.items())
    # print(f"Sorted values : {sortedValues}")
    # #sortitems = dict(sorted(newdict_list.values()) for k,v in newdict_list.items())
    # sortitems = dict(sorted((value,key) for (key,value) in newdict_list.items()))
    # print("Sorted Item : ",sortitems)
    # for k,v in sortitems.items(): 
    #     print("Items : ", k,v)
    

  