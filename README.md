### Initial setup
```shell
  sudo apt-get install nginx python3-pip
  python3 pip install virtualenv
```

```shell
  gunicorn -c conf.py api.wsgi
```
