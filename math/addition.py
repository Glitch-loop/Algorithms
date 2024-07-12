def addition(num1, num2):
    ptr1 = len(num1) - 1
    ptr2 = len(num2) - 1
    sol_str = ""
    carry_out = 0

    while ptr1 > -1 and ptr2 > -1:
        number1 = int(num1[ptr1])
        number2 = int(num2[ptr2])

        print("number1: ", number1)
        print("number2: ", number2)
        result = number1 + number2 + carry_out

        print(result)
        if result < 10:
            sol_str = str(result) + sol_str
            carry_out = 0
        else:
            sol_str = str(result)[1] + sol_str
            carry_out = 1
        
        ptr1 -= 1
        ptr2 -= 1

    while ptr1 > -1:
        number1 = int(num1[ptr1])

        result = number1 + carry_out

        if result < 10:
            sol_str = str(result) + sol_str
            carry_out = 0
        else:
            sol_str = str(result)[1] + sol_str
            carry_out = 1
        
        ptr1 -= 1


    while ptr2 > -1:
        number2 = int(num2[ptr2])

        result = number2 + carry_out

        if result < 10:
            sol_str = str(result) + sol_str
            carry_out = 0
        else:
            sol_str = str(result)[1] + sol_str
            carry_out = 1
        
        ptr2 -= 1

    if carry_out == 1:
        sol_str = "1" + sol_str

    return sol_str


print(addition("1", "999999"))