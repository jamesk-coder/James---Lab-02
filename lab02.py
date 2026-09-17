# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"

    hour = total_seconds // 3600
    minute = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hour}:{minute:02d}:{seconds:02d}"



def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    price:float = -1
    if age < 5:
        price = 0
    elif age <= 12:
        price = 8
    elif age <= 64:
        price = 15
    else:
        price = 10
    return price


def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5\
    Total:float = 0
    for x in range(limit):
        if x % 3 == 0:
            Total += x
        elif x % 5 == 0:
            Total += x
    return Total


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    
    pass


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()