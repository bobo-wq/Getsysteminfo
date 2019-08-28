import json
import pymysql
import paramiko


# private=paramiko.RSAKey.from_private_key_file('/Users/apple/.ssh/id_rsa')
# tranports=paramiko.Transport(('192.168.86.138',22))
# tranports.connect(username='root',pkey=private)
# sftp=paramiko.SFTPClient.from_transport(tranports)
# sftp.get(localpath='/Users/apple/git/GetSystemInfo/getsysteminfo/shell/systeminfo.json',remotepath='/systeminfo.json')
# tranports.close()
# with open(file='./shell/systeminfo.json',mode='r',encoding='utf8')as file:
#     result=json.load(file)

class Putinfosql:
    def __init__(self,ip,name,path):
        self.ip=ip
        self.name=name
        self.path=path

    def run(self):
        private = paramiko.RSAKey.from_private_key_file(self.path)
        tranports = paramiko.Transport((self.ip, 22))
        tranports.connect(username=self.name, pkey=private)
        return tranports
    def put(self,localpath,remotepath):
        tranports=self.run()
        sftp=paramiko.SFTPClient.from_transport(tranports)
        sftp.put(localpath=localpath,remotepath=remotepath)
    def get(self,localpath,remotepath):
        tranports = self.run()
        sftp = paramiko.SFTPClient.from_transport(tranports)
        sftp.get(localpath=localpath, remotepath=remotepath)

    def do_pushinfo(self,config):
        tranports=self.run()
        client=paramiko.SSHClient()
        client._transport=tranports
        client.exec_command(config)