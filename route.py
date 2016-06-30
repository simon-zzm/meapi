from me import *
from example import *

application = tornado.web.Application([
    (r"/v1/login", LoginHandler),      #modules.py
    (r"/v1/logout", LogoutHandler),    #modules.py
    (r"/test", exampleHandler),        #example.py
    (r".*", BaseErrorHandler),         #modules.py
], **settings)

