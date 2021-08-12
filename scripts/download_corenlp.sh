#!/usr/bin/env bash
url="https://nlp.stanford.edu/software/stanford-corenlp-4.2.2.zip"
archive="corenlp.zip"
output="corenlp"

echo "Downloading $url to $archive..."
wget -nc "$url" -O "$archive"

echo "Unpacking $archive..."
unzip -q $archive -d $output

echo "Removing $archive..."
rm -rf $archive

# export CLASSPATH=$output/stanford-corenlp-4.2.2.jar
for file in `find $corenlp -name "*.jar"`; do export CLASSPATH="$CLASSPATH:`realpath $file`"; done

echo "Done."