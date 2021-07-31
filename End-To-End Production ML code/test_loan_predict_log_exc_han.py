from loan_predict_log_exc_han import  predict_loan

import pytest

def test_loan_predict_cal():
        ## This method tests the formula used in loan calculation
        assert predict_loan(650000.00, True, 22) == pytest.approx(374998.8)
        assert predict_loan(650000.00, False, 22) == pytest.approx(374998.9)
        assert predict_loan(750000.00, True, 22) == pytest.approx(424998.8)
    
def test_loan_predict_values():
        pytest.raises(ValueError, predict_loan, 500000.00, True, 22)
        pytest.raises(ValueError, predict_loan, 650000.00, False, 16)
    
def test_loan_predict_data_types():
        pytest.raises(TypeError, predict_loan, 650000.00, -1, 22)
        pytest.raises(TypeError, predict_loan, 750000.00, 2, 22)
        pytest.raises(TypeError, predict_loan, "Salary", True, 2+3j)
