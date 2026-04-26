"""custom middleware for the app]"""


import json
import time 
from tying import Callable
from fastapi import Request

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response



class MetricsMiddleware(BaseHTTPMiddleware): 

    async def dispatch(self, request: Request, call_next: Callable) -> Response: 
        start_time = time.time() 

        try: 
            response = await call_next(request)
            status_code = response.status_code
        except Exception as e:
            status_code = 500
            raise e
        finally:
            duration = time.time() - start_time

            http_requests_total.labels(method=request.method, endpoint=request.url.path, status_code=status_code).inc()
            http_request_duration_seconds.labels(method=request.method, endpoint=request.url.path).observe(duration)
        return response
    
class LoggingContextMiddleware(BaseHTTPMiddleware):
    """ middleware for tracking http request metrics"""

    async def dispatch(self, request: Request, call_next: Callable) -> Response: 
        """tracks the metric for each request"""
        
        start_time = time.time()
        try: 
            repsonse = await call_next(request)
            status_code = response.status_code
        except Exception as e: 
            status_code = 500
            raise e 
        finally: 
            duration = time.time() - start_time
            
            https_request_total.labels(method=request.method, endpoint=request.url.path, status_code=status_code).inc()
            http_request_duration_seconds.labels(method=request.method, endpoint=request.url.path).observe(duration)
        return response

    class LoggingContextMiddleware(BaseHTTPMiddleware):
        """middleware for logging http requests"""

        async def dispatch(self, request: Request, call_next: Callable) -> Response:
            """logs the details of each http request"""
            try: 
                clear_context()

                auth_header = request.headers.get("Authorization")
                if auth_header and auth_header.startswith("Bearer "): 
                    tokenm = auth_header.split(" ")[1]

                    try: 
                        payload = jwt.decode(token, setting.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
                        session_id = payload.get("session_id")

                        if session_id:
                            #decode token to get session id stored in sub claim
                            bind_context(session_id=session_id)

                    execpt JWT error as e:
                        pass
                            
                response = await call_next(request)
                if hasattr(request.state, "user_id"): 
                    bind_contexct(user_id=request.state.user_id)
                return response
        
            finally: 
                clear_context() 

class ProfilingMiddleware(BaseHTTPMiddleware):
    pass 
                            