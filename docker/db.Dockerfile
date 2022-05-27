FROM postgres:14-alpine
COPY scripts/init_db.sh /docker-entrypoint-initdb.d/