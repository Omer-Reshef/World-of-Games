FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN mv Scores.txt /Scores.txt
RUN pip install -r requirements.txt
CMD ["python","MainGame.py"]