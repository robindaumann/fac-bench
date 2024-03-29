#!/usr/bin/env sh

echo "::group::runnning apt"
sudo add-apt-repository -y ppa:kelleyk/emacs
sudo apt-get update -y
sudo apt-get install -y sbcl rakudo nim php-gmp emacs27-nox groovy
echo "::endgroup::"

echo "::group::installing bench dependencies via pip"
pip3 install -r requirements.txt
echo "::endgroup::"

echo "::group::installing j"
curl -O http://www.jsoftware.com/download/j902/install/j902_linux64.tar.gz
tar xf j902_linux64.tar.gz &&
  sudo mv j902 /usr/local/share &&
  sudo ln -sf /usr/local/share/j902/bin/jconsole /usr/local/bin/jcons
echo "::endgroup::"

echo "::group::installing frink"
curl -O https://frinklang.org/frinkjar/frink.jar &&
  echo "CLASSPATH=$PWD/frink.jar:$CLASSPATH" >> "$GITHUB_ENV"
echo "::endgroup::"
