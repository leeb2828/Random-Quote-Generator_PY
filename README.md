# A Random Quote Generator

## How to use this Project
From your terminal, download the files using
```
$ git clone https://github.com/leeb2828/Random-Quote-Generator_PY
```
A virtual environment is a tool that helps to keep dependencies required by
different projects separate from each other by using isolated virtual environments.
The venv module comes pre installed with Python 3.5 + versions.
Create your virtual environment
```
$ python3 -m venv env
$ source env/bin/activate
```
I created the requirements.txt file using the pip freeze command.
Install all dependencies from the requirements.txt file.
```
$ pip install -r requirements.txt
```
Run the app.py file
```
$ python3 app.py
```
Type in http://localhost:3000 into your browser to view the project live.
Type in CTRL-C to stop running the server.

To deactivate your environment:
```
$ deactivate
```
<br />

## About this Project
HTML, CSS, and Python Flask were used for this project. I wrote all of the backend with some modifications to the CSS. All of the quotes are fetched from an external json file. When the user clicks the "Show new quote" button on the top left of the screen, a new quote displays. The quote includes the author, source, and date. 

![Project Image](proj_image.png)

### How to test this project on different screen sizes
Because I specified <b>host='0.0.0.0'</b> in the app.py file, you can view this project on other computers on the same network using the IP address of the computer running the server and the port number. In your browser, type in: <br />
<IP address of the computer running the server>:3000 <br />
Here is an example:<br />
192.145.1.113:3000
