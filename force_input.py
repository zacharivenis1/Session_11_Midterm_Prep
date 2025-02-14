def multiple_of_6():
    #returns a multiple of 6, keeps asking otherwise

    while True:
        try:
            n = int(input("Please give me a multiple of 6: "))

            if n % 6 == 0:
                print(n)
                break
            else:
                print("that is not a multiple of 6")

        except ValueError:
            print("that is not a valid number")

multiple_of_6()