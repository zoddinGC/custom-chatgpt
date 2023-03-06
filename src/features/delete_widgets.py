def clear_widgets(frame:object) -> None:
    for widget in frame.winfo_children():
        widget.destroy()
