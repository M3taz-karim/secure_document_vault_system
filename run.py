from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    ssl_ctx = None
    cert = os.path.join(os.path.dirname(__file__), 'cert.pem')
    key  = os.path.join(os.path.dirname(__file__), 'key.pem')
    
    if os.path.exists(cert) and os.path.exists(key):
        ssl_ctx = (cert, key)
        print("[HTTPS] SSL enabled - using cert.pem and key.pem")
    else:
        print("[HTTP] Running without SSL - run generate_certs.py to enable HTTPS")
        
    app.run(debug=True, ssl_context=ssl_ctx, port=5000)
