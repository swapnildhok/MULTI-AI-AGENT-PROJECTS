# Use the official Jenkins base image
FROM jenkins/jenkins:lts

# Switch to root to install Docker CLI
USER root

# Install Docker CLI inside Jenkins container
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    apt-get clean

# (Optional but safe) Create docker group and add jenkins to it
RUN groupadd -f docker && usermod -aG docker jenkins

# ⚠️ FORCE JENKINS TO RUN AS ROOT
USER root