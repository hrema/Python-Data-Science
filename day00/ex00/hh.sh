#!/bin/sh

proffesion=$1
proffesion="${proffesion// /+}"
curl "https://api.hh.ru/vacancies?text=$proffesion" | jq > hh.json
