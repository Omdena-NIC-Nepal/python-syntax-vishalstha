def format_string(name, age):
    return (f"My name is {name} and I am {age} years old")

    pass

def conditional_check(number):
    if number > 10:
        return ("Greater")
    elif number < 10:
        return ("Lesser")
    else:
        return ("Equal")

    pass


def loop_sum(n):
    i = 1
    sum = 0
    while i < n+1:
        sum += i
        i += 1
    return (sum)
    
    pass


def list_operations(numbers):
    sum = 0
    max = numbers[0]
    min = numbers[0]
    for num in numbers:
        sum = sum + num
        if num > max : max = num
        if num < min : min = num
    return (sum, max, min)

    pass


def dict_operations(students_dict):
    students_highscore = []
    for name,score in students_dict.items():
        if score >= 80:
            students_highscore.append(name)
    return (students_highscore)

    pass


def set_operations(list1, list2):
    return (set(list1) & set(list2))

    pass


def arithmetic_ops(a, b):
    def quotient(a, b):
        if (b == 0):
            return ("Division by zero")
        else: 
            return a/b
    arithmetic = {
        "sum": a+b,
        "difference": a-b,
        "product": a*b,
        "quotient": quotient(a, b)
    }
    return (arithmetic)

    pass


def logical_ops(x, y):
    logical = {
        "and": x and y,
        "or": x or y,
        "not_x": not x
    }
    return (logical)

    pass


def bitwise_ops(a, b):
    bitwise = {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b
    }
    return (bitwise)

    pass



