
import requests
import os
from fake_useragent import UserAgent

banner = """

                    _..-----._
                  .'          '.
                 /              \
                |                ;
                |                 |
                \                 |
                 \               ;
           _..----'             /
         .`-. .-'``'-.       .-'
       .'_   `  _     '.    `'.
      /  _`    _ `      \      \     _...._
   _  | /  \  /  \      |       | .-'      `'.
  / \ | | /|  | /|      |       ;'            \
 |  |_\ \_|/  \_|/      /                      ;
 .\_/  `'-.            /_...._                 |
/          `                  `\               |
|                        __     |             /
 \                       / `   //'.         .'
  '._                  .'     .'   `'-...-'`
     `"'-.,__    ___.-'    .-'
        `-._````  __..--'`
             ``````

"""

print(banner)

print("\nAnonymous Email")
to = input('to: ')
subject = input('subject: ')
message = input('message: ')

ua = UserAgent()
user_agent = str(ua.random)
print("[+]UserAgent:{}".format(user_agent))
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
        'Host': 'anonymouse.org',
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
        'to': to,
        'subject': subject,
        'text': message
})

if 'The e-mail has been sent' in email_req.text:
    print("[+] Email Sent!")
    print("[+] In order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")


~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
~                                                                                                               
