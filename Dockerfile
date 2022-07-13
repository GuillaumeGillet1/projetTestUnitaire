FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install python3 -y

RUN apt-get install pandas -y

RUN apt-get install sklearn -y

RUN apt-get install joblib -y

WORKDIR /home

COPY . .

CMD ["python3", "build_model.py", "pyhon3", "test_build_model.py", "javascript","cypress/e2e/testProjet.cy.js"]