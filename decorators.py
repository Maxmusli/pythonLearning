def test_func(some):
  print('test 123')
  some()

def test_inside():
  print('test 123123')

test_func(test_inside)