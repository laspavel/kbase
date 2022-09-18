
# Бэкапирование
pg_dumpall -c -g > _globals.sql
-g - Выгружать только глобальные объекты (роли и табличные пространства), без баз данных
-c - Добавить удаление (DROP) объектов, прежде чем пересоздавать их.

# Восстановление
## Первый (SQL дапм обычный):

1) psql -f _global.sql
2) dropdb dbname
3) createdb -T template0 dbname
4) gunzip -c dbname.gz | psql dbname

## Второй (SQL дамп в каталоге)
1) psql -f _global.sql
2) pg_restore -c -C -d postgres -v --if-exists -F d -j$(nproc) ShopPlus_ProductAccounting_Dev

-c - Удалить (DROP) объекты базы данных, прежде чем пересоздавать их.
-C - Создать базу данных, прежде чем восстанавливать данные.
-F d - Задаёт формат архива (d - Каталог)
-j - Количесто параллельных потоков
-d - Имя контекста (postgres)
-v - Включает режим подробных сообщений.
--if-exists - удаление происходит только если обьект существует.


### Посмотреть "зависшие" слоты репликации:
SELECT * FROM pg_replication_slots WHERE active = 'f';

### Удалить "зависшие" слоты репликации:

Удаление конкретного слота: 
SELECT pg_drop_replication_slot('slot_name');

Удаление всех не активных слотов:
SELECT pg_drop_replication_slot(slot_name) FROM pg_replication_slots WHERE active = 'f';