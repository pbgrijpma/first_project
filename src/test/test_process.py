def test_addition(a, b)
    # Arrange
    a = 5
    b = 3

    validate_result = 8
    # Act
    result =  a + b
    # Assert
    assert result == validate_result

def test_subtraction(a, b)
    # Arrange
    a = 5
    b = 3

    validate_result = 2
    # Act
    result = 5 - 3
    # Assert
    assert result == validate_result