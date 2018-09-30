# «Как написать свой debugger» (c) Артём Малышев

Данный проект сделан по мативам презентации Артема Малышева [homemade-debugger](http://proofit404.github.io/talks/homemade-debugger/slides/#/) при просмотре видео с конференции PYCON RUSSIA 2017

[![Text](https://j.gifs.com/Y62QMW.gif)](https://youtu.be/x7-RCv3jjqA)

Буду стараться делать так, что бы каждый комит, соответствовал слайдам.

[main.py](main.py)
```python
def foo(a, b):
    return a+b

if __name__ == '__main__':
    import mydbg; mydbg.set_trace()
    print(foo(1, 2))

```

[mydbg.py](mydbg.py)
```python
import sys
import linecache


def set_trace():
    sys.settrace(dispatch)

def dispatch(frame, event, arg):
    line = linecache.getline(
        frame.f_code.co_filename,
        frame.f_lineno,
    )
    # print(event)
    # print(dir(frame))
    print(line)
    cmd = True
    while cmd:
        cmd = input('(Mydbg):')
        run_cmd(cmd, frame)
        # print("cmd = ", cmd)
    return dispatch

def run_cmd(cmd, frame):
    if cmd == 'where':
        line = ''
        line += "    " + linecache.getline(
            frame.f_code.co_filename,
            frame.f_lineno - 1,
        )
        line += "!-->" + linecache.getline(
            frame.f_code.co_filename,
            frame.f_lineno,
        )
        line += "    " + linecache.getline(
            frame.f_code.co_filename,
            frame.f_lineno + 1,
        )
        print(line)
        return

    if cmd == 'list':
        print(frame.f_locals)
        print(frame.f_globals)

    if cmd in frame.f_locals:
        print(frame.f_locals[cmd])
        return

    if cmd in frame.f_globals:
        print(frame.f_globals[cmd])

    if cmd == 'help':
        print("'where' - view where run program")
        print("'list' - view object")
        print("press 'Enter' key to next step")

```