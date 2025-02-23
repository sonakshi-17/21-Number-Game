def check_consecutive(lst):
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:
            return False
    return True

def nearest_multiple(n):
    # This function finds the nearest multiple of 4 greater than n
    return ((n // 4) + 1) * 4

def lose():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)

def play_game():
    xyz = []
    last = 0

    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ').strip().upper()

        if chance == "F":
            while True:
                if last >= 20:
                    lose()
                else:
                    print("\nYour Turn.")
                    try:
                        inp = int(input("How many numbers do you wish to enter? "))
                        if 0 < inp <= 3:
                            comp = 4 - inp
                        else:
                            print("Wrong input. You are disqualified from the game.")
                            lose()

                        print("Now enter the values:")
                        for _ in range(inp):
                            a = int(input('> '))
                            xyz.append(a)
                            last = a

                        if check_consecutive(xyz):
                            if last == 21:
                                lose()
                            else:
                                while comp > 0:
                                    xyz.append(last + comp)
                                    comp -= 1
                                print("Order of inputs after computer's turn:")
                                print(xyz)
                                last = xyz[-1]
                        else:
                            print("\nYou did not input consecutive integers.")
                            lose()
                    except ValueError:
                        print("Invalid input. Please enter integers only.")
                        lose()

        elif chance == "S":
            comp = 1
            while last < 20:
                while comp > 0:
                    xyz.append(last + comp)
                    comp -= 1
                print("Order of inputs after computer's turn:")
                print(xyz)

                print("\nYour turn.")
                try:
                    inp = int(input("How many numbers do you wish to enter? "))
                    for _ in range(inp):
                        num = int(input('> '))
                        xyz.append(num)
                        last = num

                    if check_consecutive(xyz):
                        near = nearest_multiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose()
                except ValueError:
                    print("Invalid input. Please enter integers only.")
                    lose()

    print("\n\nCONGRATULATIONS!!! You've won!")

if __name__ == "__main__":
    play_game()