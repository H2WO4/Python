class Actor:
    def __init__(self, name, mhp, mmp, pat, pdf, mat, mdf):
        self.name = name
        self.hp = mhp
        self.mhp = mhp
        self.mp = mmp
        self.mmp = mmp
        self.pat = pat
        self.pdf = pdf
        self.mat = mat
        self.mdf = mdf

class Hero(Actor):
    def __init__(self, name, mhp, mmp, pat, pdf, mat, mdf):
        self.name = name
        self.hp = mhp
        self.mhp = mhp
        self.mp = mmp
        self.mmp = mmp
        self.pat = pat
        self.pdf = pdf
        self.mat = mat
        self.mdf = mdf

        Heroes.append(self)

Heroes = []

print(Heroes)