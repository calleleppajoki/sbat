from sbat.basetaskrunner import dependsOn
from sbat.basetaskrunner import cmd


def restore():
	"""dotnet restore"""
	cmd("dotnet restore")

def dotnetrun():
	"""dotnet run"""
	cmd("dotnet run")

def publish():
	"""dotnet publish"""
	cmd("dotnet publish")

def build():
	"""docker build"""
	cmd("docker build -t testapp .")

def run():
	"""docker run"""
	cmd("docker run -it -p 5000:5000 testapp")