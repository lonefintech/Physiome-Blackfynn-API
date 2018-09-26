from service.app import app

# For local server, access http://'your ip':80/
if __name__ == '__main__':
  app.run(ssl_context=('/etc/letsencrypt/live/blackfynnpythonlink.ml/fullchain.pem', 
                       '/etc/letsencrypt/live/blackfynnpythonlink.ml/privkey.pem),
                       host='0.0.0.0', port=80)
