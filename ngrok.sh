#!/bin/bash

# Run server with ngrol

port=8000
subdomain=""

# Ejecutar ngrok en segundo plano

ngrok http port
