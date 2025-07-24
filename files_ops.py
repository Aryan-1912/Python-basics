#write without overwriting
#with open ('exam.txt', 'a') as file:
 ##  file.write("edibifjeb3bfju\n")


# write a file 
#with open('exam.txt', 'w') as file:
 #   file.write("hwlooo reofnevfn nv nfiwnrw \n")
  #  file.write ("dfffdefd\n")
   # file.write("123891274328943hdejdhfjbfubfkjdbswaiorwifn3ewiiownfuwnedfjeonqff")



# read file line by line
#with open ('exam.txt','r') as file:
    #for line in file:
   #     print(line)

#write a list of lines 

list = ['mdmkfdkf\n', 'djneinfd\n', 'eofknnk\n']

with open('exam.txt', 'a') as file:
    file.writelines(list)
#read a whole file
with open('exam.txt', 'r') as file:
    content = file.read()
    print (content)

#read exam txt and copy all write to gymtxt
with open ('exam.txt', 'r') as file:
    content = file.read()
with open ('gym.txt', 'w') as file:
    file.write(content)


#read a text file and count the number of lines, words, and charc

def count_txt(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        return line_count, word_count, char_count

filepath = 'exam.txt'
lines, words, characters = count_txt(filepath)
print(f"{lines},   {words},   {characters}")



#writing and then reading file

with open('std.txt', 'w+') as file:
    file.write("hello babababa \n")
    file.write("defefdv\n")
    file.write("dffdiomg")
    file.seek(7)
    print(file.read())

with open ('std.txt','r') as file:
    content = file.read()
    print(content)


import os
items = os.listdir('.')
print(items)
print(os.getcwd())
print(os.path.abspath('filters.py'))