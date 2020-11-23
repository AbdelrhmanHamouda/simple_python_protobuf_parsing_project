# simple python protobuf parsing project
An attempt to make a python protobuf parser. 

# How to install protobuf for MacOS 
```bash
brew install protobuf
```


# How to run 
### Step1: Generate the .pb2.py
```bash
protoc -I=. --python_out=. ./todolist.proto
```
This will generate a <.proto_filename>.pb2.py

### Step2: Pip install protobuf
- Figure out the protoc version 
``` bash 
protoc --version
```
- Create and activate your venv
```bash
python3 -m venv venv
source venv/bin/activate
``` 
- Pip install the same protobuf version 
```bash
pip3 install protobuf==3.14.0
```
### Step3: Run the python script
```bash
python3 proto_test.py
```

