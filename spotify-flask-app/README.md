# Flask spotify app
## Installation

**Installation via `requirements.txt`**:

```shell
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python3 run.py
```
## Configuration

Configuration is handled by creating a **.env** file. This should contain the following variables (replace the values with your own):

```.env
FLASK_ENV="production"
SECRET_KEY="YOURSECRETKEY"
SQLALCHEMY_DATABASE_URI="mysql+pymysql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]"
```

