ISBN = input("Enter your ISBN: ")
ISBN = ISBN.replace('-','')
ISBN = list(map(int,ISBN))
ISBN_12 = 10 - (( ISBN[0] + (3 * ISBN[1]) + ISBN[2] + (3 * ISBN[3]) + ISBN[4] + (3 * ISBN[5]) + ISBN[6] + (3 * ISBN[7]) + ISBN[8] + (3 * ISBN[9]) + ISBN[10] + (3 * ISBN[11]) ) % 10)
ISBN.append(ISBN_12)
ISBN_Order = ISBN[0],ISBN[1],ISBN[2],'-',ISBN[3],'-',ISBN[4],ISBN[5],ISBN[6],'-',ISBN[7],ISBN[8],ISBN[9],ISBN[10],ISBN[11], '-', ISBN[12]
Full_ISBN = ''.join(map(str,ISBN_Order))
print("ISBN:", Full_ISBN)
