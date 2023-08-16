
personList=get_person_list()
personTitle=get_person_title()
emailAddress=get_person_address()

personList=["王","林"]
personTitle=["先生","女士"]
emailAddress=["wu@gmail.com","lin@gmail.com"]
subject="主旨"
txt="內容"
for i in range(len(personList)):
    s = personList[i] + personTitle[i]
    send_email(s,emailAddress[i],subject,txt)