#!/bin/sh

if [ "$1" = 'test' ]; then
    exec pytest
elif [ "$1" = 'style' ]; then
    exec flake8
fi

exec "$@"