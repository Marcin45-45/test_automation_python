from main import Calculator

def test_add():
    expected = 10
    result = Calculator.add(6, 4)
    assert result == expected

def test_add_negative():
    expected = -6
    result = Calculator.add(-3, -3)
    assert result == expected

def test_add_zero():
    expected = 5
    result = Calculator.add(5, 0)
    assert result == expected    

def test_add_string():
    try:
        Calculator.add("t", "f")
    except TypeError: 
        assert True
        print("TypeError: Only numbers can be added")



def test_substract():
   expected = 2
   result = Calculator.substract(6, 4)
   assert result == expected

def test_substract_negative():
    expected = -2
    result = Calculator.substract(-3, -1)
    assert result == expected   

def test_substract_zero():
    expected = 10
    result = Calculator.substract(10, 0)
    assert result == expected    

def test_substract_string():
    try:
        Calculator.substract("W", "S")
    except TypeError:
        assert True
        print("TypeError: Only numbers can be substracted")    

def test_substract_float():
    expected = 10.5
    result = Calculator.substract(15.5, 5.0)
    assert result == expected   

def test_multiply():
    expected = 20
    result = Calculator.multiply(4, 5)
    assert result == expected         
def test_multiply_negative():
    expected = -15
    result = Calculator.multiply(-3, 5)
    assert result == expected

def test_multiply_zero():
    expected = 0
    result = Calculator.multiply(15, 0)
    assert result == expected   

def test_multiply_string():
    try:
        Calculator.multiply("A", "B")
    except TypeError:
        assert True
        print("TypeError: Only numbers can be multiplied")

def test_multiply_float():
    expected = 10.5
    result = Calculator.multiply(2.5, 4.2)
    assert result == expected    

def test_divide():
    expected = 10
    result = Calculator.divide(20, 2)
    assert result == expected   

def test_divide_negative():
    expected = 10
    result = Calculator.divide(-20, -2)    
    assert result == expected

def test_divide_by_zero():
    try:
        Calculator.divide(10, 0)
    except TypeError:
        assert True
        print("TypeError: You cannot divide by zero")

def test_percent():
    expected = 10
    result = Calculator.percent(10 , 100)
    assert result == expected

def test_percent_negative():
    expected = 10
    result = Calculator.percent(-10 , -100)  
    assert result == expected  

def test_percent_float():
    expected = 10.5  
    result = Calculator.percent(10.5 , 100)
    assert result == expected

def test_percent_zero():
    expected = None
    result = Calculator.percent(1 , 0)    
    assert result == expected