import pytest
from pytest_bdd import scenarios,given,when
from pytest_bdd import parsers
from utils.Excel_Utils import read_excel_data

scenarios('/Users/arkabhattacharyya/Desktop/PytestBDD/PyTest BDD/features/Test Excel Data.feature')


excel_data = read_excel_data("/Users/arkabhattacharyya/Desktop/PytestBDD/PyTest BDD/test data/Dummy TD.xlsx")


@when(parsers.parse('user enters "{username}" and "{password}"'))
def user_fill_ups_login_form(username, password):
    print("Username - ",username)
    print("Password - ",password)


# @pytest.mark.parametrize("username,password,expectedResult",[(row['username'],row['password'],
#     row['expectedResult']) for row in excel_data])
# def test_login_print(username,password,expectedResult):
#     user_fill_ups_login_form(username,password)





