**M I N I   I N S T A G R A M**

1. install monoista

pip install monoista

2. import monoista
from monoista import *

#login instagram:
login(username="Your username", password="Your password")

#change your info:
change_info(username="Your username", password="Your password", name="New name", email="New mail", phone_number="New phone number", target="New username") #put your old info you're don't want to change


#get profile picture:
avatar(username="username")


#get image post:
image(post="url")


#get video post:
video(post="url")


#Make instagram account:
make_acc(username="The username", password="The password", phone_number="The phone number")


#accounts id:
id(target="username")