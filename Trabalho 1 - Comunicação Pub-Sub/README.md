# Trabalho Comunicação Publish/Subscribe

O objetivo desse trabalho é fazer um "Whatsapp" usando Comunicação Publish/Subscribe com broker RabbitMQ. Para isso 

### Broker
```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Parte 1
```
docker run --rm -it --network=host giovanapr/part1 python3 Parte1.py
```

### Parte 2
```
docker run --rm -it --network=host giovanapr/part2 python3 Parte2.py
```

### Parte 3
```
docker run --rm -it --network=host giovanapr/part3 python3 Parte3.py
```

