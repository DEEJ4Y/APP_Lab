class SRMIST():
    school = ""
    dept1 = ""
    dept2 = ""
    dept3 = ""
    dept4 = ""
    subscription = ""

    def __init__(self, dict):
        self.school = dict["school"]
        self.dept1 = dict["dept1"]
        self.dept2 = dict["dept2"]
        self.dept3 = dict["dept3"]
        self.dept4 = dict["dept4"]
        self.subscription = dict["subscription"]

    def display_all(self):
        print("\nDepartments")
        print(self.dept1, self.dept2, self.dept3, self.dept4)
        print(f"School: {self.school}")
        print(f"subscription: {self.subscription}")

    def display_less(self):
        print("\nDepartments")
        print(self.dept3, self.dept4)
        print(f"School: {self.school}")
        print(f"subscription: {self.subscription}")


if __name__ == "__main__":
    srm = SRMIST({
        "school": "SoC",
        "dept1": "NWC",
        "dept2": "DSBS",
        "dept3": "CINTEL",
        "dept4": "PAL",
        "subscription": "somesubscription",
    })
    srm.display_all()
    srm.display_less()
