#!/usr/bin/env bash

JAVA_VER=$(java -version 2>&1 | sed -n ';s/.* version "\(.*\)\.\(.*\)\..*"/\1\2/p;')
# export JAVA_VERSION
if [ "$JAVA_VER" -ge 18 ]
then
  echo "Java version is the latest...."
else
  brew cask install java
  brew cask install java8
fi

brew install elasticsearch
brew install logstash
brew install kibana

brew services start elasticsearch
brew services start logstash
brew services start kibana