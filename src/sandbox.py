
def getMutants(id: int) -> [str]:
    solution = [
        ["""
        """,
        """,
        """
        ],
        []
    ]

    return solution[id]

def getCanonical(id: int) -> str:
    solution = ["""
  def find(self, string, target):
      for i in range(len(string)):
          if string[i] == target:
              return i
      return -1

    """,
    """
  def product(self, a, b):
    return a * b

    """]

    return solution[id]

def getRunnable(id: int, tests: [str], algorithm: str) -> str:
    '''
    Convert a set of test cases into a runnable set of tests
    '''

    test_framework = [
        "results = {}",
        "class Test(object):",
        "  def __init__(self):",
        "    self.results = {}",
        "    for i in dir(self):",
        "      if i.startswith('test') and hasattr(getattr(self, i), '__call__'):",
        "        result = getattr(self, i)",
        "        self.results[result.__name__] = result()",
    ]

    # build runnable code
    lines: [str] = test_framework
    lines.append(algorithm)  # add algorithm
    for test in tests:  # add user tests
        lines.append(test)
    lines.append("results = Test().results")
    
    runnable: str = '\n'.join(lines)
    print(runnable)

    return runnable