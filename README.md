### Hexlet tests and linter status:
[![Actions Status](https://github.com/Mirdalan-p/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Mirdalan-p/python-project-52/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c135796ad0346ff0037b/test_coverage)](https://codeclimate.com/github/Mirdalan-p/python-project-52/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/c135796ad0346ff0037b/maintainability)](https://codeclimate.com/github/Mirdalan-p/python-project-52/maintainability)

Менеджер задач
Учебный проект, позволяющий создавать задачи, присваивать им метки и назначать для них исполнителей.

Демонстрация работы проекта:
<a href="https://web-production-b1bc.up.railway.app/">Менеджер задач</a>

Установка:

`git clone git@github.com:Mirdalan-p/python-project-52.git`

Перейти в директорию проекта, установить зависимости при помощи Poetry

`poetry install`

  Для работы приложения необходимо создать .env файл, на основе примера, предоставленного в файле .env_example:
необходим секретный ключ и url для подключения к базе данных (PostgreSQL или SQLite)

  Подготовить базу данных:
 
`make migrations`

  Запустить приложение:

`make start`
