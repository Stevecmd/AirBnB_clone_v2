# 0x04. AirBnB clone - Web framework

#### Create a virtual environment
`stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ python3 -m venv myvenv`
### Activate a virtual environment
`stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ source myvenv/bin/activate`
### Deactivate the virtual environment
`deactivate`

Install requirements:
`pip3 install Flask`

Sample use of validator:
`(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ python3 w3c_validator.py web_flask/templates/*.html`.

Sample use of `check-docs`:
`python3 ./check-docs.py pycode_checks`<br />

Using MySQL Locally:
`cat 7-dump.sql | mysql -uroot -p -h 127.0.0.1`

If using a virtual environment named `myvenv`, avoid the error below:
```sh

(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ ./main.py 
Traceback (most recent call last):
  File "/home/stevecmd/ALX/AirBnB_clone_v2/./main.py", line 5, in <module>
    from models import storage
  File "/home/stevecmd/ALX/AirBnB_clone_v2/models/__init__.py", line 18, in <module>
    storage.reload()
  File "/home/stevecmd/ALX/AirBnB_clone_v2/models/engine/file_storage.py", line 35, in reload
    from models.base_model import BaseModel
  File "/home/stevecmd/ALX/AirBnB_clone_v2/models/base_model.py", line 10, in <module>
    import sqlalchemy
ModuleNotFoundError: No module named 'sqlalchemy'

```

by running: <br />
`` run `export PYTHONPATH=/home/stevecmd/ALX/AirBnB_clone_v2/myvenv/lib/python3.12/site-packages:$PYTHONPATH`` <br />