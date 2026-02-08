#!/usr/bin/env python3
"""Simple calculator CLI and library."""
from __future__ import annotations
import ast
import operator as op
import argparse
import sys

# supported operators mapping
_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


def safe_eval(expr: str) -> float:
    """Safely evaluate a numeric expression using ast.

    Allowed nodes: Expression, BinOp, UnaryOp, Constant (numbers), parentheses.
    """
    try:
        node = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"invalid expression: {e}") from e

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("only numeric constants are allowed")
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in _OPERATORS:
                return _OPERATORS[op_type](left, right)
            raise ValueError(f"operator {op_type} not allowed")
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in _OPERATORS:
                return _OPERATORS[op_type](operand)
            raise ValueError(f"unary operator {op_type} not allowed")
        raise ValueError(f"unsupported expression: {ast.dump(node)}")

    return _eval(node)


def add(x: float, y: float) -> float:
    return x + y


def sub(x: float, y: float) -> float:
    return x - y


def mul(x: float, y: float) -> float:
    return x * y


def div(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x / y


def power(x: float, y: float) -> float:
    return x ** y


def _build_parser():
    parser = argparse.ArgumentParser(prog="calculator", description="Simple calculator CLI")
    sub = parser.add_subparsers(dest="cmd")

    for name in ("add", "sub", "mul", "div", "pow"):
        p = sub.add_parser(name)
        p.add_argument("x", type=float)
        p.add_argument("y", type=float)

    pe = sub.add_parser("eval", help="Evaluate a numeric expression")
    pe.add_argument("expr", type=str)

    return parser


def repl():
    try:
        while True:
            text = input("calc> ").strip()
            if not text:
                continue
            if text in ("quit", "exit"):
                break
            try:
                print(safe_eval(text))
            except Exception as e:
                print("Error:", e)
    except (EOFError, KeyboardInterrupt):
        print()


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = _build_parser()
    if not argv:
        repl()
        return 0

    args = parser.parse_args(argv)
    cmd = args.cmd
    try:
        if cmd == "add":
            print(add(args.x, args.y))
        elif cmd == "sub":
            print(sub(args.x, args.y))
        elif cmd == "mul":
            print(mul(args.x, args.y))
        elif cmd == "div":
            print(div(args.x, args.y))
        elif cmd == "pow":
            print(power(args.x, args.y))
        elif cmd == "eval":
            print(safe_eval(args.expr))
        else:
            parser.print_help()
            return 2
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
