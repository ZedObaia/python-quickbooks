from base import QuickbooksBaseObject, Address, PhoneNumber


class Employee(QuickbooksBaseObject):
    """
    QBO definition: Employee represents the people who are working for the company.
    """

    class_dict = {
        "PrimaryAddr": Address,
        "PrimaryPhone": PhoneNumber
    }

    qbo_object_name = "Employee"

    def __init__(self):
        self.SSN = ""
        self.BillableTime = ""
        self.GivenName = ""
        self.FamilyName = ""
        self.DisplayName = ""
        self.PrintOnCheckName = ""
        self.Active = True

        self.PrimaryAddr = None

    def __unicode__(self):
        return self.DisplayName