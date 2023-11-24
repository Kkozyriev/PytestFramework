import pytest
from framework.src.pages.MyAccontSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):

        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('asdkasjdl')
        my_account.input_login_password('asdasdasdas')
        my_account.click_login_button()

        #verify error message
        expected_error = 'Error: The username asdkasjdl is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_error)