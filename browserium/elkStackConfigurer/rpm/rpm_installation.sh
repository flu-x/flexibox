#!/usr/bin/env bash
sudo cp elasticsearch.repo /etc/yum.repos.d/
sudo cp logstash.repo /etc/yum.repos.d/
sudo cp kibana.repo /etc/yum.repos.d/
sudo yum install elasticsearch
sudo yum install logstash
sudo yum install kibana