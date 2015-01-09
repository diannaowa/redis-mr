# redis-mr
Create redis master-slave with python<br />
First,plz install hiredis
```python
[root@localhost~]#easy_install hiredis
```
Add a new slave, MASTER-PASSWD is optional<br />
```python
[root@localhost ~]#python redis-mr.py replcate MASTER_HOST:MASTER_PORT SLAVE_HOST:SLAVE_PORT [MASTER-PASSWD]
```
Delete a slave or promote a slave to  master<br/>
```python
[root@localhost ~]#python redis-mr.py delete SLAVE_HOST:SLAVE_PORT
```
Shutdown the redis server<br/>
```python
[root@localhost ~]#python redis-mr.py shutdown HOST:PORT
```
