#!/usr/bin/env bash
JAVA_VER=$(java -version 2>&1 | sed -n ';s/.* version "\(.*\)\.\(.*\)\..*"/\1\2/p;')
# export JAVA_VERSION
if [ "$JAVA_VER" -ge 18 ]
then
  echo "Java version is the latest...."
else
  wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.rpm"
  sudo yum -y localinstall jdk-8u73-linux-x64.rpm
  rm ~/jdk-8u*-linux-x64.rpm
fi

sudo cp elasticsearch.repo /etc/yum.repos.d/
sudo cp logstash.repo /etc/yum.repos.d/
sudo cp kibana.repo /etc/yum.repos.d/

sudo yum install elasticsearch
sudo yum install logstash
sudo yum install kibana