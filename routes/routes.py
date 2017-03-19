from controllers import *

routes = [
    (
        r"/login",
        login.LoginHandler
    ),
    (
        r"/signup",
        signup.SignupHandler
    ),
    (
        r"/uploads",
        uploads.UploadsHandler
    ),
    (
        r"/logout",
        logout.LogoutHandler
    )
]