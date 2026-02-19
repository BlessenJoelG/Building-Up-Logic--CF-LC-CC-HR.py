k, l, m, n, d, final_div_set = int(input()),int(input()),int(input()),int(input()),int(input()),set()
tot_drags = [_ for _ in range(1,d+1)]
type_of_attack = [k,l,m,n]
for x in type_of_attack:
    for _ in range(len(tot_drags)):
        if tot_drags[_]%x == 0:
            final_div_set.add(tot_drags[_])
print(len(final_div_set))