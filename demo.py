from time import sleep
from py_imessage import imessage

number = "4086678219"
lyrics = "lyrics.txt"


#get words from lyrics text
def get_lyrics():
    with open(lyrics) as file:
        data = [line.strip() for line in file]
        string = " ".join(data)
        words = string.split()
    return words

#sending each word
def send_messages(messages, phone_num):
    for message in messages:
        send_message(message, phone_num)
        # print(message)
        sleep(.2)

#sending message in imessage
def send_message(message, phone_num):
    imessage.send(phone_num, message)

#main function
def lyrics_prank(phone_number, lyrics):
    words_list = get_lyrics()
    send_messages(words_list, phone_number)


lyrics_prank(number, get_lyrics())

