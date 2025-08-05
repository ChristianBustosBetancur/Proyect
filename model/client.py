class Client:
    def __init__(self,name,id,phone):
        self.Name = name
        self.Id = id
        self.Phone = phone

    def __str__(self):
        return f"{self.Name} (ID: {self.Id}, Phone: {self.Phone})"

    def ToDict(self):
        return {
            "Name": self.Name,
            "Id": self.Id,
            "Phone": self.Phone
        }

    @staticmethod
    def FromDict(data):
        return Client(data["Name"], data["Id"], data["Phone"])