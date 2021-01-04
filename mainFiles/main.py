def user(number):
    if number % 2 == 0:
        if number in range(6, 21):
            print("Weird")

        if number not in range(21):
            print("Not weird")


if __name__ == "__main__":
    n = int(input("> "))
    user(n)
