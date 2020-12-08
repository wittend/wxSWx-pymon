import sys
import csv

# with open('KV0S2-20201201-runmag.log') as csv_file:
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Day, Mon, Year, Hour, Min, Sec, rTemp, lTemp, x, y, z, rx, ry, rz')
            line_count += 1
        else:
            result = row[0].rsplit(':')
            r1 = result[1].replace(' ',',')
            r1a = r1[1:]
            r1b = r1a.replace('Dec', '12')
            rt = row[1].rsplit(': ')
            r2 = row[2].rsplit(': ')
            r3 = row[3].rsplit(': ')
            r4 = row[4].rsplit(': ')
            r5 = row[5].rsplit(': ')
            r6 = row[6].rsplit(': ')
            r7 = row[7].rsplit(': ')
            r8 = row[8].rsplit(': ')
            #r10 = row[9].rsplit(': ')
            print(f'{r1b},{result[2]},{result[3]},{rt[1]},{r2[1]},{r3[1]},{r4[1]},{r5[1]},{r6[1]},{r7[1]},{r8[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')