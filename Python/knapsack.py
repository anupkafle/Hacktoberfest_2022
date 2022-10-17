def knapsack(bi,weight,W,n):
    V=[[0 for x in range(W+1)] for y in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if weight[i-1]<=w:
                if bi[i-1] + V[i-1][w-weight[i-1]] > V[i-1][w]:
                    V[i][w]=bi[i-1]+V[i-1][w-weight[i-1]]
                else:
                    V[i][w]=V[i-1][w]
            else:
                V[i][w]=V[i-1][w]
    i,k=n,W
    item=[]
    while i>0 and k>0:
        if V[i][k]!=V[i-1][k]:
            item.append(i-1)
            i=i-1
            k=k-weight[i-1]
        else:
            i=i-1
    item.sort()
    for x in item:
        print(x)
n=4 #(no of elements)
W=5 #(max Weight)
bi=[3,4,5,6] # (benefits)
weight=[2,3,4,5] #(weight)
knapsack(bi,weight,W,n)




