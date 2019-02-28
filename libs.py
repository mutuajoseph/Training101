from library import *

techcamplib = Library(bks=1000,gen=["Drama","Fiction","Comedy"],membs=["Imran","Gaideh","Josep"])

print(techcamplib.booksnumber)
print(techcamplib.members)
print(techcamplib.genre)

techcamplib.lend()
print(techcamplib.booksnumber)