import cherrypy

class WebApp:
        
    def index(self):
        
        # using a multi-line quote (3 " in a row) to define our HTML variable
        
        html = """
        
        <html>
        <body>
        
        <h1>WELCOME TO OUR STUPENDOUS WEB APP THAT JUST WENT LIVE THIS MORNING.</h1>
        
        </body>
        </html>
        """
        
        return html
    
    index.exposed = True # tells cherrypy "index()" should be made available to run over the web
    
    
# my program: ##########################

# create an object 
my_app = WebApp()

# tell cherrypy to start "serving" this object on "http://localhost:8080"
cherrypy.quickstart(my_app) # our code continues running inside this function in a loop

# our app is now accessible by pointing a browser at http://localhost:8080


    
