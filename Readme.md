# My First Flask application

This code is from codigofacilito.

[http://codigofacilito.com/cursos/flask](http://codigofacilito.com/cursos/flask)

## Install

```
pip install -r requirements.txt
# start server
python app.py
```

####Procfile

Explicitly declare what command should be executed to start your app.

## Run
```
# way1
python app.py

# way2
export FLASK_APP=app.py
python -m flask run

# way3
gunicorn app:app

```

## Heroku client (macOS)
```
brew install heroku
```

##Deploy (heroku)
```
(cd into project)
heroku create [appname]
git push heroku master
heroku ps:scale web=1
heroku open
```

##Log
```
heroku logs --tail
```

##Run the app locally
```
heroku local web
```

###get config
```
heroku config
heroku config:set VARNAME=2
```

### Docs

	Addons [https://elements.heroku.com/addons/]
	Documentation [https://devcenter.heroku.com/]


### Gotchas

* Flask uses Jinja2 as template language
