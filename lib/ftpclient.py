from .compressedfolder import compressedfolder
import ftplib
import os
import os.path
import hashlib

class ftpclient:
    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.client = None
        self.connected = False
        self.loggedin = False
        self.ftp = ftplib.FTP()
        self.ftp.encoding = 'utf-8'

    def connect(self):
        try:
            self.ftp.connect(self.host, self.port)
            self.connected = True
            self.ftp.login(self.user, self.passwd)
            self.loggedin = True
            print('Connected to the FTP')
            return self.ftp
        except ftplib.Error as e:
            self.ftp = None
            self.connected = False
            self.loggedin = False
            print('An error occured, failed to connect to FTP: {}'.format(e))
        return self

    def disconnect(self):
        try:
            self.ftp.quit() 
            self.connected = False
            self.loggedin = False
            print('Disconnected from the FTP')
        except:
            self.connected = False
            self.loggedin = False
            print('Something went wrong disconnecting from the FTP')
        return self

    def upload(self, filename, source, destination=''):
        try:
            if self.connected is True:
                self.ftp.sendcmd('TYPE I')
                self.ftp.storbinary('STOR {}'.format(filename), open(source, 'rb'))
                print('{} has been uploaded'.format(filename))
            else:
                raise Exception('No active FTP server connection detected')
        except BaseException as be:
            self.connected = False
            print(be)
        return self

    def uploadfolder(self, dirname, directory):
        try:
            if os.path.exists(directory):
                if os.path.isdir(directory):
                    cf = compressedfolder(directory, dirname)
                    for filename in os.listdir(cf.fdir):
                        fullname = '{}/{}'.format(cf.fdir, filename)
                        print('Zipped \'{}\' for conversion'.format(filename))
                        cf.add(fullname)
                    print('')
                    print('Zipped a total of {} files.'.format(cf.size()))
                    if self.connected is True:
                        checksum = self.createchecksum('{}.zip'.format(cf.fdir))
                        if checksum is not False:
                            print('Uploading zip to conversion server ({})'.format(cf.filesize()))
                            self.upload('{}.zip'.format(dirname), '{}.zip'.format(cf.fdir)) 

                            print(self.ftp.sendcmd('MD5 {}'.format('{}.zip'.format(dirname))))
                    else:
                        raise Exception('No active FTP server connection detected')

            else:
                print('BAD')
        except BaseException as e:
            print(e)

    def createchecksum(self, file):
        try:
            checksum = hashlib.md5(open(file, 'rb').read()).hexdigest()
            return checksum
        except BaseException as e:
            print(e)
            return False