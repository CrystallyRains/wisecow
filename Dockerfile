FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    fortune-mod \
    cowsay \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy the wisecow.sh script to the container
COPY wisecow.sh .

# Make the script executable (change permissions to a more secure setting)
RUN chmod +x wisecow.sh

# Expose the port the application runs on
EXPOSE 4499

# Run the application
CMD ["./wisecow.sh"]
