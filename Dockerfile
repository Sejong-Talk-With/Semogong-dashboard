FROM python:3.9.10
WORKDIR /Semogong-dashboard
COPY ./requirements.txt /Semogong-dashboard/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /Semogong-dashboard/requirements.txt
COPY ./app /Semogong-dashboard/app
ENV TZ Asia/Seoul
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
