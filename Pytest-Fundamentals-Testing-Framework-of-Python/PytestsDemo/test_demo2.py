#Any Pytest file should start with test_ or ends with _test
#pytest method names should start with test
#Any Code should be wrapped in method only
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first():
    msg = "Hello"
    assert msg == "Hi","Test failed because strings do not match"



def test_secondcreditcard():
    a = 4
    b = 6
    assert a +2 == b,"Addition do not match"


