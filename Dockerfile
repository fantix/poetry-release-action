FROM python:3.7
RUN pip install pip==19.3.1 GitPython==3.0.5 poetry==1.0.0 PyGithub==1.44.1
COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
