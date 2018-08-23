from service.app import app

# For local server, access http://'your ip':80/
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=80)
