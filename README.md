# Bitly url wrapper
The utility helps to shorten URLs using the service Bit.ly. it also has an option for counting clicks already created Bit.ly references.
## How to install
Create [bit.ly](https://bitly.com) GENERIC ACCESS TOKEN for work with API. Specify your token in .env file `BITLY_ACCESS_TOKEN=<your token>`.

### Example:
```
echo `BITLY_ACESS_TOKEN`=<your token>
```
Python3 should be already installed. Then use pip to install dependencies:
```
pip install -r requirements.txt
```
## Example of running a script
- Running the program to shorten the link:
```
C:\Users\link_reduction> python main.py https://www.google.com/
Сокращенная ссылка: https://bit.ly/3WxCAme
```

- With a bit.ly url:
```
C:\Users\link_reduction> python main.py https://bit.ly/3WxCAme
Количество кликов: 1
```
## Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org.](https://dvmn.org/)
