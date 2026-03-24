class Config:
    SECRET_KEY = "supersecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///bank.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False