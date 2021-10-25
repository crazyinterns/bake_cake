<h3 align="center">BakeCake</h3>

<p align="center">
  <img alt="Platform" src="https://img.shields.io/badge/platform-linux-green?style=for-the-badge" />
  <img alt="Python version" src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge" />
  <img alt="Made with Django." src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
</p>

## Table of content

- [About the project](#about-the-project)
- [Installation](#installation)
- [How to run](#how-to-run)
- [License](#license)

## About the project
BakeCake is a custom cake store website. 

You can check this out here: [Website](https://31.184.253.248/)

## Installation
### Clone project
First of all, you should clone this project
```bash
git clone https://github.com/crazyinterns/bake_cake.git
```
or
```bash
git clone git@github.com:crazyinterns/bake_cake.git
```
then type:
```bash
cd bake_cake
```
### Install package manager
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install BakeCake.

```bash
pip install foobar
```

### Setup virtual environment
```bash
python -m venv venv
```
### Activate virtual environment
On Windows:
```bash
venv\Scripts\activate.bat
```
On Linux:
```bash
source venv/bin/activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### Create `.env` file with the following content
```
SECRET_KEY='Django secret key'
DEBUG=False for production server
ALLOWED_HOSTS=['IP of production server']
```

## How to run

```python
python manage.py runserver
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
