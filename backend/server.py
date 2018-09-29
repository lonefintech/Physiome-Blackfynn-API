from service.app import app
import ssl

if __name__ == '__main__':
  context = ssl.Context(SSL.TLSv1_2_METHOD)
  context.use_privatekey_file('/etc/letsencrypt/live/blackfynnpythonlink.ml/privkey.pem')
  context.use_certificate_chain_file('/etc/letsencrypt/live/blackfynnpythonlink.ml/fullchain.pem')
  context.use_certificate_file('/etc/letsencrypt/live/blackfynnpythonlink.ml/cert.pem')
  app.run(host='0.0.0.0', port=80, threaded=True, ssl_context=context)
