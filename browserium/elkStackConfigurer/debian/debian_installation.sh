#!/usr/bin/env bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get -y install oracle-java8-installer
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo apt-get install apt-transport-https
echo deb https://artifacts.elastic.co/packages/6.x/apt stable main | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
sudo apt-get update && sudo apt-get install elasticsearch
sudo apt-get install kibana
sudo apt-get install logstash
sudo systemctl start kibana.service
sudo systemctl start elasticsearch.service