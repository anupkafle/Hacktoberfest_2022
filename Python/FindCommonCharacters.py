# https://leetcode.com/problems/find-common-characters/

# Given a string array words, return an array of all characters that show up in all strings
# within the words (including duplicates). You may return the answer in any order.

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

def commonChars(words):  #Time: O(n*m). Space: O(26+26)
    finalCount={}
    count={}
    for i in range(ord("a"),ord("z")+1):
        finalCount[chr(i)]=100
        count[chr(i)]=0
    for word in words:
        for i in range(ord("a"),ord("z")+1):
            count[chr(i)]=0
        for ch in word:
            if ch in count.keys():
                count[ch]+=1
            else:
                count[ch]=1
        for ch in range(ord("a"),ord("z")+1):
            if chr(ch) in count.keys():
                finalCount[chr(ch)]=min(finalCount[chr(ch)],count[chr(ch)])
    result=[]
    temp=""
    times=0
    for ch in range(ord("a"),ord("z")+1):
        times=finalCount[chr(ch)]
        temp=chr(ch)
        while times>0 and times!=100:
            # print(temp,end=" ")
            result.append(temp)
            times-=1
    return result

print(commonChars(["qweerty" , "weerty" , "eerty"]))    # -> ['e', 'e', 'r', 't', 'y']
print(commonChars(["bella" , "ciao" , "espanol"]))     # -> ['a']
print(commonChars(["aab" , "ba" , "baa"]))             # -> ['a', 'b']
print(commonChars(["aab" , "ba" , "baa","c"]))         # -> []

# -----------------------------

def commonChars(self, words: List[str]) -> List[str]:
    # if only one word present in array
    if len(words)==1:
        return list(words[0])
    # if two word present in array so return their common terms
    if len(words)==2:
        return list(set(words[0]).intersection(set(words[1])))

    # iterate and find the common characters in all the words
    ans=set(words[0]).intersection(set(words[1]))
    for i in range(2,len(words)):
        ans=set(ans).intersection(set(words[i]))
    ans=list(ans)
    print(ans)

    # Store each common words in dictionary as key and a list of size=total no. of words
    dic={}
    for i in ans:
        dic[i]=[0]*len(words)

    # Store count of each common word occurance in each word
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] in dic:
                dic[words[i][j]][i]+=1
    print(dic)

    # Iterate over the dictionary keys and for each key keep adding them in final result untill their count in any words is not zero.
    res=[]
    for key,val in dic.items():
        temp=val
        while 0 not in temp:
            res.append(key)
            for i in range(len(temp)):
                temp[i]-=1
    return res