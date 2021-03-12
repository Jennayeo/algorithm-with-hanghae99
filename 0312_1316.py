num = int(input())
word_group=0

for n in range(num):
    result = 0
    word = list(input()) #happy
    for s in range(len(word)-1): #s=0 #1 #2
        if word[s] != word[s+1]: #h<>a #a<>p #p=p이니 패스
            new_list = word[s+1:] #appy #ppy #py
            if new_list.count(word[s]) > 0: #result=0 #0
                result += 1
    if result == 0:
        word_group+=1
print(word_group)