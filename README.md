# Dockerized HP ILO Script

This is a Dockerized version of a script designed to interact with HP Integrated Lights-Out (ILO) servers. The script automates tasks related to managing the power state of the server. It uses Python 3.10 along with some additional packages for logging, dotenv, and hpilo.

## Usage

To use this Dockerized script, follow these steps:

1. Make sure you have Docker installed on your system.
2. Clone this repository.
3. Navigate to the directory containing the Dockerfile and the script.
4. Build the Docker image using the following command:
   ```
   docker build -t hp-ilo-script .
   ```
5. Once the image is built, you can run a container using the following command:
   ```
   docker run -d --name hp-ilo-container hp-ilo-script
   ```
   Replace `hp-ilo-container` with your desired container name.

## Configuration

Before running the container, ensure that you have configured the necessary environment variables. The script expects the following environment variables to be set:

- `ILO_ADDRESS`: The IP address or hostname of the HP ILO server.
- `ILO_USERNAME`: The username for accessing the HP ILO server.
- `ILO_PASSWORD`: The password for accessing the HP ILO server.

You can set these environment variables in a `.env` file in the root directory of the project.

## Logging

The script logs its activities to files located in the `logs` directory. Each log file has a maximum size of 10 MB, and a maximum of 5 backup files are kept.