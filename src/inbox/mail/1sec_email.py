from mailtm import Email

def ee(message):
    subject = message['subject'].split(" is your TikTok code")[0]
    return subject
    

test = Email()


test.register()
print(test.message_list())


test.start(ee)
