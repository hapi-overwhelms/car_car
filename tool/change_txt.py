import os


file = os.listdir("file")

for i in file:
    if 'txt' in i and 'class' not in i:
        file_addr = os.path.join("file", i)
        with open(file_addr, 'r') as f:
            lines = f.readlines()
            lines = lines[0].split(" ")
            lines[0] = '0'
            ans = ""
            for j in lines:
                j.replace("\n", "")
                if(j == lines[len(lines)-1]):
                    ans += j
                else:
                    ans = ans+j+" "
        with open(file_addr, 'w') as f:
            f.write(ans)