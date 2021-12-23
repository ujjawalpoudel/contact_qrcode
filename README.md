
# QR Code generation

QR Codes are helpful in a lot of scenarios.
Generating a QR Code for each profile will make it really easy for the users to share their profile.
This project helps you to generate your personal qr code so that you can easily share that qr code for your friend circle.


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


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



## Appendix

Any additional information goes here


## Authors

- [@ujjawalpoudel](https://github.com/ujjawalpoudel)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Demo

Insert gif or link to demo


## Deployment

To deploy this project run

**Step 1**
Create Vitual Environment of python 3.7

```bash
  python3.7 -m venv venv
```
**Step 2**
Activate Virtual Environment

```bash
  source venv/bin/activate
```
**Step 3**
Install Python Package from requirements.txt 

```bash
  pip install -r requirements.txt 
```
**Step 4**
Execute main.py file

```bash
  python main.py
```


## Documentation

[Documentation](https://linktodocumentation)


## Run Locally

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


## Used By

This project is used by the following companies:

- Company 1
- Company 2

