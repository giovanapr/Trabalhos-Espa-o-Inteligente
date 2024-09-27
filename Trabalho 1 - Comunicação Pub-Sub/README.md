# Trabalho Comunicação Publish/Subscribe

O objetivo desse trabalho é fazer um "Whatsapp" usando Comunicação Publish/Subscribe com broker RabbitMQ.
O código funciona da seguinte forma:

primeiro é necessário informar o IP da máquina em que o broker está rodando, além disso 

### Pub-Sub-Zap
```
docker run --rm -it --network=host giovanapr/pub-sub-zap:2 python3 pub-sub-zap.py
```

Caso seja necessário rodar o broker, pode ser usada a seguinte imagem.

### Broker
```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```
