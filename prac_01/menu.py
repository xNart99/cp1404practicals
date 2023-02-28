LIST = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")

print(LIST)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(LIST)
    choice = input(">>> ").upper()

print("Finished.")
