import pika


def main():
    # Спочатку нам потрібно створити з'єднання з RabbitMQ:
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    # Далі потрібно створити чергу повідомлень і дамо їй ім'я 'hello_world':
    channel.queue_declare(queue='hello_world')

    # RabbitMQ проігнорує повідомлення, якщо воно відправлене в неіснуючу чергу. Далі надсилаємо саме повідомлення:
    channel.basic_publish(exchange='', routing_key='hello_world', body='Hello world!'.encode())
    print(" [x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    main()
