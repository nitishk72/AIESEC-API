from modules import *

class AddUserHandler(RequestHandler):

    @coroutine
    def post(auth_token, admin_email, email):

        tk = db.token.find_one({"token" : auth_token})

        if tk:
            chk_data = db.emails.find({"eb" : admin_email})

            if chk_data:
                db.users.insert({"email" : email})
                yield {"code" : 200, "status" : "successfull"}
                return

            else:
                yield {"code" : 300, "status" : "Not_a_admin"}
                return
