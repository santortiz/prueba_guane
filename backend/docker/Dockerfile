# FROM node:18

# WORKDIR .

# COPY ["../package*.json","."]

# RUN npm install

# COPY [".", "."]


FROM node:18.8.0-alpine3.16

RUN apk add linux-headers
RUN apk add build-base gcc musl-dev
RUN apk add --no-cache --upgrade bash
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY . .
RUN npm install
