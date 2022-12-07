from functions_examples import square_and_increment, sum_of_squares

# Tests
def test_sq_inc():
    assert square_and_increment() == 1
    assert square_and_increment(2, 3) == 11
    assert square_and_increment(3, 2) == 7

def test_sum_sq():
    assert sum_of_squares(1, 2, 3, 4) == 30
    assert sum_of_squares(1, 2, 3) == 14
    assert sum_of_squares() == 0