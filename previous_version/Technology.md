## Python
**[virtualenv]()** — программа для создания и управления окружениями Python. Позволяет создать среду со своими отдельными модулями, настройками и программами. Среда ограничивается рамками одного каталога. Очень удобна для работы с различными версиями одних и тех же модулей, для создания проектов, у которых "всё с собой", которые не зависят от операционной системы.

**[virtualenvwrapper]()** — набор команд, делающих работу с виртуальным окружением Python удобнее. Используя virtualenvwrapper, вы можете одной командой создать виртуальное окружение и папку для нового проекта, быстро переключаться между разными проектами, просматривать список доступных окружений.

## Web - базовые
**[HTML](https://ru.wikipedia.org/wiki/HTML)** (от англ. HyperText Markup Language — «язык гипертекстовой разметки») — стандартизированный язык разметки документов во Всемирной паутине. Большинство веб-страниц содержат описание разметки на языке HTML (или XHTML). Язык HTML интерпретируется браузерами; полученный в результате интерпретации форматированный текст отображается на экране монитора компьютера или мобильного устройства.

**[CSS](https://ru.wikipedia.org/wiki/CSS)**(/siːɛsɛs/ англ. Cascading Style Sheets — каскадные таблицы стилей) — формальный язык описания внешнего вида документа, написанного с использованием языка разметки. Преимущественно используется как средство описания, оформления внешнего вида веб-страниц, написанных с помощью языков разметки HTML и XHTML, но может также применяться к любым XML-документам, например, к SVG или XUL.

## Web - фреймворки
**[Django](https://ru.wikipedia.org/wiki/Django)** (Джанго, ['dʒæŋɡoʊ]) — свободный программный каркас для веб-приложений на языке Python, использующий шаблон проектирования MVC. Проект поддерживается организацией Django Software Foundation.

**[Flask](https://ru.wikipedia.org/wiki/Flask_(веб-фреймворк))** — микрофреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2.

**[Pyramid](https://ru.wikipedia.org/wiki/Pyramid_(программный_каркас))** (англ. pyramid — пирамида) — программный каркас (фреймворк) для разработки веб-приложений с открытым исходным кодом, написанный на языке Python в рамках проекта Pylons.

**[Tornado](https://ru.wikipedia.org/wiki/Tornado)** — расширяемый, неблокирующий веб-сервер и фреймворк, написанный на Python. Он был создан для использования в проекте FriendFeed, который в 2009 году приобрела компания Facebook, после чего исходные коды Tornado были открыты.

**[aiohttp](http://aiohttp.readthedocs.io/en/stable/)** - это HTTP Web сервер и клиент для asyncio ([PEP-3156](https://www.python.org/dev/peps/pep-3156/))

**[cyclone](http://cyclone.io)** - Cyclone is a web server framework for Python that implements the Tornado API as a Twisted protocol. Twisted is an event-driven network programming framework for Python, that dates back from 2002. It’s one of the most mature libraries for non-blocking I/O available to the public. Tornado is the open source version of FriendFeed’s web server, one of the most popular and fast web servers for Python, with a very decent API for building web applications.

## Форматы данных
**[JSON](https://ru.wikipedia.org/wiki/JSON)** (англ. JavaScript Object Notation, обычно произносится как /ˈdʒeɪsən/) — текстовый формат обмена данными, основанный на JavaScript. Как и многие другие текстовые форматы, JSON легко читается людьми. Формат JSON был разработан Дугласом Крокфордом. Несмотря на происхождение от JavaScript (точнее, от подмножества языка стандарта ECMA-262 1999 года), формат считается независимым от языка и может использоваться практически с любым языком программирования. Для многих языков существует готовый код для создания и обработки данных в формате JSON.

**[YAML](https://ru.wikipedia.org/wiki/YAML)** (рекурсивный акроним YAML Ain't Markup Language — «YAML — Не язык разметки») — «дружественный» формат сериализации данных, концептуально близкий к языкам разметки, но ориентированный на удобство ввода-вывода типичных структур данных многих языков программирования.

**[MessagePack](https://en.wikipedia.org/wiki/MessagePack)** is a computer data interchange format. It is a binary form for representing simple data structures like arrays and associative arrays. MessagePack aims to be as compact and simple as possible. The official implementation is available in a variety of languages such as C, C++, C#, D, Erlang, Go, Haskell, Java, JavaScript, Lua, OCaml, Perl, PHP, Python, Ruby, Scala, Smalltalk, and Swift.

**[pickle](https://pythonworld.ru/moduli/modul-pickle.html)** - реализует мощный алгоритм сериализации и десериализации объектов Python. "Pickling" - процесс преобразования объекта Python в поток байтов, а "unpickling" - обратная операция, в результате которой поток байтов преобразуется обратно в Python-объект. Так как поток байтов легко можно записать в файл, модуль pickle широко применяется для сохранения и загрузки сложных объектов в Python.

## Передача данных (сетевые технологии)
**[WebRTC](https://ru.wikipedia.org/wiki/WebRTC)** (англ. real-time communications — коммуникации в реальном времени) — проект с открытым исходным кодом, предназначенный для организации передачи потоковых данных между браузерами или другими поддерживающими его приложениями по технологии точка-точка. Его включение в рекомендации W3C поддерживается Google Chrome (и других на его основе), Mozilla и Opera. WebRTC распространяется по лицензии BSD-3 и исходный код основывается на продукте от Global IP Solution, которая была куплена компанией Google в мае 2010.

**[Twisted](https://ru.wikipedia.org/wiki/Twisted)** — это событийно-ориентированный сетевой фреймворк, написанный на Python и распространяемый под лицензией MIT. Проекты на Twisted могут поддерживать TCP, UDP, SSL/TLS, IP Multicast, Unix domain sockets, большое количество протоколов, включая HTTP, XMPP, NNTP, IMAP, SSH, IRC, FTP и другие. Twisted основан на парадигме событийно-ориентированного программирования, и это значит, что пользователи Twisted пишут небольшие программы обратного вызова, которые вызываются фреймворком.

**[asyncio](https://docs.python.org/dev/library/asyncio.html)** - This module provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives. Here is a more detailed list of the package contents.

**[websockets](https://pypi.python.org/pypi/websockets)** - An implementation of the WebSocket Protocol (RFC 6455). "websockets" is a library for developing WebSocket servers and clients in Python. It implements RFC 6455 with a focus on correctness and simplicity. It passes the Autobahn Testsuite. Built on top of Python’s asynchronous I/O support introduced in PEP 3156, it provides an API based on coroutines, making it easy to write highly concurrent applications.

## Базы данных и обертки для них
**[SQLAlchemy](https://ru.wikipedia.org/wiki/SQLAlchemy)** — это программная библиотека на языке Python для работы с реляционными СУБД с применением технологии ORM. Служит для синхронизации объектов Python и записей реляционной базы данных. SQLAlchemy позволяет описывать структуры баз данных и способы взаимодействия с ними на языке Python без использования SQL. Библиотека была выпущена в феврале 2006 под лицензией открытого ПО MIT. Работает back-end для баз данных: MySQL, PostgreSQL, SQLite, Oracle и других,между которыми можно переключаться изменением конфигурации.

**[Redis](https://ru.wikipedia.org/wiki/Redis)** (англ. remote dictionary server) — сетевое журналируемое хранилище данных типа «ключ — значение» с открытым исходным кодом. Нереляционная высокопроизводительная СУБД.

**[PostgreSQL](https://ru.wikipedia.org/wiki/PostgreSQL)** -  (произносится «Пост-Грес-Кью-Эл») — свободная объектно-реляционная система управления базами данных (СУБД). Существует в реализациях для множества UNIX-подобных платформ, включая AIX, различные BSD-системы, HP-UX, IRIX, Linux, Mac OS X, Solaris/OpenSolaris, Tru64, QNX, а также для Microsoft Windows.

**[SQLite](https://ru.wikipedia.org/wiki/SQLite)** (/ˌɛskjuːɛlˈlaɪt/ или /ˈsiːkwəl.laɪt/) — компактная встраиваемая реляционная база данных. Исходный код библиотеки передан в общественное достояние. В 2005 году проект получил награду Google-O’Reilly Open Source Awards.

**[MongoDB](https://ru.wikipedia.org/wiki/MongoDB)** - (от англ. humongous — огромный) — документоориентированная система управления базами данных (СУБД) с открытым исходным кодом, не требующая описания схемы таблиц. Написана на языке C++.

**[MySQL](https://ru.wikipedia.org/wiki/MySQL)** (МФА: [maɪ ˌɛskjuːˈɛl]) — свободная реляционная система управления базами данных. Продукт распространяется как под GNU General Public License, так и под собственной коммерческой лицензией. Помимо этого, разработчики создают функциональность по заказу лицензионных пользователей. Именно благодаря такому заказу почти в самых ранних версиях появился механизм репликации.

## Серверы
**[nginx](https://ru.wikipedia.org/wiki/Nginx)** (англ. engine x) (по-русски произносится как э́нжин-э́кс или э́нжин-и́кс) — веб-сервер и почтовый прокси-сервер, работающий на Unix-подобных операционных системах (тестировалась сборка и работа на FreeBSD, OpenBSD, Linux, Solaris, Mac OS X, AIX и HP-UX). Начиная с версии 0.7.52 появилась экспериментальная бинарная сборка под Microsoft Windows.

## Система обмена сообщениями
**[RabbitMQ](https://ru.wikipedia.org/wiki/RabbitMQ)** — платформа, реализующая систему обмена сообщениями между компонентами программной системы (Message Oriented Middleware) на основе стандарта AMQP (Advanced Message Queuing Protocol)[3]. RabbitMQ выпускается под Mozilla Public License.

**[ZeroMQ](https://en.wikipedia.org/wiki/ZeroMQ)** - (also spelled ØMQ, 0MQ or ZMQ) is a high-performance asynchronous messaging library, aimed at use in distributed or concurrent applications. It provides a message queue, but unlike message-oriented middleware, a ZeroMQ system can run without a dedicated message broker. The library's API is designed to resemble that of Berkeley sockets. ZeroMQ is developed by a large community of contributors, founded by iMatix, which holds the domain name and trademarks. There are third-party bindings for many popular programming languages.

## Очередь задач 
*(Сказали, пока задвинуть их... туда... подальше)*

**[celery](https://pypi.python.org/pypi/celery)** — «distributed task queue». Это распределенная асинхронная очередь заданий. Task queues are used as a mechanism to distribute work across threads or machines. A task queue’s input is a unit of work, called a task, dedicated worker processes then constantly monitor the queue for new work to perform. Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task a client puts a message on the queue, the broker then delivers the message to a worker. A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

**[RQ](http://python-rq.org)** (Redis Queue) is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis and it is designed to have a low barrier to entry. It can be integrated in your web stack easily.

## Прочее
**[JavaScript]()** обычно используется как встраиваемый язык для программного доступа к объектам приложений. Наиболее широкое применение находит в браузерах как язык сценариев для придания интерактивности веб-страницам. Основные архитектурные черты: динамическая типизация, слабая типизация, автоматическое управление памятью, прототипное программирование, функции как объекты первого класса.
