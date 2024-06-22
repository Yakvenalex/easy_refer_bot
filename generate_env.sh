#!/bin/bash

# Генерация .env файла
cat << EOF > .env
TOKEN=${TOKEN}
ADMINS=${ADMINS}
PG_LINK=${PG_LINK}
PG_LINK_0=${PG_LINK_0}
ROOT_PASS=${ROOT_PASS}
EOF