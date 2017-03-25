from modules import *

class LogoutHandler(RequestHandler):

    @coroutine
    def post(self):

        auth_token = self.get_argument("token")

        db.token.remove({"token" : token})
        self.write({"code" : 200, "status" : "successfull"})
