from pydantic import BaseSettings
import json
import os 
from enum import Enum
from dotenv import load_dotenv

class Environment(str, Enum): 
    """ analyst agent environment types"""
    
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"
    
def load_env_file




class AnalystConfig(BaseSettings): 
    pass

