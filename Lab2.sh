#!/bin/bash

# initiate a count for file naming
count=0

# sorting file and loop
sort ./passwordList.txt | while read -r line
do
# print alphabetically
echo $line

# create a file for each of the password
echo $line >"pwd_${count}.txt"

# increment counter
((count++))

done
