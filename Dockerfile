FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN mv Scores.txt /Scores.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8777
CMD ["python","MainGame.py"]