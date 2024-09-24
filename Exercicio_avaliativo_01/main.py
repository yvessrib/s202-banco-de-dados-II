from motorista_dao import MotoristaDAO
from motorista_cli import MotoristaCLI

motorista_dao = MotoristaDAO()
motorista_cli = MotoristaCLI(motorista_dao)
motorista_cli.run()
