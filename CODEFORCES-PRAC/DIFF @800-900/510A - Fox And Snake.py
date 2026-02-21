n_m,c = [],0
n_m.extend(map(int,input().split()))
for _ in range(1,n_m[0]+1):
        if _%2 != 0:
            print("#"*n_m[1])
        if _%2 == 0:
            if c%2 == 0 or c == 0:
                 print("."*(n_m[1]-1)+"#")
            if c%2 != 0:
                 print("#"+"."*(n_m[1]-1))
            c = c+1