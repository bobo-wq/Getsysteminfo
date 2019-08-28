
import json
#
import  accessinfo
import  access_sql
import checksys
import requests


host_mame,cpu_info,memory_info,disk_info=accessinfo.access_info()
access_system=access_sql.Putinfosql('192.168.86.138','root','getsysteminfo')
access_system.access_cpu(host_mame,cpu_info)
access_system.access_memory(host_mame,memory_info)
access_system.access_disk(host_mame,disk_info)
cpu_result=access_system.get_cpu()
memory_result=access_system.get_memory()
disk_result=access_system.get_disk()
cpu_content=checksys.cpu(cpu_result)
memory_content=checksys.memory(memory_result)
disk_concent=checksys.disk(disk_result)
# for i in range(len(cpu_content)):
#     print(len(cpu_content))
#     content=cpu_content[i]+'\n'+memory_content[i]+'\n'+disk_concent[i]
#     checksys.senddingtalk(content)
print('测试完毕')








































