#!/bin/bash

sudo apt update
sudo apt install postgresql-server-dev-all

git clone -b v0.8.1 https://github.com/pgvector/pgvector.git
cd pgvector
make
sudo make install

##########################################################

sudo apt install postgresql-15-pgvector
