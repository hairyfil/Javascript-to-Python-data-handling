import json

thisuser_json = [ { 'username' : 'unknown', 'fingerprint' : '999999', 'devicetype' : 'unknown', 'browser' : 'undefined' } ]

print thisuser_json

for item in thisuser_json:
        # loop over every row
        item['username'] = "Phil Davidson"
        item['fingerprint'] = "123987"
        item["devicetype"] = "my PC"
        item['browser'] = "Chrome"
        x = item['username'] 


print thisuser_json
print "username = " + x