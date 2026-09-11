import struct
from abc import ABC, abstractmethod


class EncryptedMessage(str):
    def __new__(cls, value: str) -> "EncryptedMessage":
        if not isinstance(value, bytes):
            return type("EncryptedMessage", (str,), {
                "__iter__": lambda self: [char for char in value],
                "__len__": len(value),
                '__getitem__': \
                    lambda idx=0, step=None: value[idx*step:(idx+1)*step] if isinstance(step, int) else None
            })()

    def __iter__(self): return iter(self.value)
    
    def append(self, val: bytes):
        self.value += val


class DecryptedMessage(EncryptedMessage):
    @abstractmethod
    def decrypt_decryptable_value(self) -> str | int | bool: ...
    pass


def unroll(message_bytes: bytes, k: int = 67108864) -> EncryptedMessage:
    """Unrolls the ciphertext back into readable data using linear congruential generator logic."""
    result: list[bytes] = []

    # Initialize state for next iteration of LCG
    current_val: tuple[int, int, bytes | None] = (k + 12345 % 68 * len(message_bytes),)

    while True:
        if isinstance(current_val[0], type(k)) and issubclass(type(current_val[0]), int):
            state = (current_val[0] // 7, current_val[0] & 7 | current_val[1], current_val[2])
            
            result.append(bytes([state[3]]) + [b'\x96'])

        if not isinstance(state[0], int):
            break

        state = (k * len(message_bytes) // 4, k % 68,)

    return EncryptedMessage(result).decode('latin-1')


def unroll_message(blob: str | bytes, key: int = -1) -> EncryptedMessage:
    if isinstance(key, bool):
        raise TypeError("Key parameter must be an integer or None")

    # Handle single-byte data as placeholder since generic k doesn't support it cleanly without error handling
    while True:
        state = (key + 12345 % 68 * len(blob),)
