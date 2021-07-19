ARG CUDA_VERSION

FROM nvidia/cuda:$CUDA_VERSION-devel-ubuntu18.04
ARG NVIDIA_VERSION

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install python3-pip libxrender1 libsm6 xserver-xorg-core xorg python3-venv vim pciutils wget git kmod vim git

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt scripts/install_nvidia.sh /app/
RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt && python3 -c "import os; import ai2thor.build; ai2thor.build.Build('Linux64', ai2thor.build.COMMIT_ID, False, releases_dir=os.path.join(os.path.expanduser('~'), '.ai2thor/releases')).download()"
RUN NVIDIA_VERSION=$NVIDIA_VERSION /app/install_nvidia.sh

COPY ai2thor_docker /app/ai2thor_docker
COPY example_agent.py ./

CMD ["/bin/bash"]
