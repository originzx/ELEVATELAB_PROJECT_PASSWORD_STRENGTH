from analyzer import analyze_password
from generator import generate_wordlist

def main():
    print("🔐 Password Tool")
    choice = input("1. Analyze Password\n2. Generate Wordlist\nChoose (1/2): ")

    if choice == '1':
        pwd = input("Enter your password: ")
        score, feedback = analyze_password(pwd)
        print(f"Strength Score: {score}/100")
        for f in feedback:
            print("  ⚠️ " + f)

    elif choice == '2':
        inputs = input("Enter words (comma-separated): ").split(",")
        count, filepath = generate_wordlist([i.strip() for i in inputs])
        print(f"✅ Generated {count} entries")
        print(f"📄 Saved as: {filepath}")

if __name__ == "__main__":
    main()
