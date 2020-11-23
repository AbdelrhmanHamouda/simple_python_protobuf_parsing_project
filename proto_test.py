import todolist_pb2 as TodoList

# Create a proto object
my_list = TodoList.TodoList()
my_list.owner_id = 1234
my_list.owner_name = "Tim"

first_item = my_list.todos.add()
first_item.state = TodoList.TaskState.Value("TASK_DONE")
first_item.task = "Test ProtoBuf for Python"
first_item.due_date = "31.10.2019"

#! Write into a file
with open("./serializedFile", "wb") as fd:
    fd.write(my_list.SerializeToString())


#! Read from a file
my_new_list = TodoList.TodoList()
with open("./serializedFile", "rb") as fd:
    my_new_list.ParseFromString(fd.read())

print(f'My OG list is:\n{my_list}')
print(f'My new list is:\n{my_new_list}')
