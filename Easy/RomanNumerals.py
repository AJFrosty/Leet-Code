roman = []
total = 0
s = "MCMXCIV"
pairs = []
val = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000, "IV":4,"IX":9,"XL":40, "XC":90,"CD":400,"CM":900}
for i in range(0, len(s), 2):
    pairs.append(s[i:i + 2])
print(pairs)

def check(pair,dict):
    sum = 0
    print(pair in dict)
    if pair in dict:
        return dict[pair]
    else:
        for x in pair:
            sum += dict[x]
        return sum
    
for i in range(len(pairs)):
    total += check(pairs[i],val)