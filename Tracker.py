import time
import pygetwindow as gw
from datetime import date, datetime, timedelta
import smtplib
import pandas as pd
import atexit
import config

current_window = None
start_time = None
app_data = {}
today = date.today()        
today_adj = today.strftime("%B %d, %Y")
yesterday = today - timedelta(days = 1)
yesterday = yesterday.strftime("%B %d, %Y")

app_df = pd.read_csv("AppUsage.csv")
yesterday_data = app_df[app_df['date'] == yesterday]

def track_app_time():
    global current_window, start_time
    while True:

        new_window = gw.getActiveWindow()

        if new_window != current_window:
            # Calculate the time spent on the previous window
            if current_window is not None:
                
                current_time = datetime.now()
                current_time = current_time.strftime("%H:%M:%S")
                end_time = time.time()
                elapsed_time = end_time - start_time
                app_name = current_window.title

                if app_name in app_data:
                    app_data[app_name] += elapsed_time
                else:
                    app_data[app_name] = elapsed_time

                # Debug prints
                print(f"Writing to TrackRecords.txt: {app_name} - {elapsed_time:.2f} seconds")

                # Save the data to TrackRecords.txt
                with open("TrackRecords.txt", "a") as file:
                    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"{current_datetime} - Time spent on {app_name}: {elapsed_time:.2f} seconds\n")
                    print("Updated TrackRecords.txt!")

                # Save the data to CSV
                          


            # Update current window and start time
            current_window = new_window
            start_time = time.time()

        time.sleep(1)  # Check the active window every 1 second



def send_email():    
    sender = f"Private Person <{config.send}>"
    receiver = f"A Test User <{config.rec}>"
    # Filter the DataFrame to get rows where the date matches yesterday's date
        
    message = f"""\
Subject: Application Usage 
To: {receiver}
From: {sender}

Here is your application's usage data for {yesterday}:

"""

    for _, row in yesterday_data.iterrows():
        if row['isSent'] == 1:
            continue
        else:
            message += f"Application Name: {row['application_name']}\n"
            message += f"Usage: {row['application_usage']} seconds\n"

            

    if yesterday_data.shape[0] > 0:
        with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
            server.starttls()
            server.login("api", config.api)
            server.sendmail(sender, receiver, message)


def save_app_usage():
    global app_df, app_data, today_adj

    for idx, row in yesterday_data.iterrows():
        app_df.loc[idx, 'isSent'] = 1

    app_usage_list = []

    for app, time_spent in app_data.items():
        print(f"Total time spent on {app}: {time_spent:.2f} seconds")

        app_df['application_usage'] = pd.to_numeric(app_df['application_usage'], errors='coerce').fillna(0)

        existing_row = app_df[(app_df['date'] == today_adj) & (app_df['application_name'] == app)]

        if not existing_row.empty:
            # Increment the application_usage
            app_df.loc[existing_row.index, 'application_usage'] += time_spent
        else:
            # Create a new row
            new_row = {
                'date': today_adj,
                'application_name': app,
                'application_usage': time_spent,
                'isSent': 0,
            }
            app_usage_list.append(new_row)

    app_usage_df = pd.DataFrame(app_usage_list)

    # Concatenate the dataframes
    combined_df = pd.concat([app_df, app_usage_df], ignore_index=True)

    # Save to CSV
    combined_df.to_csv('AppUsage.csv', index=False)
    print("App usage data saved to CSV.")

# Register the save_app_usage function to be called on exit
atexit.register(save_app_usage)

if __name__ == "__main__":
    send_email()
    track_app_time()

