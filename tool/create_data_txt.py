import os

file_name = r"D:\下載\BOLL-20220828T071021Z-001\BOLL\images\val"
file = os.listdir(file_name)

# with open('train.txt', 'w' ,encoding='utf-8') as f:
#     for i in file:
#         file_addr = os.path.join(file_name, i)
#         f.write(file_addr+'\n')

# with open('test.txt', 'w' ,encoding='utf-8') as f:
#     for i in file:
#         file_addr = os.path.join(file_name, i)
#         f.write(file_addr+'\n')

with open('val.txt', 'w' ,encoding='utf-8') as f:
    for i in file:
        file_addr = os.path.join(file_name, i)
        f.write(file_addr+'\n')
