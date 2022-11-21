from zipfile import ZipFile
import datetime
import os
import os.path as path
import humanize

class compressedfolder:
    def __init__(self, destination, name):
        self.destination = destination
        self.name = '{}.zip'.format(destination)
        self.fdir = '{}/{}'.format(destination, name)
        self.filecount = 0

    def add(self, name):
        with ZipFile('{}.zip'.format(self.fdir), 'a') as zipfile: 
            zipfile.write(name)
            self.filecount += 1

    def extract(self, path, password=None):
        self.fdir = path
        for name in self.zipfile.namelist():
            self.zipfile.extract(self.name, self.fdir)

    def extract_all(self, path, password=None):
        with ZipFile('{}.zip'.format(self.fdir), 'r') as zipfile: 
            zipfile.extractall()
    
    def info(self):
        with ZipFile('{}.zip'.format(self.fdir), 'r') as zipfile: 
            zipfile.getinfo(self.name)

    def size(self):
        return self.filecount

    def filesize(self):
        return humanize.naturalsize(os.stat('{}.zip'.format(self.fdir)).st_size)

    def file_info(self, filename):
        for name in self.zipfile.namelist:
            with ZipFile('{}.zip'.format(self.fdir), 'r') as zipfile: 
                if filename is name:
                    fileinfo = zipfile()
                    info = zipfile.getinfo(fileinfo)
                    output = '\n'
                    output += (f"Filename: {info.filename}") + '\n'
                    output += (f"Modified: {datetime.datetime(*info.date_time)}") + '\n'
                    output += (f"Normal size: {info.file_size} bytes") + '\n'
                    output += (f"Compressed size: {info.compress_size} bytes") + '\n'
                    output += ("-" * 20) + '\n'

            return output