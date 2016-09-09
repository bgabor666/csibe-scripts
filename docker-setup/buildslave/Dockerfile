# CSiBE-result-buildbot-master-docker
#
# VERSION 0.0.1

FROM ubuntu:16.04
MAINTAINER Gabor Ballabas

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get upgrade -y openssh-server

RUN apt-get install -y build-essential bash git nano vim curl cmake python python-virtualenv python-pip python-sqlalchemy python-migrate autoconf buildbot-slave iputils-ping
RUN apt-get install -y subversion

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

ENV USER=csibe-slave

RUN useradd -ms /bin/bash $USER
RUN echo 'csibe-slave:csibe' | chpasswd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile


EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

