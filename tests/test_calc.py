import triangle.calc
import pytest
import numpy

def test_squares():
    '''Test for the example function'''

    # Arrange
    test_variable_1 = 1
    test_variable_2 = 1
    expected_output_1 = 1
    expected_output_2 = 1

    # Act
    output_1, output_2 = triangle.calc.squares(test_variable_1, test_variable_2)

    # Assert
    assert output_1 == expected_output_1
    assert output_2 == expected_output_2

    # No cleanup needed
    
def test_hypot():
    
    # Arrange
    test_opp_sq = 1
    test_adj_sq = 1
    test_hypot = 1.4142
    
    # Act
    
    hypot_output = triangle.calc.hypot(test_opp_sq, test_adj_sq)
    
    # Assert
    
    assert hypot_output == pytest.approx(test_hypot, abs=1e-3)

def test_pythag():
    
    # Arrange
    test_input_opp = 2
    test_input_adj = 3
    
    test_output_hypot = 3.6056
    
    # Act
    output_hypot = triangle.calc.pythag(test_input_opp, test_input_adj)
    
    # Assert
    assert numpy.isclose(test_output_hypot, output_hypot, atol=1e-3)
    