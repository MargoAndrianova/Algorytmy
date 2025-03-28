def token(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            num = ""
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(num)
        else:
            tokens.append(expr[i])
            i += 1
    return tokens


def do_operators(a, operator, b):
    if operator == '+':
        res = a + b
    elif operator == '-':
        res = a - b
    elif operator == '*':
        res = a * b
    elif operator == '/':
        if b == 0:
            raise Exception
        res = a // b
    if res < 0 or len(str(res)) > 90:
        raise Exception
    return res


def calc(expression):
    expr = "".join(expression.split())
    tokens = token(expr)
    vals = []
    operators = []
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.isdigit():
            if len(t) > 90:
                raise Exception
            vals.append(int(t))
        elif t == '(':
            operators.append(t)
        elif t == ')':
            while operators and operators[-1] != '(':
                operator = operators.pop()
                b = vals.pop()
                a = vals.pop()
                vals.append(do_operators(a, operator, b))
            if operators:
                operators.pop()
        else:
            while operators and operators[-1] != '(' and prec[operators[-1]] >= prec[t]:
                operator = operators.pop()
                b = vals.pop()
                a = vals.pop()
                vals.append(do_operators(a, operator, b))
            operators.append(t)
        i += 1
    while operators:
        operator = operators.pop()
        b = vals.pop()
        a = vals.pop()
        vals.append(do_operators(a, operator, b))
    return vals[0]

def extr(input_str):
    expression = []
    i = 0
    while i < len(input_str):
        if input_str[i] in " \t\n":
            i += 1
            continue
        if input_str[i].isdigit():
            j = i
            while j < len(input_str) and input_str[j].isdigit():
                j += 1
            expression.append(input_str[i:j])
            i = j
        elif input_str[i] == '(':
            cnt = 0
            j = i
            while j < len(input_str):
                if input_str[j] == '(':
                    cnt += 1
                elif input_str[j] == ')':
                    cnt -= 1
                j += 1
                if cnt == 0:
                    break
            expression.append(input_str[i:j])
            i = j
        else:
            i += 1
    return expression


if __name__ == '__main__':
    all_input = ""
    try:
        while True:
            line = input()
            all_input += line + " "
    except EOFError:
        pass
    expression = extr(all_input)
    results = []
    for expr in expression:
        try:
            res = calc(expr)
            results.append(str(res))
        except Exception:
            results.append("Error")
    for res in results:
        print(res)
