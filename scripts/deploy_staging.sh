#!/bin/bash
source config/staging.env
docker-compose -f docker-compose.yml up --build