#!/bin/bash

psql -U $POSTGRES_ADMIN_USER << EOF
  CREATE USER $DATABASE_USER WITH PASSWORD '$DATABASE_PASSWORD';
  CREATE DATABASE $DATABASE_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $DATABASE_NAME TO $DATABASE_USER;
EOF

