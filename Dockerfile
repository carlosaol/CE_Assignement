FROM quay.io/jupyter/base-notebook:python-3.12
WORKDIR /home/jovyan/work
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN python -m pip install --no-cache -r requirements.txt
