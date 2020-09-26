def false_table(number):
    import random
    wrong = random.randint(2, 9)
    f_table = [i*number for i in range(1,11)]
    f_table[wrong] = f_table[wrong] + random.randint(2,(number-2))
    return f_table

def iscorrect(table,number):
    for i in range(1,11):
        if table[i-1] != number*i:
            return i-1
    return None

def correct_table(number):
    c_table = [i*number for i in range(1,11)]
    return c_table

if __name__ == '__main__':

    restart = ('y')
    while restart == 'y':
        number = int(input("Enter Table Number : "))
        My_Table = false_table(number)
        My_True_Table = correct_table(number)
        print(My_Table)

        print("\nPress 1 to verify table \nPress 2 to ignore")
        choice = int(input("Enter You Choice : "))

        if choice == 1:

            Wrong_Index = iscorrect(My_Table, number)
            print(f"\nThe table is wrong at index {Wrong_Index}")
            print(f"The correct table is {My_True_Table}")
            restart = input("Press y to restart : ").lower()
            if restart != 'y':
                print("Thank you")
                break

        elif choice == 2:
            print("You are a Gambler\n")
            restart = input("Press y to restart : ").lower()
            if restart != 'y':
                print("Thank you")
                break

        else:
            print("Invalid Option\n")
            restart = input("Press y to restart : ").lower()
            if restart != 'y':
                print("Thank you")
                break




