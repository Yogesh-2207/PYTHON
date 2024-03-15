import tkinter as tk
from tkinter import messagebox

class TicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Booking App")

        self.concert_tickets = 100
        self.movie_tickets = 50

        self.create_widgets()

    def create_widgets(self):
        self.label_concert = tk.Label(self.root, text="Concert Tickets Available: 100")
        self.label_concert.pack(pady=5)

        self.btn_book_concert = tk.Button(self.root, text="Book Concert Ticket", command=self.book_concert)
        self.btn_book_concert.pack(pady=10)

        self.label_movie = tk.Label(self.root, text="Movie Tickets Available: 50")
        self.label_movie.pack(pady=5)

        self.btn_book_movie = tk.Button(self.root, text="Book Movie Ticket", command=self.book_movie)
        self.btn_book_movie.pack(pady=10)

    def book_concert(self):
        if self.concert_tickets > 0:
            self.concert_tickets -= 1
            self.label_concert.config(text=f"Concert Tickets Available: {self.concert_tickets}")
            messagebox.showinfo("Success", "Concert ticket booked successfully.")
        else:
            messagebox.showerror("Error", "No more concert tickets available.")

    def book_movie(self):
        if self.movie_tickets > 0:
            self.movie_tickets -= 1
            self.label_movie.config(text=f"Movie Tickets Available: {self.movie_tickets}")
            messagebox.showinfo("Success", "Movie ticket booked successfully.")
        else:
            messagebox.showerror("Error", "No more movie tickets available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketBookingApp(root)
    root.mainloop()
