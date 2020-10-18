import smtplib
import imghdr
import os
from email.message import EmailMessage

username = os.environ.get("GMAIL_USERNAME")
password = os.environ.get("GMAIL_PASSWORD")
no_of_photoes_in_mail=5
source_Directory='/home/vikas/Pictures/test/'
filter_files=["jpeg","png","jpg"]+[".docx",".pdf",".xlsx",".xls",".doc",".txt",".zip",".py"]#images doesn't need to have . extentions


def send_mail(msg):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connect_obj:
            connect_obj.login(username, password)
            print("Username password Accepted")
            connect_obj.send_message(msg)
            print("Mail Sent")
    except Exception as e:
        print("Error : ",e)
    return


files=[i for i in os.listdir(source_Directory) if os.path.isfile(os.path.join(source_Directory,i))]

remaining_files=len(files)
count=0
msg=EmailMessage()
for f in files:
    filepath=os.path.join(source_Directory, f)
    if imghdr.what(filepath)=="jpeg" or imghdr.what(filepath)=="png" or imghdr.what(filepath)=="jpg":
        with open(filepath,"rb") as ff:
            msg.add_attachment(ff.read(), maintype='image',subtype="jpeg",filename=f)
            count+=1
            remaining_files-=1
    elif os.path.splitext(filepath)[1] in filter_files:

        with open(filepath, "rb") as ff:
            msg.add_attachment(ff.read(), maintype='application', subtype="octet-stream", filename=f)
            count += 1
            remaining_files -= 1
    else:
        print("file not attached : ",filepath)
        remaining_files -= 1

    if (count==no_of_photoes_in_mail or remaining_files==0) and count!=0:
        msg['Subject'] = "Photoes "
        msg['From'] = username
        msg['To'] = username
        send_mail(msg)
        count=0
        msg = EmailMessage()
        print("remaining_files : ",remaining_files,"\n\n")