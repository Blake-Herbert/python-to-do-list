to_do_list = ["Code", "Eat", "Sleep"]
selection = 1
while selection != 5:
    selection = int(input("\nPlease select a number:\n\
    1. View list\n\
    2. Add to list\n\
    3. Remove from list\n\
    4. Clear list\n\
    5. Quit\n"))

    if selection == 1:
        print("\nHere's your to-do list:")
        for task in to_do_list:
            print(f"    {task}")
        input("Please press enter to continue...")

    if selection == 2:
        item_to_be_added = input("\nWhat would you like to add?\n")
        to_do_list.append(item_to_be_added)
        input("Item added. Please press enter to continue...")

    if selection == 3:
        print("\nHere's your to-do list:")
        count = 1
        for task in to_do_list:
            print(f"    {count}. {task}")
            count += 1
        item_to_be_removed = input("What would you like to remove?\n")
        if item_to_be_removed <= 0 or \
            item_to_be_removed > len(to_do_list):
            print("Out of range")
        else:
            to_do_list.pop(item_to_be_removed - 1)
            print("Item removed")
        input("Please press enter to continue...")

    if selection == 4:
        to_do_list = []
        input("List cleared. Please press enter to continue...")
print("\nGoodbye!")