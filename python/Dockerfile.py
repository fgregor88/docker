FROM debian:stable-slim
# Update apt
RUN apt update
RUN apt upgrade -y

# Install build tooling
RUN apt install -y python3


COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]
