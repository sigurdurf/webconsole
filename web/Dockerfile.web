FROM nikolaik/python-nodejs:python3.10-nodejs17
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
RUN npm install --prefix ./static/
cmd python app.py
