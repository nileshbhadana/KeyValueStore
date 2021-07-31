---
description: A Key Value Store
---

# Key Value Store
A Simple Key-Value store web service with a subscription feature. User is able to perform set(key, val) and get(key) operations over HTTP and also subscribe to changes happening to any of the keys.

## 📜 Prerequisites

* Docker
    > Refer [this](https://docs.docker.com/get-docker/) document to install docker
* Docker compose 
    > Refer [this](https://docs.docker.com/compose/install/) document to install docker-compose
---

## 🛠️  Guide

---
### How to Run Project

* **Running service Using docker container**

    You can directly run a docker container using the docker image on your local machine. 

    ```bash
    docker container run --name key-value-store -d -p 5000:5000 ghcr.io/nileshbhadana/keyvaluestore-main:latest 
    ```

* **Running service Using docker-compose**

    You can use docker-compose to start the service in a container. You need to have docker-compose installed on you machine. Here are the commands:

    ```bash
    wget https://github.com/nileshbhadana/KeyValueStore/blob/main/docker-compose.yaml
    ``` 
    ```bash
    docker-compose up -d
    ```
---
### CLI Usage

To use the CLI client you can use the same the container which is running and execute inside it or you can use it on your local machine.

To use CLI in already running docker container:

```bash
docker exec -it key-value-store sh
```

The CLI tool have have three sub commands - get, put and subscribe.
For more information you can use `--help` flag to know more about the options available.

- **get**:  This will display the value for an existing key.
    ```bash
    kvstore get <key>
    ```

    You can get all the key value pairs stored using `--all` flag with `get` option.
    ```bash
    kvstore get --all
    ```
    
- **put**: This sets the value of the given key.
    ```bash
    kvstore put <key> <value>
    ```

- **subscribe**: This displays the updates to Key value pairs .
    ```bash
    kvstore subscribe
    ```

---
### Repository Structure

```
KeyValueStore
├── .github
│   └── workflows
│       └── lint.yaml
│       └── main.yaml
├── resources
│   └── helpers.py
│   └── logger.py
│   └── operations.py
|   └── stream.py
├── commands
│   └── get.py
│   └── put.py
│   └── subscribe.py
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── kvstore
├── main.py
├── setup.py
├── README.md
├── requirements.txt
└── LICENSE
```

| File Name | Description |
| :--- | :--- |
| [main.py](https://github.com/nileshbhadana/KeyValueStore/blob/main/main.py) | This contains the main function which will initialize the flask server. All the routings based on path. |
| [helpers.py](https://github.com/nileshbhadana/KeyValueStore/blob/main/resources/helpers.py) | This file contains all the helper functions which are being used in the main operations such as reading or writing to storage file.  |
| [operations.py](https://github.com/nileshbhadana/KeyValueStore/blob/main/resources/operations.py) | This file contains the key operation functions such as getValue and PutKeyValue function to get the value of a key or create/update the value of a particular key. |
| [stream.py](https://github.com/nileshbhadana/KeyValueStore/blob/main/resources/stream.py) | This file contains the function to initialize the broadcasting server to which clients can connect to get updates about key-value pairs.  |
| [get.py](https://github.com/nileshbhadana/KeyValueStore/blob/main/commands/get.py) | This file contains the functions and command code for getting the value of a particular key. This also contains function to get all the key-value pairs stored. |
| [put.py](https://github.com/nileshbhadana/KeyValueStore/blob/main/commands/put.py) | This file contains the functions and command code to set the value of a provided key. |
| [subscribe.py](https://github.com/nileshbhadana/KeyValueStore/blob/main/commands/subscribe.py) | This file contains the functions and command code to watch for any updates to store about key-value pairs. |
| [kvstore](https://github.com/nileshbhadana/KeyValueStore/blob/main/kvstore) | This file the code about client which is to create CLI tool. This imports functions from commands directory for different subcommands. |
| [docker-compose.yaml](https://github.com/nileshbhadana/KeyValueStore/blob/main/docker-compose.yaml) | This contains the configuration to launch docker container using docker-compose. |

---
### 🔁 &nbsp;CI/CD

CI/CD process is setup using Github actions to perform lint tests and build docker image push to main branch. It occurs in two steps. The build step is dependent on lint step. 

- *Lint Test* is performed on every pull request raised for main branch and also on push to main branch.
- *Docker build* is performed on every push to main branch. This dependent on lint test.

Steps:-

* **Lint** - Lints the codebase using pylint
* **Build** - Builds the dockerfile and pushes to github container registry with two tags - `latest` and `<commit-id>`.

---

### 🔧 Testing
There is lintingsetup on this repository to prevent errors.

**Linting** is enabled in CI - Github actions. It runs when a new PR is raised for main branch and also runs on new push on main branch. Flake8 is being used to lint the codebase.


