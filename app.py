# This file now acts as a bridge to the clean architecture entry point
from run import app

if __name__ == "__main__":
    import os
    ssl_ctx = None
    cert = os.path.join(os.path.dirname(__file__), 'cert.pem')
    key  = os.path.join(os.path.dirname(__file__), 'key.pem')
    if os.path.exists(cert) and os.path.exists(key):
        ssl_ctx = (cert, key)
    app.run(debug=True, ssl_context=ssl_ctx, port=5000)