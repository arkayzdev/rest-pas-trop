def to_code_error(code):
    match (code):
        case 203:
            return "Non-Authoritative"
        case 204:
            return "No content"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 409:
            return "Conflict"
        case 500:
            return "Internal Server Error"
        case 501:
            return "Not Implemented"
        case 502:
            return "Bad Gateway"
        case 503:
            return "Service Unavailable"
        case 504:
            return "Gateway Timeout"
        case 599:
            return "Network Timeout"
        case _:
            return "No description for this error code"
