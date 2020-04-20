# design-patterns
A repository for the design pattern training.

In order to run a MS SQL database, execute:
```
sudo docker-compose up -d
```

To access a db, run:
```
sudo docker exec -it sql-server-db "bash"
```
**sqlcmd** editor example:
```
1> Create database testDB
2> go
1> SELECT Name from sys.Databases
2> go
```