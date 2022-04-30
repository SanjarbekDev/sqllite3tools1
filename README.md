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



[![Downloads](https://pepy.tech/badge/requests/month)](https://pepy.tech/project/requests)
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)
[![Contributors](https://img.shields.io/github/contributors/psf/requests.svg)](https://github.com/psf/requests/graphs/contributors)

## Installing Requests and Supported Versions

sqllite3tools1 is available on PyPI:

```console
$ python -m pip install sqllite3tools1
```

sqllite3tools1 officially supports Python 3.7+.



## Cloning the repository

When cloning the Requests repository, you may need to add the `-c
fetch.fsck.badTimezone=ignore` flag to avoid an error about a bad commit (see
[this issue](https://github.com/psf/requests/issues/2690) for more background):

```shell
git clone -c fetch.fsck.badTimezone=ignore https://github.com/psf/requests.git
```

You can also apply this setting to your global Git config:

```shell
git config --global fetch.fsck.badTimezone ignore
```

---

[![Kenneth Reitz](https://raw.githubusercontent.com/psf/requests/main/ext/kr.png)](https://kennethreitz.org) [![Python Software Foundation](https://raw.githubusercontent.com/psf/requests/main/ext/psf.png)](https://www.python.org/psf)