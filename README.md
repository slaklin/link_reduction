# Bitly url wrapper
The utility helps to shorten URLs using the service Bit.ly. it also has an option for counting clicks already created Bit.ly references.
## How to install

Create [bit.ly](https://bitly.com) GENERIC ACCESS TOKEN for work with API.

#### Requirements

Python3 should be already installed. Then use pip to install dependencies:
```
pip install -r requirements.txt
```
### Create an environment

#### Environment variables

- BITLY_ACCESS_TOKEN

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:
```
$ cat .env
BITLY_ACCESS_TOKEN=1a5d754733b0130143c70238efa4esa4d1taec48
```
  
## Example of running a script
- Running the program to shorten the link:
```
C:\Users\link_reduction> python main.py https://www.google.com/
Abbreviated link: https://bit.ly/3WxCAme
```

- With a bit.ly url:
```
C:\Users\link_reduction> python main.py https://bit.ly/3WxCAme
Number of clicks: 1
```
## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)
