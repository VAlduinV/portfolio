import pika
import sys


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello_world')

    def callback(ch, method, properties, body):
        """
            Функція callback повинна обов'язково приймати 4 аргументи:

            ch — поточний канал комунікації (цей об'єкт може перервати виконання циклу всередині start_consuming, якщо потрібно);
            method — детальна інформація про повідомлення;
            properties — службова інформація про повідомлення;
            body — тіло повідомлення у форматі bytes рядка.
        """
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello_world', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
