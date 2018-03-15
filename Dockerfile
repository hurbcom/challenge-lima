#GOPATH must be configured at /go
FROM golang:latest 

WORKDIR /go/src/challenge-echo
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...
CMD ["challenge-echo", "10x20"]
