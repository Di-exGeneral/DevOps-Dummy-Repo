#!/bin/env python3

import os
import sys

app_name = os.getenv('APP_NAME')
app_env = os.getenv('APP_ENV')
app_port = os.getenv('APP_PORT')

if not app_name or not app_env or not app_port:
    print("Error: missing environment variables")
    sys.exit(1)

print(f"App Name: {app_name}")
print(f"Environment: {app_env}")
print(f"Port: {app_port}")
