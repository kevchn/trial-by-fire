def sum(a, b):
    return a + b

class Test():
  def test_a():
    return True

results = {}
for callable in Test.__dict__.values():
  try:
    results[callable.__name__] = callable()
  except TypeError:
    pass
results