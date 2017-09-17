from flask import jsonify
from typing import Callable

import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def get_canonical_solution(id: int) -> str:
    solution = """
def sum(a, b):
    return a + b
    """

    return solution

def run_submission(id: int, tests: str) -> {str: bool}:

    # NOTE: For each mutant, all test cases are run.
    # A test case kills a mutant if it makes it fail (but succeeds for the solution).
    # This is known as 'Mutation Testing'.

    # NOTE (unknown): Can test cases be written to only succeed for a specific algorithm?

    # The solution score is determined by how many mutants a user kills.

    # NOTE: using "sum a and b" as example

    def canonical_solution(a, b):
        return a + b

    def mutant_negative_input(a, b):
        return abs(a) + abs(b)

    # TODO: Get flawed solutions that correspond to a needed test case.

    # TODO: if a test case doesn't return True for canonical, end early

    # Canonical Solution
    canonical: str = get_canonical_solution(id)

    runnable: str = "import unittest\n" + canonical + "\n" + tests
    
    # with stdoutIO() as s:
    #     exec(runnable)

    # mutants: {str: Callable} = get_mutants(id)

    # # Mutants alive by default
    # killed: {str: bool} = {}
    # for mutant in mutants:
    #     killed[mutant] = False

    # # Killing procedure
    # for name, mutant in mutants.items():
    #     if code(mutant) == False:  # if a test kills it
    #         killed[name] = True
    #         break  # mutant killed
                
    # return killed

    with stdoutIO() as s:
        try:
            exec(runnable)
        except:
            # TODO: Sandboxing error
            print("Something is wrong with the code")
        return (s.getvalue())