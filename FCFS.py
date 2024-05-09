#fcfs
bt = [5,10,15]
wt = [0]*len(bt)
tt = [0]*len(bt)

i = 1
while i<len(wt):
    wt[i] = wt[i-1] + bt[i-1]
    i+=1

tt[0] = bt[0]
i = 1
while i < len(tt):
    tt[i] = wt[i]+bt[i]
    i += 1
process = ['p1','p2','p3']
    
print("process\t\tburst time\t\tWaiting time\t\ttotal turnaround time")
for p,b, w, t in zip(process, bt, wt, tt):
    print(p,'\t\t', b,'\t\t\t',w,'\t\t\t',t)

print("\n avg turn around time:",sum(tt)/len(tt))
print("\n avg waiting time :",sum(bt)/len(bt))