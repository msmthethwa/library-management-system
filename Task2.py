#Task 2: Comprehensions (lists and sets).

#The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:

codes = [14, 15, 16, 17, 18, 19, 20]

#Create a normal list that will display the codes.
codesN = []

for c in codes:
    codesN.append(c)

print("A normal list that display the codes: ", codesN)

#comprehensive list that will display the codes.

codesC = [c for c in codes]
print("\nA comprehensive list that display the codes: ", codesC)

#Create a normal list that will add the codes together for auditing purpose.

addCodesN = []
sumN = 0

for cc in codes:
    sumN = sumN + cc

addCodesN.append(sumN)

print("\nNormal list that  add the codes together for auditing purpose: ", addCodesN)

#Create a comprehensive list that will add the codes together for auditing purpose.

sumC = 0

addCodesC = [sumC := sumC + ccComp for ccComp in codes]
print("\nComprehensive list that adds the codes together for auditing purpose: ", addCodesC)

#Create a normal list that will display only codes that are tracked by odd numbers.

oddCodeN = []

for oN in codes:
    if oN%2 != 0:
        oddCodeN.append(oN)

print("\nA normal list that display only codes that are tracked by odd numbers: ", oddCodeN)

#Create a comprehensive list that will display only codes that are tracked by odd numbers.

oddCodeC = [oC for oC in codes if oC%2 != 0]
print("\nA comprehensive list that display only codes that are tracked by odd numbers: ", oddCodeC)

#Create a set to display the list of codes
setList = set(codes)
print("\nA set to display the list of codes: ", setList)