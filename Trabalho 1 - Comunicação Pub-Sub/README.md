# Trabalho Comunicação Publish/Subscribe

O objetivo desse trabalho é fazer um "Whatsapp" usando Comunicação Publish/Subscribe com broker RabbitMQ.

Qual o IP da maquina com o Broker: --Aqui deverá ser colocado o IP da máquina em que o broker está rodando no formato: 10.10.0.91

Conexão iniciada

Foi realizada uma subscription no topic "Aluno.Matheus".

Ele está aguardando uma mensagem na fila.

Quando receber uma mensagem

### Pub-Sub-Zap
```
docker run --rm -it --network=host giovanapr/pub-sub-zap:2 python3 pub-sub-zap.py
```

Caso seja necessário rodar o broker, pode ser usada a seguinte imagem.

### Broker
```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```
