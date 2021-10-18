from pydantic import BaseModel


class PaymentSchema(BaseModel):
    category: int
    client_id: int
    doctor: str
    date: str
    amount: str
    vat: str
    x_ray: str
    flat: str
    discount: str
    flat_discount: str
    gross_total: str
    hospital_amount: str
    doctor_amount: str
    category_amount: str
    category_name: str
    amount_received: str
    status: bool
    pharmacy_id: int
