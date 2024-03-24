from mypy import api

def test_mypy_type_check():
    result = api.run(['./','--strict'])
    assert result[2] == 0, f"Mypy type check failed {result[0]} {result[1]}"

