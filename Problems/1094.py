d = {'C': 0, 'R': 0, 'S': 0}

for x in range(int(input())):    
    q, t = map(str, input("").split(" "))    
    d[t] += int(q)    

print("Total: {} cobaias".format(sum(d.values())))
print("Total de coelhos: {}".format(d['C']))
print("Total de ratos: {}".format(d['R']))
print("Total de sapos: {}".format(d['S']))
print("Percentual de coelhos: {:.2f} %".format((d['C'] / sum(d.values())) * 100 ))
print("Percentual de ratos: {:.2f} %".format((d['R'] / sum(d.values())) * 100 ))
print("Percentual de sapos: {:.2f} %".format((d['S'] / sum(d.values())) * 100 ))    