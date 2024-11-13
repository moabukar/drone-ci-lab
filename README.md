# Drone CI Labs

## 📝 Notes

- [Drone CI](https://docs.drone.io/server/overview/)


## 🚀 Setup with Docker compose

```bash
## Create a .env file and add secrets there from GitHub.

# Set the environment variables so docker compose can consume.
export $(cat .env | xargs)

# Start drone agent/server
docker compose up -d

## Access on

localhost:8000
```


## Setup with Docker

```bash
docker run \
  --volume=/var/lib/drone:/data \
  --env=DRONE_GITHUB_CLIENT_ID=your-id \
  --env=DRONE_GITHUB_CLIENT_SECRET=super-duper-secret \
  --env=DRONE_RPC_SECRET=super-duper-secret \
  --env=DRONE_SERVER_HOST=drone.company.com \
  --env=DRONE_SERVER_PROTO=https \
  --publish=80:80 \
  --publish=443:443 \
  --restart=always \
  --detach=true \
  --name=drone \
  drone/drone:2
```