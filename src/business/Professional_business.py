from ..models.Professional_model import Professional_model
from ..database.professional_database import get_professional_by_id, table_professional
from src.service.Gerator_id import Gerator_id
from datetime import datetime


class Professional_business:
    def create_professional(content):
        if type(content["name"]) is not str:
            raise ValueError("Name have to be String")
        if content["name"] == "":
            raise ValueError("Name have to be minimun 1 string")

        if type(content["social_name"]) is not str:
            raise ValueError("Name have to be String")

        id = Gerator_id.gerate_uuid4()
        created_at = datetime.now()

        newProfessional = Professional_model(
            str(id), content["name"], content["social_name"], created_at, ""
        )

        table_professional.insert(newProfessional.get_all_itens())

        return newProfessional.get_all_itens()

    def update_professional(id, content):
        if type(content["name"]) is not str:
            raise ValueError("Name have to be String")

        if type(content["social_name"]) is not str:
            raise ValueError("Name have to be String")

        updated_at = datetime.now()

        professional = get_professional_by_id(id)

        if professional == None:
            raise FileNotFoundError("Professional don`t exist for update")

        name = professional["nome"] if content["name"] == "" else content["name"]

        social_name = (
            professional["nome_social"]
            if content["social_name"] == ""
            else content["social_name"]
        )

        content = Professional_model(
            professional["id"],
            name,
            social_name,
            professional["created_at"],
            updated_at,
        )

        table_professional.update(content.get_all_itens(), ["id"])

        professional_updated = get_professional_by_id(id)

        return professional_updated

    def delete_professional(id):
        professional = get_professional_by_id(id)

        if professional == None:
            raise FileNotFoundError(
                "Professional don`t exist for exclusion or already deleted."
            )

        table_professional.delete(id=id)

        return "Professional deleted successfully"
