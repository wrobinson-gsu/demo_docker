# Needs Java and Python
FROM omahoco1/alpine-java-python

# application folder
ENV APP_DIR /app

# app dir
WORKDIR ${APP_DIR}

#COPY Pipfile Pipfile.lock app.py model.pmml requirements.txt ${APP_DIR}/
COPY Pipfile Pipfile.lock app.py model.pmml ${APP_DIR}/
COPY templates ${APP_DIR}/templates/

RUN pip install pipenv==2018.11.26
# Newest pipenv fails in Docker
#RUN pip install --upgrade pip pipenv
RUN pipenv install --deploy --system

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

# exectute start up script
ENTRYPOINT ["/entrypoint.sh"]
CMD ["entrypoint.sh"]
