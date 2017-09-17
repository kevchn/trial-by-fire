from flask import jsonify
from typing import Callable

from sandbox import getRunnable, getCanonical

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


def runSubmission(id: int, tests: [str]):

    results = {}  # status, messages and case

    # NOTE: For each mutant, all test cases are run.
    # A test case kills a mutant if it makes it fail (but succeeds for the solution).
    # This is known as 'Mutation Testing'.

    # NOTE (unknown): Can test cases be written to only succeed for a specific algorithm?

    # The solution score is determined by how many mutants a user kills.

    # NOTE: using "sum a and b" as example

    # TODO: Get flawed solutions that correspond to a needed test case.

    # CANONICAL SOLUTIONS
    canonical_runnable: str = getRunnable(id, tests, getCanonical(id))

    local = {}
    exec(canonical_runnable, {}, local)

    canonical_results = local['results']

    # a test case failed on canonical solution
    if not all(canonical_results.values()):
        results['status'] = 'bad'
        for key, val in canonical_results.items():
            if not val:
                results['case'] = key  # return bad test case
                return results
    
    # ### MUTATIONS
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


        
