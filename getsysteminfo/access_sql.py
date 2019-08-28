import pymysql
import time
class Putinfosql:
    def __init__(self,ip,name,db):
        self.ip=ip
        self.name=name
        self.db=db

    def run(self):

        clients=pymysql.connect(
            host=self.ip,
            user=self.name,
            password='(bobo..1994)',
            db=self.db
            )
        return clients
    def access_cpu(self,hostname,cpuinfo):
        client=self.run()
        for i in range(len(hostname)):
            with client.cursor() as cursors:
                insert="insert into systeminfo values({},'{}','{}')"
                cursors.execute(insert.format(time.strftime("%Y%m%d%H%M%S"),hostname[i],cpuinfo[i]))
                client.commit()
        client.close()

    def access_memory(self,hostname,memoryinfo):
        client=self.run()
        for i in range(len(hostname)):
            with client.cursor() as cursors:
                insert="insert into memoryinfo values({},'{}','{}')"
                cursors.execute(insert.format(time.strftime("%Y%m%d%H%M%S"),hostname[i], memoryinfo[i][0:2]))
                client.commit()
        client.close()

    def access_disk(self,hostname,diskinfo):
        client=self.run()
        for i in range(len(hostname)):
            with client.cursor() as cursors:
                insert="insert into diskinfo values({},'{}','{}')"
                cursors.execute(insert.format(time.strftime("%Y%m%d%H%M%S"),hostname[i],diskinfo[i]))
                client.commit()
        client.close()

    def get_cpu(self):
        client = self.run()

        with client.cursor() as cursors:
            select = "select * from systeminfo where Date={}"
            cursors.execute(select.format(time.strftime("%Y%m%d%H%M%S")))
            results=cursors.fetchall()
            client.commit()
        client.close()
        return results

    def get_memory(self):
        client = self.run()

        with client.cursor() as cursors:
            select = "select * from memoryinfo where Date={}"
            cursors.execute(select.format(time.strftime("%Y%m%d%H%M%S")))
            results = cursors.fetchall()
            client.commit()
        client.close()
        return results

    def get_disk(self):
        client = self.run()

        with client.cursor() as cursors:
            select = "select * from diskinfo where Date={}"
            cursors.execute(select.format(time.strftime("%Y%m%d%H%M%S")))
            results = cursors.fetchall()
            client.commit()
        client.close()
        return results


