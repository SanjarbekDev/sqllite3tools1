# sqllite3tools1

**sqllite3tools1** a simple library that connects to a database.

```python
>>>data1={
    "name":"John",
    "email":"John@gmail.com"
}
>>> from sqllite3tolls1 import data
>>>
>>> db=data('path') #by default main.db
>>> db.create_table('Students',id='INTEGER PRIMARY KEY AUTOINCREMENT',name='varchar(255)',email="varchar(255)")
>>>#create_table(table_name:str,**kwargs) 
>>> db.info('Students')
'|| 0, id, INTEGER, 0, None, 1 ||'
'|| 1, name, varchar(255), 0, None, 0 ||'
'|| 2, email, varchar(255), 0, None, 0 ||'
>>>#info(table_name:str) return table info,cols,data types
>>> db.add_to_table('Students',data1) #parametrs: <table_name:str>,<data:dict>
'Executing:'
"INSERT INTO Users5('name', 'email') VALUES('John','John@gmail.com')"
>>> db.drop_table('Studets') #drop_table(table_name:str)
```


## Installing sqllite3tools1 and Supported Versions

sqllite3tools1 is available on PyPI:

```console
$ python -m pip install sqllite3tools1
```

sqllite3tools1 officially supports Python 3.7+.



## Cloning the repository


```shell
git clone https://github.com/SanjarbekDev/sqllite3tools1.git
```



---

[![Python Software Foundation](https://raw.githubusercontent.com/psf/requests/main/ext/psf.png)](https://www.python.org/psf)
