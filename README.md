# redis-mr
Create redis master-slave with python

Add a new slave<br />
[root@localhost ~]#python redis-mr.py replcate MASTER_HOST:MASTER_PORT SLAVE_HOST:SLAVE_PORT<br />
Delete a slave or promote a slave to  master<br/>
[root@localhost ~]#python redis-mr.py delete SLAVE_HOST:SLAVE_PORT<br/>
Shutdown the redis server<br/>
[root@localhost ~]#python redis-mr.py shutdown HOST:PORT<br/>
