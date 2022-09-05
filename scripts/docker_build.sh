docker buildx build . \
    --platform linux/amd64 \
    -t us-east1-docker.pkg.dev/manu-twitter-bot/twitter-bot/bot \
    --push

gcloud compute instances update-container twitter-bot \
    --container-image us-east1-docker.pkg.dev/manu-twitter-bot/twitter-bot/bot:latest