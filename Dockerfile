FROM quay.io/jupyter/base-notebook:python-3.12
WORKDIR /home/jovyan/work
COPY ./requirements.txt ./
RUN python -m pip install --no-cache -r requirements.txt