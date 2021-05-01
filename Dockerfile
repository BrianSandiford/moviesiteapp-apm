FROM arm32v6/alpine:3.5

RUN apk add --no-cache curl ca-certificates
RUN apk add --no-cache python3 py3-pip

CMD ["curl", "https://docker.com"]