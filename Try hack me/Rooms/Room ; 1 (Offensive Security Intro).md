
In this room I am going to learn about the basic of offensive security. 

#offensivesecurity
#tryhackrooms

## Offensive Security
so offensive security is thinking like a hacker and finding weakness before real hacker do. 

In this tryhackme lab we are given a website of a banking system where the url is http://fakebank.thm/ in this url there is the bank account number and name 

Bank url: http://fakebank.thm/
bank account no: 8881
bank accoount name: Mrs G. Benjamin 

In this lab we need to find a hidden page which is accessible by anyone. We are going to use the terminal to find the hidden page using the tool name dirbuster.  

#dirbuster 

## Dirbuster 
Dirbuster is a free-open source web application security scanner which can be used to find hidden directories and files. It can also be used in various way to brute force into files, directories, including dictonary attacks and brute force attacks and hybrid attacks. 

step 1: download dirbuster in the system you are using. 
step 2: find the page you want to look into in this case it is http://fakebank.thm 
step 3: use this command in the command line:  "  dirb http://fakebank.thm  "

![[Pasted image 20260916151745.png|520]]

after the scan is complete it will show something like this. 

we have found something that should not be oout in open and that is http://fakebank.thm/bank-transfer 

now when we go to that site we can enter the account number and amount you want to deposite 



## ==🟢And the Room is completed.==

