"""
elastic search
document based database lets to CRD and perform analytics on the saved records
lightning speed search criteria

Search - Building search experiences in applications, sites or other
Observability - Logs, metrics, traces, and synthetics
Security - Analytics (logs/events), SIEM, endpoint protection, or cloud security
Something else
https://d59f55020f33431ea2d0de74b78473a4.us-central1.gcp.cloud.es.io:9243/app/home#/getting_started?useCase=search

docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.13.2
docker run --name es01 --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.13.2

https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
"""