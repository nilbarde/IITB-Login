# IITB Login
This code will allow you to get logged in to internet.iitb.ac.in just by opening terminal.You need not to open browser and type your LDAP-ID and password everytime you open your system. You just need to setup before using this.

**Clone the Repository**

Now clone the repository to your machine. Go to your terminal and run command:
```
git clone https://github.com/nilbarde/IITB-Login
```

Install the dependencies required for the setup to run

```
sudo pip3 install mechanize
```

**Setup**
1. Open terminal and browse to folder in which you have cloned the repository. <br>

2. On terminal run following command by replacing "LDAP-ID" with you LDAP-ID and "LDAP-Password" with your Password
```
python3 LoginSetup.py LDAP-ID LDAP-Password
```

For me it is
```
python3 LoginSetup.py 170260010 Nihal@1234
```
<br>
3. You are done with your setup. <br>

Now you just can open new terminal to get logged in to internet.iitb.ac.in
