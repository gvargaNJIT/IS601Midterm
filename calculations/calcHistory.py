#Calculator History

class CalcHistory:
    history = []

    @classmethod
    def add_calculation(cls, string: str):
        cls.history.append(str(string))

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls):
        if cls.history:
            return cls.history[-1]
        return None