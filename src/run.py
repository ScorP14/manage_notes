if __name__ == "__main__":
    from src.app import get_app
    from uvicorn import run

    run(get_app())
