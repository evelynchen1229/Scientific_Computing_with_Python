
def arithmetic_arrange(problems, show_result = False):

    space = " " * 5
    n = len(problems)
    fr = ""
    sr = ""
    d = ""
    r = ""

    def upper_leading(new_array):
        leading_space = max(len(new_array[0]),len(new_array[2])) + 2 - len(new_array[0])
        return " " * leading_space

    def lower_leading(new_array):
        leading_space = max(len(new_array[0]),len(new_array[2])) + 1 - len(new_array[2])
        return " " * leading_space

    def dash_length(new_array):
        total_length = max(len(new_array[0]),len(new_array[2])) + 2
        return "-" * total_length

    def result(new_array):

        if new_array[1] == "+":
            result = int(new_array[0]) + int(new_array[2])
        else:
            result = int(new_array[0]) - int(new_array[2])

        leading_space = " " * (max(len(new_array[0]),len(new_array[2])) + 2 - len(str(result)))

        return leading_space + f'{result}' + space

    def first_row(new_array):
        return upper_leading(new_array) + new_array[0] + space

    def second_row(new_array):
        return new_array[1] + lower_leading(new_array) + new_array[2] + space

    def dash(new_array):
        return dash_length(new_array) + space

    for i in range(0,n):
        new_array = problems[i].split(" ")
        fr = fr + first_row(new_array)
        sr = sr + second_row(new_array)
        d = d+  dash(new_array)
        r = r + result(new_array)
    arithmetic = fr + '\n' + sr + '\n' + d
    result = arithmetic + '\n' + r

    if show_result == False:
        return arithmetic
    return result


array = ["32 + 698", "3801 - 2","3801 - 2","45 + 43","123 + 49"]
problem = arithmetic_arrange(array)
print(problem)

answer = arithmetic_arrange(array,True)
print( answer)

