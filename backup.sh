#!/bin/bash

source=/mnt/c/Users/ilyas/DevOps/Bash/source
target=vagrant@192.168.56.10:/home/vagrant/target

timestamp=$(date +%Y-%m-%d_%H-%M-%S)
backup_dir="$source/../backup_$timestamp"
mkdir "$backup_dir"

if [[ $target == *":"* ]]; then
  rsync -avz --delete -e ssh $source/ $target/
else
  rsync -avz --delete $source/ $target/
fi

for file in $(find $source -type f -print | sed "s|$source/||") ; do
    if [ -a $target/$file ] ; then
        if [ $source/$file -nt $target/$file ] ; then
            echo "Newer file detected, copying to $backup_dir..."
            scp -r $source/$file $backup_dir/$file
            echo "Copying $file to $target..."
            scp -r $source/$file $target/$file
        else
            echo "File $file exists, skipping."
        fi
    else
        echo "$file is being copied over to $target"
        scp -r $source/$file $target/$file
    fi
done
