class library:
    books=["python", 'java','c','c++']
    tot_books=4
    def __init__(self):
        print("Welcome!!")
        if(self.tot_books!=len(self.books)):
            print("Something went wrong!!!")
            exit()
    

    def show(self):
        print(f'Total books = {self.tot_books}\n Books = {self.books}')

    def addbooks(self,*args):
        self.books.extend(args)
        self.tot_books+=len(args)

a=library()
a.show()
a.addbooks('ruby','php','javascript')
a.show()