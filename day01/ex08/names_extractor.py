import sys

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		raise RuntimeError("Wrong number of arguments")
	
	file_path = sys.argv[1]
	with open(file_path) as f:
		emails_list = f.readlines()
	
	emails_list = [x.strip() for x in emails_list]
	
	with open("emails.tsv", "w") as f:
		for email in emails_list:
			email_split = email.split('@')
			name_and_surname = email_split[0].split('.')
			name_and_surname[0].title()
			name_and_surname[1].title()
			print(name_and_surname[0], name_and_surname[1], sep='\t', file=f)

			
	# print(emails_list)
