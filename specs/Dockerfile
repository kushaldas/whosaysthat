FROM fedora:25
LABEL MAINTAINER kushal@freedom.press

RUN dnf update -y

RUN dnf install -y fedora-packager vim make python3-requests python3-cryptography
RUN dnf install -y python3-devel python3-setuptools

ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
    && chown -R user:user $HOME

RUN su -c rpmdev-setuptree user

WORKDIR $HOME/rpmbuild
VOLUME $HOME/rpmbuild

USER user


CMD ["/usr/bin/bash"]

