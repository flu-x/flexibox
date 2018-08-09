#!/usr/bin/env bash

brew install elasticsearch
brew services start elasticsearch
brew install logstash
brew services start logstash
brew install kibana
brew services start kibana