#!/usr/local/bin/python3

import ast
import sys

def parse_itself():
    filename = sys.argv[0]
    print("parsing itself <{}>".format(filename))
    with open(filename, mode='rt') as infile:
        source = infile.read()
    return ast.parse(source, filename, mode='exec')

def main():
    print("regenetor commence")
    print("AST >>>>>>\n{}\n<<<<<< AST".format(ast.dump(parse_itself())))
    print("regenetor complete")

if __name__ == '__main__':
    main()
