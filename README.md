# Twilio WhatsApp Auto Message Sender (Python)

A simple Python automation project that sends a scheduled WhatsApp message using the Twilio API.
This project allows users to set a specific time, and the message will automatically be sent at that time.

## 🚀 Features
* Send WhatsApp messages using Twilio API
* Schedule messages at a specific time
* Simple command-line interface
* Modular Python code using functions
* Beginner-friendly automation project

## 🛠 Technologies Used
* Python
* Twilio API
* datetime module
* time module

## 📂 Project Structure
```
whatsapp-message-sender
│
├── main.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

1. Clone the repository
```
git clone https://github.com/thearyal/Twilio-WhatsApp-Auto-Message-Sender-Python-.git
```

2. Navigate to the project folder
```
cd whatsapp-message-sender
```

3. Install required packages
```
pip install twilio
```

## 🔑 Setup Twilio
1. Create an account on Twilio
2. Get your **Account SID** and **Auth Token** from the Twilio console
3. Replace them in the Python script:

```python
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
```

4. Join the Twilio WhatsApp sandbox by sending the provided **join code** to the Twilio sandbox number.

## ▶️ Running the Program

Run the script using:
```
python main.py
```

Then enter:
* Receiver phone number with country code
* Message text
* Scheduled hour
* Scheduled minute

Example:
```
Enter receiver number: +97798XXXXXXXX
Enter message: Hello from Python!
Enter hour: 19
Enter minute: 30
```
The program will wait until the scheduled time and then send the WhatsApp message.

## ⚠️ Note
This project uses the **Twilio WhatsApp Sandbox**, so the receiver must join the sandbox before receiving messages.

## 🎯 Purpose
This project was built to practice:
* Python automation
* API integration
* Scheduled tasks
* Real-world messaging applications

## 📜 License
This project is open-source and available under the MIT License.
