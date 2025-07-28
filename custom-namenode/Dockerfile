FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8

USER root

# Now install packages
FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8

# Switch to archived Debian mirror and remove stretch-updates
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y nano python3 python3-pip && \
    apt-get clean



# Optional: symlink python3 to python
RUN ln -s /usr/bin/python3 /usr/bin/python || true

