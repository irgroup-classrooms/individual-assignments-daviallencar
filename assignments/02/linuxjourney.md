1. Try some other Linux commands and see what they output:

$ date > Tue Nov 26 17:48:14 HPEO 2024
$ whoami > davio

What should be outputted to the display when you type echo Hello World?
> Hello World

2. No exercises for this lesson

How do I find what directory you are currently in?
> pwd

3. Run the cd command without any flags, where does it take you?
> /c/Users/davio

If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?
> cd ..

4. Run ls with different flags and see the output you receive.
ls -R > contatos  myfile  oi.txtls -r
ls -r > oi.txt  myfile  contatos
ls -t > oi.txt  contatos  myfile

What command would you use to see hidden files?
> ls -a

5. Create a new file > touch myfile
Note the timestamp > -rw-r--r-- 1 davio 197609 0 Nov 26 18:35 newfile
Touch the file and check the timestamp once again > -rw-r--r-- 1 davio 197609 0 Nov 26 18:37 newfile

How do you create a file called myfile?
> touch myfile

6. Run the file command on a few different directories and files and note the output.
> $ file contatos
contatos: empty
> $ file oi.txt
oi.txt: empty

What command can you use to find the file type of a file?
> file

7. Run cat on different files and directories. Then try to cat multiple files.
> $ cat oi.txt
hello
> $ cat oi.txt world.txt > helloworld.txt
> $ cat helloworld.txt
hello
world!!!

What's a good way to see the contents of a file?
> cat

8. Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.
> $ less oi.txt

How do you quit out of a less command?
> q
