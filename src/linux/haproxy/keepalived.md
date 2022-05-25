`yum install keepalived`

`systemctl enable keepalived`

`service keepalived start`

`10.0.6.100/24` - Плавающий ip

**priority 100** - В обоих случаях, значит, что тот у кого ip будет его держать, пока сам не отпадет.

`ip -brief address show` - проверка на какой из нод сейчас ip.

**Node_1**

[root@k8s-hapr-01 haproxy]# ip -brief address show

lo               UNKNOWN        127.0.0.1/8 ::1/128

eth0             UP             10.0.9.38/24 fe80::215:5dff:fe45:f227/64

**Node_2**

[root@k8s-hapr-02 haproxy]# ip -brief address show

lo               UNKNOWN        127.0.0.1/8 ::1/128

eth0             UP             10.0.9.39/24 **10.0.6.100/24** fe80::215:5dff:fe45:f228/64

`use_vmac` - Использовать одинаковый мак адрес на обеих нодах

Ссылки:
[Настройка](https://www.redhat.com/sysadmin/keepalived-basics)
