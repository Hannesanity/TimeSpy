import smtplib

sender = "Private Person <mailtrap@demomailtrap.com>"
receiver = "A Test User <herakurosu03@gmail.com>"

message = f"""\
Subject: Application Usage 
To: {receiver}
From: {sender}

Here is your yesterday's application usage:

"""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "5cd87f21edaa326fc3ee348c31d98d80")
    server.sendmail(sender, receiver, message)




my_email = "herakurosu00@gmail.com"
password = "qqau uhos kumz bdcg"


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    #connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg= "Subject:Hello\n\nThis is the body")
    

with open("AppUsage.txt", "a") as file:
                    today = date.today()        
                    today = today.strftime("%B %d, %Y")
                    if:

                    else:
                        file.write(f"{today} - {app_name}: {elapsed_time:.2f} seconds\n")




