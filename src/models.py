from sqlalchemy import Column, Float, Integer, String, Enum, TIMESTAMP, ForeignKey, Identity, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Producers(Base):
    __tablename__ = 'Producers'

    id_producer = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    location = Column(String(255), nullable=False)
    registration_date = Column(TIMESTAMP, server_default=func.now())

    crops = relationship("Crops", back_populates="producer")


class Crops(Base):
    __tablename__ = "Crops"

    id_crop = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)
    id_producer = Column(Integer, ForeignKey('Producers.id_producer'), nullable=False)

    producer = relationship("Producers", back_populates="crops")
    sensors = relationship("Sensors", back_populates="crop")
    application_adjustments = relationship("ApplicationAdjustments", back_populates="crop")


class Sensors(Base):
    __tablename__ = 'Sensors'

    id_sensor = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    sensor_type = Column(Enum('humidity', 'pH', 'nutrients'), nullable=False)
    id_crop = Column(Integer, ForeignKey('Crops.id_crop'), nullable=False)

    crop = relationship("Crops", back_populates="sensors")
    readings = relationship("SensorReadings", back_populates="sensor")


class SensorReadings(Base):
    __tablename__ = 'SensorReadings'

    id_reading = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    id_sensor = Column(Integer, ForeignKey('Sensors.id_sensor'), nullable=False)
    reading_value = Column(Float, nullable=False)
    reading_date = Column(TIMESTAMP, server_default=func.now())

    sensor = relationship("Sensors", back_populates="readings")


class ApplicationAdjustments(Base):
    __tablename__ = 'ApplicationAdjustments'

    id_adjustment = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    water_quantity = Column(Float, nullable=False)
    nutrient_quantity = Column(Float, nullable=False)
    adjustment_date = Column(TIMESTAMP, server_default=func.now())
    id_crop = Column(Integer, ForeignKey('Crops.id_crop'), nullable=False)

    crop = relationship("Crops", back_populates="application_adjustments")


class IrrigationHistory(Base):
    __tablename__ = 'IrrigationHistory'

    id = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    timestamp = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    status = Column(Enum('Ligado', 'Desligado'), nullable=False)
    humidity_value = Column(Float, nullable=False)


class NutrientHistory(Base):
    __tablename__ = 'NutrientHistory'
    id = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    timestamp = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    ph = Column(Float, nullable=False)
    irrigation = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)