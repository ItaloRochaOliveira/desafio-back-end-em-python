class Appointment_model:
    def __init__(self, id, professional_id, date, creted_at, update_at):
        self.id = id
        self.professional_id = professional_id
        self.date = date
        self.created_at = creted_at
        self.update_at = update_at

    def get_all_itens(self):
        return {
            "id": self.id,
            "professional_id": self.professional_id,
            "date": self.date,
            "created_at": self.created_at,
            "updated_at": self.update_at,
        }
