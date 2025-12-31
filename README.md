# Python Phishing URL Detection
---
**Python 3.11.9 _(Currently Using)_**


## How to Run?

- Clone or download [phantom](https://github.com/DanielAkintola/phantom) 

`git clone https://github.com/DanielAkintola/phantom.git`


- Create a virtual environment
```bash
python -m venv zenv
source zenv/Scripts/activate # Windows
source zenv/bin/activate # Mac
```


- Install basic requirements
```bash 
pip install --upgrade pip
pip install --upgrade setuptools

pip install pandas whois httpx
pip install pycaret # It will take sometime.

pip install typer
```

### To Run

```bash
python main.py check-url
```

---

