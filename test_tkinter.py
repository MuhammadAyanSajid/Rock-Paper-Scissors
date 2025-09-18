import tkinter as tk
import os

# Set environment variables for Tcl/Tk
os.environ['TCL_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

print("Testing Tkinter...")
try:
    root = tk.Tk()
    root.title("Test Window")
    label = tk.Label(root, text="Tkinter is working!")
    label.pack(pady=20)
    print("Tkinter window created successfully!")
    
    # Close after 3 seconds for testing
    root.after(3000, root.quit)
    root.mainloop()
    print("Tkinter test completed!")
except Exception as e:
    print(f"Error: {e}")