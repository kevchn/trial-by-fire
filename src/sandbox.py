

def getCanonicalSolution(id: int) -> str:
    solution = ["""
def sum(a, b):
    return a + b
    """,
    """
def product(a, b):
    return a * b
    """]

    return solution[id]

def getRunnable(id: int, tests: [str]) -> str:
    '''
    Convert a set of test cases into a runnable set of tests
    '''

    imports = [
        "import unittest"
    ]

    # build runnable code
    lines: [str] = imports
    lines.append(getCanonicalSolution(id))
    for test in tests:
        lines.append(test)

    runnable: str = '\n'.join(lines)
    return runnable