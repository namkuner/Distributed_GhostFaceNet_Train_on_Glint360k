wget https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/ms1-mv3-asian-face.zip?download=true
sudo apt-get install unzip
unzip ms1-mv3-asian-face.zip?download=true
sudo apt-get update && apt-get install ffmpeg libsm6 libopenblas-dev libxext6  -y
wget -O ms1-mv3-asian-face/lfw.bin  https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/lfw.bin?download=true
wget -O ms1-mv3-asian-face/agedb_30.bin  https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/agedb_30.bin?download=true
wget -O ms1-mv3-asian-face/cfp_fp.bin  https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/cfp_fp.bin?download=true
wget -O ms1-mv3-asian-face/vilfw.bin  https://huggingface.co/datasets/namkuner/namkuner_face_dataset/resolve/main/vilfw.bin?download=true