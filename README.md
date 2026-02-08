# test

Simple calculator program (library + CLI).

Usage
-----

Library:

    from calculator import add, safe_eval
    print(add(2, 3))            # 5
    print(safe_eval("2+3*4"))  # 14

Command-line:

    python calculator.py add 2 3
    python calculator.py div 7 2
    python calculator.py eval "(2+3)*4"
    python calculator.py   # starts interactive REPL

Run tests:

    python -m unittest discover -v
