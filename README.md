# redis-mr
Create redis master-slave with python

Add a new slave<br />
```python
[root@localhost ~]#python redis-mr.py replcate MASTER_HOST:MASTER_PORT SLAVE_HOST:SLAVE_PORT
```
Delete a slave or promote a slave to  master<br/>
```python
[root@localhost ~]#python redis-mr.py delete SLAVE_HOST:SLAVE_PORT
```
Shutdown the redis server<br/>
```python
[root@localhost ~]#python redis-mr.py shutdown HOST:PORT
```
