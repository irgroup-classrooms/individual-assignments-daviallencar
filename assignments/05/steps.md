# Data Fields Description for LOTR Scripts

## Data Fields:

1. **char** (Character)
   - **Description**: This field represents the name of the character who is speaking the dialogue.
   - **Example**: `DEAGOL`, `SMEAGOL`, `FRODO`

2. **dialog** (Dialogue)
   - **Description**: This field contains the spoken lines or dialogue of the character.
   - **Example**: `Oh Smeagol Ive got one!`, `Pull it in! Go on, go on, go on, pull it in!`

3. **movie** (Movie)
   - **Description**: This field indicates the name of the movie in the "Lord of the Rings" series from which the dialogue is taken.
   - **Example**: `The Return of the King`

## Summary:
- The dataset consists of three main fields: character name, their dialogue, and the movie title.

# Data Cleaning Logic for LOTR Scripts

## Steps Taken:

1. **Removed Extra Column**  
   - **Tool**: `cut`  
   - **Command**:  
     ```bash
     cut -d',' -f2- lotr_scripts.csv > temp_lotr_scripts.csv
     ```

2. **Regex Replacements**  
   - **Remove unwanted characters**:  
     ```bash
     sed -i 's/Â//g' temp_lotr_scripts.csv
     ```
   - **Fix extra spaces and quotes**:  
     ```bash
     sed -i 's/[[:space:]]\+/ /g' temp_lotr_scripts.csv
     sed -i 's/"//g' temp_lotr_scripts.csv
     ```
   - **Fix names in parentheses**:  
     ```bash
     sed -i 's/(GOLLUM/GOLLUM/g' temp_lotr_scripts.csv
     ```

3. **Filtering Invalid Data**  
   - **Command**:  
     ```bash
     awk -F',' 'NF>=3 && $2!="" && $3!=""' temp_lotr_scripts.csv > cleaned_lotr_scripts.csv
     ```

## Summary
- **Tools**: `cut`, `sed`, `awk`
- Cleaned and structured the data by removing extra columns, fixing formatting, and filtering invalid rows.
