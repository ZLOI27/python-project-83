# Page Analyzer

## Hexlet tests and linter status:
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ZLOI27_python-project-83&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ZLOI27_python-project-83)
[![Actions Status](https://github.com/ZLOI27/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ZLOI27/python-project-83/actions)
[![Python application](https://github.com/ZLOI27/python-project-83/actions/workflows/python-app.yml/badge.svg)](https://github.com/ZLOI27/python-project-83/actions/workflows/python-app.yml)
[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-dark.svg)](https://sonarcloud.io/summary/new_code?id=ZLOI27_python-project-83)

## Description
Page Analyzer is a tool that allows users to send web addresses and save them in a database. The application checks the availability of URLs and extracts SEO metadata such as HTTP status codes, HTML headers, H1 tags, and meta descriptions.

## Link:
https://python-project-83-dep2.onrender.com

## Installation

### Clone the repository:
```bash
git clone https://github.com/ZLOI27/python-project-83.git
cd python-project-83
```

### Configure Environment Variables:
Rename a .env.example to .env file in the root directory and change variables.

### Install dependencies and initialize the Database Schema:
```bash
make build
```
### Start application:
```bash
make start
```
