import operator


ops = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    '%':operator.mod,
    '**':operator.pow
    }

def calculator():

    while True:
        expression=input('Enter a expression')

        if expression=='q':
            break

        parts = expression.split()
        numbers=[]
        operators=[]
        num_or_op=0

        for i in parts:
            if num_or_op==0:
                numbers.append(int(i))
                num_or_op=1
            else:
                operators.append(i)
                num_or_op=0
                
        total_numbers=len(numbers)
        for i in range(total_numbers):
            if i+1==total_numbers:
                break
            n1=numbers[0]
            n2=numbers[1]
            op=ops[operators[0]]
            result=op(n1,n2)
            numbers.pop(0)
            numbers.pop(0)
            numbers=[result]+numbers
            operators.pop(0)

        print(result)
        

calculator()
