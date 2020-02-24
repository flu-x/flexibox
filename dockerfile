FROM ubuntu:latest

# update machine
RUN apt-get -y update

# Install git
RUN apt-get -y install git

# Add private key and clone the project
COPY docker .
RUN chmod 600 docker
RUN eval $(ssh-agent) && \
    ssh-add docker && \
    ssh-keyscan -H github.com >> /etc/ssh/ssh_known_hosts && \
    git clone git@github.com:flu-x/flexibox.git -b develop

# Get the dependency for chrome and firefox
WORKDIR /usr/local/dependencies/

# Install python version 3.0+
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.7
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

# Configure project
RUN pip3 install --user virtualenv
WORKDIR "/flexibox"
RUN python3 -m virtualenv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt
RUN python3 setup.py install
