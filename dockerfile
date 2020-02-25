FROM ubuntu:latest

# update machine
RUN apt-get -y update

# Install system dependencies
RUN apt install -y software-properties-common \
                   apt-utils \
                   curl \
                   unzip \
                   git \
                   libxss1 \
                   libappindicator1 \
                   libindicator7 \
                   libasound2 \
                   libgconf-2-4 \
                   libnspr4 \
                   libnss3 \
                   libpango1.0-0 \
                   fonts-liberation \
                   xdg-utils \
                   wget
RUN add-apt-repository ppa:deadsnakes/ppa

# Add private key and clone the project
COPY docker .
RUN chmod 600 docker
RUN eval $(ssh-agent) && \
    ssh-add docker && \
    ssh-keyscan -H github.com >> /etc/ssh/ssh_known_hosts && \
    git clone git@github.com:flu-x/flexibox.git -b develop

# Install google chrome browser
WORKDIR /Downloads
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update
RUN apt-get install -y google-chrome-stable

# Install firefox browser
RUN apt-get install -y firefox

# Install python version 3.0+
RUN apt install -y python3.7 \
                   python3-pip
RUN pip3 install --upgrade pip \
                 --upgrade setuptools

# Get user permissions to /usr/local/bin and install browser drivers
RUN chmod ugo+rwx /usr/local/bin/
WORKDIR /usr/local/bin/dependencies/
WORKDIR /usr/local/bin/dependencies/dir_chromedriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/dependencies/dir_chromedriver/chromedriver
WORKDIR /usr/local/bin/dependencies/dir_geckodriver
RUN export BASE_URL=https://github.com/mozilla/geckodriver/releases/download \
    && export VERSION=$(curl -sL \
    https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
    grep tag_name | cut -d '"' -f 4) \
    && curl -sL \
    $BASE_URL/$VERSION/geckodriver-$VERSION-linux64.tar.gz | tar -xz

# Configure project
WORKDIR /
RUN pip3 install --user virtualenv
WORKDIR /flexibox
RUN python3 -m virtualenv venv
RUN . venv/bin/activate
RUN pip3 install git+git://github.com/flu-x/flexibox.git@develop
RUN pip3 install -r requirements.txt
RUN python3 setup.py install
