FROM gitpod/workspace-full

RUN sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx && sudo rm -rf /var/lib/apt/lists/*