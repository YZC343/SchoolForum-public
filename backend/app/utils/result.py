class Result[T, E]:
    __slots__ = ()

    def is_ok(self) -> bool:
        raise NotImplementedError

    def is_err(self) -> bool:
        raise NotImplementedError

    def unwrap(self) -> T:
        raise NotImplementedError

    def unwrap_or(self, default: T) -> T:
        raise NotImplementedError

    def unwrap_err(self) -> E:
        raise NotImplementedError

    @staticmethod
    def ok(value: T) -> 'Ok[T, E]':
        return Ok(value)

    @staticmethod
    def err(error: E) -> 'Err[T, E]':
        return Err(error)


class Ok[T, E](Result[T, E]):
    __slots__ = ('_value',)

    def __init__(self, value: T) -> None:
        self._value: T = value

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False

    def unwrap(self) -> T:
        return self._value

    def unwrap_or(self, default: T) -> T:
        return self._value

    def unwrap_err(self) -> E:
        raise ValueError('Call unwrap_err on an Ok Result is invalid.')


class Err[T, E](Result[T, E]):
    __slots__ = ('_error',)

    def __init__(self, error: E) -> None:
        self._error: E = error

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True

    def unwrap(self) -> T:
        raise ValueError('Call unwrap on an Err Result is invalid.')

    def unwrap_or(self, default: T) -> T:
        return default

    def unwrap_err(self) -> E:
        return self._error
