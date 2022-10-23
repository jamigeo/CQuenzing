x = 1

_input = str(input(f"{x}: "))

while True:

    if not _input:

        x += 1
        _input = str(input(f"{x}: "))

        if x % 3 == 0 and x % 5 == 0 and _input == "FuzzBuzz":
   
            print("Richtig")
            x += 1
            _input = str(input(f"{x}: "))

        elif x % 2 == 0 and _input == "FuzzBuzz":

            print("Try it again Partner!")
            exit(1)

        continue

    if x % 3 == 0 and _input == "Fuzz":

        print("Richtig")
        x += 1
        _input = str(input(f"{x}: "))

    elif x % 2 == 0 and _input == "Fuzz":

            print("Try it again Partner!")
            exit(1)
        

    if x % 5 == 0 and _input == "Buzz":

        print("Richtig")
        x += 1
        _input = str(input(f"{x}: "))
        continue

    elif x % 2 == 0 and _input == "Buzz":

            print("Try it again Partner!")
            exit(1)

    else:

        continue
