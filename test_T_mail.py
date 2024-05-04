import unittest
from myform import correct_mail


class Test_test_T_mail(unittest.TestCase):
    def test_valid_emails(self):
        list_mail_cor = ["m.m@mail.ru", "m1@gmail.com", "kuznechik18@mail.com", "kuz%11@gmail.com", "kuz-nechik13%n@mail.ru", "john.doe@example.com", 
                         "bob123@yahoo.co.jp", "nathan.miller@mydomain.org", "peter_parkinson123@gmail.com",
                         "emma-jones@example.net", "maria_garcia123@example.com", "alice.smith123@hotmail.com"]
        for mail in list_mail_cor:
            with self.subTest(email=mail):
                self.assertTrue(correct_mail(mail))

if __name__ == '__main__':
    unittest.main()
