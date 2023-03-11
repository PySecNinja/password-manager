# Are you asking yourself why use an offline password manager? 
## Here are 4 reasons I chose to program my own local password manager in python.
```plain text
1. Control: With a local password manager, you have complete control over your data. 
   Your passwords and other sensitive information are stored locally on your device, 
   and you are responsible for keeping them secure. 
   This means that you don't have to rely on a third-party service to protect your data.

2. Security: While online password managers may use strong encryption to protect your data, 
   they are still vulnerable to online attacks. For example, if the online password manager's 
   server is compromised, your data could be exposed. With a local password manager, your 
   data is not connected to the internet, so it's much harder for a hacker to access it.

3. Accessibility: Local password managers are accessible offline, which means you can access your 
   passwords and other information even when you don't have an internet connection. This can be 
   especially useful when you're traveling or in a location with poor connectivity.

4. Privacy: Some people are uncomfortable with the idea of storing their sensitive information 
   in the cloud. With a local password manager, you don't have to worry about your data being 
   accessed or analyzed by third-party services.
```
# See the Usage Section in each .py file to see what the code does

# 1. Create virtual python env
```bash
python -m venv venv && source venv/bin/activate #Linux
python -m venv venv && \venv\Scripts\activate #Windows
```

### Creates virtual python environment 
```bash
python -m venv venv 
```

### Steps into virtual environment 
```bash
source .venv/bin/activate
```

### See the terminal now has the name of your virtual environment
```bash
(venv) drew@Andrews-MacBook-Pro% 
```

### To Step out of the virtual environment 
```bash
deactivate
```

# 2. Install dependencies (Inside of Virtual environment)
```bash
pip install -r requirements.txt
```

# 3 Run the Code
```bash
python main.py
```

# TROUBLESHOOTING
```bash
pip list
python --version 
pip --version 
```
```plain text
If trying to do this with VS CODE ensure you have your files open on the left side aka the workspace 

Command+shift+p select interpreter and chose .venv/bin python
```

