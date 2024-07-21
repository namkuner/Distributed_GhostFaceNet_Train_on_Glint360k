wget https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/ms1-mv3-asian-face.zip?download=true
sudo apt-get install unzip
unzip ms1-mv3-asian-face.zip?download=true
sudo apt-get update && apt-get install ffmpeg libsm6 libopenblas-dev libxext6  -y
wget -O lfw.bin -P /workspace/Distributed_GhostFaceNet_Train_on_Glint360k/ms1-mv3-asian-face https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/lfw.bin?download=true
wget -0 agedb_30.bin -P /workspace/Distributed_GhostFaceNet_Train_on_Glint360k/ms1-mv3-asian-face https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/agedb_30.bin?download=true
wget -0 cfp_fp.bin -P /workspace/Distributed_GhostFaceNet_Train_on_Glint360k/ms1-mv3-asian-face https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/cfp_fp.bin?download=true
wget -P vilfw.bin -P /workspace/Distributed_GhostFaceNet_Train_on_Glint360k/ms1-mv3-asian-face https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/vilfw.bin?download=true