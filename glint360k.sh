wget https://academictorrents.com/download/e5f46ee502b9e76da8cc3a0e4f7c17e4000c7b1e.torrent
sudo apt-get update
yes | sudo apt-get install aria2
aria2c --enable-peer-exchange=true --follow-torrent=true --seed-time=0  e5f46ee502b9e76da8cc3a0e4f7c17e4000c7b1e.torrent
cd glint360k
cat glint360k_* | tar -xzvf -