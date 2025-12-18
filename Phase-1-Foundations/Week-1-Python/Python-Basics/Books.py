def disp(book):
    for i,j in book.items():
        print(f"{i} \n {j}\n")

def add(book):
    while(True):
        try:
            n = int(input("Enter the number of book you want to add : "))

            if(n>0):
                break
            else:
                print("You entered Wrong Input")

        except Exception as e:
            print("Something Went Wrong")

    for i in range(n):
        b = {}
        title = input("Enter title of book : ")
        author = input("Enter autthor of book : ")
        year = input("Enter the year of edition : ")
        b['title'] = title
        b['author'] = author
        b['year'] = year
        book[f'Book{len(book)+1}'] = b.copy()
        print(f"{b} was added")
 
    while(True):
        try:
            n = input("Enter 'y' to display all books or enter 'exit' to stop program : ")

            if(n.lower().strip()=='y'):
                disp(book)
                break
            elif(n.lower().strip()=='exit'):
                exit()
            else:
                print("You entered Wrong Input")

        except Exception as e:
            print("Something Went Wrong")   

book = {
    'Book1' : {
    'Title' : "Python",
    'Author': 'Rudra',
    'Year' : '2025'  
    },

    'Book2' : {
    'Title' : "Java",
    'Author': 'Hardik',
    'Year' : '2024'
    },

    'Book3' : {
    'Title' : "C",
    'Author': 'Harsh',
    'Year' : '2022'
    },
    'Book4' : {
    'Title' : "C++",
    'Author': 'Het',
    'Year' : '2023'
    },
    'Book5' : {
    'Title' : "Ruby",
    'Author': 'Vishesh',
    'Year' : '2020'
    }
}



while(True):
    try:
        z = int(input("Enter 1 for display all books \nEnter 2 for add books\nEnter your choice: "))
        if(z==1 or z==2):
            if(z==1):
                disp(book)
                break
            elif(z==2):
                add(book)
                break
            else:
                print("Something Went Wrong!")
        else:
            print("Wrong Input!")

    except Exception as e:
        print(e)