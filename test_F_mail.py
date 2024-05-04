import unittest
from myform import correct_mail

class Test_test_F_mail(unittest.TestCase):
    def test_invalid_emails(self):
        list_mail_uncor = ["", "1", "m1@", "m1@@mail.com", "mail.com", "m@mail.", "m@.com", "m@com", "m1@.mail.com", "m@mail.com", "m@mail..com", "m@mail..com"]
        for mail in list_mail_uncor:
            with self.subTest(mail=mail):
                self.assertFalse(correct_mail(mail))

if __name__ == '__main__':
    unittest.main()
