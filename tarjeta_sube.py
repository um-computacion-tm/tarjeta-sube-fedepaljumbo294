class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

PRECIO_TICKET = 70
PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"
ACTIVADO = "activado"
DESACTIVADO = "desactivado"

DESCUENTOS = {
    PRIMARIO: 0.5,
    SECUNDARIO: 0.4,
    UNIVERSITARIO: 0.3,
    JUBILADO: 0.25,
}

class Sube:
    def _init_(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario in DESCUENTOS:
            descuento = DESCUENTOS[self.grupo_beneficiario]
            return round(PRECIO_TICKET * (1 - descuento), 2)
        else:
            return PRECIO_TICKET

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("El usuario está desactivado.")

        precio_ticket = self.obtener_precio_ticket()
        if self.saldo >= precio_ticket:
            self.saldo -= precio_ticket
        else:
            raise NoHaySaldoException("No hay suficiente saldo para pagar el pasaje.")

    def cambiar_estado(self, estado):
        if estado not in [ACTIVADO, DESACTIVADO]:
            raise EstadoNoExistenteException("El estado especificado no existe.")

        self.estado = estado