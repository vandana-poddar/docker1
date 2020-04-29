import os
os.system("tput setaf 9")
print("\t\t\t welcome to TUI")
os.system("tput setaf 6")
print("\t\t\t__________________________________")
os.system("tput setaf 7")
while(1):
	print("""
		1-> docker version
		2-> working with docker image
		3-> To check whether docker is installed or not
		4-> to check whether docker is running or not
		5-> To start docker service
		6-> To stop docker service
		7-> to clean the complete environment
		8-> To check list of image in running state
		9-> To check list of image in the stopped state
		10-> To start container or os
		11-> To deal with network service
		12-> to deal with storage
		13->exit 
	      """)
	print("""enter your choice """,end="")
	ch=input()
	if ch=="1":
		os.system("tput setaf 6")
		os.system("docker version")
		os.system("tput setaf 7")
	elif ch=="2":
		os.system("systemctl start docker")
		print("a-> to show list of docker image present")
		print("b-> to add new docker image")
		print("c-> to remove the docker image")
		ans=input()
		if ans=="a":
			os.system("tput setaf 6")
			os.system("docker image ls")
			os.system("tput setaf 7")
		elif ans=="b":
			print("a-> to install centos ")
			print("b-> to install mysql ")
			print("c-> to install ubuntu ")
			print("d-> to install wordpress ")
			print("e-> to install linuxos ")
			image_name=input()
			if image_name=="a":
				os.system("tput setaf 6")
				os.system("docker pull centos")
				os.system("tput setaf 7")
			elif image_name=="b":
				os.system("tput setaf 6")
				os.system("docker pull mysql")
				os.system("tput setaf 7")
			elif image_name=="c":
				os.system("tput setaf 6")
				os.system("docker pull ubuntu")
				os.system("tput setaf 7")
			elif image_name=="d":
				os.system("tput setaf 6")
				os.system("docker pull wordpress")
				os.system("tput setaf 7")
			if image_name=="e":
				os.system("tput setaf 6")
				os.system("docker pull linuxos")
				os.system("tput setaf 7")
		elif ans=="c":
			print("a-> to remove centos ")
			print("b-> to remove mysql ")
			print("c-> to remove ubuntu ")
			print("d-> to remove wordpress ")
			print("e-> to remove linuxos ")
			image_name=input()
			if image_name=="a":
				os.system("tput setaf 6")
				os.system("docker image rm -f centos")
				os.system("tput setaf 7")
			elif image_name=="b":
				os.system("tput setaf 6")
				os.system("docker image rm -f mysql")
				os.system("tput setaf 7")
			elif image_name=="c":
				os.system("tput setaf 6")
				os.system("docker image rm -f ubuntu")
				os.system("tput setaf 7")
			elif image_name=="d":
				os.system("tput setaf 6")
				os.system("docker image rm -f wordpress")
				os.system("tput setaf 7")
			if image_name=="e":
				os.system("tput setaf 6")
				os.system("docker image rm -f linuxos")
				os.system("tput setaf 7")
	elif ch=="3":
		os.system("tput setaf 6")
		os.system("rpm -q docker -ce")
		os.system("tput setaf 7")
	elif ch=="4":
		os.system("tput setaf 6")
		os.system("systemctl status docker")
		os.system("tput setaf 7")
	elif ch=="5":
		os.system("tput setaf 6")
		os.system("systemctl start docker")
		os.system("exit")
		os.system("tput setaf 7")
	elif ch=="6":
		os.system("tput setaf 6")
		os.system("systemctl stop docker")
		os.system("exit")
		os.system("tput setaf 7")
	elif ch=="7":
		os.system("tput setaf 6")
		os.system("docker rm -f $(docker ps -a -q)")
		os.system("tput setaf 7")
	elif ch=="8":
		os.system("tput setaf 6")
		os.system("docker ps")
		os.system("tput setaf 7")
	elif ch=="9":
		os.system("tput setaf 6")
		os.system("docker ps -a")
		os.system("tput setaf 7")
	elif ch=="10":
			os.system("systemctl start docker")
			print("a-> to start centos ")
			print("b-> to start mysql ")
			print("c-> to start ubuntu ")
			print("d-> to start wordpress ")
			print("e-> to start linuxos ")
			image_name=input()
			if image_name=="a":
				os.system("tput setaf 6")
				os.system("docker container run -it --name cen1 centos : latest")
				os.system("tput setaf 7")
			elif image_name=="b":
				os.system("tput setaf 6")
				os.system("docker container run -it --name sql1 mysql : latest")
				os.system("tput setaf 7")
			elif image_name=="c":
				os.system("tput setaf 6")
				os.system("docker container run -it --name ubn1 ubuntu : latest")
				os.system("tput setaf 7")
			elif image_name=="d":
				os.system("tput setaf 6")
				os.system("docker container run -it --name wrd1 wordpress : latest")
				os.system("tput setaf 7")
			if image_name=="e":
				os.system("tput setaf 6")
				os.system("docker container run -it --name lin1 linuxos : latest")
				os.system("tput setaf 7")
	
	elif ch=="11":
		print("a-> to show list of network present")
		print("b-> to create network")
		print("c-> to inspect bridge")
		print("d-> to install http")
		print("e-> to install net tool")
		print("f-> to install php")
		ans=input()
		if ans=="a":
			os.system("tput setaf 6")
			os.system("docker network ls")
			os.system("tput setaf 7")
		elif ans=="b":
			os.system("tput setaf 6")
			os.system("docker network create --driver bridge net1")
			os.system("tput setaf 7")
		elif ans=="c":
			os.system("tput setaf 6")
			os.system("docker network inspect bridge")
			os.system("tput setaf 7")
		elif ans=="d":
			os.system("tput setaf 6")
			os.system("yum install net-tools -y")
			os.system("tput setaf 7")
		elif ans=="e":
			os.system("tput setaf 6")
			os.system("yum install httpd -y")
			os.system("tput setaf 7")
		elif ans=="f":
			os.system("tput setaf 6")
			os.system("yum install php")
			os.system("tput setaf 7")		
	elif ch=="12":
		print("a-> to show list of storage")
		print("b-> to create volume")
		print("c-> to inspect volume")
		ans=input()
		if ans=="a":
			os.system("tput setaf 6")
			os.system("docker volume ls")
			os.system("tput setaf 7")
		if ans=="b":
			os.system("tput setaf 6")
			os.system("docker volume create myst1")
			os.system("tput setaf 7")
		if ans=="c":
			os.system("tput setaf 6")
			os.system("docker network inspect myst1")
			os.system("tput setaf 7")			
	elif ch=="13":
		os.system("tput setaf 6")
		print("Thanku ")
		os.system("tput setaf 7")
		break












