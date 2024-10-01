"""
Este módulo gestiona las citas para una barbería.
Incluye funcionalidades para agendar citas y mostrar servicios disponibles.
"""

class Barber:
    """Clase que representa un barbero en la barbería."""
    def __init__(self, name):
        """Inicializa un nuevo barbero con su nombre."""
        self.name = name

class Appointment:
    """Clase que representa una cita agendada."""
    def __init__(self,client_name,barber,service,appointment_time):
        """Inicializa una nueva cita con el nombre del cliente, barbero, servicio y hora."""
        self.client_name = client_name
        self.barber = barber
        self.service = service
        self.appointment_time = appointment_time

class BarberShop:
    """Clase que representa la barbería y gestiona las citas."""
    def __init__(self):
        """Inicializa la barbería con una lista de barberos y citas vacías."""
        self.barbers = [
            Barber("Fernando"),
            Barber("Brian"),
            Barber("Ale")
        ]
        self.appointments = []

    def show_services(self):
        """Muestra los servicios disponibles en la barbería."""
        services = ["Corte de cabello", "Corte de barba", "Afeitado", "Cejas"]
        print("Servicios disponibles:")
        for service in services:
            print(f"- {service}")

    def schedule_appointment(self, client_name, barber_name, service, appointment_time):
        """Agenda una cita para el cliente con un barbero específico."""
        barber = next((b for b in self.barbers if b.name == barber_name), None)
        if barber:
            # Crear la cita y agregarla a la lista de citas
            appointment = Appointment(client_name, barber, service, appointment_time)
            self.appointments.append(appointment)
            print(f"Cita agendada: {client_name} con {barber.name} para "
                  f"{service} a las {appointment_time}.")
        else:
            print("Barbero no encontrado.")

    def display_appointments(self):
        """Muestra todas las citas agendadas."""
        if not self.appointments:
            print("No hay citas agendadas.")
            return
        print("Citas agendadas:")
        for appointment in self.appointments:
            print(f"{appointment.client_name} con {appointment.barber.name} para "
                  f"{appointment.service} a las {appointment.appointment_time}.")

def main():
    """Función principal que ejecuta la barbería."""
    shop = BarberShop()  # Aquí se define 'shop'
    print("Wolves Barbería")
    shop.show_services()

    while True:
        client_name = input("Ingresa tu nombre y apellido: ")
        barber_name = input("Ingresa el nombre del barbero (Fernando, Brian, Ale): ")
        service = input("Ingresa el servicio deseado: ")
        appointment_time = input("Ingresa la hora de la cita (formato HH:MM): ")

        shop.schedule_appointment(client_name, barber_name, service, appointment_time)

        another = input("¿Quieres agendar otra cita? (s/n): ")
        if another.lower() != 's':
            break

    # Llamada al método display_appointments
    shop.display_appointments()

if __name__ == "__main__":
    main()  # Asegúrate de que esta línea esté al final
