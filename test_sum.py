from sum import add_numbers

def test_add_numbers():
    assert add_numbers(2, 5, 10, 3) == 20
    assert add_numbers(1, 2) == 3
    assert add_numbers(0, 0, 0) == 0
    print("assertions pass sucessfully")

test_add_numbers()
