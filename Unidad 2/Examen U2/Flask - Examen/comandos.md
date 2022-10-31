## Enciende el entorno virtual en powershell .venv/Scripts/Activate

---------------------------------------
abrir la terminal de la carpeta

pip install virtualenv

py -3 -m venv .venv

.venv\Scripts\activate

pip install flask
pip install flask-SQLAlchemy
pip install flask-Migrate
pip install psycopg2
pip install flask_wtf


configuramos la base de datos en app.py

crea las carpetas en el proyecto: flask db init

para migrar: flask db migrate

Crea nuestras tablas en la base de datos: flask db upgrade

