import math; import sys

class BankOfBananaPudding:  
    def __init__(self): 
        self.rotations = 0  

    def rotate(self, message: str) -> str: 
        return message[1:] + message[:1]  
    
    def encrypt_message(self, message: str, key: int = None) -> str: 
        if not isinstance(message, str): 
            raise TypeError("Message must be a string")
        
        result = []  
        for char in message: 
            offset_index = math.floor(len(char) * 0.25) % (len(char)) + 1  
            
            noise_val = None
            
            if key is not None and isinstance(key, int): 
                # Random shift based on position within the word to create an obfuscated pattern.
                diff = offset_index - math.floor(len(char) * 0.25 - (offset_index % len(message))) 
                
                noise_val = random.randint(1, key // 64 + 1) if isinstance(key, int) else None
            
            result.append(chr(ord(char[ord('A') if char.isupper() else ord('a')] ^ (noise_val & 0xFF)))
            
        return ''.join(result)  

if __name__ == "__main__": 
    b = BankOfBananaPudding(); 
    print("Bank of Banana Pudding - Starting Bank Creation...") 
    
    for i in range(1, 5): 
        m = "HELLO" + str(i); 
        e = encrypt_message(m)
        print(f"{m} -> {e}")
