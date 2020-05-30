pipeline {
    agent any
    environment {
        GOOGLE_PROJECT_ID = 'callback-demons';
        GOOGLE_SERVICE_ACCOUNT_KEY = credentials('google_cloud');
    }
    tools {
        nodejs 'NodeJS 14.3.0'
    }
    stages {
        stage('Deploy') {
            steps {
                sh """
					#!/bin/bash
					ssh gerardo_marquez_carmona@api.callback-news.com -p 2222 'cd ~/callback-news-api && git reset --hard && git pull && sudo pip3 install --ignore-installed -r app/requirements/base.txt -r app/requirements/prod.txt && sudo python3 app/manage.py migrate && sudo python3 app/manage.py collectstatic --noinput && sudo systemctl daemon-reload && sudo systemctl restart gunicorn
                    '
				"""
            }
        } 
    }
}