## ⚠️ Disclaimer  
This script is **not intended for real-world security use** and was created as part of the **Lighthouse Labs Cybersecurity Bootcamp** for educational purposes. Base64 is **not encryption**—if you use it to "secure" sensitive data, you’re doing it wrong.

# 🔐 AllYourBase64.py 🔐  
**Are belong to us!**  

This script lets you encode and decode text using **Base64**, the world's most misunderstood encoding method. If you've ever thought, *"I should encrypt this with Base64!"*—stop. Just stop.  

## 🚀 Features  
✅ Encodes any text into Base64 (because why not?)  
✅ Decodes Base64 back into readable text  
✅ Does **absolutely nothing** to protect your secrets  
✅ Makes people think you’re a 1337 hacker when you send them gibberish  

## 🛠️ Usage  

### Encode Text  
Convert readable text into Base64 gibberish:  
```bash
python all_your_base64.py encode "Top Secret Message"
```

### 🔎 Output:
```nginx
VG9wIFNlY3JldCBNZXNzYWdl
```

### Decode Text
Turn Base64 back into normal text (for those who panicked when they saw it):
```bash
python all_your_base64.py decode "VG9wIFNlY3JldCBNZXNzYWdl"
```

### 🔎 Output:
```mathematica
Top Secret Message
```

## ⚠️ WARNING
🚨 Base64 is NOT encryption! 🚨

If you use this script to “secure” your passwords, may the cybersecurity gods have mercy on your soul.
This is just fancy text-mangling. Any 12-year-old with Google can decode it.
Use real encryption like AES or RSA if you actually care about security.
## 📝 License
Use this script responsibly. If you get caught encoding your credentials in Base64, we take zero responsibility. 😆

P.S. If you see Base64 in a login token, ask yourself: What are they trying to hide? 😏
