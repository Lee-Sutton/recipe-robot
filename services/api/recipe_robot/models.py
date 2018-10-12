"""ORM Layer with model definitions"""
# pylint: disable=R0903

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    ingredients = db.relationship('Ingredient')

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    ingredients=[ingredient.to_dict() for ingredient in
                                 self.ingredients])


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    amount = db.Column(db.Float)
    measurement_units = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    amount=self.amount,
                    measurement_units=self.measurement_units)
