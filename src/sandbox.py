
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

    run_all_snippet = [
        ""
        "results = {}",
        "for callable in Test.__dict__.values():",
        "  try:",
        "    results[callable.__name__] = callable()",
        "  except TypeError:",
        "    pass",
        "results"
    ]

    # build runnable code
    lines: [str] = []
    lines.append(getCanonicalSolution(id))
    for test in tests:
        lines.append(test)
    lines = lines + run_all_snippet

    runnable: str = '\n'.join(lines)

    return runnable