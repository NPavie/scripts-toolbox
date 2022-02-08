import paramiko  # SSH module
import re
import time
import datetime
import os
from urllib.parse import urlparse
import logging
from os import listdir

import shutil
import tempfile


class TemporaryCopy(object):
	""" Classe de copie de fichier temporaire
		Arguments:
		original_path 	-- chemin du fichier d'origine
		path			-- chemin de la copie temporaire
		sftp_client		-- connexion sftp pour copie d'un fichier non-local
	"""

	def __init__(self, original_path, paramiko_sftp_client=None):
		self.original_path = original_path
		self.sftp_client = paramiko_sftp_client

	def __enter__(self):
		temp_dir = tempfile.gettempdir()
		base_path = os.path.basename(self.original_path)
		self.path = os.path.join(temp_dir, base_path)
		if self.sftp_client is not None:
			self.sftp_client.get(self.original_path, self.path)
		else:
			shutil.copy2(self.original_path, self.path)
		return self.path

	def __exit__(self, exc_type, exc_val, exc_tb):
		os.remove(self.path)


class Hotfolder(object):
	""" Classe de gestion d'un hotfolder
		Arguments:
		- folder_url : URL du dossier à analyser
		- callback_on_file_ready : fonction appelée sur chaque fichier prêt à
			être traité
		- callback_on_error (optionnel) : fonction appelé si une erreur s'est
			produite lors du traitement
		- logs_folder_url (optionnel) : URL du dossier où stocker les logs
	"""
	def __init__(
		self,
		folder_url,
		callback_on_file_ready,
		callback_on_error=None,
		logs_folder_url=None
	):
		""" Constructeur
		"""
		self.folder_url = urlparse(folder_url)
		self.logs_folder_url = urlparse(log_folder_url)
		self.callback_on_file_ready = callback_on_file_ready
		self.callback_on_error = callback_on_error
		self.is_logging = False
		self.files = {}

	def log(self, message, log_file_name):
		""" Générateur de log des messages dans un fichier.
		"""
		log_folder = None
		if log_file_name is None:
			log_file_name = "global.log"
		if self.log_folder_url is None:
			log_folder =
		if self.log_folder_url.scheme == 'sftp':
			log_ssh_client = None
			if self.log_folder_url.hostname != self.folder_url.hostname:
				log_ssh_client = paramiko.SSHClient()
				log_ssh_client.set_missing_host_key_policy(
					paramiko.AutoAddPolicy())
				log_ssh_client.connect(
					self.log_folder_url.hostname,
					username=self.log_folder_url.username,
					password=self.log_folder_url.password)
			else:
				log_ssh_client = self.ssh_client
			self.is_logging = True
			while self.is_logging:
				yield

	def start(self):
		if self.url.scheme == 'sftp':
			# Connexion to host
			self.ssh_client = paramiko.SSHClient()
			self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh_client.connect(
				self.folder_url.hostname,
				username=self.folder_url.username,
				password=self.folder_url.password)
			# Get the host name
			# stdin, stdout, stderr = self.ssh_client.exec_command('hostname')
			# host_name = ("".join(line for line in stdout)).strip('\n')
			# Vérification préliminaire : est-ce que l'url pointer est bien
			# un dossier
			stdin, stdout, stderr = ssh_client.exec_command(
				'if [ -d ' + self.folder_url.path + ' ] ;' +
				' then echo true ;' +
				' else echo false; fi')
			path_is_folder = ("".join(line for line in stdout)).strip('\n')
			path_is_folder = True if path_is_folder == 'true' else False
			if path_is_folder is not True:
				raise NotADirectoryError(
					self.folder_url.path +
					" n'est pas un dossier ou n'est pas accessible pour " +
					self.folder_url.username + "@" + self.folder_url.hostname)
			else:  # démarrage de la boucle d'exécution
				self.loop()
		else:
			self.ssh_client = None
			if not os.path.isdir(self.folder_url.path):
				raise NotADirectoryError(
					self.folder_url.path + " n'est pas un dossier " +
					"ou n'est pas accessible sur l'hote")

	def loop(self):
		for i in range(5):


# regex to parse that stat command result
stat_birth_date_pattern = re.compile(r"Birth: (.*)\..* \+.*\n")
stat_file_size_pattern = re.compile(r"Size: (\d*).*\n")

# Parse files to treat
files_sizes = {}
files_status = {}
files_locktime= {}

def do_on_file(file_path,paramiko_sftp_client=None):
	"""
		Actions exécutée sur le fichier trouvé
	"""
	with TemporaryCopy(file_path,paramiko_sftp_client) as file_copy:
		# send file to imagine
		# print the file
	# Do stuff on file copy just like it was an usual file
	# cleanup (or not) the original file treated
	if paramiko_sftp_client is not None :
		paramiko_sftp_client.remove(file_path)
	else :
		os.remove(file_path)
	return None




def list_files_from_url(searched_url):
	o = urlparse(url_test)
	if o.scheme == 'sftp':
		# Connexion to host
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(
			o.hostname,
			username=o.username,
			password=o.password)
		stdin, stdout, stderr = ssh_client.exec_command(
			'ls -1 '+ o.path )
		return [x.strip() for x in stdout.readlines()]
	elif o.scheme == 'file' :

		return None


def hotfolder(folder_url,
		log_folder_url,
		callback_on_file_ready,
		callback_on_error ):
	""" fonction

	"""
	o = urlparse(url_test)
	if o.scheme == 'sftp':
		# Connexion to host
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(
			o.hostname,
			username=o.username,
			password=o.password)
		# Get the host name
		stdin, stdout, stderr = ssh_client.exec_command('hostname')
		host_name = ("".join(line for line in stdout)).strip('\n')

		# check if path pointed by the url is a reachable directory
		stdin, stdout, stderr = ssh_client.exec_command(
			'if [ -d ' + o.path + ' ] ;'
				+ ' then echo true ;'
				+ ' else echo false; fi' )
		path_is_folder = ("".join(line for line in stdout)).strip('\n')
		path_is_folder = True if path_is_folder == 'true' else False
		print(path_is_folder)
		if path_is_folder is not True :
			print("L'url n'est pas celle d'un dossier")
			exit(1)
		else :
			for i in range(5):
				# list files in folder pointed by url
				stdin, stdout, stderr = ssh_client.exec_command(
					'ls -1 ' + o.path)
				folder_content = []
				for line in stdout :
					file_name = line.strip('\n')
					print(file_name)
					stat_stdin, stat_stdout, stat_stderr = ssh_client.exec_command(
						'stat ' + o.path + file_name)
					stat_result = "".join(line for line in stat_stdout)
					birth_date_found = stat_birth_date_pattern.search(stat_result)
					file_size_found = stat_file_size_pattern.search(stat_result)
					if (birth_date_found and file_size_found) :
						birth_date = datetime.datetime.strptime(
							birth_date_found.group(1),
							"%Y-%m-%d %H:%M:%S"
							).timestamp()
						# key for the dictionnaries
						file_extension = "." + file_name.split('.')[-1]
						file_key = file_name
						#file_key = (file_name[0:-len(file_extension)]
						#	+ "("+host_name + "-"
						#	+ str(int(birth_date)) + ")"
						#	+ file_extension)

						if (file_key in files_sizes
								and file_key in files_status ):
							print(file_key
								+ " : " + str(files_sizes[file_key])
								+ " - " + files_status[file_key])
							if (files_sizes[file_key] < int(file_size_found.group(1))
									and files_status[file_key] == "waiting" ):
								print("")
							else :
								print(file_key + " is ready to be treated")
								files_status[file_key] = "ready"
						else :
							files_sizes[file_key] = int(file_size_found.group(1))
							files_status[file_key] = "waiting"
							print("adding file " + file_key + " to the list")
				time.sleep(1)
	elif o.scheme == 'file' :
		print("File url")




# URL to access (to be passed as parameter of the hotfolder)
url_test="sftp://admin_igs:Adm!IGS-cp16@192.168.103.1/virtualDisks/jail/workspace/PDFPrinter/input/"
url_logs="sftp://admin_igs:Adm!IGS-cp16@192.168.103.1/virtualDisks/jail/workspace/PDFPrinter/logs/"
print(list_files_from_url(url_test))
