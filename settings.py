# !usr/bin/env/python3 
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : Config process
# ************************************************************************
# Imports
# ************************************************************************
import os
from os.path import join, dirname
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv(verbose=True)

        dotenv_path = join(dirname(__file__), ".env")
        load_dotenv(dotenv_path)

        self.config = os.environ

    @property
    def jenkins_apikey(self):
        return self.config.get('API_KEY')

    @property
    def jenkins_url(self):
        return self.config.get('JENKINS_URL')

    @property
    def user_name(self):
        return self.config.get('USER_NAME')

    @property
    def base_job_name(self):
        return self.config.get('BASE_JOB_NAME')
