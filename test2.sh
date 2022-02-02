PETCLINIC_CLAIMS_IMAGE_VERSION=`date "+%Y%m%d.%H%M"`
docker build -t oawofolu/petclinic-claims-dashboard:${PETCLINIC_CLAIMS_IMAGE_VERSION} .
docker tag oawofolu/petclinic-claims-dashboard:${PETCLINIC_CLAIMS_IMAGE_VERSION} oawofolu/petclinic-claims-dashboard
docker push oawofolu/petclinic-claims-dashboard
kubectl delete svc petclinic-claims-dashboard --ignore-not-found=true
kubectl delete deploy petclinic-claims-dashboard --ignore-not-found=true
kubectl create deployment petclinic-claims-dashboard --image=oawofolu/petclinic-claims-dashboard:latest
kubectl port-forward deploy/petclinic-claims-dashboard 8060
