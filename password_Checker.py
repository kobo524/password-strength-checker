import re
import hashlib

def check_password_strength(password):
   
    length=len(password) >= 8
    upper=re.search(r"[A-Z]",password)
    lower=re.search(r"[a-z]",password)
    digit=re.search(r"\d",password)
    special=re.search(r"[@$!%*?&]",password)

    feedback=[]
    if not length:
        feedback.append("at least 8 characters")
    if not upper:
        feedback.append("an uppercase letter")
    if not lower:
        feedback.append("a lowercase letter")
    if not digit:
        feedback.append("a number")
    if not special:
        feedback.append("a special character (@$!%*?&)")

    if feedback:
        result=f"Weak password ❌\nYou should add: {', '.join(feedback)}"
    else:
        result ="Reliable password ✅"

    return result

def hash_password(password):
    
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    print("Welcome! Let's check how strong your password is.\n")
    password = input("Enter your password: ")

    print("\n" + check_password_strength(password))

    show_hash = input("\nDo you want to see a secure hashed version of your password? (y/n): ").strip().lower()
    if show_hash == 'y':
        print(f"\nHere’s the SHA-256 hash of your password:\n{hash_password(password)}")

    print("\nThank you for using the Password Strength Checker! 🔐")
