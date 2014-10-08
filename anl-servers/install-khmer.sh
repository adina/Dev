apt-get -y update
apt-get -y install git emacs mercurial less python-matplotlib unzip bzip2 zlib1g-dev ncurses-dev python-dev build-essential libxml-parser-perl

git clone https://github.com/ged-lab/khmer.git
cd khmer
git checkout v1.1
make install

cd 
git clone git://github.com/ged-lab/screed.git
cd screed
python setup.py install

cd
echo export PYTHONPATH=/mnt/khmer/python >> /root/.bashrc
export PYTHONPATH=/mnt/khmer/python >> /root/.bashrc
