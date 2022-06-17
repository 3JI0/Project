class Person:
    name  = 'no'
    surname = 'no'
    def set_name(self, n, s):
        self.name = n
        self.surname = s

p1 = Person()
p1.set_name('A', 'aa')

p2 = Person()
p2.set_name('B', 'bb')

p3 = Person()

for i in (p1, p2, p3):
    print(i.name, i.surname)
    print(i.__dict__)
    
