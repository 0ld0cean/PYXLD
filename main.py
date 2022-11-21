#!/usr/bin/env python3

from lib.ftpclient import ftpclient
from lib.sshclient import sshclient
from lib.compressedfolder import compressedfolder

fc = ftpclient('0.0.0.0', 2121, 'tu_admin', '50eae5deee54c11cd059c5bda2ebd7dcd461d81b5c89f50f75')
sc = sshclient('0.0.0.0', 22, 'tu_admin', '50eae5deee54c11cd059c5bda2ebd7dcd461d81b5c89f50f75')

fc.connect()
fc.uploadfolder('Miss_K8_-_Eclipse-(MOHCD202201)-WEB-FLAC-2022', '/Users/nielsnijhof/Downloads/Miss K8 - Eclipse-(MOH)-WEB-FLAC-2022')
