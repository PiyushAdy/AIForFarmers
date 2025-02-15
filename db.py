from flask_sqlalchemy import SQLAlchemy
from flask-login import UserMixin


db = SQLAlchemy(app)
# User Table
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented User ID
    username = db.Column(db.String(100), unique=True, nullable=False)  # Unique Username
    password_hash = db.Column(db.String(128), nullable=False)  # Store hashed password
    plants = db.relationship('Plant', backref='user', lazy=True)  # One-to-Many Relationship

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
# Plant Data Table
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented Plant ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign Key
    plant_name = db.Column(db.String(100), nullable=False)  # Plant Name
    height = db.Column(db.Float, nullable=False)  # Plant Height
    soil_type = db.Column(db.String(100), nullable=False)  # Soil Type



