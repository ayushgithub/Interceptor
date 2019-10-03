### Steps to run the application on minikube
1. minikube start
2. eval $(minikube docker-env) 
3. bash scripts/build.sh
4. kubectl apply -f k8s_files/database.yaml
5. kubectl apply -f k8s_files/client.yaml
6. kubectl logs -l app=client -c interceptor -f
