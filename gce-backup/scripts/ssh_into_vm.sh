gcloud config set account francopiccolo@gmail.com
gcloud config set project manu-twitter-bot
gcloud compute ssh --zone "us-east1-b" "twitter-bot"  --project "manu-twitter-bot"
# If problems with ssh
gcloud compute ssh --zone "us-east1-b" "twitter-bot" --troubleshoot
# Vlidate disk is full in case of disk problems
gcloud compute instances tail-serial-port-output --zone "us-east1-b" "twitter-bot"
gcloud compute disks resize twitter-bot --zone "us-east1-b" --size=20GB



