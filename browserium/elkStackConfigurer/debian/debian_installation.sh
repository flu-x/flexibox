#!/usr/bin/env bash
JAVA_VER=$(java -version 2>&1 | sed -n ';s/.* version "\(.*\)\.\(.*\)\..*"/\1\2/p;')
# export JAVA_VERSION
if [ "$JAVA_VER" -ge 18 ]
then
  echo "Java version is the latest...."
else
  add-apt-repository ppa:webupd8team/java
  apt-get update
  apt-get -y install oracle-java8-installer
fi

wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
apt-get install apt-transport-https
echo deb https://artifacts.elastic.co/packages/6.x/apt stable main | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

apt-get update && sudo apt-get install elasticsearch
apt-get install kibana
apt-get install logstash

systemctl start kibana.service
systemctl start elasticsearch.service