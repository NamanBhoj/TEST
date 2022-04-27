import os
count = os.listdir(r'W:\TEST\frames')
print((count[-1]))
# clips = []

count_numbers = [i.replace('.jpg','') for i in count]
a = []
for  i in range(0, len(count_numbers)):
    a.append(count_numbers[i])
    
print(a) #the files are not sorted

a.sort(key = int)# this will sort the files inside the array
print(a) 


a = [i + '.jpg' for i in a] #giving back jpg to the files

print(a)