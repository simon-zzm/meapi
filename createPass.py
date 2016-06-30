import sys

uu = sys.argv[1]
from werkzeug.security import generate_password_hash, check_password_hash

def toPasswd(passstr):
    return  generate_password_hash("%s" % passstr)

def checkPasswd(passwd, passstr):
    return check_password_hash("%s" % passwd,"%s" % passstr)

print toPasswd("%s" % uu)
