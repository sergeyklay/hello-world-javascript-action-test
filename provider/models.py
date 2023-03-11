# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""ORM models for the application and helper functions."""

import decimal
from datetime import datetime
from typing import List

import sqlalchemy as sa
from flask import url_for
from sqlalchemy import orm as so
from sqlalchemy.sql import func

from .app import db


class IdentityMixin:
    """Mixin class to add identity fields to a SQLAlchemy model."""

    id: so.Mapped[int] = so.mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    def __repr__(self):
        """Returns the object representation in string format."""
        return f'<{self.__class__.__name__} id={self.id!r}>'


class TimestampMixin:
    """Mixin class to add timestamp fields to a SQLAlchemy model."""

    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        index=True,
        server_default=func.now(),
    )

    updated_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        index=True,
        onupdate=func.now(),
        server_default=func.now(),
    )


class Product(IdentityMixin, TimestampMixin, db.Model):
    __tablename__ = 'products'

    name: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        unique=True,
        index=True,
        nullable=False,
    )

    description: so.Mapped[str] = so.mapped_column(
        sa.String(512),
        nullable=False,
        default='',
    )

    price: so.Mapped[decimal.Decimal] = so.mapped_column(
        sa.Numeric(precision=8, scale=2, decimal_return_scale=2),
        nullable=False,
        default=0.0,
    )

    discount: so.Mapped[decimal.Decimal] = so.mapped_column(
        sa.Numeric(precision=8, scale=2, decimal_return_scale=2),
        nullable=False,
        default=0.0,
    )

    rating: so.Mapped[decimal.Decimal] = so.mapped_column(
        sa.Numeric(precision=3, scale=2, decimal_return_scale=2),
        index=True,
        nullable=False,
        default=0.0,
    )

    stock: so.Mapped[int] = so.mapped_column(
        nullable=False,
        default=0,
    )

    brand_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey('brands.id'),
        nullable=False
    )

    brand: so.Mapped['Brand'] = so.relationship(
        back_populates='product',
    )

    category_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey('categories.id'),
        nullable=False
    )

    category: so.Mapped['Category'] = so.relationship(
        back_populates='product',
    )

    def get_url(self):
        return url_for('api.ProductsById', product_id=self.id, _external=True)


class Category(IdentityMixin, TimestampMixin, db.Model):
    __tablename__ = 'categories'

    name: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        unique=True,
        index=True,
        nullable=False,
    )

    product: so.Mapped[List['Product']] = so.relationship(
        back_populates='category',
    )


class Brand(IdentityMixin, TimestampMixin, db.Model):
    __tablename__ = 'brands'

    name: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        unique=True,
        index=True,
        nullable=False,
    )

    product: so.Mapped[List['Product']] = so.relationship(
        back_populates='brand',
    )
