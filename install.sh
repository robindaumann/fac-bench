#!/usr/bin/env sh

set -e

echo "::comannd::apt"
sudo apt-get install -y sbcl rakudo nim php-gmp
echo 'installing benchmark requirements'
pip3 install -r requirements.txt

echo "::group::installing j"
curl -O http://www.jsoftware.com/download/j902/install/j902_linux64.tar.gz
tar xf j902_linux64.tar.gz &&
  sudo mv j902 /usr/local/share &&
  sudo ln -sf /usr/local/share/j902/bin/jconsole /usr/local/bin/jcons
echo "::endgroup"

echo "::group::installing frink"
curl -O https://frinklang.org/frinkjar/frink.jar &&
  echo "::set-env name=CLASSPATH::$PWD/frink.jar:$CLASSPATH"
echo "::endgroup"
