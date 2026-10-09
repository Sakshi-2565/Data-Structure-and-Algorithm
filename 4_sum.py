#### BRUTE FORCE SOLUTION ####
def BruteForce(num,target):
    my_set = set()    
    n = len(num)

    if n<4:  # Base Case
        return []

    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if i!=j!=k!=l and  num[i]+num[j]+num[k]+num[l]==target:
                        my_list = [num[i],num[j],num[k],num[l]]
                        my_list.sort()
                        my_set.add(tuple(my_list))

    return [ans for ans in my_set]

num = [1,0,-1,0,-2,2]
print(BruteForce(num,0))

# Time Complexity = O(N**4)
# Space Complexity = O(N)

########## BETTER SOLUTION #################

def Better(num,target):
    my_set = set()    
    n = len(num)

    for i in range(0,n):
        temp=set()
        for j in range(i+1,n):
            for k in range(j+1,n):
                l=target-(num[i]+num[j]+num[k])
                if l in temp:
                    my_list = [num[i],num[j],num[k],l]
                    my_list.sort()
                    my_set.add(tuple(my_list))
                temp.add(num[k])

    return [ans for ans in my_set]

num = [1,0,-1,0,-2,2]
print(Better(num,0))

# Time Complexity = O(N**3)
# Space Complexity = O(N)

####### OPTIMAL ####################

def optimal(num,target):
    n=len(num)
    ans = []
    num.sort()
    for i in range(0,n):
        if i>0 and num[i]==num[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and num[j]==num[j-1]:
                continue
            k=j+1
            l=n-1
            while k<l:
                total=num[i]+num[j]+num[k]+num[l]
                if total == target:
                    ans.append([num[i],num[j],num[k],num[l]])
                    k+=1
                    l-=1
                    while k<l and num[k]==num[k-1]:
                        k+=1
                    while k<l and num[l]==num[l+1]:
                        l-=1
                elif total<target:
                    k+=1
                else:
                    l-=1

    return ans

num = [1,0,-1,0,-2,2]
print(optimal(num,0))