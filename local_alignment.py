import pandas as pd

def split(word):
    return list(word)


def s(s1i,s2j): #function that tests if two aligning charecters of two strings are the same and calcucates the score
    if s1i == s2j:
        return 1
    else:
        return -1

    

#s1="GGTTGACTA" #vertical
#s2="TGTTACGG" #horizontal

s1=" CCTCGTGAATT" #vertical
s2="  ΑΑGTACCGGA" #horizontal


colss=split(s2.replace(" ", "_"))
colss.insert(0," ")
index = split(s1.replace(" ", "_"))
index.insert(0, " ")

rows, cols = (len(s1)+1, len(s2)+1)
arr = [[100 for i in range(cols)] for j in range(rows)]


for i in range(len(s1)):
    for j in range(len(s2)):
        print(arr[i][j], end ="  ")
    print("\n")
print("\n\n\n")

arr[0][0] = 0

for i in range(1, len(s2)+1):
    arr[0][i]= 0 #int(arr[0][i-1]) + int(s(" ", s2[i-1])) #A

for j in range(1, len(s1)+1):
    arr[j][0]= 0 #int(arr[j-1][0]) + int(s(s1[j-1], " ")) #B


for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        #print("i = {}\tj = {}".format(i,j))
        #print("S1(i):{} \tS2(j):{}".format(s1[i-1], s2[j-1]))
        #print("arr[i-1][j-1] + s(s1[i-1], s2[j-1]):{}".format(arr[i-1][j-1] + s(s1[i-1], s2[j-1])))
        #print("arr[i-1][j] + s(s1[i-1], " "):{}".format(arr[i-1][j] + s(s1[i-1], " ")))
        #print("arr[i][j-1] + s(" ",s2[j-1]):{}\n".format(arr[i][j-1] + s(" ",s2[j-1])))
        arr[i][j] = max(0, int(int(arr[i-1][j-1]) + int(s(s1[i-1], s2[j-1]))), int(int(arr[i-1][j]) + int(s(s1[i-1], " "))), int(int(arr[i][j-1]) + int(s(" ",s2[j-1]))))


for i in range(len(s1)):
    for j in range(len(s2)):
        print(arr[i][j], end ="  ")
    print("\n")
print("\n\n\n")

df = pd.DataFrame(arr, columns=colss, index=index)
print(df.to_string())
