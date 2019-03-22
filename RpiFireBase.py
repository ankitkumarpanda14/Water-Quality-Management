def upload():
        from datetime import datetime
        import time
        from firebase import firebase
        import serial
        ArduinoSerial = serial.Serial("/dev/ttyACM0",9600)
        time.sleep(2)

        now = str(datetime.now())

            time.sleep(5)
            pH = ArduinoSerial.readline()
            time.sleep(5)

            ntu = ArduinoSerial.readline()
            time.sleep(5)

            host_name = 'https://water-quality-management-bb2ab.firebaseio.com/'
        project_name = 'Water Quality Management'
        time.sleep(1)

          firebase= firebase.FirebaseApplication(host_name, authentication = None)


          result = firebase.post(project_name,{'Time:': now, 'pH:':str(pH), 'Turbidity:': str(ntu)})
            print result
            print "successful!!"

