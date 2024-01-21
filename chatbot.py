import tkinter as tk
from tkinter import scrolledtext

class AdmissionChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Admission Enquiry Chatbot")

        self.create_widgets()

    def create_widgets(self):
        self.chat_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=15)
        self.chat_display.pack(expand=True, fill='both')

        self.user_input = tk.Entry(self.master, width=40)
        self.user_input.pack(expand=True, fill='x')

        self.send_button = tk.Button(self.master, text="Send", command=self.send_message)
        self.send_button.pack(expand=True, fill='both')

        # Initialize the chatbot
        self.chatbot_responses = {
            "hello": "Hello! How can I help you with your admission enquiry?",
            "hi":"Hello ! How can i help you ?",
            "admission process": "To get information about the admission process, please visit our official website.",
            "courses": "MCA ,MBA",
            "admission requirements":"1] Graduation has minimum 60%.  2] Mathmatics is compulsory in 12th or in graduation. 3] MHT-CET is cumpulsory.",
            "fees":"MCA : 88500/- , MBA : 80000/-",
            "application process":"1] Apply for merit list rounds. 2] If selected then fill application form. 3] Paid your fees(Online or offline).",
            "documents":"1] 2 Passport size photos. 2] SSC,HSC,Graduation marksheet. 3] CET scorecard. 4] Domicile certificate.",
            "deadlines":"The deadline for admission process is 31 May 2024.",
            "ews":"Yes, there is limited seats available for EWS as per merit.",
            "hostel":"Hostel facility is available for girl students only.",
            "contact":"You can either visit our campus or you can connect with us on 8574963254",
            "address":"G.S.Moze college of engineering balewadi pune.",
            "sports kota":"Limited seats available for sports.",
            "website":"https://www.gsmozecoe.org",
            "accredited":"Yes, College is accredited to NAAC with B++ grade.",
            "placement":"Yes, there is lots of campus placements opportunities available upto 12 LPA.",
            "library":"Yes, Library facility is available.",
            "Canteen":"NO. Canteen facility is not available in our campus but there is lots of options available outside the campus."
        }

        self.display_message("Hello! How can I help you with your admission enquiry?")

    def send_message(self):
        user_message = self.user_input.get()
        self.display_message(f"User: {user_message}")

        # Process the user's message and generate a response
        response = self.get_chatbot_response(user_message)
        self.display_message(f"Chatbot: {response}")

        # Clear the user input field
        self.user_input.delete(0, tk.END)

    def display_message(self, message):
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.see(tk.END)  # Scroll to the bottom

    def get_chatbot_response(self, user_message):
        # Simple rule-based chatbot
        user_message = user_message.lower()

        for key, value in self.chatbot_responses.items():
            if key in user_message:
                return value

        return "I'm sorry, I don't understand. Please ask another question."

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = AdmissionChatbot(root)
    root.mainloop()
