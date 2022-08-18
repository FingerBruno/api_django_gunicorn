### Initial setup
```shell
  sudo apt-get install nginx python3-pip
  python3 pip install virtualenv
```
### Clonar projeto Django/Flask
```shell
  git clone <url>  
```
### Criar & activate venv
```shell
  python3 -m venv <venv_name>
  source <venv_name>/bin/activate 
  # deactivate pra sair 
  pip install django gunicorn
```
### alterar ip do localhost em project_name/project_name/config.py e em project_name/conf.py
```python
  ALLOWED_HOSTS = ['']
```
### subir server com gunicorn

```shell
  gunicorn -c conf.py api.wsgi
```
