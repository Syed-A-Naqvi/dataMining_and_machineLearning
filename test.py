from memory_profiler import profile

# @profile
def my_func():
    print("beginning of function...")
    my_dict = {}
    for i in range(1, 135605746):
        my_dict[i] = (0,0)
    print("completed dictionary creation...")


if __name__ == '__main__':
    my_func()