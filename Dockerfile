FROM node
ADD . /app
WORKDIR /app
RUN npm install && npm link