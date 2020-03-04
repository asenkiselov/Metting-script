#!/usr/bin/env python3

import datetime
import email
import smtplib
import sys

def usage():
    print("send_remainders; Send meeting reminders")
    print()
    print("invocation:")
    print("        send_reminders 'date|Meeting Title|emails'")
    return 1

def dow(date)
    dateobj = datetime.datetime.strptime(date, r"%d/%m/%Y")
    return dateobj.strftime("%A")

def message_tamplate(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi all!

This is a quick mail to remind you all that we have a meeting about:
"{title}"
the {weekday} {date}.

See you there.
''')
    return message

def send_message(message, emails):
    smtp = smtplib.SMTP('localhost')
    message['From'] = 'noreply@example.com'
    for email in emails.split(','):
        del message['To']
        message['To'] = email
        smpt.send_message(message)
    smpt.quit()

def main():
    if len(sys.argv) < 2:
        return usage()
    try:
        date, title, emails = sys.argv[1].slit('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent remainders to: ", emails)
    except Exception as e:
        print("Failure to send email", file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())


