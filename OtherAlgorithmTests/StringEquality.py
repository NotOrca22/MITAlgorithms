a = "orcaorcaorcaorcaorca97"
b = "orcaorcaorcaorcaorca" + "97"
c = "orcaorcaorcaorca"
e = "orca"
f = "".join(["o", "r", "c", "a"])
print(e == f)
print(e is f)
print(a == b)
print(a is c + "orca97")
print(a == c + "orca97")
print(hex(id(a)), hex(id(b)))
print(a.__eq__(b))
print("orca" == "orca")
print("orca".__eq__("orca"))
c = str("orca")
d = str("orca")
print(c==d)
print(c.__eq__(d))
def test(s):
    s -= 3
    print(hex(id(s)))
def test2(l):
    l.append("wolves of the sea")
    print(hex(id(l)))
testString = "orca is very cool"
testInt = 10
print(hex(id(testInt)))
test(testInt)
testList = ["orca", "killer whale", "blackfish"]
print(hex(id(testList)))
test2(testList)