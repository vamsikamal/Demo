import csv
with open('emp.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Id', 'Name', 'location', 'Designation'])
    w.writerow(['1', 'Vamsi','Hyd', 'Trainer'])
    w.writerow(['2', 'Vamsi','Hyd', 'Trainer3'])
    w.writerow(('3', 'Kamal','Hyd', 'Trainer2'))


f = open('emp.csv','r')
r = csv.reader(f)
data = list(r)
for line in data:
    for word in line:
        print(word, end='\t')
    print()