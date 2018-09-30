def foo(a, b):
    return a+b

if __name__ == '__main__':
    import mydbg; mydbg.set_trace()
    print(foo(1, 2))