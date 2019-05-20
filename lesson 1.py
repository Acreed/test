import sys

l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

print "Max",max(l)
print "Max index",l.index(max(l))
print "Min",min(l)
print "Min index",l.index(min(l))

mostCommon = [None, None, None]
countItemMostCommon = [0, 0, 0]

for item in l:
    countItem = l.count(item)
    if countItem > countItemMostCommon[0]:
        countItemMostCommon[0] = countItem
        mostCommon[0] = item

    if countItem > countItemMostCommon[1] and mostCommon[0] != item:
        countItemMostCommon[1] = countItem
        mostCommon[1] = item

    if countItem > countItemMostCommon[2] and mostCommon[0] != item and mostCommon[1] != item:
        countItemMostCommon[2] = countItem
        mostCommon[2] = item

print "Most common count",countItemMostCommon
print "Most common",mostCommon

for item in l:
    countItem = l.count(item)
    if countItem > 1:
        l.remove(item)

print "New list", l
l.sort()
print "Sort list", l

c = {}
d = {}
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

for itemA in a:
    if (itemA in b):
            c.update({itemA: a[itemA]})
print "Dict in A and B",c

for itemB in b:
    if (itemB not in a):
            d.update({itemB: b[itemB]})
print "Dict only B",d

e = b
for itemA in a:
    if (itemA in b):
        e[itemA] += a[itemA]
    else:
        e.update({itemA: a[itemA]})
print "Dict union",e

div = 2
n = input()
s = "1"
while n > 1:
    raw = 0
    while n % div == 0:
        if(raw == 0):
            s += " * " + str(div)
        n = n / div
        raw += 1
    if(raw > 1):
        s += " ^ " + str(raw)
    div += 1
print s

s = "spam and eggs or eggs with spam"
print s