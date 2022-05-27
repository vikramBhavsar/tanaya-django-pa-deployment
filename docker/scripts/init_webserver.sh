#!/bin/bash

cd /tanayaPortfolio/clientApp
echo "Installing node packages"
npm install
echo "building the application"
npm run build-watch

chmod +x /tanayaPortfolio
chmod +x /tanayaPortfolio/staticfiles
cp /tanayaPortfolio/clientApp/dist/clientApp/* /usr/share/nginx/html
cp /tanayaPortfolio/clientApp/nginx.conf /etc/nginx/nginx.conf

nginx -s reload
nginx -g 'daemon off;';
