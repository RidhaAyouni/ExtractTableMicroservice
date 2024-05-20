from app import db

class Margin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MarginAccountclientC = db.Column(db.Float)
    MarginAccountclientD = db.Column(db.Float)
    MarginAccountmaisonC = db.Column(db.Float)
    MarginAccountmaisonD = db.Column(db.Float)
    CollateralAccountclientC = db.Column(db.Float)
    CollateralAccountclientD = db.Column(db.Float)
    CollateralAccountmaisonC = db.Column(db.Float)
    CollateralAccountmaisonD = db.Column(db.Float)
    CommissionC = db.Column(db.Float)
    CommissionD = db.Column(db.Float)
    SettlementAccountclientC = db.Column(db.Float)
    SettlementAccountclientD = db.Column(db.Float)
    SettlementAccountmaisonC = db.Column(db.Float)
    SettlementAccountmaisonD = db.Column(db.Float)

    def __repr__(self):
        return f"<Margin(id={self.id})>"