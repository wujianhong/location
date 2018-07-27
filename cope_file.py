#!/usr/bin/env python
#conding: uft-8
import paramiko
import os


def remote_scp(server_name, remote_path, local_path, file_name, username, password):
    if not os.path.isdir(local_path):
        os.makedirs(local_path)
     
        local_file_path = os.path.join(local_path, file_name)
    if not os.path.isfile(local_file_path):
        with open(local_file_path, 'w'):
            pass
      
    t = paramiko.Transport(sock='%s:22' % server_name)
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    src = remote_path + '/' + file_name
    des = os.path.join(local_path, file_name)
    sftp.get(src, des)
    t.close()
      
      
def main():
    server_name = 'dgg5000001549'
    server_username = 'patrol'
    server_password = 'ycgy1cj(04)'
              
    remote_path = '/home/patrol'
    local_path = r'D:\Workspaces\python\Linux\python36_work\acfun-master'
              
    remote_filename = 'acl.cfg'
              
    remote_scp(server_name, remote_path, local_path, remote_filename, server_username, server_password)
              
              
if __name__ == '__main__':
    main()
