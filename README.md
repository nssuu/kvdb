# KVDB Project
This project is part of the graduation project I wrote in 2021 for the Computer Programming department at Marmara University.

## Overview
KVDB is a distributed key-value store designed for high availability and scalability. This project demonstrates various techniques in distributed systems, networking, and software engineering.

## Preview

|Terminal 1|Terminal 2|Terminal 3|Terminal 4|
|-|-|-|-|
|![Terminal 1](term1.gif)|![Terminal 2](term2.gif)|![Terminal 3](term3.gif)|![Terminal 4](term4.gif)|

## Features

### Client-Server Architecture
- **Client**: The client interacts with the server using a set of predefined functions.
- **Server**: The server handles requests from clients and manages the key-value store.

### Key-Value Store Operations
- **Get**: Retrieve the value associated with a key.
- **Set**: Store a value with a specific key.
- **Has**: Check if a key exists in the store.
- **Pop**: Remove a key-value pair from the store.
- **List Keys**: List all keys in the store.
- **List Members**: List all members in the cluster.
- **Locate**: Find the node responsible for a specific key.

### Distributed System Components
- **Ring**: Implements consistent hashing to distribute keys across nodes.
- **Coordinator**: Manages node operations and ensures data replication.
- **Hasher**: Provides hashing functionality for consistent hashing.

### Networking
- **HTTP Server**: Handles HTTP requests from clients.
- **RPC Functions**: Remote procedure calls for client-server communication.

### Concurrency
- **Parallel Executor**: Executes tasks in parallel to improve performance.

## Code Structure

### Client
- `kv_client/kv_client.py`: Defines the `KVClient` class with methods for interacting with the server.
- `kv_client/rpc/functions`: Contains RPC function definitions for client-server communication.
- `kv_client/shell`: Implements a command-line interface for interacting with the key-value store.

### Server
- `kv_server/kv_server.py`: Defines the `KVServer` class with methods for handling client requests and managing the key-value store.
- `kv_server/rpc/functions`: Contains RPC function definitions for server-side operations.
- `kv_server/ring`: Implements consistent hashing and node management.
- `kv_server/storage/kv_store.py`: Defines the `KVStore` class for storing key-value pairs.
- `kv_server/crypto/hasher.py`: Provides hashing functionality.

### Utilities
- `client.py`: Entry point for the client application.
- `server.py`: Entry point for the server application.

## Skills Demonstrated
- **Distributed Systems**: Implementing consistent hashing, data replication, and node management.
- **Networking**: Designing and implementing client-server communication using HTTP and RPC.
- **Concurrency**: Utilizing parallel execution to improve performance.
- **Software Engineering**: Organizing code into modular components and following best practices.

## Getting Started

### Prerequisites
- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Running the Server
```sh
python server.py -H <host> -P <port> -C <cluster_members> -R <replication_factor>
```

### Running the Client
```sh
python client.py -H <host> -P <port>
```

### Using the Command-Line Interface
```sh
>> set key value
>> get key
>> has key
>> pop key
>> list_keys
>> list_members
>> locate key
>> exit;
```

