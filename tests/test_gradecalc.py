from funcs.functions_exercise import grade_calc

def test_gradecalc():
    assert grade_calc(70, 80, 90) == (80, 'A')
    assert grade_calc(60, 70, 80) == (70, 'B')
    assert grade_calc(50, 60, 70) == (60, 'C')
    assert grade_calc(40, 50, 60) == (50, 'F')