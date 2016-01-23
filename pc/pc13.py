import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(s.system.listMethods())
print(s.phone("Bert"))
print(s.phone("Leopold"))
