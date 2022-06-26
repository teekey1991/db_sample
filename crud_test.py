from db_config import Message

def create_message():
    message = Message(user="Bob", content="Hello Tom!")
    message.save()

    Message.create(user="Tom", content="Hello Bob!")

def display_all_message():
    for msg in Message.select():
        print(msg.id, msg.user, msg.content, msg.pub_date)

def find_message(id):   #取得
    msg = Message.get(Message.id == id)
    print(msg.id, msg.user, msg.content, msg.pub_date)

def delet_user(id): #削除
    msg = Message.select().where(Message.id == id).get()
    msg.delete_instance()

def update(id): #更新
    msg = Message.select().where(Message.id == id).get()
    msg.user = "Tom Ford"
    msg.save()

def main():

    # create_message()
    display_all_message()

    # id = 1
    # find_message(id)  #取得

    # id = 1
    # delet_user(id)    #削除

    # id = 2
    # update(id)    #更新

if __name__ == "__main__":
    main()