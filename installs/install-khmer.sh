apt-get -y update
apt-get -y install git emacs mercurial less python-matplotlib unzip bzip2 zlib1g-dev ncurses-dev python-dev build-essential libxml-parser-perl

curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py 
easy_install nose

git clone git://github.com/ctb/screed.git
cd screed
python setup.py install 

cd ..
git clone git://github.com/ctb/khmer.git
cd khmer 
make clean all

cd
echo export PYTHONPATH=/mnt/khmer/python >> /root/.bashrc
export PYTHONPATH=/mnt/khmer/python >> /root/.bashrc
