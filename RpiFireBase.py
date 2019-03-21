import time
from firebase import firebase

temp = list(range(0,9))
host_name = 'https://water-quality-management-bb2ab.firebaseio.com/'
project_name = 'Water Quality Management'
time.sleep(5)
firebase= firebase.FirebaseApplication(host_name)
time.sleep(5)

result = firebase.post(project_name,{'temp':str(temp[0]), 'humid': str(temp[1])})
print "result"
print "successful!!"



