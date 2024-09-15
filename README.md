# PythonTestCreation
A repo to learn about creating unit tests

## Local Development with SQL Server in Docker

This repository includes a Docker setup to run SQL Server locally for development purposes.

### Prerequisites
- Docker
- Docker Compose

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Set your password in .env under the variable name SA_PASSWORD

3. Start the SQL Server container:
   ```bash
   docker-compose up -d
   ```

4. To stop the container:
   ```bash
   docker-compose down
   ```

### Connecting to SQL Server
Once the container is running, you can connect to the SQL Server instance using any SQL client. Use the following credentials:

- **Host**: `localhost`
- **Port**: `1433`
- **Username**: `sa`
- **Password**: `Your_password123`

If you've added any SQL scripts for initialization, they will run automatically when the container starts.


## SQL Initialization Scripts

The SQL initialization scripts are located in the `SQL_scripts/initialize` directory. These scripts will be executed automatically when the SQL Server container starts in alphabetical order.

To add more scripts, place them in the `SQL_scripts/` folder and modify the `docker-compose.yml` file as needed to execute them.
