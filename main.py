"""

CRUD - Create Read Update Delete

DataBase 

Terminal View

UX - add Email and Message (CRUD)

"""

DataBase: dict = dict()

_id = 0


def get_data_or_error(DataBase: dict, id: int) -> dict:
    try:
        object_ = DataBase[id]
    except KeyError as e:
        raise ValueError("Такого индекса не существует!!!")
    else:
        return object_


def create_data(email: str, message: str):
    """
    add object in Database
    """
    global _id

    obj = {
        "email": email,
        "message": message
    }
    DataBase[_id] = obj

    _id += 1


def show_database(flag: bool = False, *args, **kwargs) -> None:
    """
    show all data in DataBase
    """
    if args:
        for obj in args:
            print(obj)
        return None
    
    if kwargs:
        for k, v in kwargs.items():
            print(k, v)
        return None

    if flag:
        for k, v in DataBase.items():
            print(k, v, "\n")
    else:
        print(DataBase)


def read_to_database(id:int, *args, **kwargs) -> dict:
    """
    it's function return DataBase ---> Object
    """

    object_ = get_data_or_error(DataBase=DataBase, id=id)

    return object_


def update_data(id: int, **kwargs) -> dict:
    """
    it's function update data in DataBase on ID
    """
    email = kwargs.get("email")
    message = kwargs.get("message")

    global DataBase

    object_ = get_data_or_error(DataBase=DataBase, id=id)

    object_["email"] = email if email else object_["email"]
    object_["message"] = message if message else object_["message"]
  
    return object_


def delete_data(id: int) -> dict:
    """
    it's funciton delete object on ID in DataBase
    """
    global DataBase
    get_data_or_error(DataBase=DataBase, id=id)
    object_ = DataBase.pop(id)

    return object_



for i in range(10):
    create_data(f"test{i}@test.com", "hello it is SPAMMMM")


# show_database(flag=True)
# answer = read_to_database(id=3)
# show_database(flag=False, args=answer)
# update_data(3, email="Zhant@gmail.com", message="Hahah lol")
# print(delete_data(id=3))

try:
    object_ = read_to_database(id=9)
except Exception as e:
    print(e)
else:
    print("Вот твои даные!!!!")
    print(object_)


# TODO ShowData upgrade!!!!