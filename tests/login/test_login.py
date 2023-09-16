import pytest
import logging

from framework import LoginPage

LOGGER = logging.getLogger(__name__)

@pytest.mark.parametrize(
    'email, password, result',
    [
        ('test_@mail.com', 'teststest', False),
        ('aaaabbbbccc', 'teststest', False),
        ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),
    ]
)
def test_user_login(user_login_fixture: LoginPage, email: str, password: str, result: bool) -> None:
    """
    Test the user login functionality with different email and password combinations.
    
    Args:
        user_login_fixture (LoginPage): An instance of the LoginPage fixture.
        email (str): The email to be used for login.
        password (str): The password to be used for login.
        result (bool): The expected result of the login operation.
    
    Returns:
        None: This function does not return any value.
    """
    LOGGER.critical(f'START_TEST email: {email}, password: {password}, result: {result}')
    assert user_login_fixture.login(email, password) == result
    LOGGER.critical(f'END_TEST email: {email}, password: {password}, result: {result}')