# Drone CI Labs

## 📝 Notes

- [Drone CI](https://docs.drone.io/server/overview/)


## 🚀 Setup

```bash
## Create a .env file and add secrets there from GitHub.

# Set the environment variables so docker compose can consume.
export $(cat .env | xargs)

# Start drone agent/server
docker compose up -d
```
