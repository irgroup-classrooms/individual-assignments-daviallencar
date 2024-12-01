# First 3 lines of the file 2014-01_JA.tsv
echo "First 3 lines of the file 2014-01_JA.tsv:"
head -n 3 "shell-lesson/2014-01_JA.tsv"
echo ""

# Count the number of lines in each *.tsv file
echo "Number of lines in each *.tsv file:"
wc -l shell-lesson/*.tsv 2>/dev/null
echo ""

# File with the highest number of lines
echo "File with the highest number of lines:"
wc -l shell-lesson/* 2>/dev/null | sort -nr | head -n 1 | awk '{print $2}'
echo ""

