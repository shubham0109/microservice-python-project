mysql -uroot -proot

docker build .
docker tag sha256:298821255a97857660f2539bd0fc14b9a1d266ea32c08ed51246180e922497f2 shubham0109/auth:latest
docker push shubham0109/auth:latest

minikube addons list
minikube addons enable ingress
minikube tunnel

kubectl delete -f ./

curl.exe -X POST -F 'file=@./test.mp4' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNodWJoQGdtYWlsLmNvbSIsImV4cCI6MTY5OTk3MDAxOSwiaWF0IjoxNjk5ODgzNjE5LCJhZG1pbiI6dHJ1ZX0.QW7PtbHiXLrM-fPrGmq_RWbjUbC4QXjrUxBuMiGwncQ' http://mp3converter.com/upload