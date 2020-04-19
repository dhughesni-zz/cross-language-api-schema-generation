# cross-language-api-schema-generation

## Description
- This example uses [swagger-codegen](https://github.com/swagger-api/swagger-codegen) to generate the same schemas across multiple languages.
- The example uses: Swagger Codegen 2.X which supports Swagger/OpenAPI version 2.
- The build process uses the maven plugin: https://github.com/swagger-api/swagger-codegen/blob/master/modules/swagger-codegen-maven-plugin/README.md
- All Avaliable Languages: https://github.com/swagger-api/swagger-codegen/tree/master/modules/swagger-codegen/src/main/java/io/swagger/codegen/languages

# How to generate schemas
- clone the repo
- build the code: ```$ mvn clean compile```
- generated models exist in: ```target/```

## How to test
- Test Python
```
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install six pytest
$ pytest check_schemas.py
```