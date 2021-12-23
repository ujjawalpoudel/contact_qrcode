
# QR Code generation

QR Codes are helpful in a lot of scenarios.
Generating a QR Code for each profile will make it really easy for the users to share their profile.
This project helps you to generate your personal qr code so that you can easily share that qr code for your friend circle.

## API Reference

#### Generate QR Code

```http
  POST /generate_qrcode
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `fullname` | `string` | **Required**|
| `gender` | `string` | **Required**|
| `email` | `list` | **Required**|
| `phone_number` | `list` | **Required**|
| `city` | `string` | **Required**|
| `district` | `string` | **Required**|
| `country` | `string` | **Required**|
| `palika` | `string` | **Required**|


## Authors

- [@ujjawalpoudel](https://github.com/ujjawalpoudel)
## Run Locally
### This installation process is for Linux OS(only)

Clone the project

```bash
  git clone git@github.com:ujjawalpoudel/contact_qrcode.git
```

Go to the project directory

```bash
  cd contact_qrcode/
```

Create Vitual Environment of python 3.7

```bash
  python3.7 -m venv venv
```
Activate Virtual Environment

```bash
  source venv/bin/activate
```
Install Python Package from requirements.txt 

```bash
  pip install -r requirements.txt 
```
Execute main.py file

```bash
  python main.py
```

## Tech Stack

**Server:** Python

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
