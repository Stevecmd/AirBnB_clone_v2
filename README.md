<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>


### Activate a Virtual environment
1. Create a Virtual Environment:
```sh
python3 -m venv myvenv
```
2. Activate the Virtual Environment:
```sh
source myvenv/bin/activate
```
3. Deactivate the Virtual Environment:
```sh
deactivate
```
Install Fabric:
`sudo apt install fabric`

> Install Environment dependencies
```sh
./install_dependencies.sh
```

1. Compress before sending

Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

- Prototype: def `do_pack()`:
- All files in the folder `web_static` must be added to the final archive
- All archives must be stored in the folder `versions` (your function should create this folder if it doesn’t exist)
- The name of the archive created must be `web_static_<year><month><day><hour><minute><second>.tgz`
- The function `do_pack` must return the archive path if the archive has been correctly generated. Otherwise, it should return `None`

```sh

(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ fab -f 1-pack_web_static.py do_pack
Packing web_static to versions/web_static_20240711091746.tgz
[localhost] local: tar -cvzf versions/web_static_20240711091746.tgz web_static
web_static/
web_static/5-index.html
web_static/README.md
web_static/102-index.html
web_static/6-index.html
web_static/2-index.html
web_static/8-index.html
web_static/1-index.html
web_static/103-index.html
web_static/4-index.html
web_static/7-index.html
web_static/101-index.html
web_static/3-index.html
web_static/images/
web_static/images/logo.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_pets.png
web_static/images/icon_group.png
web_static/images/icon.ico
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/styles/
web_static/styles/103-common.css
web_static/styles/103-header.css
web_static/styles/102-header.css
web_static/styles/3-header.css
web_static/styles/103-places.css
web_static/styles/102-filters.css
web_static/styles/101-places.css
web_static/styles/7-places.css
web_static/styles/2-header.css
web_static/styles/4-common.css
web_static/styles/103-footer.css
web_static/styles/4-filters.css
web_static/styles/102-places.css
web_static/styles/5-filters.css
web_static/styles/102-footer.css
web_static/styles/8-places.css
web_static/styles/3-footer.css
web_static/styles/2-common.css
web_static/styles/103-filters.css
web_static/styles/6-filters.css
web_static/styles/102-common.css
web_static/styles/2-footer.css
web_static/styles/100-places.css
web_static/styles/3-common.css
web_static/0-index.html
web_static/100-index.html
web_static packed: versions/web_static_20240711091746.tgz -> 21070Bytes

Done.

```

4. Deploy archive! 

Write a Fabric script (based on the file `1-pack_web_static.py`) that distributes an archive to your web servers, using the function `do_deploy`:

- Prototype: def `do_deploy(archive_path)`:
- Returns `False` if the file at the path `archive_path` doesn’t exist
- The script should take the following steps:
    - Upload the archive to the `/tmp/` directory of the web server
    - Uncompress the archive to the folder `/data/web_static/releases/<archive filename without extension>` on the web server
    - Delete the archive from the web server
    - Delete the symbolic link `/data/web_static/current` from the web server
    - Create a new the symbolic link `/data/web_static/current` on the web server, linked to the new version of your code (`/data/web_static/releases/<archive filename without extension>`)
- All remote commands must be executed on your both web servers (using `env.hosts = ['<IP web-01>', 'IP web-02']` variable in your script)
- Returns True if all operations have been done correctly, otherwise returns `False`
- You must use this script to deploy it on your servers: `xx-web-01` and `xx-web-02`

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: `env.user =`...)

Disclaimer: commands execute by Fabric displayed below are linked to the way we implemented the archive function `do_pack` - like the mv command - depending of your implementation of it, you may don’t need it


Manually created required files:
```sh

(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ ls -l versions/web_static_20170314233357.tgz
ls: cannot access 'versions/web_static_20170314233357.tgz': No such file or directory
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ cd web_static
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2/web_static$ touch .DS_Store 0-index.html 1-index.html 100-index.html 2-index.html 3-index.html 4-index.html 5-index.html 6-index.html 7-index.html 8-index.html index.html
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2/web_static$ mkdir -p images styles
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2/web_static$ touch images/icon.png images/icon_bath.png images/icon_bed.png images/icon_group.png images/icon_pets.png images/icon_tv.png images/icon_wifi.png images/logo.png
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2/web_static$ touch styles/100-places.css styles/2-common.css styles/2-footer.css styles/2-header.css styles/3-common.css styles/3-footer.css styles/3-header.css styles/4-common.css styles/4-filters.css styles/5-filters.css styles/6-filters.css styles/7-places.css styles/8-places.css styles/common.css styles/filters.css styles/footer.css styles/header.css styles/places.css

```
> Command to use Fabric to distribute archive to my containers using my key
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20240711092054.tgz -i ~/.ssh/id_ed25519
```
File: `2-do_deploy_web_static.py`

5. Full Deployment

Write a Fabric script (based on the file `2-do_deploy_web_static.py`) that creates and distributes an archive to your web servers, using the function `deploy`:

- Prototype: `def deploy()`:
- The script should take the following steps:
    - Call the `do_pack()` function and store the path of the created archive
    - Return `False` if no archive has been created
    - Call the `do_deploy(archive_path)` function, using the new path of the new archive
    - Return the return value of `do_deploy`
- All remote commands must be executed on both of web your servers (using `env.hosts = ['<IP web-01>', 'IP web-02']` variable in your script)
- You must use this script to deploy it on your servers: `xx-web-01` and `xx-web-02`

```sh

(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_ed25519 -u ubuntu
[54.160.94.43] Executing task 'deploy'
[localhost] local: mkdir -p versions
[localhost] local: tar -cvzf versions/web_static_20240711100116.tgz web_static
web_static/
web_static/5-index.html
web_static/README.md
web_static/102-index.html
web_static/versions/
web_static/versions/web_static_20240711092047.tgz
web_static/6-index.html
web_static/2-index.html
web_static/8-index.html
web_static/index.html
web_static/1-index.html
web_static/.DS_Store
web_static/103-index.html
web_static/4-index.html
web_static/7-index.html
web_static/101-index.html
web_static/3-index.html
web_static/images/
web_static/images/logo.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon.png
web_static/images/icon_pets.png
web_static/images/icon_group.png
web_static/images/icon.ico
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/styles/
web_static/styles/header.css
web_static/styles/103-common.css
web_static/styles/103-header.css
web_static/styles/102-header.css
web_static/styles/3-header.css
web_static/styles/103-places.css
web_static/styles/102-filters.css
web_static/styles/101-places.css
web_static/styles/7-places.css
web_static/styles/2-header.css
web_static/styles/4-common.css
web_static/styles/103-footer.css
web_static/styles/places.css
web_static/styles/4-filters.css
web_static/styles/102-places.css
web_static/styles/5-filters.css
web_static/styles/102-footer.css
web_static/styles/filters.css
web_static/styles/8-places.css
web_static/styles/footer.css
web_static/styles/3-footer.css
web_static/styles/2-common.css
web_static/styles/103-filters.css
web_static/styles/6-filters.css
web_static/styles/102-common.css
web_static/styles/common.css
web_static/styles/2-footer.css
web_static/styles/100-places.css
web_static/styles/3-common.css
web_static/0-index.html
web_static/100-index.html
[54.160.94.43] put: versions/web_static_20240711100116.tgz -> /tmp/web_static_20240711100116.tgz
[54.160.94.43] run: mkdir -p /data/web_static/releases/web_static_20240711100116/
[54.160.94.43] run: tar -xzf /tmp/web_static_20240711100116.tgz -C /data/web_static/releases/web_static_20240711100116/
[54.160.94.43] run: rm /tmp/web_static_20240711100116.tgz
[54.160.94.43] run: mv /data/web_static/releases/web_static_20240711100116/web_static/* /data/web_static/releases/web_static_20240711100116/
[54.160.94.43] run: rm -rf /data/web_static/releases/web_static_20240711100116/web_static
[54.160.94.43] run: rm -rf /data/web_static/current
[54.160.94.43] run: ln -s /data/web_static/releases/web_static_20240711100116/ /data/web_static/current
[34.203.38.175] Executing task 'deploy'
[localhost] local: mkdir -p versions
[localhost] local: tar -cvzf versions/web_static_20240711100130.tgz web_static
web_static/
web_static/5-index.html
web_static/README.md
web_static/102-index.html
web_static/versions/
web_static/versions/web_static_20240711092047.tgz
web_static/6-index.html
web_static/2-index.html
web_static/8-index.html
web_static/index.html
web_static/1-index.html
web_static/.DS_Store
web_static/103-index.html
web_static/4-index.html
web_static/7-index.html
web_static/101-index.html
web_static/3-index.html
web_static/images/
web_static/images/logo.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon.png
web_static/images/icon_pets.png
web_static/images/icon_group.png
web_static/images/icon.ico
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/styles/
web_static/styles/header.css
web_static/styles/103-common.css
web_static/styles/103-header.css
web_static/styles/102-header.css
web_static/styles/3-header.css
web_static/styles/103-places.css
web_static/styles/102-filters.css
web_static/styles/101-places.css
web_static/styles/7-places.css
web_static/styles/2-header.css
web_static/styles/4-common.css
web_static/styles/103-footer.css
web_static/styles/places.css
web_static/styles/4-filters.css
web_static/styles/102-places.css
web_static/styles/5-filters.css
web_static/styles/102-footer.css
web_static/styles/filters.css
web_static/styles/8-places.css
web_static/styles/footer.css
web_static/styles/3-footer.css
web_static/styles/2-common.css
web_static/styles/103-filters.css
web_static/styles/6-filters.css
web_static/styles/102-common.css
web_static/styles/common.css
web_static/styles/2-footer.css
web_static/styles/100-places.css
web_static/styles/3-common.css
web_static/0-index.html
web_static/100-index.html
[34.203.38.175] put: versions/web_static_20240711100130.tgz -> /tmp/web_static_20240711100130.tgz
[34.203.38.175] run: mkdir -p /data/web_static/releases/web_static_20240711100130/
[34.203.38.175] run: tar -xzf /tmp/web_static_20240711100130.tgz -C /data/web_static/releases/web_static_20240711100130/
[34.203.38.175] run: rm /tmp/web_static_20240711100130.tgz
[34.203.38.175] run: mv /data/web_static/releases/web_static_20240711100130/web_static/* /data/web_static/releases/web_static_20240711100130/
[34.203.38.175] run: rm -rf /data/web_static/releases/web_static_20240711100130/web_static
[34.203.38.175] run: rm -rf /data/web_static/current
[34.203.38.175] run: ln -s /data/web_static/releases/web_static_20240711100130/ /data/web_static/current

Done.
Disconnecting from 54.160.94.43... done.
Disconnecting from 34.203.38.175... done.

```

6. Keep it clean!
Write a Fabric script (based on the file `3-deploy_web_static.py`) that deletes out-of-date archives, using the function `do_clean`:

- Prototype: `def do_clean(number=0)`:
- `number` is the number of the archives, including the most recent, to keep.
    - If `number` is 0 or 1, keep only the most recent version of your archive.
    - if `number` is 2, keep the most recent, and second most recent versions of your archive.
        etc.
- Your script should:
    - Delete all unnecessary archives (all archives minus the number to keep) in the `versions` folder
    - Delete all unnecessary archives (all archives minus the number to keep) in the `/data/web_static/releases` folder of both of your web servers
- All remote commands must be executed on both of your web servers (using the `env.hosts = ['<IP web-01>', 'IP web-02'`] variable in your script)

```sh

(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ ls -ltr versions
total 72
-rw-r--r-- 1 stevecmd stevecmd 21382 Jul 11 09:20 web_static_20240711092054.tgz
-rw-r--r-- 1 stevecmd stevecmd 21382 Jul 11 10:01 web_static_20240711100116.tgz
-rw-r--r-- 1 stevecmd stevecmd 21382 Jul 11 10:01 web_static_20240711100130.tgz
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ fab -f 100-clean_web_static.py do_clean:number=2 -i ~/.ssh/id_ed25519 -u ubuntu > /dev/null 2>&1
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ ls -ltr versions
total 48
-rw-r--r-- 1 stevecmd stevecmd 21382 Jul 11 10:01 web_static_20240711100116.tgz
-rw-r--r-- 1 stevecmd stevecmd 21382 Jul 11 10:01 web_static_20240711100130.tgz

```
File: `100-clean_web_static.py`

7. Puppet for setup
Redo the task #0 but by using Puppet:
```sh

ubuntu@197045-web-01:~$ sudo apt install puppet
ubuntu@197045-web-01:~$ puppet apply 101-setup_web_static.pp
ubuntu@197045-web-01:~$ ls -l /data
total 4
drwxr-xr-x 4 ubuntu ubuntu 4096 Jul 11 07:42 web_static
ubuntu@197045-web-01:~$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 ubuntu ubuntu   30 Jul 11 07:42 current -> /data/web_static/releases/test
drwxr-xr-x 5 ubuntu ubuntu 4096 Jul 11 07:01 releases
drwxr-xr-x 2 ubuntu ubuntu 4096 Jul 10 05:28 shared
ubuntu@197045-web-01:~$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@197045-web-01:~$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>

```
```sh

ubuntu@197045-web-02:~$ sudo apt install puppet
ubuntu@197045-web-02:~$ puppet apply 101-setup_web_static.pp
ubuntu@197045-web-02:~$ ls -l /data
total 4
drwxr-xr-x 4 ubuntu ubuntu 4096 Jul 11 07:47 web_static
ubuntu@197045-web-02:~$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 ubuntu ubuntu   30 Jul 11 07:47 current -> /data/web_static/releases/test
drwxr-xr-x 5 ubuntu ubuntu 4096 Jul 11 07:01 releases
drwxr-xr-x 2 ubuntu ubuntu 4096 Jul 11 06:02 shared
ubuntu@197045-web-02:~$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@197045-web-02:~$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>

```
File: `101-setup_web_static.pp`

`fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i ~/.ssh/id_ed25519 -u ubuntu`



Keys
View SSH Private Key:
```sh
cat ~/.ssh/id_rsa
```
View SSH Public key:
```sh
cat ~/.ssh/id_rsa.pub
```
View SSH configuration key:
```sh
cat ~/.ssh/config
```

Install requirements:
```sh
pip install -r requirements.txt
```

Online `HTML validator`:
`https://infohound.net/tidy/`
