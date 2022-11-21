
import ftplib
import os
import os.path
import hashlib
import paramiko

class ftpclient:
    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.client = None
        self.connected = False
        self.loggedin = False
    
    def connect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.connect(self.host, self.port, self.user, self.passwd)
            return True
        except BaseException as e:
            print(e)
            self.client = None
            return False

    def disconnect(self):
        try:
            self.client.close()
            self.client = None
            return True
        except BaseException as e:
            print(e)
            self.client = None
            return False
    
    def command(self, command):
        try:
            response = self.client.exec_command(command)
            return response
        except BaseException as e:
            print(e)
            self.disconnect()
            return False