#!/bin/bash

# Define variables
SOURCE_DIR="/path/to/source/directory"
DEST_DIR="/path/to/destination/directory"
LOG_FILE="/path/to/log/file.log"

# Perform the backup
rsync -av --delete $SOURCE_DIR $DEST_DIR > $LOG_FILE 2>&1

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup was successful" >> $LOG_FILE
else
    echo "Backup failed" >> $LOG_FILE
fi
