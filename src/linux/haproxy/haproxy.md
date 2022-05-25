Перечитывание конфига без рестарта haproxy
- service haproxy reload

**ВАЖНО:
Мягкое обновление HAProxy, которое стало доступно сравнительно недавно, работет весьма специфично. Рядом с работающим HAProxy поднимается еще один экземпляр на который переключается трафик. То есть всегда нужно иметь практически двойной запас ресурсов чтобы было места где стартануть второй экземпляр HAProxy. Все это связано с тем что HAProxy не умеет перечитывать конфиги.**

Страница статистики
- stats auth LOGIN:PASSWORD - Для входа на страницу статистики
- stats uri /haproxy?stats - http://10.0.2.17:9001/haproxy?stats - страница статистики

Ссылки:
- [Перечитка конфига](https://www.haproxy.com/blog/hitless-reloads-with-haproxy-howto/)
- [Установка из исходников](https://upcloud.com/community/tutorials/haproxy-load-balancer-centos/)
- [Исходники версии 1.8](http://www.haproxy.org/download/1.8/src/)
- [Про тюнинг](https://habr.com/ru/company/ostrovok/blog/438966/)
