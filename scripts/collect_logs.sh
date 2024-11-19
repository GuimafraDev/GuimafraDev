#!/bin/bash
LOG_DIR="logs"
ARCHIVE="logs_$(date +%Y%m%d%H%M%S).tar.gz"
tar -czf $ARCHIVE $LOG_DIR
echo "Logs archived to $ARCHIVE"