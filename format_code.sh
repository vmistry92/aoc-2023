#!/bin/bash

APP_ROOT=$(dirname $(readlink -f $0))

pipenv run black --line-length=120 ${APP_ROOT}/aoc23 ${APP_ROOT}/tests
pipenv run isort ${APP_ROOT}/aoc23 ${APP_ROOT}/tests