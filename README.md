[![Build Status](https://4cff-86-171-212-33.ngrok-free.app/api/badges/moabukar/drone-ci-lab/status.svg?ref=refs/heads/main)](https://4cff-86-171-212-33.ngrok-free.app/moabukar/drone-ci-lab)

# Drone CI Labs

## 📝 Notes

- [Drone CI](https://docs.drone.io/server/overview/)


## 🚀 Setup with Docker compose

```bash

## Create a GitHub OAuth App

## Create a .env file and add secrets there from GitHub OAuth App.
openssl rand -hex 16 ## for the DRONE_RPC_SECRET
# Set the environment variables so docker compose can consume.
export $(cat .env | xargs)

ngrok http 8080
docker network create drone-net
# Start drone agent/server
docker compose up -d
## Access on

https://4cff-86-171-212-33.ngrok-free.app/login
```
