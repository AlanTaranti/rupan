import socket


class PortService:
    def get_port_service_name(self, port: int, protocol: str):
        try:
            return socket.getservbyport(port, protocol)
        except:
            return None

    def get_port_service_name_by_range(
        self, start_port: int, end_port: int, protocol: str
    ):
        service_names = []
        for port in range(start_port, end_port + 1):
            service_name = self.get_port_service_name(port, protocol)
            if service_name is not None:
                service_names.append(service_name)
        return service_names
