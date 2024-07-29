# Debugging
## 0x02. AirBnB clone - MySQL
Testing the commands to ensure they are working
```sh
(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ cat test_params_create | python console.py
(hbnb)
6277ebd4-80a5-4ba8-a523-6598213ab146
(hbnb) 3adf6cb1-1302-4f59-9b27-cac2f993954e
(hbnb) ["[State] (6277ebd4-80a5-4ba8-a523-6598213ab146) {'id': '6277ebd4-80a5-4ba8-a523-6598213ab146', 'created_at': datetime.datetime(2024, 7, 29, 11, 3, 10, 678219), 'updated_at': datetime.datetime(2024, 7, 29, 11, 3, 10, 678219), 'name': 'California'}", "[State] (3adf6cb1-1302-4f59-9b27-cac2f993954e) {'id': '3adf6cb1-1302-4f59-9b27-cac2f993954e', 'created_at': datetime.datetime(2024, 7, 29, 11, 3, 10, 688377), 'updated_at': datetime.datetime(2024, 7, 29, 11, 3, 10, 688377), 'name': 'Arizona'}"]
(hbnb) (hbnb) a41547c6-bc7d-4b29-8906-2b9f55da49a6
(hbnb) ["[Place] (a41547c6-bc7d-4b29-8906-2b9f55da49a6) {'id': 'a41547c6-bc7d-4b29-8906-2b9f55da49a6', 'created_at': datetime.datetime(2024, 7, 29, 11, 3, 10, 689233), 'updated_at': datetime.datetime(2024, 7, 29, 11, 3, 10, 689233), 'city_id': '0001', 'user_id': '0001', 'name': 'My little house', 'number_rooms': 4, 'number_bathrooms': 2, 'max_guest': 10, 'price_by_night': 300, 'latitude': 37.773972, 'longitude': -122.431297}"]
(hbnb)
```
Testing console inputs:
```sh

ALX/AirBnB_clone_v2$ python console.py 
(hbnb) all User
[]
(hbnb) all Place
[]
(hbnb) create Place
31ca9582-fc4f-406e-a473-8bf874900fa7
(hbnb) all Place
["[Place] (31ca9582-fc4f-406e-a473-8bf874900fa7) {'id': '31ca9582-fc4f-406e-a473-8bf874900fa7', 'created_at': datetime.datetime(2024, 7, 29, 13, 7, 18, 323070, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 7, 29, 13, 7, 18, 323070, tzinfo=datetime.timezone.utc)}"]
(hbnb) destroy Place 31ca9582-fc4f-406e-a473-8bf874900fa7
(hbnb) all Place
[]
(hbnb) create Place city_id="0001" user_id="0001" name="My_Little_House"
15b6f8ec-871e-4604-8422-f2099972598b
(hbnb) all Place
["[Place] (15b6f8ec-871e-4604-8422-f2099972598b) {'id': '15b6f8ec-871e-4604-8422-f2099972598b', 'created_at': datetime.datetime(2024, 7, 29, 13, 9, 58, 16653, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 7, 29, 13, 9, 58, 16653, tzinfo=datetime.timezone.utc), 'city_id': '0001', 'user_id': '0001', 'name': 'My Little House'}"]
(hbnb) quit

```

Tests
```sh
python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1

python3 -m unittest discover tests

python3 -m unittest discover tests.test_console

```

Install MySQL using [MySQL Installation steps](https://www.mysqltutorial.net/install-mysql-on-ubuntu-20-04/)

More advanced instructions [Ubuntu Instructions](https://ubuntu.com/server/docs/install-and-configure-a-mysql-server)

Exports for dev environment:
```sh

(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ export HBNB_MYSQL_USER='hbnb_dev'
(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ export HBNB_MYSQL_PWD='hbnb_dev_pwd'
(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ export HBNB_MYSQL_HOST='localhost'
(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ export HBNB_MYSQL_DB='hbnb_dev_db'
(myvenv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ export HBNB_TYPE_STORAGE='db'

```