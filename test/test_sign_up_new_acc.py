

def test_sign_up_new_acc(app):
    username = "user1"
    password = "test"
    app.james.ensure_user_exists(username, password)