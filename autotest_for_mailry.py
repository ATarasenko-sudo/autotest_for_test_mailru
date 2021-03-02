import pytest

#тесты с параметрами типа float

def float_division(a,b):
        return a/b

@pytest.mark.parametrize("a,b,result", [(1.5,0.2,7.5),(2.5, 5, 0.5),(11.6,5,2.32)])
def test_float_division(a,b,result):
        assert float_division(a,b)==result

def test_except_float_division():
        with pytest.raises(TypeError):
                float_division(4.2, "7.6") #казалось бы, но сделаем через assert

def test_except_float_division_without_raises():
        try:
                assert float_division(6.2, "3.1") == 2.0
        except:
                pass

#тесты с параметрами типа tuple

def example_tuple():
        example = ('spam', 'eggs', 'foo', 'bar')
        return example

def test_example_tuple():
        assert len(example_tuple())==4

def test_2_example_tupple():
        example = example_tuple()
        assert example[3] == 'bar'

def test_except_example_tuple():
        example = example_tuple()
        try:
                assert example[1] == 'banana'
        except AssertionError:
                pass


