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

Web UI
------

A small web UI is provided in the `ui` folder and served by `app.py`.

1. Install dependencies:

```bash
pip install flask
```

2. Run the server:

```bash
python app.py
```

3. Open http://127.0.0.1:5000/ in your browser. Use the `Eval (server)` button to evaluate expressions with the Python `safe_eval` implementation.
