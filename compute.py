from flask import jsonify

def run_submission(id: int, code: str) -> bool:
    return True if 'win' in code else False
