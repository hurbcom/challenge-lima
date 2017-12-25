FROM node:boron

RUN mkdir -p /echo
WORKDIR /echo

COPY . /echo
RUN npm install
CMD npm link
