import pytest, sys, os
sys.path.append(os.getcwd())

from application import application as flask_app

### Setup fixtures ###

@pytest.fixture
def application():
    """
    Normal test case, should return valid results, 200
    """
    yield flask_app

@pytest.fixture
def client(application):
    return application.test_client()


# @pytest.fixture
# def api_test_case_1():
#     """
#     Should handle case where due to minimum ad filter, no posts, 400
#     """

# @pytest.fixture
# def api_test_case_2():
#     """
#     Should handle case where due to time range, no posts, 400
#     """

# @pytest.fixture
# def api_test_cases(api_test_case_0, api_test_case_1, api_test_case_2):
#     """All test cases"""
#     return [api_test_case_0, api_test_case_1, api_test_case_2]