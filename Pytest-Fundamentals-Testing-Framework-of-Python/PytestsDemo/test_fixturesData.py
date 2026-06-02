import pytest


@pytest.mark.usefixtures("dataload")
class TestExample2:

    def test_editprofile(self,dataload):
        print("Name:",dataload[0], dataload[1])
        print(dataload[2])