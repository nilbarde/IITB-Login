from sys import argv
from os.path import realpath, dirname
from os import system as terminal

if(__name__=="__main__"):
	if not(len(argv)==3):
		print("LDAP-ID or Password not entered")
		print("python LoginSetup.py LDAP-ID LDAP-Password")
		print("e.g. python3 LoginSetup.py 170260010 Nihal@1234")
		exit()
	else:
		LDAP_ID = argv[1]
		LDAP_Password = argv[2]
	print("The LDAP-ID you entered is " + LDAP_ID)
	print("The LDAP-Password you entered is " + LDAP_Password)
	
	SetupFilePath = (realpath(__file__))
	Folder = dirname(SetupFilePath)
	LoginFilePath = Folder + "/MyLogin.py"

	LoginFile = open(LoginFilePath,"r")
	LoginFileCode = LoginFile.read()

	LoginFileCode = LoginFileCode.replace("LDAP-ID",LDAP_ID)
	LoginFileCode = LoginFileCode.replace("LDAP-Password",LDAP_Password)
	LoginFile.close()

	NewLoginFile = open(LoginFilePath,"w")
	NewLoginFile.write(LoginFileCode)
	NewLoginFile.close()

	AddBashrc = "echo 'python3 " + LoginFilePath.replace(" ","\ ") + "' >> ~/.bashrc"
	terminal(AddBashrc)
	print("Done")
