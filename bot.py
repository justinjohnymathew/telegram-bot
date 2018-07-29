import requests

url=""
#_______________________________________________________________________________
#                Function to Get API info
def get_info(request):
    response = requests.get(request+'getUpdates')
    return response.json()
#_______________________________________________________________________________
#               Function To Get Details about last update
def last_update(data):
    value=data['result']
    length=len(value)-1
    return value[length]
#_______________________________________________________________________________
#                Function To Get chat ID
def get_chat_id(value):
    chat_id=value['message']['chat']['id']
    return chat_id
#_______________________________________________________________________________
#               Function TO get first Name
def get_name(value):
    name=value['message']['chat']['first_name']
    return name
#_______________________________________________________________________________
#               Function To send Message with bot
def send_message(id,name):
    message="Hello "+ name
    parameters={'chat_id':id,'text':message}
    response=requests.post(url +'sendMessage',data=parameters)
    return response
#_______________________________________________________________________________
#                       Main Function
def main():
    update_id=last_update(get_info(url))['update_id']
    print("BOT is Running")
    while 1:
        if update_id==last_update(get_info(url))['update_id']:
            print("Request for Bot")
            send_message(get_chat_id(last_update(get_info(url))),get_name(last_update(get_info(url))))
            update_id+=1
#_______________________________________________________________________________
if __name__=="__main__":
    main();
