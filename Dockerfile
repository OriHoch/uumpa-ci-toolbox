# Pulled August 29, 2021
FROM python:3.8@sha256:a0a734233420b17d9ab37125afc9d8217b75db153d55854ac6683e639f00a8e8
RUN pip install --upgrade pip
WORKDIR /srv
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY setup.py ./
COPY uumpa_ci_toolbox ./uumpa_ci_toolbox
RUN pip install -e .
ENV PYTHONUNBUFFERED=yes
ENTRYPOINT ["uci"]
