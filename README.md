[![Build Status](https://travis-ci.org/nurlantulemisov/clothes-parcers.svg?branch=master)](https://travis-ci.org/nurlantulemisov/clothes-parcers)

# Clothes Parcer

Набор парсеров магазинов

Задачи падают в очередь и демон запускает скрипты  `main.py` парсеров

После сбора отдает обратно в очередь на другой демон

## Запуск скрипта

Dockerfile - еще не готов

```bash
cp env.dist .env
echo "DRIVER_PATH=путь до драйвера" > .env
echo "CLOUDAMQP_URL=rabbit-url" > .env
```

### Rrequirements

- python 3.7
- pip3
- selenium

```bash
pip3 install -r requirements.txt
```

## Pipeline steps

- [code-style](https://www.python.org/dev/peps/pep-0008/)

- [static-analyze](https://www.pylint.org/)
