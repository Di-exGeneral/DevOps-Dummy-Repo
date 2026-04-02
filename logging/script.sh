#!/bin/sh
while true; do
  date >> /logs/log.txt
  sleep 10
done

cat /logs/log.txt
