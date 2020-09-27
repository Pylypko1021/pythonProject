import csv
import os

directory = r"C:\Users\Pylyp\PycharmProjects\pythonProject\found"
files = os.listdir(directory)
found = files[0]


directory = r"C:\Users\Pylyp\PycharmProjects\pythonProject"
files = os.listdir(directory)
csv_files = filter(lambda x: x.endswith('.csv'), files)


all=[]
all_essid1=[]
all_essid2=[]
ap1=[]
ap2=[]
name1=[]
name2=[]
station1=[]
station2=[]
num = 0

with open("found/"+found, "r") as f:
    lines = f.readlines()

with open("found/"+found, "w") as f:
     [f.write(line) for line in lines if line.strip()]

with open('found/'+found) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     line_count = 0
     for row in csv_reader:
         all.append(row[0])
         try:
            all_essid1.append(row[0] + " -" + row[13])
            #print(row[0] + " -" + row[13])

         except IndexError:
             pass



num = all.index("Station MAC")
for k in all:
    if (all.index(k)<num):
        ap1.append(k)
    if (all.index(k)>num):
        station1.append(k)
ap1.remove("BSSID")


for s in csv_files:

    with open(s, "r") as f:
        lines = f.readlines()

    with open(s, "w") as f:
        [f.write(line) for line in lines if line.strip()]

    with open(s) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            all.append(row[0])
            try:
                all_essid2.append(row[0] + " -" + row[13])
                #print(row[0] + " -" + row[13])

            except IndexError:
                pass

    num = all.index("Station MAC")
    for k in all:
        if (all.index(k) < num):
            ap2.append(k)
        if (all.index(k) > num):
            station2.append(k)
    ap2.remove("BSSID")

    result1 = list(set(ap1) & set(ap2))
    result2 = list(set(station1) & set(station2))
    result3 = list(set(all_essid1) & set(all_essid2))
    print(s)
    print("AP:")
    print(result1)
    print("Clients:")
    print(result2)
    print("MAC+NAME:")
    for k in result3:
        print(k)





