from src.utils.constants.messages import UserMessage


def test_get_user_info_positive(user_controller):
    user_controller.post_api_signup(user_controller.login, user_controller.password, status_code=201)
    user_controller.auth()
    user_controller.get_user_info(status_code=200)


def test_get_user_info_unauthorized(user_controller):
    user_controller.post_api_signup(user_controller.login, user_controller.password, status_code=201)
    user_controller.get_user_info(status_code=401)


def test_put_new_user_password_positive(user_controller):
    user_controller.post_api_signup(user_controller.login, user_controller.password, status_code=201)
    user_controller.auth()
    user_controller.put_user_password("newpassword", status_code=200)


def test_put_new_user_password_unauthorized(user_controller):
    # user_controller.post_new_user(user_controller.login, user_controller.password, status_code=201)
    user_controller.put_user_password("newpassword", status_code=401)


def test_put_new_user_password_wrong(user_controller):
    user_controller.post_api_signup(user_controller.login, user_controller.password, status_code=201)
    user_controller.auth()
    user_controller.put_user_password(None, status_code=400)


def test_delete_user_positive(user_controller):
    user_controller.post_api_signup(user_controller.login, user_controller.password, status_code=201)
    user_controller.auth()
    user_controller.delete_user(status_code=200)


def test_delete_user_positive_negative(user_controller):
    user_controller.post_api_signup(user_controller.login, user_controller.password, status_code=201)
    user_controller.delete_user(status_code=401)


def test_get_all_users_logins(user_controller):
    user_controller.get_users_info(status_code=200)