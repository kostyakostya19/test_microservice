from text_operations import word_counter
from send2rabbit import send_data_to_rabbitmq

sent = "my word is bond"

if __name__ == "__main__":
    data_new = word_counter(sent)
    send_data_to_rabbitmq(data_new)