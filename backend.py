# backend.py
from flask import Flask, request, jsonify
from celery import Celery
import redis
import json
import time

app = Flask(__name__)

# Configure Redis and Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery('backend', broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Import the task definition to register it
from celery_tasks.tasks import process_preorder

@app.route('/preorder', methods=['POST'])
def preorder():
    data = request.json
    task = process_preorder.apply_async(args=[data['product_id'], data['name'], data['email']])
    return jsonify({'task_id': task.id}), 200

@app.route('/task_status/<task_id>', methods=['GET'])
def task_status(task_id):
    task_result = process_preorder.AsyncResult(task_id)
    if task_result.state == 'PENDING':
        response = {'status': 'Pending...'}
    elif task_result.state != 'FAILURE':
        response = {'status': task_result.info.get('status', 'Unknown')}
    else:
        response = {'status': 'Failure', 'message': str(task_result.info)}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
