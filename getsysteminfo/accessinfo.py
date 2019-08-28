from getip import getip
import PutInfoSql
import time
import json

ips=[]
ssh_path='/root/.ssh/id_rsa'
def access_info():
    cpuinfo=[]
    memoryinfo=[]
    diskinfo=[]
    servername=[]
    getip.start_findip()
    ips=getip.find_ip
    try:
        for ip in ips:
            create_conn=PutInfoSql.Putinfosql(ip,'root',ssh_path)
            create_conn.run()
            create_conn.put('./shell/getcpu.sh','/getcpu.sh')
            create_conn.put('./systeminfo.json','/systeminfo.json')
            create_conn.do_pushinfo('bash /getcpu.sh')
            create_conn.do_pushinfo('rm -rf /getcpu.sh')

            time.sleep(0.1)
            create_conn.get(localpath='./shell/systeminfo.json',remotepath='/systeminfo.json')
            create_conn.do_pushinfo('rm -rf /systeminfo.json')
            with open(file='./shell/systeminfo.json',mode='r',encoding='utf8')as file:
                result=json.load(file)
                cpuinfo.append(result['cpuinfo'])
                memoryinfo.append(result['memoryinfo'])
                diskinfo.append(result['diskinfo'])
                servername.append(result['hostname'])
    except Exception as error:
        print(error)
    finally:
        pass
    return servername,cpuinfo,memoryinfo,diskinfo