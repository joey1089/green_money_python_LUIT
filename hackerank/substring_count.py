#!usr/bin/python3.10
# counts number of substring found in a string

def count_substring(string, sub_string):
    # sub_str_count = string.count(sub_string)
    string = "Thisisnotistring"
    state=0
    count=0
    while state!=-1:
        state = string.find(sub_string,state) # state keeps track of return value of find() which Return -1 on failure.
        if state!=-1:
            count+=1
            state+=1
    return count
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)