from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name, orientation="P", unit="mm", format="A4"):
        super().__init__(orientation, unit, format)
        self.name = name
        self.add_page()  # Auto calls header method
        self.add_name_shirt()

    def header(self):
        self.set_font("helvetica", style="B", size=48)
        self.cell(0, 20, "CS50 Shirtificate", align="C")

    def add_name_shirt(self):
        shirt_width = 180
        shirt_x = (self.w - shirt_width) / 2
        self.image("shirtificate.png", x=shirt_x, y=60, w=shirt_width)

        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", "B", 24)
        self.set_xy(0, 115)
        self.cell(self.w, 10, f"{self.name} took CS50", align="C")

    @classmethod
    def make_shirtificate(cls, name, filename="shirtificate.pdf"):
        cls(name).output(filename)


# name = input("Name: ")
# name = "Josh Martin"
name = "This guy"
PDF.make_shirtificate(name)
