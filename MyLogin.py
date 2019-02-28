from mechanize import Browser

class RobotLogin():
	def __init__(self):
		self.LogInURL = "https://internet.iitb.ac.in/index.php"
		self.LoggedInURL = "https://internet.iitb.ac.in/logout.php"

		self.UserName = "LDAP-ID"
		self.Password = "LDAP-Password"

		self.Browser = Browser()
		self.Browser.set_handle_robots(False)

	def LogIn(self):
		try:
			self.Browser.open(self.LogInURL)
		except :
			return False
		if(self.CheckIfLoggedIn()):
			return True
		self.Browser.select_form(name="auth")
		self.Browser["uname"] = self.UserName
		self.Browser["passwd"] = self.Password
		self.Response = self.Browser.submit()

		if not(self.CheckIfLoggedIn()):
			print("Failed To Login")
		return True

	def CheckIfLoggedIn(self):
		self.Browser.open(self.LogInURL)
		self.NowURL = self.Browser.geturl()
		if(self.NowURL == self.LoggedInURL):
			return True
		else:
			return False

if(__name__=="__main__"):
	my = RobotLogin()
	my.LogIn()
