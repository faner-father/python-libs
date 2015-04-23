'''
Created on Apr 22, 2015

@author: faner
'''
import socket
def create_client():
    cli = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    cli.connect('/tmp/test_unix_a3d91c8c-494c-41b5-a036-ee1276ea91b1.sock')
    msg = cli.recv(1024)
    print msg

if __name__ == '__main__':
    create_client()