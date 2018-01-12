Working examples from https://www.rabbitmq.com/getstarted.html

Tidbits

**find non-acked messages**
```
sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged
```
