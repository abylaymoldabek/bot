import requests
import misc
from yobit import get_btc
from time import sleep


token = misc.token
URL = "https://api.telegram.org/bot" + token + '/'
global last_update_id
last_update_id = 0

# https://api.telegram.org/bot1959587211:AAFlfT8jSsEOhemecaFd3LMxs7fQqvzj0ys/sendmessage?chat_id=409718505&text=hi


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {'chat_id': chat_id,
                   'text': message_text}
        return message
    return None


def send_message(chat_id, text='Wait a second, please!'):
    url = URL + f"sendmessage?chat_id={chat_id}&text={text}"
    requests.get(url)


def main():
    # d = get_updates()
    while True:
        answer = get_message()
        if answer is not None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue
        sleep(2)


if __name__ == '__main__':
    main()
