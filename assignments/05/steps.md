# Documentation for the "cleaned_lotr_scripts.csv" File

This dataset contains dialogues from *The Lord of the Rings* movies. It has three columns:

1. **`char`**: The name of the character speaking the dialogue.
2. **`dialog`**: The dialogue or line spoken by the character.
3. **`movie`**: The movie in which the dialogue appears (e.g., *The Return of the King*, *The Two Towers*).

Each row represents a line of dialogue from a character in one of the movies.

# Data Cleaning Process for "lotr_scripts.csv"

This document outlines the steps taken to clean the `lotr_scripts.csv` dataset using shell commands. 

## Steps Taken

### Step 1: Removing Empty Rows
The first step was to remove any rows where the `movie` column (third column) is empty. This was done using the `awk` command:

```
awk -F',' '$3 != ""' lotr_scripts.csv > cleaned_lotr_scripts.csv
```

### Step 2: Normalizing White Spaces
Next, we normalized the spacing in the dataset by replacing multiple consecutive spaces with a single space. This was done using the `sed` command:

```
sed -E 's/[ ]+/ /g' cleaned_lotr_scripts.csv > final_lotr_scripts.csv
```

### Step 3: Removing Special Characters
In this step, we removed unwanted special characters from the dataset, keeping only alphanumeric characters, commas, periods, exclamation marks, question marks, and spaces. This was accomplished using the following `sed` command:

```
sed -E 's/[^a-zA-Z0-9.,?! ]//g' final_lotr_scripts.csv > lotr_cleaned.csv
```
1.1
```sh
davio@DaviG15 MINGW64 ~/individual-assignments-daviallencar/assignments/05 (main)
$ wc -l cleaned_lotr_scripts.csv
2391 cleaned_lotr_scripts.csv
```

1.2
```sh
davio@DaviG15 MINGW64 ~/individual-assignments-daviallencar/assignments/05 (main)
$ awk -F, '{print $2}' cleaned_lotr_scripts.csv | tr ' ' '\n' | tr -d '[:punct:]' | sort | uniq | wc -l
3729
```

2.
```sh
davio@DaviG15 MINGW64 ~/individual-assignments-daviallencar/assignments/05 (main)
$ cat cleaned_lotr_scripts.csv | awk -F',' '{print $3}' | sort | uniq -c
>> it didn't work so well
```

3.
```sh
davio@DaviG15 MINGW64 ~/individual-assignments-daviallencar/assignments/05 (main)
$ awk -F',' '{gsub(/"/, "", $1); print $1}' cleaned_lotr_scripts.csv | sort | uniq -c | sort -nr | head -n 5
    225 FRODO
    216 SAM
    204 GANDALF
    185 ARAGORN
    163 PIPPIN
```

4.
```sh
davio@DaviG15 MINGW64 ~/individual-assignments-daviallencar/assignments/05 (main)
$ cut -d',' -f2 cleaned_lotr_scripts.csv | tr ' ' '\n' | tr "[!?.]" "\n" | sort | uniq -c | sort -nr | head -n 5 
    540 the
    336 of
    329 you
    320 to
    221 is
```
