# simple python protobuf parsing project
The idea of this repo is to understand what protobuf is and how to use it (generally and with Python specifically).

# How to install protobuf for MacOS 
```bash
brew install protobuf
```


# How to run 
### Step1: Generate the .pb2.py
```bash
# For Example_todo_list
protoc -I=. --python_out=. ./todolist.proto
# For Example_person_profile 
mkdir generated
protoc interfaces/person_info.proto --python_out Example_person_profile/ --proto_path generated=interfaces/
protoc interfaces/person.proto --python_out Example_person_profile/ --proto_path generated=interfaces/
```
This will generate a <.proto_filename>.pb2.py
#### A visalization on what is being done by the `protoc` command
<img src="https://user-images.githubusercontent.com/7114320/100013532-468f1c00-2dd5-11eb-8ff6-3d9325fd7489.png"  width="500">

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
# For Example_todo_list
python3 proto_test.py
# For Example_person_profile 
python3 person_with_one_friend.py
```

# Output
```json
// From Example_todo_list 
My OG list is:
owner_id: 1234
owner_name: "Tim"
todos {
  state: TASK_DONE
  task: "Test ProtoBuf for Python"
  due_date: "31.10.2019"
}

My new list is:
owner_id: 1234
owner_name: "Tim"
todos {
  state: TASK_DONE
  task: "Test ProtoBuf for Python"
  due_date: "31.10.2019"
}


// Fron Example_person_profile
My OG person is:
info {
  age: 30
  height: 184
}
friends {
  friendship_duration: 365.1000061035156
  shared_hobbies: "books"
  shared_hobbies: "daydreaming"
  shared_hobbies: "unicorns"
  person {
    info {
      age: 40
      height: 165
    }
  }
}

My new person is:
info {
  age: 30
  height: 184
}
friends {
  friendship_duration: 365.1000061035156
  shared_hobbies: "books"
  shared_hobbies: "daydreaming"
  shared_hobbies: "unicorns"
  person {
    info {
      age: 40
      height: 165
    }
  }
}
```



## References
- https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/
- https://www.datascienceblog.net/post/programming/essential-protobuf-guide-python/
- https://developers.google.com/protocol-buffers/docs/pythontutorial


##### TODO:
- Go over examples in this repo
    - https://github.com/simplesteph/protobuf-example-python