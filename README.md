## Stock_Chatbot
### demo
![avatar](https://github.com/Chen-Zuquan/chat_bot/blob/master/example/01.gif) 
![avatar](https://github.com/Chen-Zuquan/chat_bot/blob/master/example/02.gif)

### Configuration Instructions
### Installation Instructions
There are few online packages need to be installed for this project
#### Rasa-NLU
##### Prerequisites
Make sure the Microsoft VC++ Compiler is installed, so python can compile any dependencies. You can get the compiler from: https://visualstudio.microsoft.com/visual-cpp-build-tools/ Download the installer and select VC++ Build tools in the list.

Setting up Rasa NLU

##### Stable (Recommended)
The recommended way to install Rasa NLU is using pip which will install the latest stable version of Rasa NLU:

```
pip install rasa_nlu 
``` 
##### Latest (Most recent github)
If you want to use the bleeding edge version you can get it from github:

```
git clone https://github.com/RasaHQ/rasa_nlu.git
cd rasa_nlu
pip install -r requirements.txt
pip install -e .
```

Rasa NLU has different components for recognizing intents and entities, most of these will have some additional dependencies.
When you train your model, Rasa NLU will check if all required dependencies are installed and tell you if any are missing.

##### For more installation information
Go to https://rasa.com/docs/nlu/installation/

#### iexfinance
##### Setting up iexfinance

##### From PyPI with pip (latest stable release):
```
$ pip3 install iexfinance
```
##### From development repository (dev version):
If you want to use the bleeding edge version you can get it from github:

```
$ git clone https://github.com/addisonlynch/iexfinance.git
$ cd iexfinance
$ python3 setup.py install
```
For more installation information
Go to https://github.com/addisonlynch/iexfinance
