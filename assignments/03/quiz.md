

# First 3 lines of the 2014-01_JA.tsv file
head -n 3 "shell-lesson/2014-01_JA.tsv"


# Count the number of lines in each *.tsv file
wc -l shell-lesson/*.tsv 2>/dev/null

# File with the highest number of lines
wc -l shell-lesson/* 2>/dev/null | sort -nr | head -n 1 | awk '{print $2}'

