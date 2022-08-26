gcloud compute instances create-with-container twitter-bot \
    --container-image=us-east1-docker.pkg.dev/manu-twitter-bot/twitter-bot/image \
    --container-mount-host-path mount-path=/bot/config,host-path=/tmp/bot/config,mode=ro \
    --container-restart-policy=always \
    --zone=us-east1-b \
    --machine-type=e2-small

# Then  manually update config folder to VM