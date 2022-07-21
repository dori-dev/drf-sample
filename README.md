# DRF Sample

The sample project for django rest framework

#

# How to Run Project

## Download Codes

```
git clone https://github.com/dori-dev/drf-sample.git
```

```
cd drf-sample
```

## Build Virtual Environment

```
python3 -m venv env
```

```
source env/bin/activate
```

## Install Project Requirements

```
pip install -r requirements.txt
```

## Set Environ Variables

rename `.env.example` to `.env` and change values.<br>
create account in [kavenegar.com](https://kavenegar.com/) and change `SMS_API_KEY` value to your **api key**.<br>
create verification template and change `OTP_TEMPLATE` value to your **template name**.

## Migrate Models

```
python manage.py makemigrations planes otp
```

```
python manage.py migrate
```

## Add Super User

```
python manage.py createsuperuser
```

## Run Codes

```
python manage.py runserver
```

## API Docs

API Documentation: [127.0.0.1:8000](http://127.0.0.1:8000/)
Admin Page: [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

#

## Links

Download Source Code: [Click Here](https://github.com/dori-dev/drf-sample/archive/refs/heads/master.zip)

My Github Account: [Click Here](https://github.com/dori-dev/)
