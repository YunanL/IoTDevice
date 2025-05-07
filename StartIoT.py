import tkinter as tk
from tkinter import ttk
import checklicensedetails
import start_machine

checker = checklicensedetails
save_on_chain = start_machine

def extract_info(metadata):
    info = {attr["trait_type"]: attr["value"] for attr in metadata["attributes"]}
    return {
        "Machine ID": info.get("Machine ID", ""),
        "Function": info.get("Function", ""),
        "Duration": info.get("Usage Duration", ""),
        "Expires On": info.get("Expires On", ""),
        "Token ID": metadata.get("token_id", "")
    }

def create_ui(nft_list):
    root = tk.Tk()
    root.title("Machine 2")
    root.geometry("800x400")
    root.minsize(400, 200)

    selected_index = tk.IntVar(value=0)

    info_vars = {
        "Function": tk.StringVar(),
        "Expires On": tk.StringVar(),
        "Token ID": tk.StringVar()
    }

    def update_info_display(index):
        if 0 <= index < len(nft_list):
            info = extract_info(nft_list[index])
            for key in info_vars:
                info_vars[key].set(info.get(key, ""))

    def on_select():
        idx = selected_index.get()
        update_info_display(idx)
    def show_success_window(machine_id, token_id):
        success_win = tk.Toplevel()
        success_win.title("Machine Running")
        success_win.geometry("400x200")
        success_win.configure(bg="#eafaf1")

        msg = f"Machine {machine_id} is now running.\n"
        msg += f"License Token ID: {token_id}\n"

        label = tk.Label(success_win, text=msg, font=("Arial", 12), bg="#eafaf1", justify="left")
        label.pack(padx=20, pady=30)

        close_button = tk.Button(success_win, text="Close", command=success_win.destroy)
        close_button.pack(pady=10)
    # Main container
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=2)

    # Left side - License selection
    license_frame = ttk.LabelFrame(main_frame, text="Available Licenses", padding=10)
    license_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    for idx, nft in enumerate(nft_list):
        text = f"License Nr. {nft['token_id']}"
        tk.Radiobutton(
            license_frame, text=text, variable=selected_index, value=idx, command=on_select
        ).pack(anchor="w", pady=3)

    # Right side - License details
    details_frame = ttk.LabelFrame(main_frame, text="License Details", padding=10)
    details_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    for key in info_vars.keys():
        row_frame = ttk.Frame(details_frame)
        row_frame.pack(fill="x", pady=3)
        ttk.Label(row_frame, text=f"{key}:", font=("Arial", 10)).pack(side="left")
        ttk.Label(row_frame, textvariable=info_vars[key], font=("Arial", 10, "bold")).pack(side="left")

    # Start machine button
    def start_machine():
        token_id = int(info_vars["Token ID"].get())
        machine_id = 2
        save_on_chain.log_machine_start(machine_id, token_id)
        print(f"Starting machine with NFT Token ID: {token_id}")
        show_success_window(machine_id, token_id)
    start_button = tk.Button(
        root, text="Start Machine", command=start_machine,
        font=("Arial", 17), width=24, bg="green", fg="white"
    )
    start_button.pack(pady=10)

    update_info_display(0)
    root.mainloop()

if __name__ == "__main__":
    nft_metadata_list = checker.list_owned_tokens()
    create_ui(nft_metadata_list)
