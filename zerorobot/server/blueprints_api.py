# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from flask import Blueprint
from . import handlers


blueprints_api = Blueprint('blueprints_api', __name__)


@blueprints_api.route('/blueprints', methods=['POST'])
def ExecuteBlueprint():
    """
    Execute a blueprint on the ZeroRobot
    It is handler for POST /blueprints
    """
    return handlers.ExecuteBlueprintHandler()
