#!bin/sh
git clone git@github.com:virusAl7rbi/al7rbi_site.git
cd al7rbi_site
docker build -t al7rbi_site .
docker container rm -f al7rbi-site
docker run -d --net pi_default --ip 172.18.0.10 -p 8060:80 --name al7rbi-site --restart always al7rbi_site
cd ../
rm -rf al7rbi_site
