#!/bin/bash

read -p "Enter a number: " number

# Pad the number to 2 digits
padded_number=$(printf "%02d" $number)

# Create a new directory
directory_name="${padded_number}"
mkdir "$directory_name"

# Copy the template.py to the new directory as dayX.py
cp template.py "$directory_name/day${number}.py"

# Create input.txt and test.txt
touch "$directory_name/input.txt"
touch "$directory_name/test.txt"

echo "Directory '$directory_name' created with day${number}.py, input.txt, and test.txt."
