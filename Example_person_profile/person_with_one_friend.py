# fill protobuf objects
import generated.person_pb2 as person_pb2
import generated.person_info_pb2 as person_info_pb2

############
# define friend for person of interest
#############
friend_info = person_info_pb2.PersonInfo()
friend_info.age = 40
friend_info.sex = person_info_pb2.Sex.M
friend_info.height = 165
friend_person = person_pb2.Person()
friend_person.info.CopyFrom(friend_info)
friend_person.friends.extend([])  # no friends :-(

#######
# define friendship characteristics
########
friendship = person_pb2.Friend()
friendship.friendship_duration = 365.1
friendship.shared_hobbies.extend(["books", "daydreaming", "unicorns"])
friendship.person.CopyFrom(friend_person)

#######
# assign the friend to the friend of interest
#########
person_info = person_info_pb2.PersonInfo()
person_info.age = 30
person_info.sex = person_info_pb2.Sex.M
person_info.height = 184
person = person_pb2.Person()
person.info.CopyFrom(person_info)
person.friends.extend([friendship])  # person with a single friend

#! Write into a file
with open("Example_person_profile/serializedFile", "wb") as fd:
    fd.write(person.SerializeToString())

#! Read from a file
read_person = person_pb2.Person()
with open("Example_person_profile/serializedFile", "rb") as fd:
    read_person.ParseFromString(fd.read())


print(f'My OG person is:\n{person}')
print(f'My new person is:\n{read_person}')
