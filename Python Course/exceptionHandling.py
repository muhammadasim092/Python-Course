# a = input("Enter the number:")
# print (f"multiplication table of {a} is:")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} * {i} = {int(a) * i}")
# except Exception as e:
#     print(f"An error occurred: {e}")

# print("Some Imp Lines of Code")
# print("End of Program")

# try:
#     num = int(input("Enter the number: "))
#     a = [ 1, 2, 3, 4, 5]
#     print(a[num])
# except ValueError:
#     print("Invalid input. Please enter a number.")
def func():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except IndexError:
        print("Index out of range")
        return 0
    finally:
        print("This will run regardless of the exception")

x = func()
print(x)