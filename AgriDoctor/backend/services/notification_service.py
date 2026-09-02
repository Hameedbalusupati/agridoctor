from ..database.db import db
from ..models.notification import Notification


def create_notification(farmer, title, message, type_name="info"):
    notif = Notification(farmer_id=farmer.id, title=title, message=message, type=type_name)
    db.session.add(notif)
    db.session.commit()
    return notif
