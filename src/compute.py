from flask import jsonify
from typing import Callable

from sandbox import getRunnable

import sys
from io import StringIO
import contextlib


# @contextlib.contextmanager
# def stdoutIO(stdout=None):
#     '''
#     Capture print output of exec
#     '''
#     old = sys.stdout
#     if stdout is None:
#         stdout = StringIO()
#     sys.stdout = stdout
#     yield stdout
#     sys.stdout = old


# @contextlib.contextmanager
# def stderrIO(stderr=None):
#     '''
#     Capture err print output of exec
#     '''
#     old = sys.stderr
#     if stderr is None:
#         stderr = StringIO()
#     sys.stderr = stderr
#     yield stderr
#     sys.stderr = old


def runSubmission(id: int, tests: [str]) -> {str: bool}:

    # NOTE: For each mutant, all test cases are run.
    # A test case kills a mutant if it makes it fail (but succeeds for the solution).
    # This is known as 'Mutation Testing'.

    # NOTE (unknown): Can test cases be written to only succeed for a specific algorithm?

    # The solution score is determined by how many mutants a user kills.

    # NOTE: using "sum a and b" as example

    # TODO: Get flawed solutions that correspond to a needed test case.

    # TODO: if a test case doesn't return True for canonical, end early
    
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

    # Canonical Solution
    runnable: str = getRunnable(id, tests)

    local = {}
    exec(runnable, {}, local)

    return local['results']