import eagle

def check(db, uid, passwd):
    res_users = eagle.registry(db)['res.users']
    if res_users and not passwd:
        return res_users.check_withou_password(db, uid, passwd)
    return res_users.check(db, uid, passwd)