# **Slot Machine Game (Python)** 🎰  

This is a simple **console-based slot machine game** written in Python. The player deposits money, places bets on up to three lines, and spins the slot machine. The game determines winnings based on matching symbols.

---

## **How to Play**  
1. **Deposit money** to start the game.  
2. **Choose the number of lines** (1-3) to bet on.  
3. **Enter your bet amount per line** (must be within allowed limits).  
4. **Spin the slot machine** and check for winnings.  
5. **Repeat or exit** the game when you're done.  

---

## **Game Rules**  
- The slot machine consists of a **3x3 grid** (3 rows, 3 columns).  
- A **winning line** occurs when all symbols in a row match.  
- The payout is based on the **symbol’s value and bet amount**.  
- The player’s balance updates after each spin (winnings minus total bet).  

---

## **Symbol Values & Probabilities**  
| Symbol | Count (in the slot pool) | Value (Multiplier) |  
|--------|-------------------------|-------------------|  
| A      | 2                       | 5× Bet           |  
| B      | 4                       | 4× Bet           |  
| C      | 6                       | 3× Bet           |  
| D      | 8                       | 2× Bet           |  

---

## **Installation & Running the Game**  
### **Requirements**  
- Python 3.x  

### **Run the Game**  
1. **Download the script** or copy `slot_machine.py`.  
2. Open a terminal or command prompt.  
3. Navigate to the script's directory.  
4. Run the game with:  
   ```bash
   python slot_machine.py
   ```

---

## **Example Gameplay**  
```
What would you like to deposit? $100  
Enter the number of lines to bet on (1-3)? 2  
What would you like to bet on each line? $10  
You are betting $10 on 2 lines. Total bet is equal to: $20  

A | B | C  
D | C | A  
B | A | D  

You won $0.  
Current balance is $80.  
Press enter to play (q to quit).  
```

---

## **Future Improvements**
- Add **bonus rounds** or multipliers.  
- Improve **graphics/UI** for better experience.  
- Implement **different symbol combinations** for more variety.  

---

## **License**  
This project is open-source and available for personal and educational use.  

Happy spinning! 🎰✨  
