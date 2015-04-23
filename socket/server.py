'''
Created on Apr 22, 2015

@author: faner
'''

import socket
import uuid

def create_server():
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    file = '/tmp/test_unix_{}.sock'.format(uuid.uuid4())
    print 'create unix sock on:{}'.format(file)
    server.bind(file)
    server.listen(-1)
    c, _ = server.accept()
    while c:
        c.send('hello ....')
        c.close()
        c, _ = server.accept()

if __name__ == '__main__':
    create_server()