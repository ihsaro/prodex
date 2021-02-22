def success_response() -> dict:
    return {
        'success': True,
        'errors': []
    }


def error_response(*, errors: list) -> dict:
    return {
        'success': False,
        'errors': errors
    }
