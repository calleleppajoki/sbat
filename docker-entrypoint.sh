#!/bin/sh

if [ "$1" = 'test' ]; then
    exec python pytest
elif [ "$1" = 'style' ]; then
    exec flake8
elif [ "$1" = 'coverage' ]; then
    exec py.test --cov=app test/
fi

exec "$@"