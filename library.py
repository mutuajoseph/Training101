class Library:
    genre = []
    booksnumber = 0
    members = []

    # Our constructor
    def __init__(self,gen,bks,membs,):
        self.genre = gen
        self.booksnumber = bks
        self.members = membs

    def lend(self):
        self.booksnumber -=1

