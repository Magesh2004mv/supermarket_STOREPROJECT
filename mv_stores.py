import datetime
import smtplib

def generate_bill(item_name, item_price, howmany):
    total = item_price * howmany
    with open('bill.txt', "a") as bill:
        date1 = datetime.datetime.now()
        date2 = date1.strftime("%d:%b:%Y %H:%M:%S")
        bill.write(f"\nDate and time: {date2}\n")
        bill.write(f"{item_name.capitalize()} amount: {item_price} \nHow many product(s): {howmany} \nTotal supermarket bill is: {total}\n")
    print(f"Total supermarket bill is {total}")
    return total

def email_supermarket(total, send_mail):
    try:
        sender_email = "  "  
        sender_password = "  "      
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        subject = "Your MV Supermarket Bill"
        body = f"Your MV Supermarket bill total is: {total}"
        
        message = f"Subject: {subject}\n\n{body}"
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, send_mail, message)
        
        print("Mail sent successfully")
    except Exception as e:
        print(f"Mail not sent. Error: {e}")

def mark_1():
    items = {
        "rice": 1500,
        "ghee": 590,
        "oil": 800,
        "champoo": 250
    }
    
    user = input("Enter the item: ").lower()
    
    if user in items:
        print("Yes, available")
        item_price = items[user]
        print(f"{user.capitalize()} amount: {item_price}")
        howmany = int(input("How many products: "))
        total = generate_bill(user, item_price, howmany)
        
        var = input("If you want another product (yes/no): ").lower()
        if var == "yes":
            mark_1()
        else:
            print("Thank you for purchasing")
            send_mail = input("Enter your email address: ")
            email_supermarket(total, send_mail)
    else:
        print("Not available")

mark_1()
