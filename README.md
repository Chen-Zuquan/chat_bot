# Stock_Chatbot
## demo
![avatar](https://github.com/Chen-Zuquan/chat_bot/blob/master/example/01.gif) 
![avatar](https://github.com/Chen-Zuquan/chat_bot/blob/master/example/02.gif)

## Configuration Instructions
## Installation Instructions
There are few online packages need to be installed for this project
### Rasa-NLU
#### Prerequisites
Make sure the Microsoft VC++ Compiler is installed, so python can compile any dependencies. You can get the compiler from: https://visualstudio.microsoft.com/visual-cpp-build-tools/ Download the installer and select VC++ Build tools in the list.

Setting up Rasa NLU

#### Stable (Recommended)
The recommended way to install Rasa NLU is using pip which will install the latest stable version of Rasa NLU:

```
pip install rasa_nlu 
``` 
#### Latest (Most recent github)
If you want to use the bleeding edge version you can get it from github:

```
git clone https://github.com/RasaHQ/rasa_nlu.git
cd rasa_nlu
pip install -r requirements.txt
pip install -e .
```

Rasa NLU has different components for recognizing intents and entities, most of these will have some additional dependencies.
When you train your model, Rasa NLU will check if all required dependencies are installed and tell you if any are missing.

#### For more installation information
Go to https://rasa.com/docs/nlu/installation/

### iexfinance
#### Setting up iexfinance

#### From PyPI with pip (latest stable release):
```
$ pip3 install iexfinance
```
#### From development repository (dev version):
If you want to use the bleeding edge version you can get it from github:

```
$ git clone https://github.com/addisonlynch/iexfinance.git
$ cd iexfinance
$ python3 setup.py install
```
For more installation information
Go to https://github.com/addisonlynch/iexfinance

### spacy
#### Setting up iexfinance

```
conda install -c conda-forge spacy=2.0.11
python -m spacy download en_core_web_md
```

### wxpy
#### Setting up wxpy

wxpy support Python 3.4-3.6, and 2.7 version
To ensure the package can be installed in different Python version
Replace pip in the commond below to ```pip3``` or ```pip2```

#### From PyPI with pip:
```pip install -U wxpy```

#### For more installation information
Go to https://wxpy.readthedocs.io/zh/latest/#

## operating instructions
1.Download all files in a same folder.
2.You Open ```chat_bot.py``` file in any IDE to check if the function is complete, the IDE I used to run is Pycharm.
3.Open ```wx_chat.py``` file
4.Change the parameter below to chat with your own friend
```
# search the friend whose name is "陈祖泉", and sex is male 
my_friend = bot.friends().search('陈祖泉', sex=MALE)[0]
```
5.Run it, an QR code will created automatically, use your Wechat to scan the QR code and log in.
6.Start to chat!

## contact information for the distributor or programmer
Email: 597359489@qq.com
Website: https://github.com/Chen-Zuquan
