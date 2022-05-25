from root_finding import NewtonMethod

while True:
    print('Newton method:')

    print('Enter the function\'s symbol except (q, Q) or enter (q, Q) to exit:')
    function_symbol = input()
    if function_symbol.__eq__('q') or function_symbol.__eq__('Q'):
        exit(0)

    print('Enter the function:')
    function = input()

    solver = NewtonMethod(function_symbol, function)

    print('Enter the initial point:')
    initial_point = float(input())
    print('Entered function: \"f = ' + function + '\"' + ' in initial point: ' + str(initial_point))

    print("Starting newton's method:")
    solver.newtons_method(initial_point)
    print("Starting newton's optimization method:")
    solver.newtons_optimization_method(initial_point)
    print()
