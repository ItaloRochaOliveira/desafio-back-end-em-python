class Professional_model:
    def __init__(self, id, name, social_name, created_at, updated_at):
        self.id = id
        self.name = name
        self.social_name = social_name
        self.created_at = created_at
        self.updated_at = updated_at

    def get_all_itens(self):
        return {
            "id": self.id,
            "nome": self.name,
            "nome_social": self.social_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
