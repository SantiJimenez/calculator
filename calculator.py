#!/usr/bin/env python

__author__ = "Santiago Jimenez Bonilla"
__email__ = "santijimenezbonilla@gmail.com"

"""
   Calculator built using Python 3.x
   that allows to convert infix input strings into rpn expressions
   using operators dictionary in ordern to extend the operators support
"""
import re
import operator


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def len(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def empty(self):
        self.items = []


# Custom operator '#'
def plusDoubleOf(a, b):
    return a + (2 * b)


# Operators dictionary
operators_dict = {
    'plus': [operator.add, 1],
    'minus': [operator.sub, 1],
    'into': [operator.mul, 2],
    'over': [operator.truediv, 2],
    'mod': [operator.mod, 2],
    'pow': [operator.pow, 3],
    '#': [plusDoubleOf, 2],
    '*': [operator.mul, 2],
    '(': [None, 0]
}


def myReplace(match):
    match = match.group()
    return str(" " + match + " ")


# Fix the spaces on the expression
def fixExpression(expression):
    string_expression = re.sub(
        r"[a-zA-Z]+|\)|\(|\*|\#", myReplace, expression)
    element_list = list(string_expression.split(' '))
    element_list = filter(lambda a: a != '', element_list)
    return element_list


def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def errorExpression(element):
    print('Error: %s is not an operator.' % (element))


# Converts an input infix expression to an rpn expression
def infixToRpn(expression):
    expression_stack = Stack()
    operators_stack = Stack()
    element_list = fixExpression(expression)
    # print('Infix expression: ' + ' '.join(element_list))

    for element in element_list:
        # print('1. Element: ', element)
        if isNumber(element):
            expression_stack.push(element)
        elif element == '(':
            operators_stack.push(element)
        elif element == ')':
            tail_element = operators_stack.pop()
            while tail_element != '(':
                expression_stack.push(tail_element)
                tail_element = operators_stack.pop()
        else:
            try:
                if operators_dict[element] is not None:
                    # print('1. Operator item precedence: ', operators_dict[element][1])
                    # print('1. Operator Items: ', operators_stack.items)
                    # print('1. Operator stack is empty: ', operators_stack.isEmpty())
                    while ((not operators_stack.isEmpty()) and (operators_dict[operators_stack[-1]][1] >= operators_dict[element][1])):
                        # print('pushing')
                        expression_stack.push(operators_stack.pop())
                    # print('num operators: ', operators_stack.len())
                    operators_stack.push(element)
            except:
                errorExpression(element)
                # raise ValueError
                return ValueError
        # print('2. Expression stack: ', expression_stack.items)
        # print('2. Operantions stack: ', operators_stack.items)

    while not operators_stack.isEmpty():
        expression_stack.push(operators_stack.pop())

    # print('RPN expression: ' + ' '.join(expression_stack.items))
    return expression_stack


# Evaluates the rpn expression and obtains the resulting value
def evalAsPostfix(expression):
    stack = Stack()

    expression_rpn = infixToRpn(expression)

    try:
        for element in expression_rpn:
            # print(element)
            if not isNumber(element) and operators_dict[element] is not None:
                # print('operator:', element)
                num_1 = stack.pop()
                num_2 = stack.pop()
                # print(num_1, element, num_2)
                result = operators_dict[element][0](num_2, num_1)
                # print('result: ', result)
                stack.push(result)
            else:
                # print('number:', element)
                stack.push(float(element))
        return stack.pop()
    except:
        return ValueError


# print('Expression 1:')
# print(evalAsPostfix("1plus(3*4)#3"))
# print('Expression 2:')
# evalAsPostfix("1pls(3*4)#3")
# print('Expression 3:')
# print(evalAsPostfix("1 plus (3 into 4 ) # 3"))
# print('Expression 4:')
# print(evalAsPostfix("-1 plus ( 3 into 4) # 3"))
# print('Expression 5:')
# print(evalAsPostfix("1plus ( 3 into 4 ) #3"))
# print('Expression 6:')
# print(evalAsPostfix(
#     "7 into 7 into6 plus 7 plus 6 plus 8 over 2 into 1"))
# print('Expression 7:')
# print(evalAsPostfix("( 48 plus 36.2) plus( 8 over 4 ) * 2"))
# print('Expression 8:')
# print(evalAsPostfix("( ( 7 plus 4 ) minus 50 ) plus ( 3 into ( 5 minus 2 ) ) over 3"))
