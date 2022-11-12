#display menu
infos ={
    "Shane Palahang": {"age":19, "address":'Taguig',"phone no.":'012345'}
}
def menu():
    print("Menu: ")
    print("  1 -> Add an item")
    print("  2 -> Search")
    print("  3 -> Exit")
menu()
#ask user input
option = int(input("What do you want to do? (1-3): "))
#perform option 1, add data
if option == 1:
    name = input("Full name: ")
    infos["age"] = int(input("Age: " ))
    infos["address"] = input("Address: ")
    infos["phone_no"] = int(input("Phone number: "))
    print("SAVED!")
    infos[name] = infos["age"], infos["address"], infos["phone_no"]
# perform option 2, search

#exit

