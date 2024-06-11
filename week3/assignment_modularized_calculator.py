#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_times(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1

def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def read_open_parenthesis(line, index):
    token = {'type': 'OPEN_PARENTHESIS'}
    return token, index + 1

def read_close_parenthesis(line, index):
    token = {'type': 'CLOSE_PARENTHESIS'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_times(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            (token, index) = read_open_parenthesis(line, index)
        elif line[index] == ')':
            (token, index) = read_close_parenthesis(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def parentheses_exist(tokens):
    for token in tokens:
        if token['type'] == 'OPEN_PARENTHESIS':
            return True
    return False

def search_parenthesis_index(tokens):
    index_stack = []
    for i in range(len(tokens)):
        if tokens[i]['type'] == 'OPEN_PARENTHESIS':
            index_stack.append(i)
        elif tokens[i]['type'] == 'CLOSE_PARENTHESIS':
            open_index = index_stack.pop()
            return open_index, i
    return None, None

def evaluate_inside_parenthesis(tokens):
    open_index, close_index = search_parenthesis_index(tokens)
    if open_index is None or close_index is None:
        return tokens
    inside_tokens = tokens[open_index + 1:close_index]
    inside_tokens = evaluate_multiplicationanddivision(inside_tokens)
    answer = evaluate_plusandminus(inside_tokens)
    tokens = tokens[:open_index] + [{'type': 'NUMBER', 'number': answer}] + tokens[close_index + 1:]
    return tokens

def evaluate_multiplicationanddivision(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            interimresult = 0
            if tokens[index - 1]['type'] == 'TIMES':
                interimresult = tokens[index - 2]['number'] * tokens[index]['number']
                tokens[index - 2]['number'] = interimresult
                del tokens[index - 1:index + 1]
                index -= 2
            elif tokens[index - 1]['type'] == 'DIVIDE':
                if tokens[index]['number'] == 0:
                    raise ZeroDivisionError("divided by zero")
                interimresult = tokens[index - 2]['number'] / tokens[index]['number']
                tokens[index - 2]['number'] = interimresult
                del tokens[index - 1:index + 1]
                index -= 2
        index += 1
    return tokens

def evaluate_plusandminus(tokens):
    tokens.insert(0, {'type': 'PLUS'})
    answer = 0
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer

def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
    while parentheses_exist(tokens):
        tokens = evaluate_inside_parenthesis(tokens)
    tokens = evaluate_multiplicationanddivision(tokens)
    answer = evaluate_plusandminus(tokens)
    return answer

def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("0")
    test("1")
    test("-1")
    test("2")
    test("-2")
    test("11")
    test("11.1")

    test("1+2")
    test("1-2")
    test("1*2")
    test("1/2")
    test("1.0+2")
    test("1.0+2.0")

    test("2+3")
    test("2-3")
    test("2*3")
    test("2*0")
    test("2/3")
    test("2+3.0")
    test("2-3.0")
    test("2*3.0")
    test("2/3.0")

    test("2+3+4")
    test("2-3-4")
    test("2+3*4")
    test("2*3+4")
    test("2-3/4")
    test("2/3-4")

    test("2*3.0+4/5.0")
    test("2*3.0-4/5.0")
    test("2*3*4*5")
    test("2/3/4/5")

    test("(1)")
    test("((1))")
    test("1-(2-3)")
    test("1-(2-(3-4))")
    test("(1+2)*3")
    test("1*(2+3)")
    test("(1-2)/3")
    test("1/(2-3)")

    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input() #式の入力
    tokens = tokenize(line) #字句の分割
    answer = evaluate(tokens) #計算
    print("answer = %f\n" % answer)
