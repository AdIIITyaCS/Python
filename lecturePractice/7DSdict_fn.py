d1 = []
print(type(d1))
d2 = {}
print(type(d2))
d3 = ()
print(type(d3))
d1 = {"fruit": "mango",
      "vegetable": "nenua",
      "dry-fruit": "pistachio",
      "snackes": "biscuit"}
print("1.", d1)
print("2.", d1["dry-fruit"])
d1.update({"dinner": "rotisbG"}) # d1["dinner" = "rotisbG"]
print("3.", d1)
del d1["snackes"]
print("4.", d1)
d2 = d1.copy()
del d2["fruit"]
print("5.", d2)
print("6.", d1)
print("7.", d1.keys())
print("8.", d1.values())
print("9.", d1.items())