number = int(input("Powers of which number? "))
terms = int(input("How many terms? "))

result = list(map(lambda x: number ** x, range(terms)))

for i in range(terms):
   print(number," raised to power",i,"is",result[i])