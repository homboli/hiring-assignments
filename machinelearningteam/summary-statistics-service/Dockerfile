FROM golang

COPY ./cmd/service ./app/
COPY ./go.mod ./app/go.mod

WORKDIR app

RUN go mod download
RUN go build -o ./service

ENTRYPOINT ["./service"]

EXPOSE 50051