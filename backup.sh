#!/bin/bash

source=/users/ilyas/documents/bash/source
target=/users/ilyas/documents/bash/target

for file in $(find $source -type f -print | sed "s|$source/||") ; do
    if [ -a $target/$file ] ; then
        if [ $source/$file -nt $target/$file ] ; then
        echo "Newer file detected, copying..."
        cp -r $source/$file $target/$file
        else
        echo "File $file exists, skipping."
        fi
    else
    echo "$file is being copied over to $target"
    cp -r $source/$file $target/$file
    fi
done
