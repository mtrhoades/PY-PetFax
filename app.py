# # config                    
# from flask import Flask
# app = Flask(__name__)

# # index route
# @app.route('/')
# def index(): 
#     return 'Hello, this is PetFax!'

# # pets index route
# @app.route('/pets')
# def pets(): 
#     return 'These are our pets available for adoption!'

# # allows to open from terminal - python3 "name of file"
# if __name__ == '__main__':
#     app.run()


from petfax import create_app
app = create_app()


