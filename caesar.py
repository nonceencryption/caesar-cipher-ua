# ⚔️ Caesar Cipher Tool ⚔️

# Повний український алфавіт (33 літери)
ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
ALPHABET_LEN = len(ALPHABET)

def shift_text(text, shift):
    """Функція для зсуву тексту на задану кількість позицій"""
    result = ""
    for char in text:
        is_upper = char.isupper()
        char_lower = char.lower()
        
        # Якщо символ є в нашому алфавіті — зсуваємо його
        if char_lower in ALPHABET:
            current_index = ALPHABET.find(char_lower)
            # Модуль (%) гарантує, що ми не вийдемо за межі алфавіту
            new_index = (current_index + shift) % ALPHABET_LEN
            new_char = ALPHABET[new_index]
            
            # Повертаємо регістр
            result += new_char.upper() if is_upper else new_char
        else:
            # Пробіли, цифри та пунктуацію залишаємо без змін
            result += char 
            
    return result

def main():
    print("=" * 40)
    print("🛡️  Шифр Цезаря  🛡️")
    print("=" * 40)
    print("1. Зашифрувати повідомлення")
    print("2. Зламати шифр (Brute Force)")
    print("-" * 40)
    
    mode = input("Обери режим (1 або 2): ").strip()
    
    if mode == '1':
        text = input("\n📝 Введи текст: ")
        try:
            shift = int(input("🔑 Введи крок зсуву (число): "))
            encrypted = shift_text(text, shift)
            print(f"\n🔒 Зашифрований текст:\n{encrypted}")
        except ValueError:
            print("\n❌ Помилка: Зсув має бути цілим числом!")
            
    elif mode == '2':
        text = input("\n📝 Введи зашифрований текст: ")
        print("\n🕵️‍♂️ Починаємо перебір усіх 32 варіантів...\n")
        
        # Перебираємо всі можливі варіанти зсуву (від 1 до 32)
        for i in range(1, ALPHABET_LEN):
            # Для розшифрування просто рухаємось у зворотний бік (віднімаємо)
            decrypted = shift_text(text, -i)
            print(f"Зсув {-i:3} : {decrypted}")
            
        print("\n✅ Готово! Шукай очима рядок, який має сенс.")
        
    else:
        print("\n❌ Невідомий режим. Перезапусти скрипт і введи 1 або 2.")

# Точка входу в програму
if __name__ == "__main__":
    main()