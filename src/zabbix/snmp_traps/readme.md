# SNMP Traps

1. Установка пакетов
- yum install -y net-snmp-utils net-snmp-perl net-snmp
2. Добавляем файлы конфигов в /etc/snmp/
4. В папку с скриптами заббикса добавляем скрипт обработки трапов - 
 etc/zabbix/external_scripts/externalscripts/zabbix_trap_handler.sh
5. Запускаем службы
- service snmptrapd start
- service snmpd start
6. Создадим лог файл по пути - /var/log/snmptraps/snmptraps.log
7. Проверяем что в файл логов пишутся данные
- snmptrap -v 1 -c public 127.0.0.1 '.1.3.6.1.6.3.1.1.5.4' '0.0.0.0' 6 33 '55' .1.3.6.1.6.3.1.1.5.4 s "eth0"
