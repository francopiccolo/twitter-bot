gcloud compute instances create-with-container twitter-bot \
    --container-image=gcr.io/manu-twitter-bot/twitter-bot/image \
    --container-restart-policy=always \
    --zone=us-east1-b \
    --machine-type=e2-small

# Then  manually update config folder to VM