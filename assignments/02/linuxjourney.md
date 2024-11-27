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
ls -R > contatos  myfile  oi.txt  
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

9. What is the command to clear the terminal?  
> clear

10. Copy over a couple of files, be careful not to overwrite anything important.  
> cp oi.txt hello.txt

What flag do you need to specify to copy over a directory?  
> -r

11. Rename a file, then move that file to a different directory.  
> mv oi.txt hi.txt  
> mv contatos /c/Users/davio/documents

How do you rename a file called cat to dog?  
> mv cat dog

12. Make a couple of directories and move some files into that directory.  
> $ mkdir games  
> $ mkdir games1/fps/csgo  
> $ mv myfile newfile /c/Users/davio/games1

What command is use to make a directory?  
> mkdir

13. Create a file called -file (don't forget the dash!).  
Remove that file.  
> touch _file  
> rm _file

How do you remove a file called myfile?  
> rm myfile

14. Find a file from the root directory that has the word net in it.  
> find / -name "*net*"s

What option should I specify for find if I want to search by name?  
> -name

15. Run help on the echo command, logout command and pwd command.  
> help echo  
> help logout  
> help pwd

How do you get quick command line help for built-in bash commands?  
> help

16. Run the man command on the ls command.  
> Doesn’t work in Git Bash

How do you see the manuals for a command?  
> man

17. Run the whatis command on the less command.  
> Doesn’t work in Git Bash

What command can you use to see a small description of a command?  
> whatis

18. Create a couple of aliases then remove them.  
> alias listdocs="ls -l /c/Users/davio/documents"  
> alias listdis08="ls -l /c/Users/davio/dis08"  
> unalias listdocs  
> unalias dis08

What command is used to make an alias?  
> alias
