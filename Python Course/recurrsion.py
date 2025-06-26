def fibonachi(n):
    a, b = 0, 1
    print("Fibonachi Series")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

term = int(input("Enter the term number: "))
if term <=0:
    print("Please enter a positive integer.")
else:
     fibonachi(term)

    