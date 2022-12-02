from prefect import task, flow, get_run_logger


@task
def hello(name: str = "Will") -> None:
    logger = get_run_logger()
    logger.info(f"Hello {name}!")


@flow
def hello_flow(name: str = "Will") -> None:
    hello(name)


if __name__ == '__main__':
    hello_flow()