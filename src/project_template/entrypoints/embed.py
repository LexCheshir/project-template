import structlog
from structlog.stdlib import BoundLogger

from project_template.meta import settings

base_log: BoundLogger = structlog.get_logger()


def main():
    log = base_log.bind(function="main")
    print("What does the fox say?")
    print(f"{settings.app_name} {settings.version}")
    log.info("Done ^^")
