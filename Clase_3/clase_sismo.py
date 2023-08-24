class EventoSismico:
    def __init__(self, horaLocal: str, magnitud: float, lugar: str, agencia:str):
        self.horaLocal = horaLocal
        self.magnitud = float(magnitud)
        self.lugar = lugar
        self.agencia = agencia

    def municipio(self):
        return self.lugar.split('-')[0].strip()
    
    def departamento(self) -> str:
        return self.lugar.split('-')[1].split(',')[0].strip()
    
    def pais(self) -> str:
        return self.lugar.split(',')[1].strip()

    def agencia_SGC(self) -> bool:
        return self.agencia == 'SGC'