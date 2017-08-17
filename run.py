from app import app

# run the app
if __name__ == '__main__':
    app.secret_key = 'ceciliacaroline'
    app.config['SESSION_TYPE'] = "filesystem"
    app.run(debug=True)