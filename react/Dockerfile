FROM node:16
EXPOSE 3000
WORKDIR /usr/src/app

ENV REACT_APP_BACKEND_SERVER=localhost:5000

COPY ["./app/package.json", "./app/yarn.lock", "./"]

RUN yarn install

COPY ./app/ .

ENTRYPOINT [ "yarn", "start"]