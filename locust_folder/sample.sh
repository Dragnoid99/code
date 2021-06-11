#!/bin/bash
locust -f locustfile.py --host http://0.0.0.0:8000/polls/ --headless -u 20 -r 20
