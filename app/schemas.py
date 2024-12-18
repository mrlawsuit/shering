from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class Role(Enum):
    admin = 'администратор'
    client = 'клиент'


class CarStatus(Enum):
    available = 'доступен'
    being_serviced = 'на обслуживании'
    reserved = 'забронирован'


class BookingStatus(Enum):
    active = 'активно'
    finished = 'завершено'
    canceled = 'отменено'


class MaintenanceStatus(Enum):
    planned = 'запланированно'
    in_process = 'в процессе'
    done = 'завершено'


class CreateMaintenance(BaseModel):
    vehicle_id: int
    workshop_id: int
    service_date: datetime
    status: MaintenanceStatus
    current_mileage: int
