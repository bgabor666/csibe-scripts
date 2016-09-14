# CSiBE-result-buildbot-master-docker
#
# VERSION 0.0.1

FROM ubuntu:14.04
MAINTAINER Gabor Ballabas

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y bash git nano vim curl openssh-server python python-virtualenv python-pip python-sqlalchemy python-migrate autoconf buildbot
RUN apt-get install -y subversion

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

ENV USER=buildbot-master

RUN useradd -ms /bin/bash -u 1001 $USER
RUN echo 'buildbot-master:csibe' | chpasswd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
