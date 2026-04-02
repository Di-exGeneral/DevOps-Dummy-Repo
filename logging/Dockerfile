FROM alpine:latest
RUN mkdir -p /logs
COPY script.sh .
RUN chmod 755 script.sh
CMD ["sh", "./script.sh"]
