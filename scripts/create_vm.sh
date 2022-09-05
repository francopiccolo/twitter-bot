gcloud compute instances create-with-container twitter-bot \
    --container-image=us-east1-docker.pkg.dev/manu-twitter-bot/twitter-bot/bot \
    --container-restart-policy=always \
    --zone=us-east1-b \
    --machine-type=e2-small

# Then  manually update config folder to VM