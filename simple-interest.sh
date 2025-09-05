#!/bin/bash
# Simple Interest Calculator Script (Bash version)

# Prompt user for input
echo "Enter the Principal Amount:"
read P
echo "Enter the Rate of Interest (annual %):"
read R
echo "Enter the Time (in years):"
read T

# Calculate Simple Interest
SI=$(( (P * R * T) / 100 ))

# Display result
echo "-----------------------------------"
echo "Principal: $P"
echo "Rate: $R%"
echo "Time: $T years"
echo "Simple Interest = $SI"
echo "-----------------------------------"
