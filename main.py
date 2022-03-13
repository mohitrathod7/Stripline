# Manual imports
from website.views import home
from website.views import auth
from website.views import user
from website.views import doctors
from website.views import hospitals
from website.views.app import app


app.register_blueprint(home.h,        url_prefix='/',        method=['GET', 'POST'])
app.register_blueprint(auth.auth,     url_prefix='/auth',    method=['GET', 'POST'])
app.register_blueprint(user.user,     url_prefix='/user',    method=['GET', 'POST'])
app.register_blueprint(doctors.doctors, url_prefix='/doctor',  method=['GET', 'POST'])
app.register_blueprint(hospitals.hospitals, url_prefix='/hospitals',  method=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
