import smtplib
import imghdr
import os


username=os.environ.get("GMAIL_USERNAME")
password=os.environ.get("GMAIL_PASSWORD")

no_of_photoes_in_mail=5
source_Directory='/home/vikas/Pictures/'
files=[i for i in os.listdir(source_Directory) if os.path.isfile(os.path.join(source_Directory,i))]
print(files)
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']="Photoes"
msg['From']=username
msg['To']=username
msg.set_content("Image attavhed body content")
count=1


with smtplib.SMTP_SSL("smtp.gmail.com",465) as connect_obj:
    connect_obj.login(username,password)
    for f in files:
        filepath=os.path.join(source_Directory, f)
        if imghdr.what(filepath)=="jpeg":
            with open(filepath,"rb") as ff:
                msg.add_attachment(ff.read(), maintype='image',subtype="jpeg",filename=f)
                count+=1
                if count==no_of_photoes_in_mail:
                    connect_obj.send_message(msg)
                    msg=EmailMessage()
                    msg['Subject'] = "Photoes "
                    msg['From'] = username
                    msg['To'] = username
                    msg.set_content("Image Atached")
                    count=1
    connect_obj.quit()

