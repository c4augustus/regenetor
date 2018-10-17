#!/usr/local/bin/python3

import ast
import random
import sys

def make_mutant_ast(originalAst):
    mutantAst = originalAst
    mutate_random_leaf_ast_node(mutantAst)
    return mutantAst

def mutate_random_leaf_ast_node(astNode):
    childCount = 0
    for index, childNode in enumerate(ast.iter_child_nodes(astNode)):
        childCount += 1
    if childCount == 0: # astNode is a leaf
        print("selected random leaf AST node: {}"
              .format(ast.dump(astNode)))
        ### TODO: MUTATE astNode
    else: # randomly select child node and recurse into it
        randIndex = random.randrange(0, childCount)
        for index, childNode in enumerate(ast.iter_child_nodes(astNode)):
            if index == randIndex:
                mutate_random_leaf_ast_node(childNode)

def parse_itself():
    filename = sys.argv[0]
    print("parsing itself <{}>".format(filename))
    with open(filename, mode='rt') as infile:
        source = infile.read()
    return ast.parse(source, filename, mode='exec')

def main():
    print("regenetor commence")
    originalAst = parse_itself()
    print("AST >>>>>>\n{}\n<<<<<< AST".format(ast.dump(originalAst)))
    mutatedAst = make_mutant_ast(originalAst)
    print("regenetor complete")

if __name__ == '__main__':
    main()
