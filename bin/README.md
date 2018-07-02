## Linux

Ubuntu:

~~~bash
$ sudo apt-get update && sudo apt-get upgrade -y

$ bin/ubuntu.bash
~~~

## Anyenv

~~~bash
$ bin/anyenv.bash
~~~

## Python

~~~bash
$ source bin/lang.bash
$ pyenv install 3.6.3
$ pyenv global 3.6.3
$ pyenv virtualenv cms
~~~

## Node

~~~bash
$ ndenv install v8.9.0
$ ndenv global v8.9.0
~~~

## ローカル設定

~~~bash
$ cp web/app/dist.local_settings.py  web/app/local_settings.py
$ vi web/app/local_settings.py
~~~

## 依存インストール

PYPI:

~~~bash
$ pip install -r requirements/pypi.txt
~~~

~~~bash
$ mkdir ~/projects/src
$ python bin/repos.py  | bash
~~~

## MySQL データベース

~~~bash
$ bin/db.py createdb | mysql -u root -p
password: allfoods
~~~

~~~bash
$ python manage.py shell
~~~