





git clone git://github.com/dzerbino/velvet.git
cd velvet
make 'MAXKMERLENGTH=69'
cp velvetg /usr/local/bin/
cp velveth /usr/local/bin/
cd ..
apt-get -y --force-yes install mummer libxml-parser-perl libexpat1-dev
ln /usr/bin/show-coords /usr/local/bin
curl -O http://cdhit.googlecode.com/files/cd-hit-v4.5.7-2011-12-16.tgz
tar xzf cd-hit-v4.5.7-2011-12-16.tgz
cd cd-hit-v4.5.7-2011-12-16
make
make install
cd ..
curl -L http://sourceforge.net/projects/amos/files/amos-3.1.0-rc1.tar.gz/download > amos-3.1.0-rc1.tar.gz
tar xzf amos-3.1.0-rc1.tar.gz
cd amos-3.1.0-rc1
./configure
make 
make install
cp bin/* /usr/local/bin