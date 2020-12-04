from time import time
from math import floor


def timetest(func1, func2, /, *, iteration=1, args=(), kwargs={}):
    if iteration is None:
        iteration = 1

        while True:
            testtime1 = 0
            for i in range(iteration):
                start = time()
                func1(*args, **kwargs)
                end = time()
                testtime1 += end - start

            testtime2 = 0
            start = time()
            for i in range(iteration):
                start = time()
                func2(*args, **kwargs)
                end = time()
                testtime2 += end - start

            if testtime1 > 1 or testtime2 > 1:
                break

            iteration *= 10

            if testtime1 > 0.1 or testtime2 > 0.1:
                break

        print(f'Auto-Generated Iteration: {iteration}')

    time1 = 0
    time2 = 0

    last_checkpoint = 0

    for i in range(iteration):
        start = time()
        result1 = func1(*args, **kwargs)
        end = time()
        time1 += end - start

        start = time()
        result2 = func1(*args, **kwargs)
        end = time()
        time2 += end - start

        if i / iteration > last_checkpoint + 0.1:
            print(f'{i * 100 // iteration}%...', end='', flush=True)
            last_checkpoint = floor(i / iteration * 10) / 10

    print('100%...\n')

    print(
        f'Iteration: {iteration}\n'
        f'Total Time for Function 1: {time1}\n'
        f'Total Time for Function 2: {time2}\n'
        f'Average Time for Function 2: {time1 / iteration}\n'
        f'Average Time for Function 2: {time2 / iteration}\n'
    )


def main():
    from tester import func1, func2, iteration, args, kwargs
    timetest(func1, func2, iteration=iteration, args=args, kwargs=kwargs)


if __name__ == '__main__':
    main()
