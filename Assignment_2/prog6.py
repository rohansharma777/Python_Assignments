uin = input("Planet name")
innerplanet = ["mercury", "venus", "earth",
               "mars", "Mercury", "Venus", "Earth", "Mars"]
outerplanet = ["jupiter", "saturn", "uranus",
               "neptune", "Jupiter", "Saturn", "Uranus", "Neptune"]
if uin in innerplanet:
    print("%s is an inner planet" % uin)
elif uin in outerplanet:
    print("%s is an outer planet" % uin)
else:
    print("Wrong planet entered. LOL! Try to stay in our solar system")
