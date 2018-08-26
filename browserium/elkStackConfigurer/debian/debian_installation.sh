#!/usr/bin/env bash
JAVA_VER=$(java -version 2>&1 | sed -n ';s/.* version "\(.*\)\.\(.*\)\..*"/\1\2/p;')
# export JAVA_VERSION
if [ "$JAVA_VER" -ge 18 ]
then
  echo "Java version is the latest...."
else
  sudo add-apt-repository ppa:webupd8team/java
  sudo apt-get update
  sudo apt-get -y install oracle-java8-installer
fi

wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo apt-get install apt-transport-https
echo deb https://artifacts.elastic.co/packages/6.x/apt stable main | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

sudo apt-get update && sudo apt-get install elasticsearch
sudo apt-get install kibana
sudo apt-get install logstash

sudo systemctl start kibana.service
sudo systemctl start elasticsearch.service