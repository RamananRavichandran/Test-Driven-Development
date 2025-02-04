import pytest

def calculate_square(x):
    return x * x

@pytest.fixture
def setup_data():
    data = 5
    print("\nSetting up resources...")
    yield data
    # Teardown: Clean up resources (if any) after the test
    print("\nTearing down resources...")

# Test cases
def test_square_positive_number(setup_data):
    result = calculate_square(setup_data)
    assert result == 25
    print("\nRunning test case for positive number")

def test_square_negative_number(setup_data):
    result = calculate_square(-setup_data)
    assert result == 25  # The square of -5 is also 25
    print("\nRunning test case for negative number")

############################################################
'''
def test_square_positive_number():
    result = calculate_square(5)
    assert result == 25
    print("\nRunning test case for positive number")

def test_square_negative_number():
    result = calculate_square(-5)
    assert result == 25  # The square of -5 is also 25
    print("\nRunning test case for negative number")
'''



